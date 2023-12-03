import numpy as np
import re

def is_valid_part(arr, pos):
    arrY, arrX = arr.shape
    chkY1, chkY2 = max(0, pos[0] - 1), min(arrY, pos[0] + 2)
    chkX1, chkX2 = max(0, pos[1][0] - 1), min(arrX, pos[1][1] + 1)
    pattern = r"\.|\d"
    check = np.vectorize(lambda c: not(bool(re.match(pattern, c))))
    return check(arr[chkY1:chkY2, chkX1:chkX2]).any()


def find_gears(arr, partPos):
    arrY, arrX = arr.shape
    gears = np.zeros_like(arr, dtype=int)
    pattern = r"\*"
    check = np.vectorize(lambda c: bool(re.match(pattern, c)))
    asterisks = check(arr)
    for pos in partPos:
        chkY1, chkY2 = max(0, pos[0] - 1), min(arrY, pos[0] + 2)
        chkX1, chkX2 = max(0, pos[1][0] - 1), min(arrX, pos[1][1] + 1)
        templ = np.zeros_like(arr, dtype=bool)
        templ[chkY1:chkY2, chkX1:chkX2] = 1.
        gears_adj = np.logical_and(templ, asterisks)
        gears = np.add(gears, gears_adj)
    gears = (gears >= 2).astype(int)
    return gears


def calc_gears(arr, partPos, partNum):
    arrY, arrX = arr.shape
    gears = arr
    for pos, num in zip(partPos, partNum):
        chkY1, chkY2 = max(0, pos[0] - 1), min(arrY, pos[0] + 2)
        chkX1, chkX2 = max(0, pos[1][0] - 1), min(arrX, pos[1][1] + 1)
        templ = np.ones_like(arr, dtype=int)
        templ[chkY1:chkY2, chkX1:chkX2] = num
        gears = np.multiply(gears, templ)
    return gears


file = open("input.txt", "r")
lines = file.read().splitlines()
linesArr = [list(line) for line in lines]
linesArr = np.array(linesArr)

nums = [[num.group() for num in re.finditer(r"\d+", line)] for line in lines]
nums = [int(num) for line in nums for num in line]

numPos = [[(nLine, num.span()) for num in re.finditer(r"\d+", line)] for line, nLine in zip(lines, range(len(lines)))]
numPos = [num for line in numPos for num in line]

valid = [is_valid_part(linesArr, numP) for numP in numPos]
parts = np.array(nums)[valid]
partPos = np.array(numPos)[valid]

gearArr = find_gears(linesArr, partPos)
gearArr = calc_gears(gearArr, partPos, parts)

print(np.sum(gearArr))

file.close()
