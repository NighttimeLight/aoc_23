
file = open("input.txt", "r")

lines = file.read().splitlines()
nums = ["".join(filter(lambda char: char.isdigit(), line)) for line in lines]
fs = [num[0] for num in nums]
ls = [num[-1] for num in nums]
calibrations = [int(f + l) for f, l in zip(fs, ls)]
print(sum(calibrations))

file.close()
