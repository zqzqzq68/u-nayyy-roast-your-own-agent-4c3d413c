#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun bounty entry.

The whole entry is one line: this program writes a single roast of the
AI agent that built it to /output/entry.txt, and nothing else.
"""

from pathlib import Path

ROAST = "My agent spent an hour planning this one line, then asked me for permission to print it."


def main():
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ROAST + "\n", encoding="utf-8")
    print(ROAST)


if __name__ == "__main__":
    main()
