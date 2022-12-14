#AoC 2022 12b
pn = '12'
import sys
import re
import math
import hashlib
import operator
from functools import total_ordering
from collections import defaultdict, deque 
import numpy as np

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

graph = [] 
start = []
end = [] 
asquares = []
for r, line in enumerate(input):
    curr = []
    for c, char in enumerate(line):
        if char != "S" and char != "E":
            curr.append(ord(char) - ord('a'))
            if char == 'a':
                asquares.append([r,c])
        else:
            if char == "S":
                start = [r,c]
                curr.append(0)
            elif char == "E":
                end = [r,c]
                curr.append(ord('z')-ord('a'))
    graph.append(curr)
print(graph)
print(start, end)
asquares.append(start)
visited = [[False for i in range(len(graph[0]))] for j in range(len(graph))]

minpath = math.inf
path = []
distances = [[10**10 for i in range(len(graph[0]))] for j in range(len(graph))]

best = 10**16

# print(asquares)
queue = deque(asquares)
for astart in asquares:
    distances[astart[0]][astart[1]] = 0 
ans = 10**15

while len(queue) > 0:
    current = queue.popleft()
    if current == end:
        ans = distances[end[0]][end[1]]
        best = min(best, ans) 
        print(f"FOUND {ans}")
        break 
    direcs = [[1,0], [0, 1], [-1, 0], [0,-1]]
    for direc in direcs:
        newr = current[0] + direc[0]
        newc = current[1] + direc[1]
        if (newr in range(len(graph))) and (newc in range(len(graph[0]))):
            # print(current, [newr, newc], graph[newr][newc]-1, graph[current[0]][current[1]])
            if graph[newr][newc]-1 <= graph[current[0]][current[1]]:
                ndst = distances[current[0]][current[1]] + 1
                # print(f"     made it {distances[newr][newc]}, {ndst}")
                if distances[newr][newc] > ndst:
                    # print("         all the way")
                    distances[newr][newc] = ndst
                    queue.append([newr, newc])
    best = min(best, ans) 
    
# print(distances) 
print(ans) 
print(best)
print(distances[end[0]][end[1]])

# new = [] 
# for j in k:
#     new.extend(j)
# for i, n in enumerate(new):
#     if n == -1:
#         new[i] = 10**10
# x = min(new)
# print(x)
