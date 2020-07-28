with open("inputs/input_day_6.txt") as f:
    map_data = [x for x in f.read().split()]

direct_orbits = {}

def get_direct_orbits(orbits_data):
    for orbits in orbits_data:
        orbit_1, orbit_2 = orbits.split(')')
        direct_orbits[orbit_2] = orbit_1

def get_all_oribits(objects_dict):
    orbits_sum = 0
    for orbiter in objects_dict:
        next_orbit = objects_dict.get(orbiter, None)
        while next_orbit:
            orbits_sum += 1
            next_orbit = objects_dict.get(next_orbit, None)
    return orbits_sum

get_direct_orbits(map_data)
print(get_all_oribits(direct_orbits))
 