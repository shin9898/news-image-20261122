"""news-image-20261122 entry: copy the bundled entry.png to /output/entry.png.

The image is fixed in the repository, so every run writes the same bytes.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    MAKEFUN_OUTPUT_DIR=out python3.13 main.py
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
