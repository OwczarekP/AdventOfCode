with open("inputs/input_day_3.txt") as f:
    wires = [line.strip().split(',') for line in f]

wire_1 = wires[0]
wire_2 = wires[1]

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

def manhatan(coord_1, coord_2):
    intercepts = list(set(coord_1).intersection(set(coord_2)))
    abs_values = [(abs(i[0]), abs(i[1])) for i in intercepts]
    distance = min([sum(i) for i in abs_values])
    return distance


coordinate_1 = wire_coordinates(wire_1)
coordinate_2 = wire_coordinates(wire_2)
print(manhatan(coordinate_1, coordinate_2))

