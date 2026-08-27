#!/usr/bin/env python3
"""Append today's radar result to a rolling 30-day JSON log."""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

LOG_PATH = Path(".radar/history.json")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--diverged", type=int, required=True)
    p.add_argument("--checked", type=int, required=True)
    p.add_argument("--date", required=True)  # YYYY-MM-DD
    args = p.parse_args()

    LOG_PATH.parent.mkdir(exist_ok=True)
    history = []
    if LOG_PATH.exists():
        history = json.loads(LOG_PATH.read_text())

    # de-dupe same-day re-runs (workflow_dispatch reruns)
    history = [h for h in history if h["date"] != args.date]
    history.append({
        "date": args.date,
        "checked": args.checked,
        "diverged": args.diverged,
    })

    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    history = [
        h for h in history
        if datetime.strptime(h["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc) >= cutoff
    ]
    history.sort(key=lambda h: h["date"])

    LOG_PATH.write_text(json.dumps(history, indent=2) + "\n")

    total_diverged = sum(h["diverged"] for h in history)
    domains_tracked = history[-1]["checked"] if history else args.checked
    print(f"30-day window: {total_diverged} divergences across {len(history)} runs, "
          f"{domains_tracked} domains tracked/run")

if __name__ == "__main__":
    main()
