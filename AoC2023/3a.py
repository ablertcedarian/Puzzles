#AoC 2023 3.1
#%%
pn = '3'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

adj = [
	[-1, -1], [-1, 0], [-1, 1],
	[0, -1],           [0, 1],
	[1, -1], [1, 0], [1, 1],
]

#%%
def is_symbol_adjacent(row, col):
    for dx, dy in adj:
        x = row + dx
        y = col + dy
        if ((0 <= x and x < len(input)) and (0 <= y and y < len(input[0]))):
            char = input[x][y]
            if char != "." and not char.isnumeric():
                return True
    return False

#%%
valid_parts = []
for i, row in enumerate(input):
    number = 0
    symbol_adjacent = False
    for j, char in enumerate(row):
        if char.isnumeric():
            number = number * 10 + int(char)
            if not symbol_adjacent:
                symbol_adjacent = is_symbol_adjacent(i, j)
        elif number != 0:
            if symbol_adjacent:
                valid_parts.append(number)
            number = 0
            symbol_adjacent = False

    if number != 0:
        if symbol_adjacent:
            valid_parts.append(number)
        number = 0
        symbol_adjacent = False

print(valid_parts)
print(sum(valid_parts))
# %%
