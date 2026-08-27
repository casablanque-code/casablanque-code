#!/usr/bin/env python3
"""Rewrite the content between AUTO-GENERATED markers in README.md.
Simple line-based approach, no regex, no fancy matching.
"""
import argparse
import json
import sys
from pathlib import Path

README = Path("README.md")
HISTORY = Path(".radar/history.json")


def find_marker_line(lines, needle, exclude=None):
    for i, line in enumerate(lines):
        if needle in line and (exclude is None or exclude not in line):
            return i
    return -1


def main():
    print("SCRIPT VERSION: radar_update_readme.py v4 (line-based, no regex)", flush=True)
    p = argparse.ArgumentParser()
    p.add_argument("--timestamp", required=True)
    p.add_argument("--repo", required=True, help="owner/repo, for building the raw-log link")
    args = p.parse_args()

    history = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
    total_diverged = sum(h["diverged"] for h in history)
    domains_tracked = history[-1]["checked"] if history else 0
    days_covered = len(history)

    if total_diverged == 0:
        divergence_line = (
            f"> 0 divergences in the last {days_covered} days across "
            f"{domains_tracked} tracked domains -- dig hasn't lied yet.\n"
            f"> _(when it does, this line changes -- that's the interesting part)_"
        )
    else:
        recent = [h for h in history if h["diverged"] > 0][-1]
        log_date_compact = recent["date"].replace("-", "")
        log_url = (
            f"https://github.com/{args.repo}/blob/main/"
            f".radar/raw-{log_date_compact}.log"
        )
        divergence_line = (
            f"> {total_diverged} divergence(s) in the last {days_covered} days "
            f"across {domains_tracked} tracked domains -- most recent on {recent['date']}.\n"
            f"> _(mostly anycast/GeoDNS edges disagreeing between two queries -- "
            f"[full per-domain log for {recent['date']}]({log_url}))_"
        )

    new_block = [
        "<!-- AUTO-GENERATED -->",
        "",
        f"**Resolution divergence** (`gai doctor` per-domain reality check) - last run `{args.timestamp}`",
        divergence_line,
        "",
        "<!-- /AUTO-GENERATED -->",
    ]

    text = README.read_text()
    lines = text.splitlines()

    start_idx = find_marker_line(lines, "AUTO-GENERATED", exclude="AUTO-GENERATED-SIG")
    end_idx = -1
    if start_idx != -1:
        for i in range(start_idx + 1, len(lines)):
            if "/AUTO-GENERATED" in lines[i] and "SIG" not in lines[i]:
                end_idx = i
                break

    if start_idx == -1 or end_idx == -1:
        print("DEBUG: could not locate markers. Lines mentioning AUTO-GENERATED:", flush=True)
        for i, line in enumerate(lines):
            if "AUTO-GENERATED" in line:
                print(f"  line {i}: {line!r}", flush=True)
        sys.stdout.flush()
        sys.exit(f"AUTO-GENERATED markers not found (start={start_idx}, end={end_idx})")

    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1:]
    README.write_text("\n".join(new_lines) + "\n")
    print(f"Updated radar block: lines {start_idx}-{end_idx} replaced.", flush=True)


if __name__ == "__main__":
    main()
