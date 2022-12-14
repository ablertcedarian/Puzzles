#AoC 2022 12a
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
for r, line in enumerate(input):
    curr = []
    for c, char in enumerate(line):
        if char != "S" and char != "E":
            curr.append(ord(char) - ord('a'))
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
visited = [[False for i in range(len(graph[0]))] for j in range(len(graph))]

minpath = math.inf
path = []
distances = [[-1 for i in range(len(graph[0]))] for j in range(len(graph))]

queue = deque([start])
distances[start[0]][start[1]] = 0 
ans = 10**15

while len(queue) > 0:
    current = queue.popleft()
    # print(current)
    # currstr = str(current[0]) + "," + str(current[1])
    if current == end:
        ans = distances[end[0]][end[1]]
        print(ans)
        break 
    direcs = [[1,0], [0, 1], [-1, 0], [0,-1]]
    for direc in direcs:
        newr = current[0] + direc[0]
        newc = current[1] + direc[1]
        if (newr >= 0 and newr < len(graph)) and (newc >= 0 and newc < len(graph[0])):
            if graph[newr][newc]-1 <= graph[current[0]][current[1]]:
                # newstr = str(newr)+","+str(newc)
                ndst = distances[current[0]][current[1]] + 1
                if distances[newr][newc] < ndst:
                    distances[newr][newc] = ndst
                    queue.append([newr, newc])
print(distances) 
print(ans) 

# # print(res[str(end[0])+","+str(end[1])])
# for line in res:
#     print(line)
# # print(res[str(end[0])+","+str(end[1])])
# print(res[end[0]][end[1]])





# def bfs(start, path, minpath):
#     queue = []
#     queue.append(start)
#     path.append(start)
#     visited[start[0]][start[1]] = True
#     while len(queue) > 0:
#         path.append(queue.pop(0))
#         last = path[-1]

#         print(f"last {last}")
#         if graph[last[0]][last[1]] == 27:
#             minpath = min(minpath, len(path))
#             print(f"found min {minpath}")

#         direcs = [[1,0], [0, 1], [-1, 0], [0,-1]]
#         for direc in direcs:
#             newr = last[0] + direc[1]
#             newc = last[1] + direc[1]
#             if newr >= 0 and newr < len(graph) and newc >= 0 and newc < len(graph[0]):
#                 if visited[newr][newc] == False:
#                     if graph[newr][newc] <= graph[curr[0]][curr[1]]:
#                     # if graph[curr[0]][curr[1]] == "S" or graph[newr][newc] == "E" or graph[newr][newc] == "S" or graph[newr][newc] <= graph[curr[0]][curr[1]] +1:
#                         print(f"Valid newpoint {newr},{newc}")
#                         newpath = path.copy()
#                         queue.append(newpath) 
#                         # print(minpath)
#     return minpath


def dfs(curr, visited, path, minpath):
    visited[curr[0]][curr[1]] = True
    path.append(curr)
    # print(path, minpath, curr)

    if graph[curr[0]][curr[1]] == "E":
        minpath = min(minpath, len(path))
        print(len(path), path)
        return minpath 
    else:
        direcs = [[1,0], [0, 1], [-1, 0], [0,-1]]
        for direc in direcs:
            newr = curr[0] + direc[0]
            newc = curr[1] + direc[1]
            if newr >= 0 and newr < len(graph) and newc >= 0 and newc < len(graph[0]):
                if visited[newr][newc] == False:
                    if graph[newr][newc] <= graph[curr[0]][curr[1]]:
                    # if graph[curr[0]][curr[1]] == "S" or graph[newr][newc] == "E" or graph[newr][newc] == "S" or graph[newr][newc] <= graph[curr[0]][curr[1]] +1:
                        print(f"Valid newpoint {newr},{newc}")
                        minpath = min(minpath, dfs([newr, newc], visited, path, minpath))
                        # print(minpath)
    
    path.pop(0)
    visited[curr[0]][curr[1]] = False
    return minpath 

# res = dfs(current, visited, path, minpath)
