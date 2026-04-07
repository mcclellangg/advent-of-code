"""
url:    https://adventofcode.com/2015/day/8
tags:   stdout, str, ast
"""

from pathlib import Path
from typing import NewType
import ast

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().splitlines()


def part_1(data: list) -> int:
    """
    data still contains raw file text which is why `len(line)` returns number of characters of code.

    ast, Abstract syntax trees
    """
    assert len(data) == 300

    diff = 0

    for line in data:
        diff += len(line) - len(ast.literal_eval(line))

    print(f"Diff: {diff}")

    return diff


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    # print(f"PT_2| Solution: {part_2(input_data)}")
