import pytest

with open("inputs/input_day_2.txt") as f:
    intcode = [int(x) for x in f.read().split(',')]


intcode[1] = 12
intcode[2] = 2
print(intcode)

def read_intcode(input):
    for i in range(0, len(input), 4):
        if input[i] == 1:
            input[input[i+3]] =  input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] =  input[input[i+1]] * input[input[i+2]]
        elif input[i] == 99:
            break

def test():
    test_intcode = [1, 0, 0, 0, 99]
    test_intcode_2 = [1,1,1,4,99,5,6,0,99]
    read_intcode(test_intcode) 
    read_intcode(test_intcode_2)
    assert test_intcode[0] == 2
    assert test_intcode_2[0] == 30
    print(test_intcode_2)

test()
read_intcode(intcode)
print(intcode[0])