import sys

with open('dec16.txt') as f:
	field = [list(i) for i in f.read().split('\n')]
sys.setrecursionlimit(100000)


def beam(y, x, direction):
	if not (len(field) > y >= 0) or not (len(field[0]) > x >= 0):
		return
	if direction not in energy[y][x][1]:
		energy[y][x][1].append(direction)
	else:
		return
	energy[y][x][0] += 1
	if field[y][x] == '/':
		direction = (direction[1], direction[0])
		beam(y - direction[0], x + direction[1], direction)
	elif field[y][x] == '\\':
		direction = (-direction[1], -direction[0])
		beam(y - direction[0], x + direction[1], direction)
	elif field[y][x] == '-' and direction[0] != 0:
		beam(y, x + 1, (0, 1))
		beam(y, x - 1, (0, -1))
	elif field[y][x] == '|' and direction[1] != 0:
		beam(y - 1, x, (1, 0))
		beam(y + 1, x, (-1, 0))
	else:
		beam(y - direction[0], x + direction[1], direction)


totals = []
p = 0
energy = [[[0, []] for i in range(len(field[0]))] for j in range(len(field))]
beam(p, 0, (0, 1))
total = 0
for i in energy:
	for j in i:
		if j[0] != 0:
			total += 1
totals.append(total)

print(max(totals))
