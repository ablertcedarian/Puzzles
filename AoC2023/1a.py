#AoC 2023 1.1
pn = '1'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rsum = 0

for line in input:
	strval = []
	first = False
	i = 0
	while not first and i < len(line):
		char = line[i]
		if char.isdigit():
			strval.append(char)
			first = True 
		i += 1
	second = False 
	i = len(line)-1
	while not second and i > -1:
		char = line[i] 
		if char.isdigit():
			strval.append(char)
			second = True 
		i -= 1
	rsum += int("".join(strval)) 

print(rsum) 
