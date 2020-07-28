import pytest

with open("2019/inputs/input_day_1.txt") as f:
    modules_mass = [int(x) for x in f.read().split()]


def required_fuel(masses):
    return sum((int(mass/3))-2 for mass in masses)


def required_fuel_p2(masses):
    """Required fuel changed to part 2 of challange"""
    fuel_sum = 0
    fuels = [(int(mass/3))-2 for mass in masses]
    for fuel in fuels:
        while fuel > 0:
            fuel_sum += fuel
            fuel = (int(fuel/3))-2
    return fuel_sum


def test():
    assert required_fuel([1969]) == 654
    assert required_fuel([100756]) == 33583
    assert required_fuel_p2([1969]) == 966
    assert required_fuel_p2([100756]) == 50346
    

test()    
print(required_fuel(modules_mass))
print(required_fuel_p2(modules_mass))
