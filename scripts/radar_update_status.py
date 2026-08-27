#!/usr/bin/env python3
"""Rewrite the AUTO-GENERATED-STATUS badge line in README.md.
Line-based, no regex.
"""
import argparse
import sys
from pathlib import Path

README = Path("README.md")


def find_marker_line(lines, needle):
    for i, line in enumerate(lines):
        if needle in line:
            return i
    return -1


def main():
    print("SCRIPT VERSION: radar_update_status.py v1", flush=True)
    p = argparse.ArgumentParser()
    p.add_argument("--diverged", type=int, required=True)
    args = p.parse_args()

    if args.diverged == 0:
        line = "🟢 **Radar status:** 0 findings today"
    else:
        plural = "findings" if args.diverged != 1 else "finding"
        line = f"🔴 **Radar status:** {args.diverged} {plural} today"

    new_block = [
        "<!-- AUTO-GENERATED-STATUS -->",
        line,
        "<!-- /AUTO-GENERATED-STATUS -->",
    ]

    text = README.read_text()
    lines = text.splitlines()

    start_idx = find_marker_line(lines, "AUTO-GENERATED-STATUS")
    end_idx = -1
    if start_idx != -1:
        for i in range(start_idx + 1, len(lines)):
            if "/AUTO-GENERATED-STATUS" in lines[i]:
                end_idx = i
                break

    if start_idx == -1 or end_idx == -1:
        print("DEBUG: STATUS markers not found. Lines mentioning AUTO-GENERATED:", flush=True)
        for i, line_ in enumerate(lines):
            if "AUTO-GENERATED" in line_:
                print(f"  line {i}: {line_!r}", flush=True)
        sys.exit(f"AUTO-GENERATED-STATUS markers not found (start={start_idx}, end={end_idx})")

    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1:]
    README.write_text("\n".join(new_lines) + "\n")
    print(f"Updated STATUS badge: lines {start_idx}-{end_idx} replaced.", flush=True)


if __name__ == "__main__":
    main()
