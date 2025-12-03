"""
url:    https://adventofcode.com/2025/day/1
tags:   brute_force
log:    pt_1 (35m)
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
    The dial starts at 50.
    The dial is a circle from 0 to 99.
    Moving L is lower/towards 0, moving R is higher/towards 99.

    How many times does the dial point at 0?
    """
    # assert len(data) == 4570
    password = 0
    dial_position = 50

    def normalize(rotation: str) -> int:
        direction = rotation[0]
        r = int(rotation[1:])
        return -r if direction == "L" else r

    for line in data:
        dial_shift = normalize(line)
        new_position = dial_position + dial_shift

        if new_position > 99:
            while new_position > 99:
                new_position -= 100
        elif new_position < 0:
            while new_position < 0:
                new_position += 100

        dial_position = new_position
        if dial_position == 0:
            password += 1

    return password


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
