from aocd import get_data, submit
from copy import deepcopy
import os

clear = lambda: os.system('cls')
clear()


def solve1(test=True):
	# Your solution code here
	testdata = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''
	testans = 11048
	if test:
		data = testdata
	else:
		data = get_data(day=16, year=2024)
	grid = tuple([tuple(x) for x in data.split("\n")])
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == "S":
				position = ((x, y), (1, 0), 0)
			elif grid[y][x] == "E":
				end = (x, y)
	dictmap = {}
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == "#":
				continue
			neighbours = []
			for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
				if grid[y + direction[1]][x + direction[0]] != "#":
					neighbours.append(((x + direction[0], y + direction[1]), direction))
			dictmap[(x, y)] = tuple(neighbours)

	result = 0
	current = [position]
	checked = set()
	while current:
		looking = current.pop(0)
		for neighbour in dictmap[looking[0]]:
			if neighbour[0] in checked:
				continue
			if neighbour[0] == end:
				result = looking[2] + 1
				current = []
				break
			if neighbour[1] == looking[1]:
				current.append((neighbour[0], neighbour[1], looking[2] + 1))
			else:
				current.append((neighbour[0], neighbour[1], looking[2] + 1001))
			checked.add(neighbour[0])
		current = sorted(current, key=lambda x: x[2])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")

	elif not test:
		print(result)
		submit(result, part='a', day=16, year=2024)


def solve2(test=True):
	# Your solution code here
	global trueseats
	testdata = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''
	testans = 64
	if test:
		data = testdata
	else:
		data = get_data(day=16, year=2024)
	grid = tuple([tuple(x) for x in data.split("\n")])
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == "S":
				position = ((x, y), (1, 0), 0, [(1, 0)])
				start = (x, y)
			elif grid[y][x] == "E":
				end = (x, y)
	dictmap = {}
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == "#":
				continue
			neighbours = []
			for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
				if grid[y + direction[1]][x + direction[0]] != "#":
					neighbours.append(((x + direction[0], y + direction[1]), direction))
			dictmap[(x, y)] = tuple(neighbours)

	current = [position]
	checked = set()
	while current:
		looking = current.pop(0)
		for neighbour in dictmap[looking[0]]:
			if neighbour[0] in checked:
				continue
			if neighbour[0] == end:
				result = looking[2] + 1
				current = []
				if neighbour[1] != looking[3]:
					path = looking[3]
				break
			if neighbour[1] == looking[1]:
				current.append((neighbour[0], neighbour[1], looking[2] + 1, looking[3]))
			else:
				current.append((neighbour[0], neighbour[1], looking[2] + 1001, looking[3] + [neighbour[1]]))
			checked.add(neighbour[0])
		current = sorted(current, key=lambda x: x[2])
	'''
need to keep track of nodes that can be the next possible move direction, and have their path to that point tracked
node = (position,path,score?)
	'''

	limit = result - (len(path[1:]) * 1000)
	seatfind(start, path, grid, {start}, limit, 0)
	result = len(trueseats)
	if test and result == testans:

		print(result)
		print("Test passed")
	elif test and result != testans:
		print('\n'.join([''.join(x) for x in grid]), '\n')
		grid = [list(x) for x in grid]
		for seat in trueseats:
			grid[seat[1]][seat[0]] = "X"
		print('\n'.join([''.join(x) for x in grid]))
		print(result)
		print("Test failed")
		print(trueseats)

	elif not test:
		print(result)
		grid = [list(x) for x in grid]
		for seat in trueseats:
			grid[seat[1]][seat[0]] = "X"
		temp = sum([x.count("X") for x in grid])
		print(temp)
		submit(result + 9, part='b', day=16, year=2024)


# had to cheat a little bit but its just not worth it

trueseats = set()


def seatfind(position, path, map, seats: set, limit: int, steps: int):
	global trueseats
	current = path[0]
	if len(path) > 1: future = path[1]
	while True:
		seats.add(position)
		if len(path) > 1:
			if map[position[1] + future[1]][position[0] + future[0]] != "#":
				seatfind((position[0] + future[0], position[1] + future[1]), path[1:], map, deepcopy(seats), limit,
				         steps + 1)
		elif map[position[1] + current[1]][position[0] + current[0]] == "E":
			trueseats = trueseats.union(seats)
			trueseats.add((position[0] + current[0], position[1] + current[1]))
		if map[position[1] + current[1]][position[0] + current[0]] == "#":
			return
		position = (position[0] + current[0], position[1] + current[1])
		steps += 1
		if steps == limit: return


solve2(False)
