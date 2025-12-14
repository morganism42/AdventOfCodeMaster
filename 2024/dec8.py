from itertools import count

from aocd import get_data, submit
from collections import defaultdict


def solve1(test=True):
	# Your solution code here
	testdata = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
	testans = 14
	if test:
		data = testdata
	else:
		data = get_data(day=8, year=2024)
	data = [list(row) for row in data.split("\n")]
	nodes = defaultdict(list)
	antinodes = [[0 for x in range(len(data[y]))] for y in range(len(data))]
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] != '.':
				nodes[data[y][x]].append((y, x))
	for type in nodes.keys():
		for node in nodes[type]:
			current = node
			for other in nodes[type]:
				if other != current:
					if 0 <= current[0] - (other[0] - current[0]) < len(antinodes) and 0 <= current[1] - (
							other[1] - current[1]) < len(antinodes[0]):
						antinodes[current[0] - (other[0] - current[0])][current[1] - (other[1] - current[1])] = '#'

	result = sum([row.count('#') for row in antinodes])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=8, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
	testans = 34
	if test:
		data = testdata
	else:
		data = get_data(day=8, year=2024)
	data = [list(row) for row in data.split("\n")]
	nodes = defaultdict(list)
	antinodes = [[0 for x in range(len(data[y]))] for y in range(len(data))]
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] != '.':
				nodes[data[y][x]].append((y, x))
				antinodes[y][x] = '#'
	for type in nodes.keys():
		for node in nodes[type]:
			current = node
			for other in nodes[type]:
				if other != current:
					distancex = other[0] - current[0]
					x = distancex
					distancey = other[1] - current[1]
					y = distancey
					while 0 <= current[0] - (distancex) < len(antinodes) and 0 <= current[1] - (distancey) < len(antinodes[0]):
						antinodes[current[0] - (distancex)][current[1] - distancey] = '#'
						distancex += x
						distancey += y

	result = sum([row.count('#') for row in antinodes])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=8, year=2024)


solve2(False)
