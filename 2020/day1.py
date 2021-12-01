
with open('./inputs/day1.txt') as f:
    depth_list = [int(x) for x in f.read().splitlines()]


def count_increased(depth_list):
    increases = 0
    increases = sum([1 if (depth_list[i] < depth_list[i+1]) else 0 for i in range(len(depth_list)-1)])
    return increases

print(count_increased(depth_list))