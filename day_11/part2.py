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

glxs = np.where(sky == "#")
# Rows
for glx_idx, glx in enumerate(glxs[0]):
    n_less = len([row for row in rows if row < glx])
    exp = 1000000
    if n_less > 0:
        glxs[0][glx_idx] = ((exp - 1) * n_less) + glx
# Cols
for glx_idx, glx in enumerate(glxs[1]):
    n_less = len([col for col in cols if col < glx])
    exp = 1000000
    if n_less > 0:
        glxs[1][glx_idx] = ((exp - 1) * n_less) + glx
glxs = np.transpose(glxs).tolist()
pairs = list(combinations(glxs, 2))
lengths = [abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in pairs]

print(sum(lengths))

file.close()
