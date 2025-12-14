from aocd import get_data, submit


def solve1(test=True):
	# Your solution code here
	testdata = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
	testans = 36
	if test:
		data = testdata
	else:
		data = get_data(day=10, year=2024)
	data = [[int(spot) for spot in row] for row in data.split("\n")]
	trailheads = []
	for x in range(len(data)):
		for y in range(len(data[x])):
			if data[x][y] == 0:
				trailheads.append((x, y))
	result = 0
	directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
	for zero in trailheads:
		current = [zero]
		visited = set()
		ends = set()
		while len(current) > 0:
			x, y = current.pop()
			for way in directions:
				newx, newy = x + way[0], y + way[1]
				if 0 <= newx < len(data) and 0 <= newy < len(data[newx]):
					if data[newx][newy] == data[x][y] + 1 and (newx, newy) not in visited:
						current.append((newx, newy))
						if data[newx][newy] == 9:
							ends.add((newx, newy))
						visited.add((newx, newy))
		result += len(ends)
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=10, year=2024)

def solve2(test=True):
	# Your solution code here
	testdata = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
	testans = 81
	if test:
		data = testdata
	else:
		data = get_data(day=10, year=2024)
	data = [[int(spot) for spot in row] for row in data.split("\n")]
	trailheads = []
	for x in range(len(data)):
		for y in range(len(data[x])):
			if data[x][y] == 0:
				trailheads.append((x, y))
	result = 0
	directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
	for zero in trailheads:
		current = [zero]

		while len(current) > 0:
			x, y = current.pop()
			for way in directions:
				newx, newy = x + way[0], y + way[1]
				if 0 <= newx < len(data) and 0 <= newy < len(data[newx]):
					if data[newx][newy] == data[x][y] + 1:
						current.append((newx, newy))
						if data[newx][newy] == 9:
							result += 1
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=10, year=2024)
solve2(False)