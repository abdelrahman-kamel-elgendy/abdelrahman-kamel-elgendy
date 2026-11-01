#!/usr/bin/env python3
"""Regenerates three SQL-style blocks in README.md from live GitHub data:

  STREAK  -> next to the Streak card
  LANGS   -> next to the Most Used Languages card

Each block lives between <!-- NAME_START --> and <!-- NAME_END -->.
Env: GITHUB_TOKEN (required), GH_USER, README_PATH (optional). No dependencies.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.github.com/graphql"
TOP_LANGS = 6  # matches the Most Used Languages card

QUERY_CREATED = "query($u:String!){user(login:$u){createdAt}}"

QUERY_YEAR = """
query($u:String!,$from:DateTime!,$to:DateTime!){
  user(login:$u){
    contributionsCollection(from:$from,to:$to){
      totalCommitContributions
      contributionCalendar{
        weeks{contributionDays{date contributionCount}}
      }
    }
  }
}"""

QUERY_COUNTS = """
query($pr:String!,$merged:String!,$issues:String!){
  pr:search(query:$pr,type:ISSUE){issueCount}
  merged:search(query:$merged,type:ISSUE){issueCount}
  issues:search(query:$issues,type:ISSUE){issueCount}
}"""

QUERY_REPOS = """
query($u:String!,$after:String){
  user(login:$u){
    repositories(first:100,after:$after,ownerAffiliations:OWNER,isFork:false){
      pageInfo{hasNextPage endCursor}
      nodes{
        stargazerCount
        languages(first:20,orderBy:{field:SIZE,direction:DESC}){
          edges{size node{name}}
        }
      }
    }
  }
}"""


def gql(token, query, variables):
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "readme-metrics",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        out = json.load(resp)
    if "errors" in out:
        sys.exit(f"GraphQL error: {out['errors']}")
    return out["data"]


def fetch(token, user):
    now = datetime.now(timezone.utc)
    created = gql(token, QUERY_CREATED, {"u": user})["user"]["createdAt"]

    days, commits_total, commits_year = {}, 0, 0
    for year in range(int(created[:4]), now.year + 1):
        frm = datetime(year, 1, 1, tzinfo=timezone.utc)
        to = min(datetime(year, 12, 31, 23, 59, 59, tzinfo=timezone.utc), now)
        cc = gql(token, QUERY_YEAR, {
            "u": user, "from": frm.isoformat(), "to": to.isoformat(),
        })["user"]["contributionsCollection"]
        commits_total += cc["totalCommitContributions"]
        if year == now.year:
            commits_year = cc["totalCommitContributions"]
        for week in cc["contributionCalendar"]["weeks"]:
            for d in week["contributionDays"]:
                if d["date"].startswith(str(year)):
                    days[d["date"]] = d["contributionCount"]

    q = f"author:{user} type:pr"
    counts = gql(token, QUERY_COUNTS, {
        "pr": q, "merged": q + " is:merged", "issues": f"author:{user} type:issue",
    })

    stars, langs, after = 0, {}, None
    while True:
        repos = gql(token, QUERY_REPOS, {"u": user, "after": after})["user"]["repositories"]
        for repo in repos["nodes"]:
            stars += repo["stargazerCount"]
            for edge in repo["languages"]["edges"]:
                name = edge["node"]["name"]
                langs[name] = langs.get(name, 0) + edge["size"]
        if not repos["pageInfo"]["hasNextPage"]:
            break
        after = repos["pageInfo"]["endCursor"]

    return {
        "days": days,
        "stars": stars,
        "langs": langs,
        "total_commits": commits_total,
        "commits_this_year": commits_year,
        "pull_requests": counts["pr"]["issueCount"],
        "merged_pull_requests": counts["merged"]["issueCount"],
        "total_issues": counts["issues"]["issueCount"],
    }


def streaks(days, today):
    """Returns dict with current/longest lengths and their date windows."""
    longest = run = 0
    run_start = l_start = l_end = None
    for d in sorted(days):
        if days[d] > 0:
            if run == 0:
                run_start = d
            run += 1
            if run > longest:
                longest, l_start, l_end = run, run_start, d
        else:
            run = 0

    cur, cursor = 0, today
    if days.get(cursor.isoformat(), 0) == 0:  # today may not have activity yet
        cursor -= timedelta(days=1)
    end = cursor
    while days.get(cursor.isoformat(), 0) > 0:
        cur += 1
        cursor -= timedelta(days=1)
    start = cursor + timedelta(days=1)
    return {
        "current": cur, "current_start": start.isoformat(), "current_end": end.isoformat(),
        "longest": longest, "longest_start": l_start, "longest_end": l_end,
    }


def ascii_table(headers, rows, right_align_last=True):
    """Boxed result table, every line prefixed with '-- ' (SQL comment)."""
    widths = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    bar = "-- +" + "+".join("-" * (w + 2) for w in widths) + "+"

    def line(cells):
        out = []
        for i, (c, w) in enumerate(zip(cells, widths)):
            last = i == len(cells) - 1
            out.append(" " + (str(c).rjust(w) if last and right_align_last else str(c).ljust(w)) + " ")
        return "-- |" + "|".join(out) + "|"

    return "\n".join([bar, line(headers), bar, *[line(r) for r in rows], bar])


def fence(sql):
    return "```sql\n" + sql.strip("\n") + "\n```"



def render_streak(user, data, today):
    s = streaks(data["days"], today)
    active = [d for d, n in data["days"].items() if n > 0]
    rows = [
        ("total_contributions", sum(data["days"].values())),
        ("tracking_since", min(active) if active else "-"),
        ("current_streak", f"{s['current']} d"),
        ("current_window", f"{s['current_start']} → {s['current_end']}" if s["current"] else "none active"),
        ("longest_streak", f"{s['longest']} d"),
        ("longest_window", f"{s['longest_start']} → {s['longest_end']}" if s["longest"] else "-"),
    ]
    return fence(f"""-- ── contribution_calendar ────────
