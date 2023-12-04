import numpy as np

file = open("input.txt", "r")
lines = file.read().splitlines()
cardIds = [int(line.split(": ")[0].split()[1]) for line in lines]
numbers = [line.split(": ")[1] for line in lines]
winning = [set(int(num) for num in nums.split(" | ")[0].split()) for nums in numbers]
owned = [set(int(num) for num in nums.split(" | ")[1].split()) for nums in numbers]

matches = [cardWin & cardOwn for cardWin, cardOwn in zip(winning, owned)]
matchCounts = [len(match) for match in matches]

cardCounts = np.full(len(matchCounts), 1)
for cardId, cardMch in zip(cardIds, matchCounts):
    begin = cardId
    end = min(len(cardCounts), cardId+cardMch)
    copies = cardCounts[cardId - 1]
    cardCounts[begin:end] += copies

print(sum(cardCounts))

file.close()
