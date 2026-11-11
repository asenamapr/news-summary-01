"""Copy the baked-in news summary to the output directory.

Runs with no network. Reads summary.txt next to this file and writes it
byte-for-byte to <output>/entry.txt, where <output> is MAKEFUN_OUTPUT_DIR
or /output when that variable is not set. Deterministic: the same input
always produces the same output bytes.

Fail-closed: exits non-zero without writing anything if the summary is
empty or longer than 2,000 Unicode code points, so a bad summary can
never be submitted as a valid entry.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "summary.txt")
    with open(src, encoding="utf-8") as f:
        text = f.read()
    if not any(not c.isspace() for c in text) or len(text) > 2000:
        print("summary.txt must be 1-2000 characters", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
