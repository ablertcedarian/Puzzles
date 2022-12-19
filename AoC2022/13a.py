#AoC 2022 13a
pn = '13'
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

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)

with open(f'{pn}_Input.txt') as file:
    pairs = [[*map(eval, x.split())] for x in file.read().split('\n\n')]

def comparetwo(left, right):
    match left, right: 
        case int(), int():
            return (left>right) - (left<right)
        case int(), list():
            return comparetwo([left], right)
        case list(), int():
            return comparetwo(left, [right])
        case list(), list():
            for internal in map(comparetwo, left, right):
                if internal:
                    return internal
            return comparetwo(len(left), len(right))

correct = sum(i for i, p in enumerate(pairs, 1) if comparetwo(*p) == -1)

print(correct)
