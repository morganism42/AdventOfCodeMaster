from aocd import get_data

data = get_data(year=2015, day=6)


def parse(data):
	data = data.splitlines()
	commands = []
	action = 0
	depth = 0
	for command in data:
		if command[:7] == 'turn on':
			action = 1
			depth = 8
		elif command[:8] == 'turn off':
			action = -1
			depth = 9
		elif command[:6] == 'toggle':
			action = 0
			depth = 7
		numbers = []
		for numpair in command[depth:].split('through'):
			temp = numpair.split(',')
			numbers.append((int(temp[0]), int(temp[1])))
		commands.append((action, tuple(numbers)))
	return commands



def solve1(data):
	commands = parse(data)
	grid = [[-1 for i in range(1000)] for j in range(1000)]
	for command in commands:
		for x in range(command[1][0][0], command[1][1][0]+1):
			for y in range(command[1][0][1], command[1][1][1]+1):
				if command[0] == 0:
					grid[x][y] *= -1
				else:
					grid[x][y] = command[0]

	return sum([line.count(1) for line in grid])
def solve2(data):
	commands = parse(data)
	grid = [[0 for i in range(1000)] for j in range(1000)]
	for command in commands:
		for x in range(command[1][0][0], command[1][1][0]+1):
			for y in range(command[1][0][1], command[1][1][1]+1):
				if command[0] == 0:
					grid[x][y] += 2
				else:
					grid[x][y] += command[0]
				if grid[x][y]<0:grid[x][y] = 0

	return sum([sum(line) for line in grid])
print(solve2(data))
