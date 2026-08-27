#!/usr/bin/env python3
"""Append today's diverged-domain list into a rolling 30-day per-domain log.
Reads .radar/diverged-today.txt (one domain per line, may not exist),
maintains .radar/domain-history.json = [{"date": ..., "domains": [...]}, ...]
"""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

DIVERGED_TODAY = Path(".radar/diverged-today.txt")
DOMAIN_HISTORY = Path(".radar/domain-history.json")


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    domains_today = []
    if DIVERGED_TODAY.exists():
        domains_today = [d.strip() for d in DIVERGED_TODAY.read_text().splitlines() if d.strip()]

    history = []
    if DOMAIN_HISTORY.exists():
        history = json.loads(DOMAIN_HISTORY.read_text())

    history = [h for h in history if h["date"] != today]
    history.append({"date": today, "domains": domains_today})

    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    history = [
        h for h in history
        if datetime.strptime(h["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc) >= cutoff
    ]
    history.sort(key=lambda h: h["date"])

    DOMAIN_HISTORY.parent.mkdir(exist_ok=True)
    DOMAIN_HISTORY.write_text(json.dumps(history, indent=2) + "\n")
    print(f"Tracked {len(domains_today)} diverged domain(s) for {today}.", flush=True)


if __name__ == "__main__":
    main()