SELECT
    total_contributions,
    tracking_since,
    current_streak,
    current_window,
    longest_streak,
    longest_window
FROM
    contribution_calendar
WHERE
    username = '{user}';

-- ── Result ({today}) ──
{ascii_table(["metric", "value"], rows)}
-- 6 rows in set""")


def render_langs(user, data, today):
    langs = sorted(data["langs"].items(), key=lambda kv: kv[1], reverse=True)[:TOP_LANGS]
    total = sum(data["langs"].values()) or 1
    rows = [(name, f"{100 * size / total:.2f}%") for name, size in langs]
    return fence(f"""-- ── repo_languages ───────────────
SELECT
    language,
    ROUND(100 * SUM(bytes) / SUM(SUM(bytes)) OVER (), 2) AS share
FROM
    repo_languages
WHERE
    owner = '{user}'
    AND is_fork = FALSE
GROUP BY
    language
ORDER BY
    share DESC
LIMIT {TOP_LANGS};

-- ── Result ({today}) ──
{ascii_table(["language", "share"], rows)}
-- {len(rows)} rows in set""")


def inject(text, name, block):
    pattern = re.compile(rf"(<!-- {name}_START -->)(.*?)(<!-- {name}_END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"{name}_START / {name}_END markers not found in README")
    return pattern.sub(lambda m: f"{m.group(1)}\n{block}\n{m.group(3)}", text, count=1)


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit(
            "No token found. Add an `env:` block with GITHUB_TOKEN to the "
            "workflow step that runs this script (indented under the step)."
        )
    user = os.environ.get("GH_USER", "abdelrahman-kamel-elgendy")
    path = os.environ.get("README_PATH", "README.md")
    today = datetime.now(timezone.utc).date()

    data = fetch(token, user)
    blocks = {
        "STREAK": render_streak(user, data, today),
        "LANGS": render_langs(user, data, today),
    }
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for name, block in blocks.items():
        text = inject(text, name, block)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("metrics blocks updated:", ", ".join(blocks))


if __name__ == "__main__":
    main()