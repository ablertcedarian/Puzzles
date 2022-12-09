#AoC 2022 9b
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
pos = [[0,0] for _ in range(10)]
visited["0,0"] = 1

for i, line in enumerate(input):
    direc = line[0]
    dist = int(line[1])
    for i in range(dist):
        # hx, hy = pos[0][0], pos[0][1]
        if direc == "R":
            pos[0][0] += 1
        elif direc == "U":
            pos[0][1] += 1
        elif direc == "L":
            pos[0][0] -= 1 
        elif direc == "D":
            pos[0][1] -= 1
        for point in range(1,10):
            tx,ty = pos[point][0], pos[point][1]
            hx,hy = pos[point-1][0], pos[point-1][1]
            thdist = math.sqrt((hy-ty)**2 + (hx-tx)**2)
            # print(point, line)
            # print(f"    {thdist}")
            # print(f"    {hx,hy, tx,ty}")
            while thdist >= 2:
                xgap = hx - pos[point][0]
                ygap = hy - pos[point][1]
                if xgap == 0:
                    pos[point][1] += np.sign(ygap) * 1
                elif ygap == 0:
                    pos[point][0] += np.sign(xgap) * 1
                elif abs(xgap) > abs(ygap):
                    # print("         xgap bigger")
                    pos[point][0] += np.sign(xgap) * (abs(xgap) - 1)
                    pos[point][1] += np.sign(ygap)
                elif abs(xgap) < abs(ygap):
                    # print("         ygap bigger")
                    pos[point][0] += np.sign(xgap)
                    pos[point][1] += np.sign(ygap) * (abs(ygap) - 1)
                elif abs(xgap) == abs(ygap):
                    pos[point][0] += np.sign(xgap) * (abs(xgap) - 1)
                    pos[point][1] += np.sign(ygap) * (abs(ygap) - 1)
                # print(f"        {hx, hy, pos[point][0],pos[point][1]}")
                if point == 9:
                    strhash = str(pos[point][0])+','+str(pos[point][1])
                    if strhash not in visited:
                        visited[strhash] = 1
                        # print(f"         incremented {len(visited), visited}")
                thdist = math.sqrt((hy-pos[point][1])**2 + (hx-pos[point][0])**2)
            # pos[point][0], pos[point][1] = tx,ty 

print(visited)
print(len(visited))



