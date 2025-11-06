"""
url:    https://adventofcode.com/2015/day/4
tags:   md5, hash, cryptography
"""

from pathlib import Path
import hashlib


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip()


def find_suffix(data: list, hash_prefix: str) -> str:
    """Brute force solution to get lowest decimal number that creates the valid MD5 hash.

    Will there always be an answer?

    Is there a way to apply a sorting algo to decimal generation? How do You tell if a guess is better or worse?
    """
    k_prefix = "".join(data)
    n = len(hash_prefix)  # 0000

    # Generate decimals
    for i in range(0, 10000000):
        k_suffix = i

        k = f"{k_prefix}{k_suffix}"
        hex_hash = hashlib.md5(k.encode()).hexdigest()

        if hex_hash[:n] == hash_prefix:
            print(f"Suffix found: {k_suffix}")
            print(f"Hash found: {hex_hash}")
            return k_suffix

    return "No hash found..."


def part_1(data: list) -> str:
    return find_suffix(data=data, hash_prefix="00000")


def part_2(data: list) -> int:
    return find_suffix(data=data, hash_prefix="000000")


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
