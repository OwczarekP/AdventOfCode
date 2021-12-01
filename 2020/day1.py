with open('./inputs/day1.txt') as f:
    input_list = [int(x) for x in f.read().splitlines()]


def count_increased(depth_list):
    increases = sum([1 if (depth_list[i] < depth_list[i+1]) else 0 for i in range(len(depth_list)-1)])
    return increases


print(count_increased(input_list))


#Part two
def count_increased_sums(depth_list):
    to_skip = 3-len(depth_list) % 3
    increases = sum([1 if (sum(depth_list[i:i+3]) < sum(depth_list[i+1:i+4])) else 0 for i in range(0, len(depth_list)-to_skip)])
    return increases


print(count_increased_sums(input_list))