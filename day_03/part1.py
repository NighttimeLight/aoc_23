import numpy as np
import re

def isValidPart(arr, pos):
    arrY, arrX = arr.shape
    chkY1, chkY2 = max(0, pos[0] - 1), min(arrY, pos[0] + 2)
    chkX1, chkX2 = max(0, pos[1][0] - 1), min(arrX, pos[1][1] + 1)
    pattern = r"\.|\d"
    check = np.vectorize(lambda c: not(bool(re.match(pattern, c))))
    return check(arr[chkY1:chkY2, chkX1:chkX2]).any()


file = open("input.txt", "r")
lines = file.read().splitlines()
linesArr = [list(line) for line in lines]
linesArr = np.array(linesArr)

nums = [[num.group() for num in re.finditer(r"\d+", line)] for line in lines]
nums = [int(num) for line in nums for num in line]

numPos = [[(nLine, num.span()) for num in re.finditer(r"\d+", line)] for line, nLine in zip(lines, range(len(lines)))]
numPos = [num for line in numPos for num in line]

valid = [isValidPart(linesArr, numP) for numP in numPos]
parts = np.array(nums)[valid]

print(sum(parts))

file.close()
