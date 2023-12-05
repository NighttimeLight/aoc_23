
def get_mapping(input, mapping):
    for map in mapping:
        src_b, src_e = map[1], map[1]+map[2]
        if (src_b <= input) and (input < src_e): return map[0] + (input - map[1])
    return input


file = open("input.txt", "r")
input_str = file.read().rstrip()
groups = input_str.split("\n\n")
seeds = [int(seed) for seed in groups[0].lstrip("seeds: ").split()]
groups = [[tuple(map(int, a_map.split())) for a_map in group.splitlines()[1:]] for group in groups[1:]]

mapped = seeds
for lvl in groups:
    mapped = [get_mapping(to_map, lvl) for to_map in mapped]
print(min(mapped))

file.close()
