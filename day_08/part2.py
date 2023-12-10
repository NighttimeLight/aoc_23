import math


file = open("input.txt", "r")
lines = file.read().split("\n\n")
path, mapping = lines
mapping = mapping.splitlines()
map_dict = {}
for node in mapping:
    map_dict[node[0:3]] = {"L": node[7:10], "R": node[12:15]}

currs = [key for key in map_dict.keys() if key[2]=="A"]
ends = [""] * len(currs)
counts = [0] * len(currs)
loops = [0] * len(currs)
totals = [0] * len(currs)
for i in range(len(currs)):
    while currs[i][2] != "Z":
        currs[i] = map_dict[currs[i]][path[totals[i]%len(path)]]
        counts[i] += 1
        totals[i] += 1
    ends[i] = currs[i]
    currs[i] = map_dict[currs[i]][path[totals[i] % len(path)]]
    loops[i] += 1
    totals[i] += 1
    while currs[i][2] != "Z":
        currs[i] = map_dict[currs[i]][path[totals[i]%len(path)]]
        loops[i] += 1
        totals[i] += 1

n = 1
for i in counts:
    n = math.lcm(n, i)
print(n)

file.close()
