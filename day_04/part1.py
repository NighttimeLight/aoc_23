
file = open("input.txt", "r")
lines = file.read().splitlines()
cardIds = [line.split(": ")[0].split()[1] for line in lines]
numbers = [line.split(": ")[1] for line in lines]
winning = [set(int(num) for num in nums.split(" | ")[0].split()) for nums in numbers]
owned = [set(int(num) for num in nums.split(" | ")[1].split()) for nums in numbers]

matches = [cardWin & cardOwn for cardWin, cardOwn in zip(winning, owned)]
matchCounts = [len(match) for match in matches]
points = [pow(2, count - 1) if count > 0 else 0 for count in matchCounts]

print(sum(points))

file.close()
