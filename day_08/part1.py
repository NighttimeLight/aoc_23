
file = open("input.txt", "r")
lines = file.read().split("\n\n")
path, mapping = lines
mapping = mapping.splitlines()
map_dict = {}
for node in mapping:
    map_dict[node[0:3]] = {"L": node[7:10], "R": node[12:15]}

curr = "AAA"
count = 0
while curr != "ZZZ":
    curr = map_dict[curr][path[count%len(path)]]
    count += 1

print(count)

file.close()
