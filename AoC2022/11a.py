#AoC 2022 11a
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

activity = [0 for _ in range(len(monkeys))]
for roundNum in range(20):
    for monkeyNum in range(len(monkeys)):
        for _ in range(len(monkeyClean[monkeyNum][0])):
            print()
            print(monkeyClean[monkeyNum])
            activity[monkeyNum] += 1
            if len(monkeyClean[monkeyNum][0]) > 1:
                currItem = monkeyClean[monkeyNum][0].pop(0)
            else:
                currItem = monkeyClean[monkeyNum][0][0]
                monkeyClean[monkeyNum][0] = []
            operation = monkeyClean[monkeyNum][1]
            print(currItem, operation)
            onum = currItem if operation[1] == "old" else int(operation[1])
            if operation[0] == "*":
                currItem *= onum
            elif operation[0] == "+":
                currItem += onum
            print(currItem)
            currItem = currItem // 3
            print(currItem, monkeyClean[monkeyNum][2])
            print(monkeyClean, monkeyClean[monkeyNum][3], monkeyClean[monkeyNum][4])
            if currItem % monkeyClean[monkeyNum][2] == 0:
                monkeyClean[monkeyClean[monkeyNum][3]][0] = monkeyClean[monkeyClean[monkeyNum][3]][0] + [currItem]
                print(f"thrown to {monkeyClean[monkeyNum][3]}, {monkeyClean[monkeyClean[monkeyNum][3]][0]}")
            else:
                monkeyClean[monkeyClean[monkeyNum][4]][0] = monkeyClean[monkeyClean[monkeyNum][4]][0] + [currItem]
                print(f"thrown to {monkeyClean[monkeyNum][4]}, {monkeyClean[monkeyClean[monkeyNum][4]][0]}")
print()
for monkey in monkeyClean:
    print(monkey)
print()

print(activity)
activity = sorted(activity, reverse=True)
print(activity[0], activity[1], activity[0]*activity[1])