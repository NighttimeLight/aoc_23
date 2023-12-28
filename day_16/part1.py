import numpy as np


def process(tab, to, chk, frm, energ, chked, to_chk):
    yt, xt = to
    yc, xc = chk
    energ[yc][xc] = True
    if (yt < len(tab)) and (yt >= 0) and (xt < len(tab[0])) and (xt >= 0):
        if chk not in chked[yt][xt]:
            chked[yt][xt].append(chk)
            to_chk.append((to, chk))


def check(tab, chk, frm, energ, chked, to_chk):
    yc, xc = chk
    yf, xf = frm
    ydiff, xdiff = yc - yf, xc - xf
    if tab[yc][xc] == ".":
        process(tab, to=(yc + ydiff, xc + xdiff), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
    elif tab[yc][xc] == "/":
        process(tab, to=(yc - xdiff, xc - ydiff), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
    elif tab[yc][xc] == "\\":
        process(tab, to=(yc + xdiff, xc + ydiff), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
    elif tab[yc][xc] == "|":
        if xdiff == 0:
            process(tab, to=(yc + ydiff, xc), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
        else:
            process(tab, to=(yc + 1, xc), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
            process(tab, to=(yc - 1, xc), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
    elif tab[yc][xc] == "-":
        if ydiff == 0:
            process(tab, to=(yc, xc + xdiff), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
        else:
            process(tab, to=(yc, xc + 1), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)
            process(tab, to=(yc, xc - 1), chk=chk, frm=frm, energ=energ, chked=chked, to_chk=to_chk)


file = open("input.txt", "r")
lines = file.read().splitlines()
tab = [list(line) for line in lines]

chked = [[[] for tile in row] for row in tab]
energ = [[False] * len(row) for row in tab]

to_chk = [((0, 0), (0, -1))]
while to_chk:
    chk_ = to_chk.pop(0)
    chk, frm = chk_
    check(tab, chk, frm, energ, chked, to_chk)

print(np.array(energ).sum())

file.close()
