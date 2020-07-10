import pytest
import copy

with open("inputs/input_day_2.txt") as f:
    intcode = [int(x) for x in f.read().split(',')]


intcode_copy = copy.deepcopy(intcode)
intcode[1] = 12
intcode[2] = 2


def read_intcode(input):
    for i in range(0, len(input), 4):
        if input[i] == 1:
            input[input[i+3]] =  input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] =  input[input[i+1]] * input[input[i+2]]
        elif input[i] == 99:
            break
    return input[0]


def find_parameters():
    for noun in range(100):
        for verb in range(100):
            memory = intcode_copy.copy()
            memory[1] = noun
            memory[2] = verb
            if read_intcode(memory) == 19690720:
                return 100 * noun + verb


def test():
    test_intcode = [1, 0, 0, 0, 99]
    test_intcode_2 = [1,1,1,4,99,5,6,0,99]
    assert read_intcode(test_intcode) == 2
    assert read_intcode(test_intcode_2) == 30

test()
print(read_intcode(intcode))
print(find_parameters())