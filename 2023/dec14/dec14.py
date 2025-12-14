from copy import deepcopy

with open('dec14.txt') as f:
	lines = f.read().split('\n')
	data = [list(line) for line in lines]


# functions to move the rock around
def moveup(x, y):
	for i in range(y, 0, -1):
		if data[i - 1][x] in 'O#':
			data[i][x] = 'O'
			return
	data[0][x] = 'O'


def moveright(x, y):
	for i in range(x, len(data[y]) - 1):
		if data[y][i + 1] in 'O#':
			data[y][i] = 'O'
			return
	data[y][-1] = 'O'


def movedown(x, y):
	for i in range(y, len(data) - 1):
		if data[i + 1][x] in 'O#':
			data[i][x] = 'O'
			return
	data[-1][x] = 'O'


def moveleft(x, y):
	for i in range(x, 0, -1):
		if data[y][i - 1] in 'O#':
			data[y][i] = 'O'
			return
	data[y][0] = 'O'


# cycle through the rock's movements
def cycle():
	for y, line in enumerate(data):
		for x, space in enumerate(line):
			if space == 'O':
				data[y][x] = '.'
				moveup(x, y)
	for y, line in enumerate(data):
		for x in range(len(line)):
			if line[x] == 'O':
				line[x] = '.'
				moveleft(x, y)
	for y in range(len(data) - 1, -1, -1):
		for x in range(len(data[y]) - 1, -1, -1):
			if data[y][x] == 'O':
				data[y][x] = '.'
				movedown(x, y)
	for y in range(len(data) - 1, -1, -1):
		for x in range(len(data[y]) - 1, -1, -1):
			if data[y][x] == 'O':
				data[y][x] = '.'
				moveright(x, y)


past = []
for j in range(1000000000):  # cycle the rocks till you're at a state you've been before
	past.append(deepcopy(data))
	cycle()
	if data in past:
		break
repeats = past[past.index(data):]  # states that are part of the loop
index = ((1000000000 - (j + 1)) % len(repeats))  # index of the state you're at at the end of the 1 billionth cycle
data = repeats[index]
weight = 0
for x, line in enumerate(data):
	for y, space in enumerate(line):
		if space == 'O':
			weight += len(data) - x
print(weight)
