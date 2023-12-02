import numpy as np
import re

file = open("input.txt", "r")

lines = file.read().splitlines()
linesSpl = [line.split(": ") for line in lines]
linesSpl = np.array(linesSpl)
games, infos = linesSpl[:, 0], linesSpl[:, 1].tolist()
ids = np.array(np.char.split(games).tolist())[:, 1].astype(int)
infos = [re.split(", |; ", info) for info in infos]

infosRed = [list(filter(lambda cubes: re.findall("red", cubes), info)) for info in infos]
countsRed = [[int(cubes.split(" ")[0]) for cubes in info] for info in infosRed]
reds = [max(counts)>12 for counts in countsRed]

infosGreen = [list(filter(lambda cubes: re.findall("green", cubes), info)) for info in infos]
countsGreen = [[int(cubes.split(" ")[0]) for cubes in info] for info in infosGreen]
greens = [max(counts)>13 for counts in countsGreen]

infosBlue = [list(filter(lambda cubes: re.findall("blue", cubes), info)) for info in infos]
countsBlue = [[int(cubes.split(" ")[0]) for cubes in info] for info in infosBlue]
blues = [max(counts)>14 for counts in countsBlue]

alls = np.logical_not(np.logical_or(np.logical_or(reds, greens), blues))
possibles = ids[alls]

print(sum(possibles))


file.close()
