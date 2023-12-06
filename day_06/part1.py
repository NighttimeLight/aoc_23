import math


def get_roots(t, d):
    sq = math.sqrt(t*t - 4*d)
    lower = (t - sq) / 2
    upper = (t + sq) / 2
    return [math.floor(lower) + 1, math.ceil(upper) - 1]


file = open("input.txt", "r")
lines = file.read().splitlines()
lines = [list(map(int, line.split()[1:])) for line in lines]
times, dists = lines
ranges = [get_roots(t, d) for t, d in zip(times, dists)]
n_ways = [t_range[1] - t_range[0] + 1 for t_range in ranges]
n_ways = [n if n > 0 else 0 for n in n_ways]

print(math.prod(n_ways))

file.close()
