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
	elif field[y][x - 1] in '-FL':
		pos.append([[y, x], [y, x - 1]])
	elif field[y + 1][x] in '|JL':
		pos.append([[y, x], [y + 1, x]])
	elif field[y - 1][x] in '|F7':
		pos.append([[y, x], [y - 1, x]])
	return pos


y, x = findStart(field)
start = [y, x]
positions = firstep(y, x)
steps = 1
loop = True
path = positions[0].copy()
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
	path.append(positions[0][1])  # add the next step to the path
	if positions[0][1] == start:
		loop = False


def mapout(y, x, path, mapped, area=0):  # floodfills an area bound by the path
	area += 1
	if [y + 1, x] not in path and [y + 1, x] not in mapped:
		mapped.append([y + 1, x])
		mapped, area = mapout(y + 1, x, path, mapped, area)
	if [y - 1, x] not in path and [y - 1, x] not in mapped:
		mapped.append([y - 1, x])
		mapped, area = mapout(y - 1, x, path, mapped, area)
	if [y, x + 1] not in path and [y, x + 1] not in mapped:
		mapped.append([y, x + 1])
		mapped, area = mapout(y, x + 1, path, mapped, area)
	if [y, x - 1] not in path and [y, x - 1] not in mapped:
		mapped.append([y, x - 1])
		mapped, area = mapout(y, x - 1, path, mapped, area)
	return mapped, area


def findside(path):  # finds a | on the edge of the map and returns what side is inside the path
	for i in path:
		if i[1] + 1 == len(field[0]) and field[i[0]][i[1]] == '|':
			return True, i
		elif i[1] == 0 and field[i[0]][i[1]] == '|':
			return False, i


left, start = findside(path)
if left:
	direction = 'left'
else:
	direction = 'right'
side = direction  # which side is inside the path
mapped = []  # area that is mapped out
total = 0  # variable that ended up being unused but isn't worth removing due to being in functions
overpath = path.copy()  # listen, I did this at 2am and I don't remember why I did this the way I did, over path is the original path
path2 = path[path.index(start):]  # path 2 is one side of the path originating from the | on the edge of the map
path = path[:path.index(start) + 1]  # the other side of the path

for n in range(len(path) - 1, -1, -1):
	i = path[n]
	# for bends floodfills the side before the corner
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp
	# for corners determines the change of direction
	if field[i[0]][i[1]] == 'L':
		if path[n + 1][0] < i[0]:
			if direction == 'right':
				direction = 'up'
			elif direction == 'left':
				direction = 'down'
		elif path[n + 1][1] > i[1]:
			if direction == 'up':
				direction = 'right'
			elif direction == 'down':
				direction = 'left'
	elif field[i[0]][i[1]] == '7':
		if path[n + 1][1] < i[1]:
			if direction == 'down':
				direction = 'left'
			elif direction == 'up':
				direction = 'right'
		elif path[n + 1][0] > i[0]:
			if direction == 'left':
				direction = 'down'
			elif direction == 'right':
				direction = 'up'
	elif field[i[0]][i[1]] == 'F':
		if path[n + 1][1] > i[1]:
			if direction == 'down':
				direction = 'right'
			elif direction == 'up':
				direction = 'left'
		elif path[n + 1][0] > i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	elif field[i[0]][i[1]] == 'J':
		if path[n + 1][1] < i[1]:
			if direction == 'up':
				direction = 'left'
			elif direction == 'down':
				direction = 'right'
		elif path[n + 1][0] < i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	# for bends floodfills the side after the corner
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp

path = path2
direction = side


#same as above but for the other side of the path
for n, i in enumerate(path):
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp
	if field[i[0]][i[1]] == 'L':
		if path[n - 1][0] < i[0]:
			if direction == 'right':
				direction = 'up'
			elif direction == 'left':
				direction = 'down'
		elif path[n - 1][1] > i[1]:
			if direction == 'up':
				direction = 'right'
			elif direction == 'down':
				direction = 'left'
	elif field[i[0]][i[1]] == '7':
		if path[n - 1][1] < i[1]:
			if direction == 'down':
				direction = 'left'
			elif direction == 'up':
				direction = 'right'
		elif path[n - 1][0] > i[0]:
			if direction == 'left':
				direction = 'down'
			elif direction == 'right':
				direction = 'up'
	elif field[i[0]][i[1]] == 'F':
		if path[n - 1][1] > i[1]:
			if direction == 'down':
				direction = 'right'
			elif direction == 'up':
				direction = 'left'
		elif path[n - 1][0] > i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	elif field[i[0]][i[1]] == 'J':
		if path[n - 1][1] < i[1]:
			if direction == 'up':
				direction = 'left'
			elif direction == 'down':
				direction = 'right'
		elif path[n - 1][0] < i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp


#creates a nice visual for the map
fancymap = []
for i in range(len(field)):
	fancymap.append([])
	for j in range(len(field[i])):
		if [i, j] in mapped:
			fancymap[-1].append('O')
		elif [i, j] in overpath:
			fancymap[-1].append(field[i][j])
		else:
			fancymap[-1].append('.')
	fancymap[-1] = ''.join(fancymap[-1])
for i in fancymap:
	print(i)
