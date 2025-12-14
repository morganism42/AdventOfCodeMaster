from aocd import get_data, submit
from copy import deepcopy
from math import floor

data = get_data(day=21, year=2023)
test = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''


def spread(field, location):
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	newcations = []
	for way in directions:
		if 0 <= location[0] + way[0] < len(field) and 0 <= location[1] + way[1] < len(field[0]):
			if field[location[0] + way[0]][location[1] + way[1]] != '#':
				newcations.append((location[0] + way[0], location[1] + way[1]))
	return newcations


def parse(data):
	field = tuple([tuple(i) for i in data.split('\n')])
	for y in range(len(field)):
		for x in range(len(field[y])):
			if field[y][x] == 'S':
				start = (y, x)
				return field, start


def endstate(field, loops, start):
	locations = [start]
	for loop in range(int(loops)):
		newlocations = []
		for location in locations:
			newlocations += spread(field, location)
		locations = set(newlocations)
	return len(locations)


def part1(field, start, loops):
	locations = [start]
	for loop in range(loops):
		newlocations = []
		for location in locations:
			newlocations += spread(field, location)
		locations = set(newlocations)
	return len(locations)





field, start = parse(data)
# print(part1(field, start, 64))
