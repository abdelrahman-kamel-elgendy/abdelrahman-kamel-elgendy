#!/usr/bin/env python3
"""Regenerates the metrics.sql block in README.md from live GitHub data.

Replaces everything between <!-- METRICS_START --> and <!-- METRICS_END -->.
Env: GITHUB_TOKEN (required), GH_USER, README_PATH (optional). No dependencies.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone

API = "https://api.github.com/graphql"

QUERY_CREATED = "query($u:String!){user(login:$u){createdAt}}"

QUERY_YEAR = """
query($u:String!,$from:DateTime!,$to:DateTime!){
  user(login:$u){
    contributionsCollection(from:$from,to:$to){
      totalCommitContributions
      contributionCalendar{
        totalContributions
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
    start_year = int(created[:4])

    days, commits_total, commits_year = {}, 0, 0
    for year in range(start_year, now.year + 1):
        frm = datetime(year, 1, 1, tzinfo=timezone.utc)
        to = min(datetime(year, 12, 31, 23, 59, 59, tzinfo=timezone.utc), now)
        cc = gql(token, QUERY_YEAR, {
            "u": user,
            "from": frm.isoformat(),
            "to": to.isoformat(),
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
        "pr": q,
        "merged": q + " is:merged",
        "issues": f"author:{user} type:issue",
    })
    return {
        "days": days,
        "total_commits": commits_total,
        "commits_this_year": commits_year,
        "pull_requests": counts["pr"]["issueCount"],
        "merged_pull_requests": counts["merged"]["issueCount"],
        "total_issues": counts["issues"]["issueCount"],
    }


def streaks(days, today):
    """Returns (current, longest, current_start, current_end)."""
    longest = run = 0
    for d in sorted(days):
        run = run + 1 if days[d] > 0 else 0
        longest = max(longest, run)

    cur, cursor = 0, today
    if days.get(cursor.isoformat(), 0) == 0:  # today may not have activity yet
        cursor -= timedelta(days=1)
    end = cursor
    while days.get(cursor.isoformat(), 0) > 0:
        cur += 1
        cursor -= timedelta(days=1)
    start = cursor + timedelta(days=1)
    return cur, longest, start, end


def render(user, data, today):
    cur, longest, start, end = streaks(data["days"], today)
    rows = [
        ("total_commits", str(data["total_commits"])),
        ("commits_this_year", str(data["commits_this_year"])),
        ("total_contributions", str(sum(data["days"].values()))),
        ("pull_requests", str(data["pull_requests"])),
        ("merged_pull_requests", str(data["merged_pull_requests"])),
        ("total_issues", str(data["total_issues"])),
        ("current_streak", f"{cur} d"),
        ("longest_streak", f"{longest} d"),
    ]
    w1 = max(len(k) for k, _ in rows) + 1
    w2 = max(len(v) for _, v in rows) + 2
    bar = "-- +" + "-" * (w1 + 1) + "+" + "-" * (w2 + 1) + "+"
    table = "\n".join(f"-- | {k.ljust(w1 - 1)} | {v.rjust(w2 - 1)} |" for k, v in rows)
    streak_line = (
        f"-- streak window: {start} → {end}" if cur else "-- streak window: none active"
    )
    return f"""```sql
-- ──────────────────────────────────
--  Querying developer stats
--  from github.db
-- ──────────────────────────────────
SELECT
    total_commits,
    commits_this_year,
    total_contributions,
    pull_requests,
    merged_pull_requests,
    total_issues,
    current_streak,
    longest_streak
FROM
    github_stats
WHERE
    username = '{user}'
    AND year = YEAR(CURDATE());

-- ── Result ─────────────────────────
-- as of {today}
{bar}
{table}
{bar}
{streak_line}
-- 1 row in set
```"""


def inject(text, block):
    pattern = re.compile(r"(<!-- METRICS_START -->)(.*?)(<!-- METRICS_END -->)", re.S)
    if not pattern.search(text):
        sys.exit("METRICS_START / METRICS_END markers not found in README")
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

    block = render(user, fetch(token, user), today)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    with open(path, "w", encoding="utf-8") as f:
        f.write(inject(text, block))
    print("metrics block updated")


if __name__ == "__main__":
    main()