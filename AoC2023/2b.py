#AoC 2023 2.2
pn = '2'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

possibleSum = 0

for line in input:
	gameID = line.split(":")[0][5:]
	print(gameID)
	subsets = line.split(":")[1].split(";")
	bluemin = 0
	redmin = 0
	greenmin = 0
	for subset in subsets:
		pars = subset.split(",")
		for par in pars:
			count = par.split(" ")
			# print(f"Color: {count[2]}, Count: {count[1]}")
			match count[2]:
				case "blue":
					bluemin = max(bluemin, int(count[1]))
				case "red":
					redmin = max(redmin, int(count[1]))
				case "green":
					greenmin = max(greenmin, int(count[1]))
	else:
		possibleSum += bluemin * redmin * greenmin

print(possibleSum)
	