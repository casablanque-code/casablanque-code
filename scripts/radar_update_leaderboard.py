#!/usr/bin/env python3
"""Rewrite the AUTO-GENERATED-LEADERBOARD table in README.md from
.radar/domain-history.json. Line-based, no regex.
"""
import json
import sys
from collections import Counter
from pathlib import Path

README = Path("README.md")
DOMAIN_HISTORY = Path(".radar/domain-history.json")
TOP_N = 5


def find_marker_line(lines, needle):
    for i, line in enumerate(lines):
        if needle in line:
            return i
    return -1


def main():
    print("SCRIPT VERSION: radar_update_leaderboard.py v1", flush=True)

    history = json.loads(DOMAIN_HISTORY.read_text()) if DOMAIN_HISTORY.exists() else []
    counts = Counter()
    for entry in history:
        counts.update(entry.get("domains", []))

    table_lines = [
        "**Most disagreeing domains (30 days)**",
        "",
        "| Domain | Divergences |",
        "| :--- | ---: |",
    ]
    if not counts:
        table_lines.append("| _(no divergences yet)_ | — |")
    else:
        for domain, count in counts.most_common(TOP_N):
            table_lines.append(f"| `{domain}` | {count} |")

    new_block = ["<!-- AUTO-GENERATED-LEADERBOARD -->", ""] + table_lines + ["", "<!-- /AUTO-GENERATED-LEADERBOARD -->"]

    text = README.read_text()
    lines = text.splitlines()

    start_idx = find_marker_line(lines, "AUTO-GENERATED-LEADERBOARD")
    end_idx = -1
    if start_idx != -1:
        for i in range(start_idx + 1, len(lines)):
            if "/AUTO-GENERATED-LEADERBOARD" in lines[i]:
                end_idx = i
                break

    if start_idx == -1 or end_idx == -1:
        print("DEBUG: LEADERBOARD markers not found. Lines mentioning AUTO-GENERATED:", flush=True)
        for i, line_ in enumerate(lines):
            if "AUTO-GENERATED" in line_:
                print(f"  line {i}: {line_!r}", flush=True)
        sys.exit(f"AUTO-GENERATED-LEADERBOARD markers not found (start={start_idx}, end={end_idx})")

    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1:]
    README.write_text("\n".join(new_lines) + "\n")
    print(f"Updated LEADERBOARD: lines {start_idx}-{end_idx} replaced.", flush=True)


if __name__ == "__main__":
    main()
