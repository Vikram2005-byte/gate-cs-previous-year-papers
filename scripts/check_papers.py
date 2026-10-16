#!/usr/bin/env python3
"""Check that the expected GATE CS PDFs exist and look like PDF files."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = (
    *(f"{year}_CS.pdf" for year in range(2007, 2017)),
    "2017_CS1.pdf",
    "2017_CS2.pdf",
    *(f"{year}_CS.pdf" for year in range(2018, 2024)),
    "2024_CS1.pdf",
    "2024_CS2.pdf",
    "2025_CS1.pdf",
    "2025_CS2.pdf",
    "2026_CS1.pdf",
    "2026_CS2.pdf",
)

def is_pdf(path: Path) -> bool:
    """Allow a PDF signature within the first 1,024 bytes, as PDF readers do."""
    try:
        with path.open("rb") as file:
            header = file.read(1024)
    except OSError as exc:
        print(f"ERROR: cannot read {path.relative_to(ROOT)}: {exc}")
        return False

    if not header:
        print(f"ERROR: {path.relative_to(ROOT)} is empty")
        return False
    if b"%PDF-" not in header:
        print(f"ERROR: {path.relative_to(ROOT)} has no PDF signature in its first 1,024 bytes")
        return False
    return True


def main() -> int:
    missing = []
    invalid = []

    for filename in EXPECTED_FILES:
        path = ROOT / filename
        if not path.is_file():
            missing.append(filename)
            print(f"MISSING: {filename}")
        elif not is_pdf(path):
            invalid.append(filename)
        else:
            print(f"OK: {filename}")

    if missing or invalid:
        print(f"\nValidation failed: {len(missing)} missing, {len(invalid)} invalid.")
        return 1

    print(f"\nValidation passed: all {len(EXPECTED_FILES)} expected papers exist and have a PDF signature.")
    print("Note: this checks filenames and file signatures, not page completeness or official authenticity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
