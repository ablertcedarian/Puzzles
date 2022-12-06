#AoC 2022 6b
pn = '6'
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
print(line)

marker = 0 
buffer = []
for i,n in enumerate(line):
    print(buffer) 
    if len(set(buffer)) == len(buffer) and len(buffer) == 14:
        marker = i
        break
    else:
        if len(buffer) > 13:
            buffer.pop(0)
        buffer.append(n)

print(marker) 
