#AoC 2022 5a
pn = '5'
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

init = []
instrucs = []
for i,line in enumerate(input):
    if line == "":
        instrucs = input[i+1:]
        break
    init.append(line)

count = int(max(init[-1].split(" ")))
stacks = [[] for i in range(count)]
init = init[:-1]
for stack in init[::-1]:
    print(stack)
    for stacknum in range(1,count+1):
        if 1+(4*(stacknum-1)) < len(stack):
            letter = stack[1+(4*(stacknum-1))]
            print(letter, stacknum)
            if letter != " ":
                stacks[stacknum-1].append(letter) 
print(stacks) 

moves = [] 
for i,line in enumerate(instrucs):
    info = line.split(" ")
    moves.append([int(info[1]), int(info[3]), int(info[5])])

print(moves)

for move in moves:
    for count in range(move[0]):
        crate = stacks[move[1]-1].pop(-1)
        stacks[move[2]-1].append(crate)
print(stacks)
final = ''.join([x[-1] for x in stacks])
print(final)