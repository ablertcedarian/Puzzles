#AoC 2022 1.1
pn = '2'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip().split(" "))

shapeScore = {"X":1,"Y":2,"Z":3}
lose = {"A": 3, "B": 1, "C": 2}
draw = {"A": 1, "B": 2, "C": 3}
win = {"A": 2, "B": 3, "C": 1}
totalScore = 0
for round in input:
    if round[1] == "X":
        totalScore += 0
    elif round[1] == "Y":
        totalScore += 3
    elif round[1] == "Z":
        totalScore += 6
    if round[1] == "X":
        totalScore += lose[round[0]]
    elif round[1] == "Y":
        totalScore += draw[round[0]]
    elif round[1] == "Z":
        totalScore += win[round[0]]


    # print(totalScore, round)

print(totalScore)

