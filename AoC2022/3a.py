#AoC 2022 3a
pn = '3'
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

# split halves 
commonLetters = []
for sack in input:
    n = len(sack) // 2
    first = sack[:n]
    snd = sack[n:]
    cmn = ''.join(set(first).intersection(snd))
    if cmn.isupper():
        commonLetters.append(ord(cmn)-ord('A')+27)
    else:
        commonLetters.append(ord(cmn)-ord('a')+1)

print(commonLetters)
print(sum(commonLetters))


