with open("inputs/input_day_1.txt") as f:
    modules_mass = [int(x) for x in f.read().split()]

print(modules_mass)

def required_fuel(masses):
    return sum((int(mass/3))-2 for mass in masses)

print(required_fuel(modules_mass))

def required_fuel_p2(masses):
    """Required fuel changed to part 2 of challange"""
    fuel_sum = 0
    fuels = [(int(mass/3))-2 for mass in masses]
    for fuel in fuels:
        while fuel > 0:
            fuel_sum += fuel
            fuel = (int(fuel/3))-2
    return fuel_sum

print(required_fuel_p2([1969]))
print(required_fuel_p2(modules_mass))