"""
url:    https://adventofcode.com/2015/day/5
tags:   string
"""

from pathlib import Path


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip().splitlines()


# CONFIG
NAUGHTY = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"


def part_1(data: list) -> int:
    """
    Strings are all the same length, and lowercase.

    Brute force solution.
    """
    nice = 0

    # iter strings
    for kid in data:
        v_seen = 0  # 3 vowels
        dupe_char = 0  # 2 repeating chars
        bad = False

        for chars in NAUGHTY:
            if chars in kid:
                bad = True
                break

        if not bad:
            prev = ""
            for char in kid:
                if char == prev:
                    dupe_char += 1
                if char in VOWELS:
                    v_seen += 1
                prev = char

        if v_seen >= 3 and dupe_char >= 1:
            nice += 1

    print(f"Found {nice} strings!")
    return nice


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
