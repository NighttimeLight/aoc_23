
def process(tab, to, chk, frm, dst, to_chk):
    yt, xt = to
    yc, xc = chk
    yf, xf = frm
    if (yt < len(tab)) and (yt >= 0) and (xt < len(tab[0])) and (xt >= 0):
        new_dst = dst[yf][xf] + 1
        if (dst[yc][xc] == 0) or (new_dst < dst[yc][xc]):
            dst[yc][xc] = new_dst
            to_chk.append((to, chk))


def check(tab, chk, frm, dst, to_chk):
    yc, xc = chk
    yf, xf = frm
    if tab[yc][xc] == "|":
        if (yc == (yf + 1)) and (xc == xf):
            process(tab, to=((yc+1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == (yf - 1)) and (xc == xf):
            process(tab, to=((yc-1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
    elif tab[yc][xc] == "-":
        if (yc == yf) and (xc == (xf + 1)):
            process(tab, to=(yc, (xc+1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == yf) and (xc == (xf - 1)):
            process(tab, to=(yc, (xc-1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
    elif tab[yc][xc] == "L":
        if (yc == (yf + 1)) and (xc == xf):
            process(tab, to=(yc, (xc+1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == yf) and (xc == (xf - 1)):
            process(tab, to=((yc-1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
    elif tab[yc][xc] == "J":
        if (yc == (yf + 1)) and (xc == xf):
            process(tab, to=(yc, (xc-1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == yf) and (xc == (xf + 1)):
            process(tab, to=((yc-1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
    elif tab[yc][xc] == "7":
        if (yc == (yf - 1)) and (xc == xf):
            process(tab, to=(yc, (xc-1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == yf) and (xc == (xf + 1)):
            process(tab, to=((yc+1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
    elif tab[yc][xc] == "F":
        if (yc == (yf - 1)) and (xc == xf):
            process(tab, to=(yc, (xc+1)), chk=chk, frm=frm, dst=dst, to_chk=to_chk)
        elif (yc == yf) and (xc == (xf - 1)):
            process(tab, to=((yc+1), xc), chk=chk, frm=frm, dst=dst, to_chk=to_chk)


file = open("input.txt", "r")
lines = file.read().splitlines()
tab = [list(line) for line in lines]
start = [(row_id, row.index("S")) for row_id, row in enumerate(tab) if "S" in row][0]
dst = [[0] * len(row) for row in tab]

start_y, start_x = start
to_chk = []
to_chk.append(((start_y+1, start_x), start))
to_chk.append(((start_y, start_x+1), start))
to_chk.append(((start_y-1, start_x), start))
to_chk.append(((start_y, start_x-1), start))
while to_chk:
    chked = to_chk.pop(0)
    chk, frm = chked
    check(tab, chk, frm, dst, to_chk)

max_dst = max(max(row) for row in dst)
print(max_dst)

file.close()
