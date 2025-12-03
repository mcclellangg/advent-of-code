"""
url:    https://adventofcode.com/2025/day/3
tags:   todo
log:    00m
"""

from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"

    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().splitlines()


def part_1(data: list) -> int:
    """Return solution for part_1."""
    return 0


# def part_2(data: list) -> int:
#     """Return solution for part_2."""
#     return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    # print(f"PT_2| Solution: {part_2(input_data)}")
