import numpy as np


def get_vert(pattern):
    r, c = pattern.shape
    for i in range(1, c):
        m = min(i, c-i)
        left = pattern[:, i-m:i]
        right = pattern[:, i:i+m]
        right = np.flip(right, axis=1)
        match = np.equal(left, right)
        if np.all(match):
            return i
    return 0


def get_horz(pattern):
    r, c = pattern.shape
    for i in range(1, r):
        m = min(i, r-i)
        top = pattern[i - m:i, :]
        bot = pattern[i:i + m, :]
        bot = np.flip(bot, axis=0)
        match = np.equal(top, bot)
        if np.all(match):
            return i
    return 0


file = open("input.txt", "r")
patterns = file.read().split("\n\n")
patterns = [np.array([list(line) for line in pattern.split()]) for pattern in patterns]

summary = sum([get_vert(pat) + 100*get_horz(pat) for pat in patterns])
print(summary)

file.close()
