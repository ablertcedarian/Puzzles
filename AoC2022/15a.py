#AoC 2022 15a
pn = '15'
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
