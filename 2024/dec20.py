from collections import defaultdict
from ctypes import HRESULT

from aocd import get_data, submit


def solve1(test=True):
	# Your solution code here
	testdata = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
	if test:
		data = testdata
	else:
		data = get_data(day=20, year=2024)
	grid = [list(x) for x in data.split('\n')]
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == 'S':
				start = (x, y)
				grid[x][y] = 0
			elif grid[x][y] == 'E':
				end = (x, y)
				grid[x][y] = '.'
	steps = 0
	position = start
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	positions = [start]
	while position != end:
		for direction in directions:
			newposition = (position[0] + direction[0], position[1] + direction[1])
			if 0 <= newposition[0] < len(grid) and 0 <= newposition[1] < len(grid[0]) and grid[newposition[0]][
				newposition[1]] == '.':
				position = newposition
				steps += 1
				grid[position[0]][position[1]] = steps
				positions.append(position)
				break
	cheats = defaultdict(list)
	cheating = ((2, 0), (0, 2), (-2, 0), (0, -2))
	for position in positions:
		for cheat in cheating:
			newposition = (position[0] + cheat[0], position[1] + cheat[1])
			if 0 <= newposition[0] < len(grid) and 0 <= newposition[1] < len(grid[1]) and grid[newposition[0]][
				newposition[1]] != '#':
				if grid[newposition[0]][newposition[1]] > grid[position[0]][position[1]]:
					saved = grid[newposition[0]][newposition[1]] - grid[position[0]][position[1]] - 2
					cheats[saved].append((newposition, position))
	result = 0
	for saved in cheats:
		if saved >= 100:
			result += len(cheats[saved])

	if test:
		print(cheats)
	elif not test:
		print(result)
		submit(result, part="a", day=20, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
	if test:
		data = testdata
	else:
		data = get_data(day=20, year=2024)
	grid = [list(x) for x in data.split('\n')]
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == 'S':
				start = (x, y)
				grid[x][y] = 0
			elif grid[x][y] == 'E':
				end = (x, y)
				grid[x][y] = '.'
	steps = 0
	position = start
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	positions = [start]
	while position != end:
		for direction in directions:
			newposition = (position[0] + direction[0], position[1] + direction[1])
			if 0 <= newposition[0] < len(grid) and 0 <= newposition[1] < len(grid[0]) and grid[newposition[0]][
				newposition[1]] == '.':
				position = newposition
				steps += 1
				grid[position[0]][position[1]] = steps
				positions.append(position)
				break
	cheats = defaultdict(list)
	cheating = []
	for x in range(-20, 21):
		for y in range(-20, 21):
			if 2<=abs(x) + abs(y) <= 20:
				cheating.append((x, y))
	positions = set(positions)
	for position in positions:
		for cheat in cheating:
			newposition = (position[0] + cheat[0], position[1] + cheat[1])
			if newposition in positions and grid[newposition[0]][newposition[1]] != '#':
				if grid[newposition[0]][newposition[1]] > grid[position[0]][position[1]]:
					saved = grid[newposition[0]][newposition[1]] - grid[position[0]][position[1]] - (abs(cheat[0]) + abs(cheat[1]))

					cheats[saved].append((newposition, position))
	result = 0
	for saved in cheats:
		if saved >= 100:
			result += len(cheats[saved])

	if test:
		print(cheats)
	elif not test:
		print(result)
		submit(result, part="b", day=20, year=2024)


solve2(False)
