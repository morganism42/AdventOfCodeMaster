with open('dec10.txt') as f:
	field = f.read().split('\n')


def findStart(lines):  # finds the starting position
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == 'S':
				return i, j


def firstep(y, x):  # finds the first step in both directions
	pos = []
	if field[y][x + 1] in '-J7':
		pos.append([[y, x], [y, x + 1]])
	if field[y][x - 1] in '-FL':
		pos.append([[y, x], [y, x - 1]])
	if field[y + 1][x] in '|JL':
		pos.append([[y, x], [y + 1, x]])
	if field[y - 1][x] in '|F7':
		pos.append([[y, x], [y - 1, x]])
	print(pos)
	return pos


y, x = findStart(field)
positions = firstep(y, x)
steps = 1
loop = True
while loop:
	steps += 1
	for n, i in enumerate(
			positions.copy()):  # in both directions look at the next steps pipe and determine the step after that
		if field[i[1][0]][i[1][1]] == '|':
			if i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
		elif field[i[1][0]][i[1][1]] == '-':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
			elif i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif field[i[1][0]][i[1][1]] == 'L':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif field[i[1][0]][i[1][1]] == '7':
			if i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
			elif i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
		elif field[i[1][0]][i[1][1]] == 'F':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
			elif i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif field[i[1][0]][i[1][1]] == 'J':
			if i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
	if positions[0][1] == positions[1][1]:
		loop = False
print(positions)
print(steps)
