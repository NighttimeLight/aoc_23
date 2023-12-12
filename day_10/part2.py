from shapely.geometry import Polygon


def process_dst(tab, to, chk, frm, to_chk, kwargs):
    dst = kwargs.get("dst", None)
    org = kwargs.get("org", None)
    orgs = kwargs.get("orgs", None)
    yt, xt = to
    yc, xc = chk
    yf, xf = frm
    if (yt < len(tab)) and (yt >= 0) and (xt < len(tab[0])) and (xt >= 0):
        new_dst = dst[yf][xf] + 1
        if (dst[yc][xc] == 0) or (new_dst < dst[yc][xc]):
            dst[yc][xc] = new_dst
            orgs[yc][xc] = org
            to_chk.append((to, chk, org))


def process_loop(tab, to, chk, frm, to_chk, kwargs):
    loop = kwargs.get("loop", None)
    yt, xt = to
    yc, xc = chk
    yf, xf = frm
    if (yt < len(tab)) and (yt >= 0) and (xt < len(tab[0])) and (xt >= 0):
        if tab[yc][xc] in "LJ7F":
            loop.append(chk)
        to_chk.append((to, chk))


def check(tab, chk, frm, action, to_chk, **kwargs):
    yc, xc = chk
    yf, xf = frm
    if tab[yc][xc] == "|":
        if (yc == (yf + 1)) and (xc == xf):
            action(tab, ((yc+1), xc), chk, frm, to_chk, kwargs)
        elif (yc == (yf - 1)) and (xc == xf):
            action(tab, ((yc-1), xc), chk, frm, to_chk, kwargs)
    elif tab[yc][xc] == "-":
        if (yc == yf) and (xc == (xf + 1)):
            action(tab, (yc, (xc+1)), chk, frm, to_chk, kwargs)
        elif (yc == yf) and (xc == (xf - 1)):
            action(tab, (yc, (xc-1)), chk, frm, to_chk, kwargs)
    elif tab[yc][xc] == "L":
        if (yc == (yf + 1)) and (xc == xf):
            action(tab, (yc, (xc+1)), chk, frm, to_chk, kwargs)
        elif (yc == yf) and (xc == (xf - 1)):
            action(tab, ((yc-1), xc), chk, frm, to_chk, kwargs)
    elif tab[yc][xc] == "J":
        if (yc == (yf + 1)) and (xc == xf):
            action(tab, (yc, (xc-1)), chk, frm, to_chk, kwargs)
        elif (yc == yf) and (xc == (xf + 1)):
            action(tab, ((yc-1), xc), chk, frm, to_chk, kwargs)
    elif tab[yc][xc] == "7":
        if (yc == (yf - 1)) and (xc == xf):
            action(tab, (yc, (xc-1)), chk, frm, to_chk, kwargs)
        elif (yc == yf) and (xc == (xf + 1)):
            action(tab, ((yc+1), xc), chk, frm, to_chk, kwargs)
    elif tab[yc][xc] == "F":
        if (yc == (yf - 1)) and (xc == xf):
            action(tab, (yc, (xc+1)), chk, frm, to_chk, kwargs)
        elif (yc == yf) and (xc == (xf - 1)):
            action(tab, ((yc+1), xc), chk, frm, to_chk, kwargs)


file = open("input.txt", "r")
lines = file.read().splitlines()
tab = [list(line) for line in lines]
start = [(row_id, row.index("S")) for row_id, row in enumerate(tab) if "S" in row][0]
dst = [[0] * len(row) for row in tab]
orgs = [[(-1,-1)] * len(row) for row in tab]

start_y, start_x = start
to_chk = []
to_chk.append(((start_y+1, start_x), start, (start_y+1, start_x)))
to_chk.append(((start_y, start_x+1), start, (start_y, start_x+1)))
to_chk.append(((start_y-1, start_x), start, (start_y-1, start_x)))
to_chk.append(((start_y, start_x-1), start, (start_y, start_x-1)))
while to_chk:
    chked = to_chk.pop(0)
    chk, frm, org = chked
    check(tab, chk, frm, process_dst, to_chk, dst=dst, org=org, orgs=orgs)

max_dst = max(max(row) for row in dst)
max_pos = [(row_id, row.index(max_dst)) for row_id, row in enumerate(dst) if max_dst in row][0]

max_org = orgs[max_pos[0]][max_pos[1]]
loop = [start]
to_chk = [(max_org, start)]
while to_chk:
    chked = to_chk.pop(0)
    chk, frm = chked
    check(tab, chk, frm, process_loop, to_chk, loop=loop)
loop.append(start)

polygon = Polygon(loop)
print(int(polygon.area - polygon.length / 2 + 1))

file.close()
