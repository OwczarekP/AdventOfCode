import copy

with open('./inputs/day3.txt') as f:
    input_list = f.read().splitlines()


def count_gamma_epsilon(binary_list, reverse=False): #reverse for part two
    epsilon = ''
    gamma = ''
    for i in range(len(binary_list[0])):
        count = 0
        for line in binary_list:
            if line[i] == '1':
                count += 1
        if count > len(binary_list)/2:
            gamma += '1'
            epsilon += '0'
        elif count == len(binary_list)/2:
            if reverse:
                gamma += '0'
                epsilon += '0'
            else:
                gamma += '1'
                epsilon += '1'
        else:
            gamma += '0'
            epsilon += '1'
    return gamma, epsilon


gam, eps = count_gamma_epsilon(input_list)
print(int(eps, 2) * int(gam, 2))

#Part two

def get_oxygen(binary_list):
    oxygen = copy.deepcopy(binary_list)
    oxygen = list(set(oxygen))
    for i in range(0, len(binary_list[0])):
        most_common = count_gamma_epsilon(oxygen)[0]
        for k in range((len(oxygen)-1), -1, -1):
            if oxygen[k][i] != most_common[i]:
                oxygen.remove(oxygen[k])
            if len(oxygen) == 1:
                return oxygen[0]


def get_co2(binary_list):
    co2 = copy.deepcopy(binary_list)
    co2 = list(set(co2))
    for i in range(0, len(binary_list[0])):
        least_common = count_gamma_epsilon(co2, reverse=True)[1]
        for k in range((len(co2)-1), -1, -1):
            if co2[k][i] != least_common[i]:
                co2.remove(co2[k])
            if len(co2) == 1:
                return co2[0]


oxy = get_oxygen(input_list)
co = get_co2(input_list)
print(int(oxy, 2) * int(co, 2))



