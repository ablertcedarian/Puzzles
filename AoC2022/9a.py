#AoC 2022 9a
pn = '9'
import sys
import re
import math
import hashlib
import operator
from functools import total_ordering
from collections import defaultdict 
import numpy as np

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip().split(" "))

print(input)

visited = {}
hx, hy = 0,0
tx, ty = 0,0 
visited["0,0"] = 1

for line in input:
    direc = line[0]
    dist = int(line[1])
    for i in range(dist):
        if direc == "R":
            hx += 1
        elif direc == "U":
            hy += 1
        elif direc == "L":
            hx -= 1 
        elif direc == "D":
            hy -= 1
        thdist = math.sqrt((hy-ty)**2 + (hx-tx)**2)
        # print(line)
        # print(f"    {thdist}")
        # print(f"    {hx,hy, tx,ty}")
        if thdist >= 2:
            xgap = hx - tx
            ygap = hy - ty 
            if xgap == 0:
                ty += np.sign(ygap) * (abs(ygap) - 1)
            elif ygap == 0:
                tx += np.sign(xgap) * (abs(xgap) - 1)
            elif abs(xgap) > abs(ygap):
                # print("         xgap bigger")
                tx += np.sign(xgap) * (abs(xgap) - 1)
                ty += ygap 
            elif abs(xgap) < abs(ygap):
                # print("         ygap bigger")
                tx += xgap 
                ty += np.sign(ygap) * (abs(ygap) - 1)
            # print(f"        {tx,ty}")
            strhash = str(tx)+','+str(ty)
            if strhash not in visited:
                visited[strhash] = 1
                # print(f"         incremented {visited}")

print(visited)
print(len(visited))



