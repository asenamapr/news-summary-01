"""Copy the baked-in news summary to the output directory.

Runs with no network. Reads summary.txt next to this file and writes it
byte-for-byte to <output>/entry.txt, where <output> is MAKEFUN_OUTPUT_DIR
or /output when that variable is not set. Deterministic: the same input
always produces the same output bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "summary.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
