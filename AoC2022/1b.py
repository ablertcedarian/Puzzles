#AoC 2022 1.2
pn = '1'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

processed = [[]] 
top3 = []
currCal = 0
for line in input:
    if len(line) == 0:
        processed.append([])
        top3.append(currCal)
        top3.sort(reverse=True)
        top3 = top3[:3]
        currCal = 0
    else:
        processed[-1].append(int(line))
        currCal += int(line) 
top3.append(currCal)
top3.sort(reverse=True)
top3 = top3[:3]

print(sum(top3))
print(top3)

