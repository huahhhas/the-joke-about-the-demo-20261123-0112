"""The joke about the demo.

A one-line joke about working beside AI coding agents, written to
/output/entry.txt for make.fun's "The joke about the demo" bounty.
The entry is gated to 1-280 characters: a single line, no trailing newline.
"""

import os

JOKE = "My agent rehearsed the demo a hundred times, then live on stage it said, 'Let me just improve this real quick' \u2014 and it's still improving."

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = " ".join(JOKE.split())
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
