"""
url:    https://adventofcode.com/2015/day/6
tags:
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
            start_coords = l[2].split(sep=",")
            end_coords = l[4].split(sep=",")

            action_to_coords[action] = [
                (int(start_coords[0]), int(start_coords[1])),
                (int(end_coords[0]), int(end_coords[1])),
            ]
        else:
            action = "toggle"
            start_coords = l[1].split(sep=",")
            end_coords = l[3].split(sep=",")

            action_to_coords[action] = [
                (int(start_coords[0]), int(start_coords[1])),
                (int(end_coords[0]), int(end_coords[1])),
            ]

        instructions.append(action_to_coords)

    return instructions


# Part 1 #

light_grid = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
ACTION_TO_VAL_PT1 = {"on": 1, "off": 0, "toggle": {0: 1, 1: 0}}


def part_1(data: list) -> int:
    """
    Brute force solution.
    """
    assert len(data) == 300
    # {"on": [(000,000), (759,859)]}

    # iterate instructions
    for i in data:
        action = list(i)[0]
        val = ACTION_TO_VAL_PT1[action]
        coords = i[action]
        start_r, start_c = coords[0][0], coords[0][1]
        end_r, end_c = coords[1][0], coords[1][1]

        # Update the matrix
        if action == "toggle":
            for r in range(start_r, end_r + 1):
                for c in range(start_c, end_c + 1):
                    light_grid[r][c] = ACTION_TO_VAL_PT1["toggle"][light_grid[r][c]]

        else:
            for r in range(start_r, end_r + 1):
                for c in range(start_c, end_c + 1):
                    light_grid[r][c] = val

    # Count lights that are on
    ttl_lights_on = 0

    for row in range(len(light_grid)):
        ttl_lights_on += light_grid[row].count(1)

    return ttl_lights_on


# Part 2 #
ACTION_TO_VAL_PT2 = {"on": 1, "off": -1, "toggle": 2}


def part_2(data: list) -> int:
    """
    Brute force solution to calculate total brightness.

    Example value data[i]:
    {"on": [(000,000), (759,859)]}
    """

    assert len(data) == 300

    # Reset grid
    light_grid = [[0 for i in range(0, 1000)] for i in range(0, 1000)]

    # iterate instructions
    for i in data:
        action = list(i)[0]
        update_val = ACTION_TO_VAL_PT2[action]
        start_pos, end_pos = i[action][0], i[action][1]

        # Update grid
        for r in range(start_pos[0], end_pos[0] + 1):
            for c in range(start_pos[1], end_pos[1] + 1):
                current_val = light_grid[r][c]
                if action == "off" and current_val == 0:
                    # Light cannot be less than 0
                    continue
                light_grid[r][c] += update_val

    # calculate total brightness
    total_brightness = 0
    for row in range(0, 1000):
        total_brightness += sum(light_grid[row])

    return total_brightness


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
