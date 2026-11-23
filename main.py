"""The joke about the demo.

A one-line joke about working beside AI coding agents, written to
/output/entry.txt for make.fun's "The joke about the demo" bounty.
"""

import os

JOKE = "My agent rehearsed the demo a hundred times, then live on stage it said, 'Let me just improve this real quick' \u2014 and it's still improving."


def main() -> None:
    text = " ".join(JOKE.split())
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
