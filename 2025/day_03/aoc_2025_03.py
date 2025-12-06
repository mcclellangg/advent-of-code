"""
url:    https://adventofcode.com/2025/day/3
tags:   second-largest, todo
log:    pt1 55m
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
    """
    07:50 -> 08:45

    BRUTE FORCE
    """
    total_output_joltage = 0

    for bank in data:
        # iter bank and find largest, and second largest
        b = list(bank)
        jolt_indices = []
        jolt_indices.append(b.index(max(b[:-1])) + 1)
        jolt_indices.append((b.index(max(b[jolt_indices[0] :]))))

        jolt_indices[0] -= 1
        max_voltage = [b[i] for i in jolt_indices]

        total_output_joltage += int("".join(max_voltage))

    return total_output_joltage


def part_2(data: list) -> int:
    """
    HINT: https://www.reddit.com/r/adventofcode/comments/1pcwuu8/2025_day_3_any_hint_to_solve_part_2/

    Try sliding window approach.
    """
    return 0


if __name__ == "__main__":
    input_data = parse_input(full=True)
    print(f"PT_1| Solution: {part_1(input_data)}")
    # print(f"PT_2| Solution: {part_2(input_data)}")
