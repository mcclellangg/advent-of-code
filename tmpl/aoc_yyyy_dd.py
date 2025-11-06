"""
url:    https://adventofcode.com/
tags:   tag1
"""

from pathlib import Path


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip()


def part_1(data: list) -> int:
    """Return solution for part_1."""
    return 0


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
