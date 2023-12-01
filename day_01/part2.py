import re

digitDict = {"one": "1", "two": "2", "three": "3",
             "four": "4", "five": "5", "six": "6",
             "seven": "7", "eight": "8", "nine": "9"}
revDict = {"eno": "1", "owt": "2", "eerht": "3",
             "ruof": "4", "evif": "5", "xis": "6",
             "neves": "7", "thgie": "8", "enin": "9"}

file = open("input.txt", "r")

lines = file.read().splitlines()
linesRev = [line[::-1] for line in lines]

pattern = '|'.join(sorted(k for k in digitDict))
patternRev = '|'.join(sorted(k for k in revDict))
linesF = [re.sub(pattern, lambda m: digitDict.get(m.group(0)), line, 1) for line in lines]
linesLRev = [re.sub(patternRev, lambda m: revDict.get(m.group(0)), line, 1) for line in linesRev]
linesL = [line[::-1] for line in linesLRev]

numsF = ["".join(filter(lambda char: char.isdigit(), line)) for line in linesF]
numsL = ["".join(filter(lambda char: char.isdigit(), line)) for line in linesL]
fs = [num[0] for num in numsF]
ls = [num[-1] for num in numsL]
calibrations = [int(f + l) for f, l in zip(fs, ls)]
print(sum(calibrations))

file.close()
