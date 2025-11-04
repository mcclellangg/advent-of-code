"""
# Day 02

url: https://adventofcode.com/2015/day/2
"""

from pathlib import Path

# Part 1 #

# Load and parse input
FILE_PATH = Path(__file__).parent / "input.txt"
data = FILE_PATH.read_text().strip().splitlines()
dimensions = [d.split("x") for d in data]  # Sort seems expensive

# Verify input
assert len(dimensions) == 1000

total_sq_ft = 0

# Calculate sq ft
for d in dimensions:
    d = [int(s) for s in d]
    d.sort()
    l, w, h = d[0], d[1], d[2]
    slack = d[0] * d[1]
    sq_ft = (2 * (l * w)) + (2 * (w * h)) + (2 * (h * l))

    total_sq_ft += slack + sq_ft

print(f"Total sq ft to order: {total_sq_ft}")

# Part 2 #
"https://adventofcode.com/2015/day/2#part2"

total_ft_ribbon = 0

# Calculate total ribbon needed
for d in dimensions:
    d = [int(s) for s in d]
    d.sort()
    l, w, h = d[0], d[1], d[2]
    ft_wrap = (l * 2) + (w * 2)
    ft_bow = l * w * h

    total_ft_ribbon += ft_wrap + ft_bow

print(f"Total ft ribbon to order: {total_ft_ribbon}")
