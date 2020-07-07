with open("inputs/input_day_1.txt") as f:
    modules_mass = [int(x) for x in f.read().split()]

print(modules_mass)

def required_fuel(masses):
    fuel_sum = 0 
    for mass in masses:
        fuel_sum += (int(mass/3))-2
    print(fuel_sum)

required_fuel(modules_mass)