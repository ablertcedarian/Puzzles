#AoC 2022 10a
pn = '10'
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
		input.extend(line.rstrip().split(" "))

totalSignalStrength = 0
totalSum = 1
for i,n in enumerate(input):
	if (i in [20, 60, 100, 140, 180, 220]):
		if i == 220:
			totalSignalStrength += i * (totalSum-1)
		else:
			totalSignalStrength += i * (totalSum)
		print(i*totalSum, i, totalSum, n)
	if n[-1].isdigit():
		totalSum += int(n) 
		# print(n, totalSum)

# print(input)
print(totalSum)
print(totalSignalStrength)
	