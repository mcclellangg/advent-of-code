"""
url:    https://adventofcode.com/2025/day/2
tags:   brute_force
log:    pt_1 (30m)
"""

from pathlib import Path
from typing import NewType

Data = NewType("Data", list[str])


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"

    input_file = Path(__file__).parent / file_name
    product_data = input_file.read_text().strip().split(",")

    return [pd.strip() for pd in product_data]


def part_1(data: list) -> int:
    invalid_id_total = 0

    for id_range_str in data:
        assert "\n" not in id_range_str
        id_ranges = id_range_str.split("-")
        start, end = id_ranges[0], id_ranges[1]

        for i in range(int(start), int(end) + 1):
            num_str = str(i)
            n = len(num_str)
            mid = int(n / 2)
            if n % 2 == 0:
                if num_str[:mid] == num_str[mid:]:
                    invalid_id_total += int(num_str)

    return invalid_id_total


if __name__ == "__main__":
    input_data = parse_input()
    print(f"PT_1| Solution: {part_1(input_data)}")
