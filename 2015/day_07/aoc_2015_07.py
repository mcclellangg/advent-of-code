"""
url:    https://adventofcode.com/2015/day/7
tags:   bitwise-ops, fun, circuit, bobby

# RESOURCES #
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
"""

from pathlib import Path
from pprint import pprint


# Load input
def parse_input() -> list:
    """Return input in the form of a list."""
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text().strip().splitlines()


# Emulate sample
def emulate_circuit() -> dict:
    """
    Perform a series of bitwise operations and return a map of signal_wire -> value.
    """
    operations = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]

    circuit_map = {
        "x": 123,
        "y": 456,
    }

    circuit_map["d"] = circuit_map["x"] & circuit_map["y"]
    circuit_map["e"] = circuit_map["x"] | circuit_map["y"]
    circuit_map["f"] = circuit_map["x"] << 2
    circuit_map["g"] = circuit_map["y"] >> 2
    circuit_map["h"] = ~circuit_map["x"] & 0xFFFF  # NOT 123 = 65412
    circuit_map["i"] = ~circuit_map["y"] & 0xFFFF  # NOT 456 = 65079

    # sort map in alphabetical order
    return dict(sorted(circuit_map.items()))


# TEST Emulation #
# from pprint import pprint
# emulated = emulate_circuit()
# pprint(emulated)


def part_1(data: list) -> dict:
    """
    Return the signal of wire a.

    Create a map to represent wires, and emulate the circuit.
    Emulate the circuit by iterating over the instructions, and then return the value of the needed wire.
    """
    assert len(data) == 339

    wire_to_cmd = {}  # "ai": "af AND ah"
    bw_ops = ["NOT", "AND", "RSHIFT", "LSHIFT", "OR"]

    for instruction in data:
        parsed = instruction.split(" -> ")
        wire_to_cmd[parsed[1]] = parsed[0]

    # I'm worried recursion won't solve it ... (I don't think I can always reach the base case ...)
    # NOW: Go over cmds until ALL wires have a signal
    # for each wire (signal, or cmds)
    # if signal return
    # if cmds then
    # parse to find wires, get signal from wires

    # How to handle executing ops once you have signals?

    return wire_to_cmd


def part_2(data: list) -> int:
    """Return solution for part_2."""
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
