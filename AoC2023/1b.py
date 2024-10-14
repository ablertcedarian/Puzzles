#AoC 2023 1.2
pn = '1'
import sys
import copy

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rsum = 0

digitletters = {"o": {"n": {"e": 1}},
				"t": {"w": {"o": 2}, "h": {"r": {"e": {"e": 3}}}},
				"f": {"o": {"u": {"r": 4}}, "i": {"v": {"e": 5}}},
				"s": {"i": {"x": 6}, "e": {"v": {"e": {"n": 7}}}},
				"e": {"i": {"g": {"h": {"t": 8}}}},
				"n": {"i": {"n": {"e": 9}}}}

digitlettersr = {"e": {"n": {"o": 1, "i": {"n": 9}}, "e": {"r": {"h": {"t": 3}}}, "v": {"i": {"f": 5}}},
				 "o": {"w": {"t": 2}},
				 "r": {"u": {"o": {"f": 4}}},
				 "x": {"i": {"s": 6}},
				 "n": {"e": {"v": {"e": {"s": 7}}}},
				 "t": {"h": {"g": {"i": {"e": 8}}}}}

letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# for line in input:
# 	strval = []
# 	first = False
# 	i = 0
# 	wordProgress = copy.deepcopy(digitletters) 
# 	while not first and i < len(line):
# 		char = line[i]
# 		if char.isdigit():
# 			strval.append(char)
# 			first = True 
# 			# print(f"found digit {char}")
# 		elif char in wordProgress.keys():
# 			# print(f"processed {char}")
# 			if isinstance(wordProgress[char], int):
# 				strval.append(str(wordProgress[char]))
# 				first = True 
# 			else:
# 				wordProgress = wordProgress[char]
# 			# print(f"to {strval} with {wordProgress}")
# 		else:
# 			wordProgress = copy.deepcopy(digitletters)
# 			if char in wordProgress.keys():
# 				wordProgress = wordProgress[char]
# 		i += 1
		
# 	second = False 
# 	i = len(line)-1
# 	wordProgress = copy.deepcopy(digitlettersr)
# 	# print("         second")
# 	while not second and i > -1:
# 		char = line[i] 
# 		if char.isdigit():
# 			strval.append(char)
# 			second = True 
# 			# print(f"found digit {char}")
# 		elif char in wordProgress.keys():
# 			# print(f"processed {char}")
# 			if isinstance(wordProgress[char], int):
# 				strval.append(str(wordProgress[char]))
# 				second = True 
# 			else:
# 				wordProgress = wordProgress[char]
# 			# print(f"to {strval} with {wordProgress}")
# 		else:
# 			wordProgress = copy.deepcopy(digitlettersr)
# 			if char in wordProgress.keys():
# 				wordProgress = wordProgress[char]
# 		i -= 1
# 	rsum += int("".join(strval)) 

for line in input:
	strval = []
	first = False
	i = 0
	wordProgress = copy.deepcopy(digitlettersr) 
	while not first and i < len(line):
		char = line[i]
		if char.isdigit():
			strval.append(char)
			first = True 
			# print(f"found digit {char}")
		else:
			for j in range(len(letters)):
				if line[i:].startswith(letters[j]):
					strval.append(str(j+1))
					first = True
		i += 1
		
	second = False 
	i = len(line)-1
	wordProgress = copy.deepcopy(digitlettersr)
	# print("         second")
	while not second and i > -1:
		char = line[i] 
		if char.isdigit():
			strval.append(char)
			second = True 
			# print(f"found digit {char}")
		else:
			for j in range(len(letters)):
				if line[:i+1].endswith(letters[j]):
					strval.append(str(j+1))
					second = True
		i -= 1
	rsum += int("".join(strval)) 

print(rsum) 
