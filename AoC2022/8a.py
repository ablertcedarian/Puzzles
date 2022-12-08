#AoC 2022 8a
pn = '8'
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
		input.append([int(x) for x in line.rstrip()])

print(input)

visible = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
print(visible)

for r in range(len(input)):
    tallest = input[r][0]
    visible[r][0] = 1
    for c in range(1, len(input[0])):
        curr = input[r][c]
        if curr > tallest:
            tallest = curr 
            visible[r][c] = 1
    tallest = input[r][-1]
    visible[r][-1] = 1
    for c in range(len(input[0])-1,0, -1):
        curr = input[r][c]
        if curr > tallest:
            tallest = curr 
            visible[r][c] = 1
    
for c in range(len(input[0])):
    tallest = input[0][c]
    visible[0][c] = 1
    for r in range(1, len(input)):
        curr = input[r][c]
        if curr > tallest:
            tallest = curr 
            visible[r][c] = 1
    tallest = input[-1][c]
    visible[-1][c] = 1
    for r in range(len(input)-1,0, -1):
        curr = input[r][c]
        if curr > tallest:
            tallest = curr 
            visible[r][c] = 1

print(visible)
sums = map(sum, visible)
print(sum(sums))
    

