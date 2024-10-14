#AoC 2023 2.1
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
	possible = True 
	for subset in subsets:
		if not possible:
			break
		pars = subset.split(",")
		for par in pars:
			count = par.split(" ")
			# print(f"Color: {count[2]}, Count: {count[1]}")
			match count[2]:
				case "blue":
					if int(count[1]) > 14:
						possible = False
						print("Breaking")
						break 
				case "red":
					if int(count[1]) > 12:
						possible = False
						print("Breaking")
						break
				case "green":
					if int(count[1]) > 13:
						possible = False 
						print("Breaking")
						break 
	else:
		if possible:
			print("adding")
			print()
			possibleSum += int(gameID)

print(possibleSum)
	