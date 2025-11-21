"""
url:    https://adventofcode.com/2015/day/7
tags:   todo
log:    20m
"""

from pathlib import Path


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip().splitlines()


def part_1(data: list) -> int:
    """
    Return the signal of wire a.

    Create a graph to represent wires, and gates
    """
    assert len(data) == 339

    # Iter instructions and build circuit

    # Circuit rules (wires first, then gates)
    # All wires have signal via (value, -> wire, gate)
    # All wires get signal from ONE source
    # Gates provide NO signal until all inputs have a signal
    # Suspect wires are one way (a -> b NOT b -> a)

    return 0


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
