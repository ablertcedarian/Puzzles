#AoC 2022 1.1
pn = '1'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

processed = [[]] 
maxCal = 0
currCal = 0
for line in input:
    if len(line) == 0:
        processed.append([])
        maxCal = max(maxCal, currCal)
        currCal = 0
    else:
        processed[-1].append(int(line))
        currCal += int(line) 

print(maxCal)

