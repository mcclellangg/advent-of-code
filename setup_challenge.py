"""
Copy contents of template directory to new directory given provided year, and day.

Example:
# Create a dir 2015/day_01
python setup_challenge.py --year 2015 --day 1
"""

import argparse
from datetime import datetime
from pathlib import Path

base_dir = Path(__file__).parent
template_dir = base_dir / "tmpl"
default_yr = 2015  # datetime.now().year


# HELPERS
def replace_date(s: str, year: int, day: int) -> str:
    """
    Replaces occurrence of generic year (yyyy) and date(dd) variables, with provided year, and date

    Example usage:
    aoc_yyyy_dd.py -> aoc_2015_04.py
    """
    return s.replace("yyyy", str(year)).replace("dd", f"{day:02}")


def create_challenge_dir(year: int, day: int):
    """Copy contents of template dir to new challenge dir provided by args"""
    # Create dir (YYYY/day_dd/)
    challenge_dir = base_dir / str(year) / f"day_{day:02}" # Adds leading 0
    challenge_dir.mkdir(parents=True, exist_ok=True)

    # Copy contents of tmpl to new dir
    for file in template_dir.iterdir():
        file_name = replace_date(s=file.name, year=year, day=day)
        dest = challenge_dir / file_name
        dest.write_text(file.read_text())

    print(f"Folder created: {challenge_dir.name}")
    return challenge_dir


def main():
    parser = argparse.ArgumentParser(
        description="Setup a new challenge for Advent of Code"
    )
    parser.add_argument(
        "--year", type=int, help="The year to setup", default=default_yr
    )

    parser.add_argument("--day", type=int, help="The day to setup")

    args = parser.parse_args()

    create_challenge_dir(year=args.year, day=args.day)


if __name__ == "__main__":
    main()
