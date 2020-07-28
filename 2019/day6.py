with open("2019/inputs/input_day_6.txt") as f:
    map_data = [x for x in f.read().split()]

direct_orbits = {}

def get_direct_orbits(orbits_data):
    for orbits in orbits_data:
        orbit_1, orbit_2 = orbits.split(')')
        direct_orbits[orbit_2] = orbit_1

def get_all_oribits(objects_dict):
    orbits_sum = 0
    for orbit in objects_dict:
        next_orbit = objects_dict.get(orbit)
        while next_orbit:
            orbits_sum += 1
            next_orbit = objects_dict.get(next_orbit)
    return orbits_sum

def get_path_oribits(objects_dict, searched_orbit, path):
    next_orbit = objects_dict.get(searched_orbit)
    while next_orbit:
        path.append(next_orbit)
        next_orbit = objects_dict.get(next_orbit)
    return path


def find_minimum_path(path_1, path_2):
    i = 0
    for orbit in path_1:
        if orbit not in path_2:
            i += 1
        if orbit in path_2:
            i += path_2.index(orbit)
            break
    return i


you_path = []
san_path = []

get_direct_orbits(map_data)
print(get_all_oribits(direct_orbits))
you_path = get_path_oribits(direct_orbits, 'YOU', you_path)
san_path = get_path_oribits(direct_orbits, 'SAN', san_path)
print(find_minimum_path(you_path, san_path))
 