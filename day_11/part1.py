from itertools import combinations
import numpy as np

file = open("input.txt", "r")
lines = file.read().splitlines()
lines = [list(line) for line in lines]
sky = np.array(lines)

empt = (sky == ".")
rows = np.all(empt, axis=1)
cols = np.all(empt, axis=0)
rows = np.where(rows)[0]
cols = np.where(cols)[0]
sky = np.insert(sky, rows, ".", axis=0)
sky = np.insert(sky, cols, ".", axis=1)

glxs = np.transpose(np.where(sky == "#")).tolist()
pairs = list(combinations(glxs, 2))
lengths = [abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) for g1, g2 in pairs]

print(sum(lengths))

file.close()
