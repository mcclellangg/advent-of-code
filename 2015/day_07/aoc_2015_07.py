"""
url:    https://adventofcode.com/2015/day/7
tags:   bitwise-ops, fun, circuit, bobby, dependency-graph

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

    # BUG: this is halfway finished, I wrote this much then had Gemini bring it home.
    """
    assert len(data) == 339

    wire_to_cmd = {}  # "ai": "af AND ah" # BUG: create better pre-parsing
    bw_ops = ["NOT", "AND", "RSHIFT", "LSHIFT", "OR"]

    for instruction in data:
        parsed = instruction.split(" -> ")
        wire_to_cmd[parsed[1]] = parsed[0].split(" ")  # [x, ["af", "AND", "ab"]]

    def resolve_wire(wire: str):
        signal = wire_to_cmd[wire]

        if isinstance(signal, int):
            return signal

        # Add logic to parse commands
        # NOTE: small edge case if there is a num in the command

        # NOTE: I got this far and understood the logic of what I wanted, but was too lazy to write it out, and to also write out a dispatch table. I felt pretty good that would solve this problem so I then pawned that work off onto Gemini.

        if len(signal) == 3 and signal[2].isalpha():
            pass

    return wire_to_cmd


import operator
from functools import lru_cache


def part_1_gemini(data: list) -> int:
    """
    Look into aspects I don't fully understand before moving on:
    - lru_cache (never used this before)
    - why call the operations 'tokens'?

    Things I don't like about this:
    - redundant and ambiguous naming (res AND result), just say signal
    - do I NEED lru? Why not just use a dict? That seems more explicit

    Solution:
    - https://gemini.google.com/share/03709a394f82
    """
    assert len(data) == 339

    wire_to_cmd = {}
    mask = 0xFFFF

    # 1. Dispatch Table for bitwise operations
    # We use lambdas or operator functions for consistency
    dispatch = {
        "AND": operator.and_,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        "NOT": lambda val: ~val & mask,
    }

    # Pre-parse: Map output wire to its command list
    for instruction in data:
        command, output_wire = instruction.split(" -> ")
        wire_to_cmd[output_wire] = command.split(" ")

    @lru_cache(None)
    def resolve(wire):
        # Base case: if the "wire" is actually a number string (e.g., "123")
        if wire.isdigit():
            return int(wire)

        # Since the cmd value is not a specific value, refer to them generically as `tokens`
        tokens = wire_to_cmd[wire]

        # Case 1: Direct Assignment (e.g., "123 -> x" or "lx -> ly")
        if len(tokens) == 1:
            res = resolve(tokens[0])

        # Case 2: Unary Operation (e.g., "NOT ax -> ay")
        elif len(tokens) == 2:
            op = tokens[0]
            val = resolve(tokens[1])
            res = dispatch[op](val)

        # Case 3: Binary Operation (e.g., "x AND y -> z")
        elif len(tokens) == 3:
            left = resolve(tokens[0])
            op = tokens[1]
            right = resolve(tokens[2])
            res = dispatch[op](left, right)

        return res & mask

    # Assuming we are looking for the signal on wire 'a'
    return resolve("a")


def part_1_no_lru(data: list) -> int:
    """
    lru is just syntactic sugar for using a regular dictionary.

    I got some feedback from Claude, and updated variables to make more sense to me.
    """
    assert len(data) == 339

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

    for instruction in data:
        command, output_wire = instruction.split(" -> ")
        wire_to_cmd[output_wire] = command.split(" ")

    # part2
    wire_to_cmd["b"] = ["956"]

    def resolve(wire):
        if wire in cache:
            return cache[wire]

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

        signal = signal & mask
        cache[wire] = signal
        return signal

    return resolve("a")


def part_2(data: list) -> int:
    """Return solution for part_2."""
    # Change wire b to '956' reset, and rerun
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    # print(f"PT_1| Solution: {part_1(input_data)}")
    # print(f"Gem PT 1| Solution {part_1_gemini(input_data)}")
    print(f"PT 1| No LRU Solution {part_1_no_lru(input_data)}")
    print(f"PT_2| Solution: {part_2(input_data)}")
