"""
# Day 03

url: https://adventofcode.com/2015/day/3
"""
from pathlib import Path


# Part 1 # 

# Whiteboard
# 10:09 -> 10:17
# 10:30 -> 10:47

# Load input
input_file = Path(__file__).parent / 'input.txt'
input_data = input_file.read_text().strip() # <>>>vv^^^

# Solve 
positions = [(0,0)]
current = (0,0) # x,y
direction_to_update = {
    "<": (-1, 0), # WEST
    ">": (1, 0), # EAST
    "^": (0, 1), # NORTH
    "v": (0, -1) # SOUTH

}

# iter directions
for d in input_data:
    x,y = current[0], current[1]
    update = direction_to_update[d]
    new_position = (x + update[0], y + update[1])
    positions.append(new_position)
    current = new_position

visited = set(positions)

print(f"Houses with >= 1 gift: {len(visited)}")

# Part 2 #
# https://adventofcode.com/2015/day/3#part2
