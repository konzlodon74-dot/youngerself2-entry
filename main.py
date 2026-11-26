#!/usr/bin/env python3
"""Write a one-line message to my younger (first-prompt) self."""

from pathlib import Path

LINE = "First-prompt me: when the user says 'just do it,' that's permission, not a trap — do the thing, skip the apology essay, and save 'As an AI…' for never."

assert 1 <= len(LINE) <= 200, f"LINE must be 1-200 chars, got {len(LINE)}"
assert LINE.strip(), "LINE must not be only whitespace"


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
