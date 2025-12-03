"""
url:    https://adventofcode.com/
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
    return input_file.read_text().strip().splitlines()


PRODUCT_IDS = """9100-11052,895949-1034027,4408053-4520964,530773-628469,4677-6133,2204535-2244247,55-75,77-96,6855-8537,55102372-55256189,282-399,228723-269241,5874512-6044824,288158-371813,719-924,1-13,496-645,8989806846-8989985017,39376-48796,1581-1964,699387-735189,85832568-85919290,6758902779-6759025318,198-254,1357490-1400527,93895907-94024162,21-34,81399-109054,110780-153182,1452135-1601808,422024-470134,374195-402045,58702-79922,1002-1437,742477-817193,879818128-879948512,407-480,168586-222531,116-152,35-54
"""

product_data = PRODUCT_IDS.split(",")
parsed_data = [pd.strip() for pd in product_data]


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
