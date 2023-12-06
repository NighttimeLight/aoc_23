import math
import re


def get_roots(t, d):
    sq = math.sqrt(t*t - 4*d)
    lower = (t - sq) / 2
    upper = (t + sq) / 2
    return [math.floor(lower) + 1, math.ceil(upper) - 1]


file = open("input.txt", "r")
lines = file.read().splitlines()
lines = [re.sub(r'\w+:\s+', "", line) for line in lines]
lines = [int(re.sub(r'\s+', "", line)) for line in lines]
time, dist = lines
t_range = get_roots(time, dist)
n_ways = t_range[1] - t_range[0] + 1

print(n_ways)

file.close()
