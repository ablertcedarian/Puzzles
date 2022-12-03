#AoC 2022 3b
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

triple = [] 
with open(f'{pn}_Input.txt') as file:
    for line in file:
        triple.append(line.rstrip())
        if len(triple) == 3:
            input.append(triple)
            triple = []

# split halves 
commonLetters = []
for triple in input:
    a,b,c = triple[0], triple[1], triple[2] 
    cmn = ''.join(set(a).intersection(b).intersection(c))
    if cmn.isupper():
        commonLetters.append(ord(cmn)-ord('A')+27)
    else:
        commonLetters.append(ord(cmn)-ord('a')+1)

print(commonLetters)
print(sum(commonLetters))


