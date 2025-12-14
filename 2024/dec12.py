from aocd import get_data, submit


def floodfill(grid, x, y, flooded, perimeter):
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	flooded.add((x, y))
	for dx, dy in directions:
		nx, ny = x + dx, y + dy
		if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
			if grid[nx][ny] != grid[x][y]:
				perimeter.add((x, y, nx, ny))
			elif (nx, ny) not in flooded:
				floodfill(grid, nx, ny, flooded, perimeter, )
		else:
			perimeter.add((x, y, nx, ny))
	return flooded, perimeter


def solve1(test=True):
	# Your solution code here
	testdata = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
	testans = 1930
	if test:
		data = testdata
	else:
		data = get_data(day=12, year=2024)
	grid = [list(x) for x in data.splitlines()]
	result = 0
	for x in range(len(grid[0])):
		for y in range(len(grid)):
			if grid[x][y] == '.':
				continue
			flooded = set()
			perimeter = set()
			flooded, perimeter = floodfill(grid, x, y, flooded, perimeter)
			result += len(perimeter) * len(flooded)
			for flood in flooded:
				grid[flood[0]][flood[1]] = '.'

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
		print(result)
	elif not test:
		print(result)
		submit(result, part="a", day=12, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
	testans = 1206
	if test:
		data = testdata
	else:
		data = get_data(day=12, year=2024)
	grid = [list(x) for x in data.splitlines()]
	result = 0
	for x in range(len(grid[0])):
		for y in range(len(grid)):
			if grid[x][y] == '.':
				continue
			flooded = set()
			perimeter = set()
			flooded, perimeter = floodfill(grid, x, y, flooded, perimeter)
			sides = 0
			for wall in perimeter:
				if (wall[0] + 1, wall[1], wall[2] + 1, wall[3]) in perimeter or (wall[0], wall[1] + 1, wall[2], wall[3] + 1) in perimeter:
					continue
				else:
					sides += 1
			result += len(flooded) * sides

			for flood in flooded:
				grid[flood[0]][flood[1]] = '.'

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
		print(result)
	elif not test:
		print(result)
		submit(result, part="b", day=12, year=2024)


solve2(False)
