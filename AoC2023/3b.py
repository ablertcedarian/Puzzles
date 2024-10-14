#AoC 2023 3.2
#%%
pn = '3'
import sys

input = []

with open(f'{pn}_Input.txt') as file:
	for line in file:
		input.append(list(line.rstrip()))

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
            if char != "." and not isinstance(char, int) and not char.isnumeric():
                return True
    return False

def mark_with_number(row, col, number):
    print(row, col, number)
    iterator = number
    while iterator > 0:
        input[row][col] = number
        col -= 1
        iterator = iterator // 10

#%%
valid_parts = set()
for i, row in enumerate(input):
    number = 0
    symbol_adjacent = False
    for j, char in enumerate(row):
        print(i, j, char)
        if char.isnumeric():
            number = number * 10 + int(char)
            if not symbol_adjacent:
                symbol_adjacent = is_symbol_adjacent(i, j)
        elif number != 0:
            if symbol_adjacent:
                valid_parts.add(number)
                mark_with_number(i, j-1, number)
            number = 0
            symbol_adjacent = False

    if number != 0:
        if symbol_adjacent:
            valid_parts.add(number)
            mark_with_number(i, j, number)
        number = 0
        symbol_adjacent = False

for row in input:
    print(row)
#%%
def get_gear_ratio(row, col):
    parts = set()
    for dx, dy in adj:
        x = row + dx
        y = col + dy
        if (
            (0 <= x and x < len(input)) and
            (0 <= y and y < len(input[0]))
        ):
            element = input[x][y]
            if isinstance(element, int) and element not in parts:
                parts.add(element)

    if len(parts) == 2:
        parts_list = list(parts)
        return parts_list[0] * parts_list[1]

    return 0

# %%
gear_ratios = []
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == "*":
            gear_ratios.append(
                get_gear_ratio(i, j)
            )
print(gear_ratios)
print(sum(gear_ratios))
# %%
