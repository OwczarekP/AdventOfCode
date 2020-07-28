with open("2019/inputs/input_day_3.txt") as f:
    wires = [line.strip().split(',') for line in f]

wire_1 = wires[0]
wire_2 = wires[1]

#Part 1
def wire_coordinates(input):
    coordinates = []
    xy = [0,0]
    for i in input:
        for _ in range(int(i[1:])):
            if i[0] == 'L': xy[0] -= 1
            elif i[0] == 'R':xy[0] += 1
            elif i[0] == 'U': xy[1] += 1
            elif i[0] == 'D': xy[1] -= 1
            coordinates.append(tuple(xy[:]))
    return coordinates


def manhatan(wire1, wire2):
    coord_1 = wire_coordinates(wire1)
    coord_2 = wire_coordinates(wire2)
    intercepts = list(set(coord_1).intersection(set(coord_2)))
    abs_values = [(abs(i[0]), abs(i[1])) for i in intercepts]
    distance = min([sum(i) for i in abs_values])
    return distance

#Part 2
def wire_coordinates_steps(wire):
    coordinates = set()
    steps = {}
    num_steps = 0
    xy = [0, 0]
    for move in wire:
        dir = move[0]
        distance = int(move[1:])

        if dir== 'L':
            for moved in range(0, distance):
                coordinates.add((xy[0] - moved, xy[1]))
                steps[(xy[0] - moved, xy[1])] = num_steps
                num_steps += 1
            xy[0] -= distance

        elif dir == 'R':
            for moved in range(0, distance):
                coordinates.add((moved + xy[0], xy[1]))
                steps[(moved + xy[0], xy[1])] = num_steps
                num_steps += 1
            xy[0] += distance

        elif dir == 'U':
            for moved in range(0, distance):
                coordinates.add((xy[0], moved + xy[1]))
                steps[(xy[0], moved + xy[1])] = num_steps
                num_steps += 1
            xy[1] += distance

        elif dir == 'D':
            for moved in range(0, distance):
                coordinates.add((xy[0], xy[1] - moved))
                steps[(xy[0], xy[1] - moved)] = num_steps
                num_steps += 1
            xy[1] -= distance

    return coordinates, steps
    

def manhatan_steps(wire1, wire2):
    wire_coord_1, nb_steps_1 = wire_coordinates_steps(wire1)
    wire_coord_2, nb_steps_2 = wire_coordinates_steps(wire2)
    intersections = wire_coord_1 & wire_coord_2
    distance = 0
    for crossed in intersections:
        combined_steps = nb_steps_1[crossed] + nb_steps_2[crossed]
        if not distance or combined_steps < distance:
            distance = combined_steps
    return distance


def test():
    test_1_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    test_1_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
    assert manhatan(test_1_1, test_1_2) == 159
    assert manhatan_steps(test_1_1, test_1_2) == 610


test()

print(manhatan(wire_1, wire_2))
print(manhatan_steps(wire_1, wire_2))