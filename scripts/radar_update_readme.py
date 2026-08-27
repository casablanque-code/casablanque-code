#!/usr/bin/env python3
"""Rewrite the content between AUTO-GENERATED markers in README.md."""
import argparse
import json
import re
from pathlib import Path

README = Path("README.md")
HISTORY = Path(".radar/history.json")

START = "<!-- AUTO-GENERATED — do not edit manually, see .github/workflows/*.yml -->"
END = "<!-- /AUTO-GENERATED -->"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--timestamp", required=True)
    args = p.parse_args()

    history = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
    total_diverged = sum(h["diverged"] for h in history)
    domains_tracked = history[-1]["checked"] if history else 0
    days_covered = len(history)

    if total_diverged == 0:
        divergence_line = (
            f"> 0 divergences in the last {days_covered} days across "
            f"{domains_tracked} tracked domains — dig hasn't lied yet.\n"
            f"> _(when it does, this line changes — that's the interesting part)_"
        )
    else:
        recent = [h for h in history if h["diverged"] > 0][-1]
        divergence_line = (
            f"> {total_diverged} divergence(s) in the last {days_covered} days "
            f"across {domains_tracked} tracked domains — most recent on {recent['date']}.\n"
            f"> _(see .radar/history.json for the full log)_"
        )

    block = f"""{START}

**Resolution divergence** (`gai doctor` per-domain reality check) · last run `{args.timestamp}`
{divergence_line}

{END}"""

    text = README.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit("AUTO-GENERATED markers not found in README.md")
    text = pattern.sub(block, text)
    README.write_text(text)

if __name__ == "__main__":
    main()
