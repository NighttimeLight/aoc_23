import numpy as np


def tilt_n(tab):
    for col_n in range(tab.shape[1]):
        col = tab[:, col_n]
        solids = np.where(col == "#")[0]
        for s, e in zip([0] + list(solids + 1), list(solids) + [len(col)]):
            tab[s:e, col_n] = np.sort(tab[s:e, col_n])[::-1]


def tilt_s(tab):
    for col_n in range(tab.shape[1]):
        col = tab[:, col_n]
        solids = np.where(col == "#")[0]
        for s, e in zip([0] + list(solids + 1), list(solids) + [len(col)]):
            tab[s:e, col_n] = np.sort(tab[s:e, col_n])


def tilt_e(tab):
    for row_n in range(tab.shape[0]):
        row = tab[row_n, :]
        solids = np.where(row == "#")[0]
        for s, e in zip([0] + list(solids + 1), list(solids) + [len(row)]):
            tab[row_n, s:e] = np.sort(tab[row_n, s:e])


def tilt_w(tab):
    for row_n in range(tab.shape[0]):
        row = tab[row_n, :]
        solids = np.where(row == "#")[0]
        for s, e in zip([0] + list(solids + 1), list(solids) + [len(row)]):
            tab[row_n, s:e] = np.sort(tab[row_n, s:e])[::-1]


def cycle(tab):
    tilt_n(tab)
    tilt_w(tab)
    tilt_s(tab)
    tilt_e(tab)


def eval(tab):
    tab = np.equal(tab, "O")
    row_tab = np.arange(tab.shape[0], 0, -1)
    row_tab = np.expand_dims(row_tab, axis=1)
    tab = np.multiply(tab, row_tab)
    return np.sum(tab)


file = open("input.txt", "r")
tab = file.read().splitlines()
tab = np.array([list(line) for line in tab])

# for i in range(200):
#     cycle(tab)
#     print(eval(tab))

file2 = open("loop.txt", "r")
loop = file2.read().splitlines()
print(loop[(1000000000 - 102) % 38 - 1])

file.close()
file2.close()
