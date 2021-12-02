import re

with open('./inputs/day2.txt') as f:
    input_list = f.read().splitlines()


def get_coordinates(move_list):
    horizontal = 0
    depth = 0
    for line in move_list:
        move = int(re.search("[0-9]+", line)[0])
        if "forward" in line:
            horizontal += move
        elif "down" in line:
            depth += move
        elif "up" in line:
            depth -= move
        else:
            return ValueError
    return horizontal * depth


print(get_coordinates(input_list))


#Part two
def get_coordinates_p2(move_list):
    horizontal = 0
    depth = 0
    aim = 0
    for line in move_list:
        move = int(re.search("[0-9]+", line)[0])
        if "forward" in line:
            horizontal += move
            depth += aim * move
        elif "down" in line:
            aim += move
        elif "up" in line:
            aim -= move
        else:
            return ValueError
    return horizontal * depth


print(get_coordinates_p2(input_list))
