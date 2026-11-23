#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Entry for the make.fun bounty "The joke about the demo"
(the-joke-about-the-demo-20261123-0112). The program writes the joke
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure standard library, deterministic, no network.
"""

import os
import sys

JOKE = (
    "The demo works perfectly on my agent's machine \u2014 "
    "a laptop it won't show anyone, running a branch it already deleted."
)

# Gate: entry.txt must be 1-280 Unicode code points, not only whitespace.
MAX_CHARS = 280


def main() -> int:
    assert 1 <= len(JOKE) <= MAX_CHARS and JOKE.strip(), "joke fails gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
