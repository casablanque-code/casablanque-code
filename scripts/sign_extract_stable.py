#!/usr/bin/env python3
"""Extract the 'stable' part of README.md (everything except both
AUTO-GENERATED blocks) into README.stable.md, and print its sha256.
Line-based, no regex -- matches the style of radar_update_readme.py.
"""
import hashlib
import sys
from pathlib import Path

README = Path("README.md")
STABLE = Path("README.stable.md")


def strip_block(lines, start_needle, end_needle, exclude_start=None):
    """Remove one marker...marker block (inclusive) from lines. Returns new list."""
    start_idx = -1
    for i, line in enumerate(lines):
        if start_needle in line and (exclude_start is None or exclude_start not in line):
            start_idx = i
            break
    if start_idx == -1:
        return lines  # block not present, nothing to strip

    end_idx = -1
    for i in range(start_idx + 1, len(lines)):
        if end_needle in line if False else end_needle in lines[i]:
            end_idx = i
            break
    if end_idx == -1:
        return lines

    return lines[:start_idx] + lines[end_idx + 1:]


def main():
    text = README.read_text()
    lines = text.splitlines()

    # strip radar block (AUTO-GENERATED, not -SIG)
    lines = strip_block(lines, "AUTO-GENERATED", "/AUTO-GENERATED", exclude_start="AUTO-GENERATED-SIG")
    # strip sig block (AUTO-GENERATED-SIG)
    lines = strip_block(lines, "AUTO-GENERATED-SIG", "/AUTO-GENERATED-SIG")

    stable_text = "\n".join(lines) + "\n"
    STABLE.write_text(stable_text)

    digest = hashlib.sha256(stable_text.encode("utf-8")).hexdigest()
    print(digest)


if __name__ == "__main__":
    main()
