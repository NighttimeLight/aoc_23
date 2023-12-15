from itertools import product
import numpy as np


def get_groups(grid):
    return repr([len(group) for group in grid.split(".") if len(group)>0]).replace(" ", "")[1:-1]


def get_all_grids(n):
    return ["".join(grid) for grid in product(".#", repeat=n)]


file = open("input.txt", "r")
lines = file.read().splitlines()
grids = [line.split()[0] for line in lines]
groups = [repr([int(n) for n in line.split()[1].split(",")]).replace(" ", "")[1:-1] for line in lines]

lens = [len(grid) for grid in grids]
grid_dict = {}
for i in range(1, max(lens)+1):
    grid_dict[i] = {}
    all_grids = get_all_grids(i)
    all_groups = [get_groups(grid) for grid in all_grids]
    for grid in all_grids:
        grouping = get_groups(grid)
        if grouping in grid_dict[i]:
            grid_dict[i][grouping].append(grid)
        else:
            grid_dict[i][grouping] = []
            grid_dict[i][grouping].append(grid)

counts = []
for grid, group, l in zip(grids, groups, lens):
    curr_grid1 = np.array(list(grid.replace("?", ".")))
    curr_grid2 = np.array(list(grid.replace("?", "#")))
    poss_grids = np.array([np.array(list(grid)) for grid in grid_dict[l][group]])
    g1=np.equal(poss_grids, curr_grid1)
    g2=np.equal(poss_grids, curr_grid2)
    test = np.logical_or(g1, g2)
    counts.append(np.sum(np.all(test, axis=1)))

print(sum(counts))

file.close()
