#AoC 2022 14a
pn = '14'
import sys
import re
import math
import hashlib
import operator
from functools import total_ordering
from collections import defaultdict, deque 
import ast 
import json 
from ast import literal_eval 
from functools import cmp_to_key

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)

with open(f'{pn}_Input.txt') as file:
    rocks = list(map(list,[(list(map(int, k.split(","))) for k in x.split(" -> ")) for x in file.read().split("\n")]))

for rockline in rocks:
    print(rockline)

grid = defaultdict(lambda : 0)

kaboomh = 0
for rocklines in rocks:
    start = -1
    for rp in rocklines:
        kaboomh = max(kaboomh, rp[1])
        if start == -1:
            start = rp 
            continue
        elif rp[0] == start[0]:
            for c in range(min(rp[1],start[1]),max(rp[1],start[1])+1):
                grid[str(rp[0])+","+str(c)] = 1
            start = rp 
        elif rp[1] == start[1]:
            for r in range(min(rp[0],start[0]),max(rp[0],start[0])+1):
                grid[str(r)+","+str(rp[1])] = 1
            start = rp 


# print(grid)
# print(len(grid.keys()))

sandcount = 0 
try:
    while True:
        # print(sandcount, len(grid))
        sx = 500
        sy = 0 
        while True: 
            # print(f"    {sx},{sy}")
            if sy >= kaboomh:
                print(sandcount)
                raise Exception 
            down = str(sx)+","+str(sy+1)
            left = str(sx-1)+","+str(sy+1)
            right = str(sx+1)+","+str(sy+1)
            if down not in grid:
                sy += 1
            elif left not in grid:
                sx -= 1
                sy += 1
            elif right not in grid:
                sx += 1
                sy += 1
            else:
                grid[str(sx)+","+str(sy)] = 2
                sandcount += 1
                break 
except Exception as e:
    print("done")

