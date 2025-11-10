"""
url:    https://adventofcode.com/2015/day/6
tags:   9:48 -> 9:59 | 10:10 -> 10:33
"""

from pathlib import Path


# Load input
def parse_input() -> list:
    """
    Return input in the form of a list.

    Return instructions. A list of dicts that map the action ('on', 'off', 'toggle' to the coordinates.)

    {"on": [(000,000), (759,859)]}
    """
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text().strip().splitlines()

    instructions = []

    for line in data:
        action_to_coords = {}
        l = line.split(sep=" ")
        action = l[1]  # ['turn', 'on', '489,959', 'through', '759,964']
        if action == "on" or action == "off":
            start = l[2].split(sep=",")
            end = l[4].split(sep=",")

            action_to_coords[action] = [
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1])),
            ]
        else:
            action = "toggle"
            start = l[1].split(sep=",")
            end = l[3].split(sep=",")

            action_to_coords[action] = [
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1])),
            ]

        instructions.append(action_to_coords)

    return instructions


light_grid = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
ACTION_TO_VAL = {"on": 1, "off": 0, "toggle": {0: 1, 1: 0}}


def part_1(data: list) -> int:
    assert len(data) == 300

    # iterate instructions
    # update grid based on action
    # return count of 1s in grid

    return 0


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
