from shapely import Polygon


def get_next(curr, act):
    dircn, length = act
    curr_y, curr_x = curr
    if dircn == "3": return (curr_y + length, curr_x)
    elif dircn == "1": return (curr_y - length, curr_x)
    elif dircn == "2": return (curr_y, curr_x - length)
    elif dircn == "0": return (curr_y, curr_x + length)


file = open("input.txt", "r")
lines = file.read().splitlines()
plan = [line.split()[2] for line in lines]
plan = [(act[-2], int(act[2:7], 16)) for act in plan]

current = (0, 0)
loop = [current]
for act in plan:
    current = get_next(current, act)
    loop.append(current)

polygon = Polygon(loop)
print(int(polygon.area + polygon.length / 2 + 1))

file.close()
