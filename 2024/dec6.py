from aocd import get_data, submit
from copy import deepcopy


def solve1(test=True):
	# Your solution code here
	testdata = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
	testans = 41
	if test:
		data = testdata
	else:
		data = get_data(day=6, year=2024)

	data = [list(x) for x in data.split('\n')]
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == '^':
				position = [i, j]
				direction = (-1, 0)
				data[i][j] = '.'
				break
	border = ((0, len(data) - 1), (0, len(data[0]) - 1))
	while border[0][1] >= position[0] + direction[0] >= border[0][0] and border[1][1] >= position[1] + direction[1] >= \
			border[1][0]:

		data[position[0]][position[1]] = 'X'
		if data[position[0] + direction[0]][position[1] + direction[1]] == '#':
			if direction == (-1, 0):
				direction = (0, 1)
			elif direction == (0, 1):
				direction = (1, 0)
			elif direction == (1, 0):
				direction = (0, -1)
			elif direction == (0, -1):
				direction = (-1, 0)
		position[0] += direction[0]
		position[1] += direction[1]
	result = sum([x.count('X') for x in data]) + 1
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=6, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
	testans = 6
	if test:
		data = testdata
	else:
		data = get_data(day=6, year=2024)

	data = [list(x) for x in data.split('\n')]
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == '^':
				position = [i, j]

				direction = (-1, 0)
				start = (i, j, direction)
				data[i][j] = '.'
				break
	border = ((0, len(data) - 1), (0, len(data[0]) - 1))
	path = set()
	while position[0] not in border[0] and position[1] not in border[1]:
		if data[position[0] + direction[0]][position[1] + direction[1]] == '#':
			if direction == (-1, 0):
				direction = (0, 1)
			elif direction == (0, 1):
				direction = (1, 0)
			elif direction == (1, 0):
				direction = (0, -1)
			elif direction == (0, -1):
				direction = (-1, 0)
		position[0] += direction[0]
		position[1] += direction[1]
		if position != [start[0], start[1]]:
			path.add((position[0], position[1]))
	result = set()
	for spot in path:
		position = [start[0], start[1]]
		direction = start[2]
		newpath = {start}
		data[spot[0]][spot[1]] = '#'
		while position[0] not in border[0] and position[1] not in border[1]:
			if data[position[0] + direction[0]][position[1] + direction[1]] == '#':
				if direction == (-1, 0):
					direction = (0, 1)
				elif direction == (0, 1):
					direction = (1, 0)
				elif direction == (1, 0):
					direction = (0, -1)
				elif direction == (0, -1):
					direction = (-1, 0)
			else:
				position[0] += direction[0]
				position[1] += direction[1]
			if (position[0], position[1], direction) in newpath:
				result.add((spot[0], spot[1]))
				break
			newpath.add((position[0], position[1], direction))
		data[spot[0]][spot[1]] = '.'

	result = len(result)
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=6, year=2024)


solve2(False)
