#!/usr/bin/env python3
"""Update the daily tip and quote blocks in README.md."""
import json
import re
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TIPS = ROOT / "tips.json"

TZ = ZoneInfo("Africa/Cairo")
QUOTE_URL = "https://zenquotes.io/api/today"
FALLBACK_QUOTE = ("First, solve the problem. Then, write the code.", "John Johnson")
RETRIES = 3


def timestamp(dt: datetime) -> str:
    offset = dt.strftime("%z")  # +0300
    return f"{dt:%Y-%m-%d %H:%M:%S}.{dt.microsecond // 1000:03d} {offset[:3]}:{offset[3:]}"


def clean(text: str) -> str:
    """Single line, and no backticks that could break the ```log fence."""
    return " ".join(str(text).split()).replace("`", "'")


def pick_tip(now: datetime) -> str:
    tips = json.loads(TIPS.read_text(encoding="utf-8"))
    if not isinstance(tips, list) or not tips:
        sys.exit("tips.json must be a non-empty JSON array")
    return clean(tips[now.date().toordinal() % len(tips)])


def fetch_quote() -> tuple[str, str, str | None]:
    """Return (quote, author, error). error is None on success."""
    last_error = "unknown error"
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(QUOTE_URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                item = json.loads(r.read())[0]
            quote, author = item["q"], item["a"]
            # ZenQuotes answers rate-limit errors with HTTP 200 and a fake "quote"
            if author == "zenquotes.io":
                raise ValueError("rate limited")
            return clean(quote), clean(author), None
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"
            if attempt < RETRIES:
                time.sleep(2 ** attempt)
    return *FALLBACK_QUOTE, last_error


def build_tip_block(ts: str, tip: str) -> str:
    svc = "tip-service"
    return "\n".join([
        "<!-- TIP_START -->",
        "```log",
        f"[{ts} INF] {svc} Fetching tip of the day...",
        f"[{ts} INF] {svc} Status: OK  \u2192  tip loaded",
        f"[{ts} TIP] {svc} {tip}",
        "```",
        "<!-- TIP_END -->",
    ])


def build_quote_block(ts: str, quote: str, author: str, error: str | None) -> str:
    svc = "quote-service"
    if error is None:
        status = [
            f"[{ts} INF] {svc} GET {QUOTE_URL}  200 OK",
            f"[{ts} INF] {svc} Message received  \u2192  quote loaded",
        ]
    else:
        status = [
            f"[{ts} WRN] {svc} Upstream unavailable ({clean(error)})",
            f"[{ts} INF] {svc} Using fallback quote",
        ]
    return "\n".join([
        "<!-- QUOTE_START -->",
        "```log",
        f"[{ts} INF] {svc} Connecting to quotes upstream...",
        *status,
        f"[{ts} QOT] {svc} {quote}",
        f"[{ts} AUT] {svc} {author}",
        "```",
        "<!-- QUOTE_END -->",
    ])


def replace_block(content: str, name: str, block: str) -> str:
    pattern = re.compile(rf"<!-- {name}_START -->.*?<!-- {name}_END -->", re.DOTALL)
    if not pattern.search(content):
        sys.exit(f"Markers for {name} not found in README.md")
    return pattern.sub(lambda _: block, content, count=1)  # lambda: no backslash interpretation


def main() -> None:
    now = datetime.now(TZ)
    ts = timestamp(now)

    tip = pick_tip(now)
    quote, author, error = fetch_quote()

    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "TIP", build_tip_block(ts, tip))
    content = replace_block(content, "QUOTE", build_quote_block(ts, quote, author, error))
    README.write_text(content, encoding="utf-8")

    print(f"Tip: {tip}")
    print(f"Quote: {quote} - {author}" + (f"  (fallback: {error})" if error else ""))


if __name__ == "__main__":
    main()