#!/usr/bin/env python3
"""Rewrite the content between AUTO-GENERATED-SIG markers in README.md.
Line-based, no regex -- same style as radar_update_readme.py.
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
    print("SCRIPT VERSION: sign_update_readme.py v1 (line-based, no regex)", flush=True)
    p = argparse.ArgumentParser()
    p.add_argument("--timestamp", required=True)
    p.add_argument("--hash", required=True)
    p.add_argument("--sig-url", required=True, help="Link to the .sig file, e.g. GitHub blob URL")
    args = p.parse_args()

    short_hash = args.hash[:16]

    new_block = [
        "<!-- AUTO-GENERATED-SIG -->",
        "",
        f"**README integrity** \u00b7 signed `{args.timestamp}` \u00b7 [verify]({args.sig_url})",
        f"> `SHA256: {short_hash}\u2026` \u00b7 [my PGP key](https://keys.openpgp.org/search?q=2A49CD4AF95F76DF38FC1F9EBFB3563375149683)",
        "> Zero Trust isn't just for infra. Don't trust this file either -- verify it.",
        "",
        "<!-- /AUTO-GENERATED-SIG -->",
    ]

    text = README.read_text()
    lines = text.splitlines()

    start_idx = find_marker_line(lines, "AUTO-GENERATED-SIG")
    end_idx = -1
    if start_idx != -1:
        for i in range(start_idx + 1, len(lines)):
            if "/AUTO-GENERATED-SIG" in lines[i]:
                end_idx = i
                break

    if start_idx == -1 or end_idx == -1:
        print("DEBUG: could not locate SIG markers. Lines mentioning AUTO-GENERATED:", flush=True)
        for i, line in enumerate(lines):
            if "AUTO-GENERATED" in line:
                print(f"  line {i}: {line!r}", flush=True)
        sys.exit(f"AUTO-GENERATED-SIG markers not found (start={start_idx}, end={end_idx})")

    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1:]
    README.write_text("\n".join(new_lines) + "\n")
    print(f"Updated SIG block: lines {start_idx}-{end_idx} replaced.", flush=True)


if __name__ == "__main__":
    main()
