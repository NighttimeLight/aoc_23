
file = open("input.txt", "r")
lines = file.read().splitlines()

seqs = [[int(value) for value in line.split()] for line in lines]
seqs = [[seq] for seq in seqs]
for seq in seqs:
    while not all(value == 0 for value in seq[-1]):
        seq.append([seq[-1][i+1] - seq[-1][i] for i in range(len(seq[-1]) - 1)])
    seq[-1].insert(0, 0)
    for lvl in reversed(range(len(seq) - 1)):
        seq[lvl].insert(0, seq[lvl][0] - seq[lvl + 1][0])
exs = [seq[0][0] for seq in seqs]

print(sum(exs))

file.close()
