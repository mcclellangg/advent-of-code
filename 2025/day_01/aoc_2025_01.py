"""
url:    https://adventofcode.com/2025/day/1
tags:   brute_force, todo
log:    pt_1 (35m) | pt_2 (01h20m)
"""

from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"

    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().splitlines()


# FUNCTIONS
def normalize(rotation: str) -> int:
    direction = rotation[0]
    r = int(rotation[1:])
    return -r if direction == "L" else r


def part_1(data: list) -> int:
    """
    The dial starts at 50.
    The dial is a circle from 0 to 99.
    Moving L is lower/towards 0, moving R is higher/towards 99.

    How many times does the dial point at 0?
    """

    password = 0
    dial_position = 50

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


def part_2(data: list) -> int:
    """
    This one really threw me for a loop. TODO: compare with others and see how it's done!
    """
    dial_position = 50  # 0 - 99
    password = 0  # increases on 0

    for rotation in data:
        r = normalize(rotation)  # 1 - 600 (+/-)

        # count excess rotations first
        while r > 100:
            r -= 100
            password += 1
        while r < -100:
            r += 100
            password += 1

        # r should be [-100, 100]
        new_position = dial_position + r
        if new_position == 0:
            password += 1

        # in range 0-99
        while new_position > 99:
            new_position -= 100
            password += 1

        # Negative positions are handled incorrectly
        while new_position < 0:
            new_position += 100
            if dial_position != 0:
                password += 1

        # update dial
        dial_position = new_position

    return password


if __name__ == "__main__":
    input_data = parse_input(full=True)
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
