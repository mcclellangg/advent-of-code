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
    """
    I don't love that a line in the data is called `kid`.
    """
    n = len(data[0])
    nice_kids = 0
    # iter data and determine how many strings are nice
    for kid in data:
        rule_1 = False
        rule_2 = False

        # 1. contains a pair that appears at least twice (but not consecutively)
        # xy___xy <> xyxy

        pair_map = {}

        for i in range(0, n - 1):
            c_pair = kid[i : i + 2]
            prev_pair_i = pair_map.get(c_pair)

            if c_pair in pair_map and i > prev_pair_i + 1:
                rule_1 = True
                break

            if c_pair not in pair_map:
                pair_map[c_pair] = i

        # 2. repeat separated by 1 letter
        # aba || aaa
        for i in range(0, n - 2):
            if kid[i] == kid[i + 2]:
                rule_2 = True
                break

        if rule_1 and rule_2:
            nice_kids += 1

    return nice_kids


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
