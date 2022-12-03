#AoC 2022 2a
pn = '2'
import sys
import re
import math
import hashlib
import operator
from functools import total_ordering
from collections import defaultdict 

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip().split(" "))

shapeScore = {"X":1,"Y":2,"Z":3}
totalScore = 0
for round in input:
    totalScore += shapeScore[round[1]]
    # print(totalScore)
    if round[1] == "X" and round[0] == "A":
        totalScore += 3
    elif round[1] == "Y" and round[0] == "B":
        totalScore += 3
    elif round[1] == "Z" and round[0] == "C":
        totalScore += 3
    elif round[1] == "X" and round[0] == "C":
        totalScore += 6
    elif round[1] == "Y" and round[0] == "A":
        totalScore += 6
    elif round[1] == "Z" and round[0] == "B":
        totalScore += 6
    # print(totalScore, round)

print(totalScore)

