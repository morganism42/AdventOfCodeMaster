from aocd import get_data, submit
from math import ceil, floor
from matplotlib import pyplot as plt


def solve1(test=True):
	# Your solution code here
	testdata = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
	testans = 12
	if test:
		data = testdata
	else:
		data = get_data(day=14, year=2024)
	if test:
		size = (7, 11)
	else:
		size = (103, 101)
	grid = [[[] for i in range(size[0])] for j in range(size[1])]
	data = data.splitlines()
	for robot in data:
		robot = robot[2:].split(" v=")
		p = robot[0].split(",")
		grid[int(p[0])][int(p[1])].append(tuple([int(i) for i in robot[1].split(',')]))

	for rep in range(100):
		newgrid = [[[] for i in range(size[0])] for j in range(size[1])]
		for x, row in enumerate(grid):
			for y, column in enumerate(row):
				if len(column) == 0:
					continue
				for bot in column:
					newx = x + bot[0]
					newy = y + bot[1]
					if newx >= size[1]:
						newx -= size[1]
					if newy >= size[0]:
						newy -= size[0]
					if newx < 0:
						newx += size[1]
					if newy < 0:
						newy += size[0]
					newgrid[newx][newy].append(bot)
		grid = newgrid
	quads = (((0, 0), (floor(size[0] / 2), floor(size[1] / 2))),
	         ((ceil(size[0] / 2), 0), (size[0], floor(size[1] / 2))),
	         ((0, ceil(size[1] / 2)), (floor(size[0] / 2), size[1])),
	         ((ceil(size[0] / 2), ceil(size[1] / 2)), (size[0], size[1])))
	result = 1
	for quad in quads:
		quadsum = 0
		for y in range(quad[0][0], quad[1][0]):
			for x in range(quad[0][1], quad[1][1]):
				quadsum += len(newgrid[x][y])
		result *= quadsum

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=14, year=2024)


def hellbox(test=True):
	# Your solution code here
	testdata = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
	testans = 12
	if test:
		data = testdata
	else:
		data = get_data(day=14, year=2024)
	if test:
		size = (7, 11)
	else:
		size = (103, 101)
	grid = [[[] for i in range(size[0])] for j in range(size[1])]
	data = data.splitlines()
	for robot in data:
		robot = robot[2:].split(" v=")
		p = robot[0].split(",")
		grid[int(p[0])][int(p[1])].append(tuple([int(i) for i in robot[1].split(',')]))

	for rep in range(10000):
		newgrid = [[[] for i in range(size[0])] for j in range(size[1])]
		for x, row in enumerate(grid):
			for y, column in enumerate(row):
				if len(column) == 0:
					continue
				for bot in column:
					newx = x + bot[0]
					newy = y + bot[1]
					if newx >= size[1]:
						newx -= size[1]
					if newy >= size[0]:
						newy -= size[0]
					if newx < 0:
						newx += size[1]
					if newy < 0:
						newy += size[0]
					newgrid[newx][newy].append(bot)
		grid = newgrid
		x = []
		y = []
		for j, row in enumerate(grid):
			for k, column in enumerate(row):
				if len(column) > 0:
					x.append(j)
					y.append(k)
		plt.scatter(x, y)
		plt.savefig(f"hellbox/{rep}.png")
		plt.close()


def solve2(test=True):
	# Your solution code here
	testdata = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
	testans = 12
	if test:
		data = testdata
	else:
		data = get_data(day=14, year=2024)
	if test:
		size = (7, 11)
	else:
		size = (103, 101)
	grid = [[[] for i in range(size[0])] for j in range(size[1])]
	data = data.splitlines()
	for robot in data:
		robot = robot[2:].split(" v=")
		p = robot[0].split(",")
		grid[int(p[0])][int(p[1])].append(tuple([int(i) for i in robot[1].split(',')]))

	for rep in range(10000):
		newgrid = [[[] for i in range(size[0])] for j in range(size[1])]
		for x, row in enumerate(grid):
			for y, column in enumerate(row):
				if len(column) == 0:
					continue
				for bot in column:
					newx = x + bot[0]
					newy = y + bot[1]
					if newx >= size[1]:
						newx -= size[1]
					if newy >= size[0]:
						newy -= size[0]
					if newx < 0:
						newx += size[1]
					if newy < 0:
						newy += size[0]
					newgrid[newx][newy].append(bot)
		grid = newgrid
		x = []
		y = []
		collision = False
		for j, row in enumerate(grid):
			for k, column in enumerate(row):
				if len(column) > 0:
					x.append(j)
					y.append(k)
				if len(column) > 1:
					collision = True
		if not collision:
			submit(rep + 1, part="b", day=14, year=2024)
