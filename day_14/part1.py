import numpy as np

file = open("input.txt", "r")
tab = file.read().splitlines()
tab = np.array([list(line) for line in tab])

for col_n in range(tab.shape[1]):
    col = tab[:, col_n]
    solids = np.where(col == "#")[0]
    for s, e in zip([0] + list(solids + 1), list(solids) + [len(col)]):
        tab[s:e, col_n] = np.sort(tab[s:e, col_n])[::-1]

tab = np.equal(tab, "O")
row_tab = np.arange(tab.shape[0], 0, -1)
row_tab = np.expand_dims(row_tab, axis=1)
tab = np.multiply(tab, row_tab)
print(np.sum(tab))

file.close()
