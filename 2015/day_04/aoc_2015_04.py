"""
url: https://adventofcode.com/2015/day/4
tags: md5, hash, cryptography
"""

from pathlib import Path
import hashlib


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip()


def part_1(data: list) -> str:
    """Brute force solution to get lowest decimal number that creates the valid MD5 hash.

    Will there always be an answer?

    Is there a way to apply a sorting algo to decimal generation? How do You tell if a guess is better or worse?
    """
    k_prefix = "".join(data)

    # Generate decimals
    for i in range(0, 1000000):
        k_suffix = i

        k = f"{k_prefix}{k_suffix}"
        hex_hash = hashlib.md5(k.encode()).hexdigest()

        if hex_hash[:5] == "00000":
            print(f"Suffix found: {k_suffix}")
            print(f"Match found: {hex_hash}")
            return k_suffix

    return "No hash found..."


def part_2(data: list) -> int:
    """Return solution for part_2.
    url: https://adventofcode.com/2015/day/4#part2
    """
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    # print(f"PT_2| Solution: {part_2(input_data)}")
