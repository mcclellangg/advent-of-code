"""
# Day 03

url: https://adventofcode.com/2015/day/3
part2: https://adventofcode.com/2015/day/3#part2
"""
from pathlib import Path


# Part 1 # 

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

print(f"PT_1| Visited at least once: {len(visited)}")

# Part 2 #

santa_xy = (0,0)
robo_xy = (0,0)
positions = [(0,0)] # (0,1)
direction_to_update = {
    "<": (-1, 0), # WEST
    ">": (1, 0), # EAST
    "^": (0, 1), # NORTH
    "v": (0, -1) # SOUTH
}

# ^v^v^v^v^v -> 11
for i,d in enumerate(input_data):
    if i % 2 == 0:
        # santa's turn
        x,y = santa_xy[0], santa_xy[1] # 0,0
        update = direction_to_update[d] # (0,1)
        new_position = (x + update[0], y + update[1]) # (0,1)
        positions.append(new_position)
        santa_xy = new_position
    else:
        # robots turn
        x,y = robo_xy[0], robo_xy[1]
        update = direction_to_update[d]
        new_position = (x + update[0], y + update[1])
        positions.append(new_position)
        robo_xy = new_position

visited_once = set(positions)
print(f"PT_2| Visited at least once: {len(visited_once)}")