#AoC 2022 11b
pn = '11'
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
for line in input:
    print(line)

monkeys = []
currMonkey = []
for n in input:
    if n == "":
        monkeys.append(currMonkey)
        currMonkey = []
    else:
        currMonkey.append(n)
monkeys.append(currMonkey)
for monkey in monkeys:
    print(monkey)

monkeyClean = [] 
for monkey in monkeys:
    items = list(map(int,monkey[1].split("items:")[1].split(",")))
    operation = monkey[2].split("old ")[1].split(" ")
    test = int(monkey[3].split("by ")[1])
    trueThrow = int(monkey[4].split("monkey ")[1])
    falseThrow = int(monkey[5].split("monkey ")[1])
    monkeyClean.append([items, operation, test, trueThrow, falseThrow])
for monkey in monkeyClean:
    print(monkey)

def moduloMultiplication(a, b, mod):
 
    res = 0; # Initialize result
 
    # Update a if it is more than
    # or equal to mod
    a = a % mod
 
    while (b):
     
        # If b is odd, add a with result
        if (b & 1):
            res = (res + a) % mod
             
        # Here we assume that doing 2*a
        # doesn't cause overflow
        a = (2 * a) % mod
 
        b >>= 1; # b = b / 2
     
    return res

activity = [0 for _ in range(len(monkeys))]
prod = np.prod([int(x[2]) for x in monkeyClean])
# print(f"mod {prod}")
starts = [x[0] for x in monkeyClean]
start = []
for k in starts:
    start.extend(k)
print(f"starting {start}")
for roundNum in range(10000):
    if roundNum % 100 == 0:
        print(roundNum)
    currs = [x[0] for x in monkeyClean]
    curr = []
    for k in currs:
        curr.extend(k)
    if curr == start and roundNum > 0:
        print(f"Found holy grail {roundNum}")
        break
    for monkeyNum in range(len(monkeys)):
        for _ in range(len(monkeyClean[monkeyNum][0])):
            # print()
            # print(monkeyClean[monkeyNum])
            activity[monkeyNum] += 1
            if len(monkeyClean[monkeyNum][0]) > 1:
                currItem = monkeyClean[monkeyNum][0].pop(0)
            else:
                currItem = monkeyClean[monkeyNum][0][0]
                monkeyClean[monkeyNum][0] = []
            operation = monkeyClean[monkeyNum][1]
            # print(currItem, operation)
            onum = currItem if operation[1] == "old" else int(operation[1])
            if operation[0] == "*":
                currItem = moduloMultiplication(currItem, onum, prod)
            elif operation[0] == "+":
                currItem = (onum + currItem) % prod 
            # print(currItem)
            # currItem = currItem // 3
            # print(currItem, monkeyClean[monkeyNum][2])
            # print(monkeyClean, monkeyClean[monkeyNum][3], monkeyClean[monkeyNum][4])
            if currItem % monkeyClean[monkeyNum][2] == 0:
                monkeyClean[monkeyClean[monkeyNum][3]][0] = monkeyClean[monkeyClean[monkeyNum][3]][0] + [currItem % prod]
                # print(f"thrown to {monkeyClean[monkeyNum][3]}, {monkeyClean[monkeyClean[monkeyNum][3]][0]}")
            else:
                monkeyClean[monkeyClean[monkeyNum][4]][0] = monkeyClean[monkeyClean[monkeyNum][4]][0] + [currItem % prod]
                # print(f"thrown to {monkeyClean[monkeyNum][4]}, {monkeyClean[monkeyClean[monkeyNum][4]][0]}")
# print()
# for monkey in monkeyClean:
#     print(monkey)
# print()


print(activity)
activity = sorted(activity, reverse=True)
print(activity[0], activity[1], activity[0]*activity[1])