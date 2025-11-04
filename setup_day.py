import argparse
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / "tmpl"

default_yr = "2015"  # datetime.now().year


# HELPERS
def replace_date(s: str, year: int, day: int) -> str:
    return s.replace("yyyy", str(year)).replace("dd", str(day))


def create_day_dir():
    """Copy contents of template dir to new day dir provided by args"""
    pass


def main():
    parser = argparse.ArgumentParser(description="Setup a new day for Advent of Code")
    parser.add_argument(
        "--year", type=int, help="The year to setup", default=default_yr
    )

    parser.add_argument("--day", type=int, help="The day to setup")

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
