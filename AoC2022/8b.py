#AoC 2022 8b
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

def getVD(r,c,input):
    checks = [[1,0],[0,1],[-1,0],[0,-1]]
    vd = 1
    for check in checks:
        score = 0
        newr = r+check[0]
        newc = c+check[1]
        starter = input[r][c]
        while (newr >= 0 and newr < len(input)) and (newc >= 0 and newc < len(input[0])):
            checking = input[newr][newc]
            # print(f"At {r},{c} with {starter}, checking {newr},{newc} with {checking}")
            if checking < starter:
                # print(" Bingo!")
                newr += check[0]
                newc += check[1]
                score += 1
            else:
                score += 1
                break 
        if score == 0:
            return 0 
        vd *= score 
    return vd 

maxvd = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        vd = getVD(r,c,input)
        visible[r][c] = vd 
        maxvd = max(vd, maxvd)

print(visible)
print(maxvd)
    

