#AoC 2022 7a
pn = '7'
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
		input.append(line.rstrip())
print(input)

tree = defaultdict(defaultdict)
path = [] 
for line in input:
    print(f"line {line}")
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5] == '/':
                curr = tree 
            elif line[5:7] == '..':
                path.pop(-1)
                curr = tree 
                for subdirec in path:
                    curr = curr[subdirec]
            else:
                direcName = line[5:]
                curr = curr[direcName]
                path.append(direcName)
        elif line[2:4] == 'ls':
            continue 
    else:
        if line[:3] == "dir":
            direcName = line[4:]
            curr[direcName] = {}
        else:
            size, name = line.split(" ")
            print(size,name)
            curr[name] = int(size) 


def getSize(sizemin, tree):
    total = 0 
    for key in tree.keys():
        if type(tree[key]) == int:
            total += tree[key]
        else:
            sizemin, temp = getSize(sizemin, tree[key])
            total += temp 
    if total <= 100000:
        sizemin.append(total)
    return sizemin, total 

print(tree)
sizemin, totalSize = getSize([], tree)
print(sizemin, totalSize)
print(sum(sizemin))

