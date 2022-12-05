#AoC 2022 4a
pn = '4'
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
		input.append(line.rstrip().split(","))

count = 0
for ranges in input:
    a,b = map(int, ranges[0].split("-"))
    c,d = map(int, ranges[1].split("-"))
    r1 = set(range(a,b+1))
    r2 = set(range(c,d+1))
    count += r1 <= r2 or r2 <= r1 
    
print(count)

