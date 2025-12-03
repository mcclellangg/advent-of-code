import aoc_2025_01 as challenge

PRODUCT_IDS = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

sample_input_01 = challenge.parse_input(file_name="sample_01.txt")
sample_input_02 = PRODUCT_IDS.split(",")
full_input = challenge.parse_input()


def test_part_1_sample_input():
    result = challenge.part_1(sample_input_01)
    assert result == 3


def test_part_1_full_input():
    result = challenge.part_1(full_input)
    assert result == 1152


def test_part_2_sample_input():
    result = challenge.part_2(sample_input_02)
    assert result == 1227775554


def test_part_2_full_input():
    result = challenge.part_2(full_input)
    assert result == 0
