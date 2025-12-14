from aocd import get_data, submit
from tqdm import trange


def solve1(test=True):
	# Your solution code here
	testdata = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
	testans = 22
	if test:
		data = testdata
		end = (6, 6)
		falling = 12
	else:
		falling = 1024
		end = (70, 70)
		data = get_data(day=18, year=2024)
	grid = [['.' for x in range(end[1] + 1)] for y in range(end[0] + 1)]
	data = [[int(i) for i in pair.split(',')] for pair in data.split('\n')]
	for fall in range(falling):
		grid[data[fall][0]][data[fall][1]] = '#'
	current = [((0, 0), 0)]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	dicgrid = {}
	for x in range(end[0] + 1):
		for y in range(end[1] + 1):
			if grid[x][y] != '#':
				dicgrid[(x, y)] = []
				for dx, dy in directions:
					if 0 <= x + dx < end[0] + 1 and 0 <= y + dy < end[1] + 1:
						if grid[x + dx][y + dy] != '#':
							dicgrid[(x, y)].append((x + dx, y + dy))
	checked = set()
	while current:
		looking = current.pop(0)
		for neighbour in dicgrid[looking[0]]:
			if neighbour in checked:
				continue
			if neighbour == end:
				result = looking[1] + 1
				current = []
				break
			else:
				current.append((neighbour, looking[1] + 1))
			checked.add(neighbour)
		current = sorted(current, key=lambda dist: dist[1])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=18, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
	testans = '6,1'
	if test:
		data = testdata
		end = (6, 6)
	else:
		end = (70, 70)
		data = get_data(day=18, year=2024)
	grid = [[['.', [0, 0, 0, 0]] for x in range(end[1] + 1)] for y in range(end[0] + 1)]
	data = [[int(i) for i in pair.split(',')] for pair in data.split('\n')]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
	result = ''
	walls = set()
	for i in trange(len(data)):
		fall = data[i]
		grid[fall[0]][fall[1]][0] = '#'
		walls.add((fall[0], fall[1]))
		if fall[0] == 0:
			grid[fall[0]][fall[1]][1][0] = 1
		elif fall[0] == end[0]:
			grid[fall[0]][fall[1]][1][1] = 1
		if fall[1] == 0:
			grid[fall[0]][fall[1]][1][2] = 1
		elif fall[1] == end[1]:
			grid[fall[0]][fall[1]][1][3] = 1
		change = True
		while change:
			change = False
			for wall in walls:
				for dx, dy in directions:
					if 0 <= wall[0] + dx <= end[0] and 0 <= wall[1] + dy <= end[1]:
						if grid[wall[0] + dx][wall[1] + dy][0] == '#':
							for edge in range(4):
								if grid[wall[0]][wall[1]][1][edge] + grid[wall[0] + dx][wall[1] + dy][1][edge] == 1:
									grid[wall[0]][wall[1]][1][edge] = 1
									grid[wall[0] + dx][wall[1] + dy][1][edge] = 1
									change = True
				checker = grid[wall[0]][wall[1]][1]
				if checker[0] + checker[1] == 2 or checker[2] + checker[3] == 2 or checker[0] + checker[2] == 2 or \
						checker[1] + checker[3] == 2:
					result = f"{fall[0]},{fall[1]}"
		if result:
			break

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=18, year=2024)


solve2()
