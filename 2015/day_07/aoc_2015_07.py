"""
url:    https://adventofcode.com/2015/day/7
tags:   bitwise-ops, fun, circuit, bobby, dependency-graph

# RESOURCES #
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types

# NOTE #

Use Gemini to refactor previous solutions:
- https://gemini.google.com/share/67f8ae5dd094
- See commit b1ecc4b8519578a581c6ab5c7f3501b3f4b8d46c for all notes
"""

from pathlib import Path
from pprint import pprint
import operator


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip().splitlines()


def solve_circuit(data: list, b_override: int = None) -> int:
    """
    Solves the circuit.
    If b_override is provided, wire 'b' is set to that value before execution.
    """
    wire_to_cmd = {}
    cache = {}
    mask = 0xFFFF

    dispatch = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        "NOT": lambda val: ~val & mask,
    }

    # Pre-parse instructions
    for instruction in data:
        command, output_wire = instruction.split(" -> ")
        wire_to_cmd[output_wire] = command.split(" ")

    # Part 2 logic: Override wire 'b' if a value is passed
    if b_override is not None:
        wire_to_cmd["b"] = [str(b_override)]

    def resolve(wire):
        # Check cache (Memoization)
        if wire in cache:
            return cache[wire]

        # Base case: raw numbers
        if wire.isdigit():
            return int(wire)

        tokens = wire_to_cmd[wire]

        # Case 1: Direct Assignment (e.g., "123 -> x" or "lx -> ly")
        if len(tokens) == 1:
            signal = resolve(tokens[0])

        # Case 2: Unary Operation (e.g., "NOT ax -> ay")
        elif len(tokens) == 2:
            op = tokens[0]
            val = resolve(tokens[1])
            signal = dispatch[op](val)

        # Case 3: Binary Operation (e.g., "x AND y -> z")
        elif len(tokens) == 3:
            left = resolve(tokens[0])
            op = tokens[1]
            right = resolve(tokens[2])
            signal = dispatch[op](left, right)

        # Apply 16-bit mask and cache result
        signal &= mask
        cache[wire] = signal
        return signal

    return resolve("a")


def part_2(data: list) -> int:
    """
    1. Get the result of Part 1.
    2. Pass that result as an override for wire 'b'.
    3. The function naturally resets the cache because it's local to the call.
    """
    a_signal_part_1 = solve_circuit(data)
    return solve_circuit(data, b_override=a_signal_part_1)


if __name__ == "__main__":
    input_data = parse_input()

    ans_1 = solve_circuit(input_data)
    ans_2 = part_2(input_data)

    print(f"PT 1| Solution: {ans_1}")
    print(f"PT 2| Solution: {ans_2}")
