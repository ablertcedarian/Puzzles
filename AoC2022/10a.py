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
		input.append(line.rstrip())

print(input)

done = False
instrucCount = 0
cycleCount = 0
cyclesLeft = 0
registerVal = 1 
strength = []
while not done:
	if instrucCount >= len(input):
		done = True 
		break
	cycleCount += 1 
	if ((cycleCount - 20) % 40) == 0:
		print(f"{cycleCount}, {registerVal}")
		strength.append(cycleCount * registerVal)
	instruc = input[instrucCount]
	if instruc == "noop":
		instrucCount += 1
		continue 
	else:
		val = instruc.split(" ")[1]
		if cyclesLeft == -1:
			cyclesLeft = 0
		elif cyclesLeft == 0:
			cyclesLeft = -1 
			print(f"	{cycleCount}, {registerVal}, {val}")
			registerVal += int(val)
			instrucCount += 1
		# else:
		# 	cyclesLeft -= 1

print(strength)
print(sum(strength))
	