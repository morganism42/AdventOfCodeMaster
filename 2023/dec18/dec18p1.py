import sys


def floodfill(y, x):
	global mapped
	if lake[y + 1][x][0] == '.' and [y + 1, x] not in mapped:
		mapped.append([y + 1, x])
		lake[y + 1][x][0] = '#'
		mapped = floodfill(y + 1, x)
	if lake[y - 1][x][0] == '.' and [y - 1, x] not in mapped:
		mapped.append([y - 1, x])
		lake[y - 1][x][0] = '#'
		mapped = floodfill(y - 1, x)
	if lake[y][x + 1][0] == '.' and [y, x + 1] not in mapped:
		mapped.append([y, x + 1])
		lake[y][x + 1][0] = '#'
		mapped = floodfill(y, x + 1)
	if lake[y][x - 1][0] == '.' and [y, x - 1] not in mapped:
		mapped.append([y, x - 1])
		lake[y][x - 1][0] = '#'
		mapped = floodfill(y, x - 1)
	return mapped


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	with open('C:\\Users\\liams\\PycharmProjects\\Advent_2023\\dec18\\dec18.txt') as f:
		instructs = [i.split(' ') for i in f.read().split('\n')]

	lake = [[['.', '']]]
	directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
	coord = (0, 0)
	mapped = []
	for i in instructs:
		newcoord = (coord[0] + directions[i[0]][0] * int(i[1]), coord[1] + directions[i[0]][1] * int(i[1]))
		if newcoord[0] < 0:
			for n in range(abs(0 - newcoord[0])):
				lake.insert(0, [['.', ''] for k in range(len(lake[0]))])
			coord = (coord[0]+abs(newcoord[0]), coord[1])
			newcoord = (0, newcoord[1])
		if newcoord[1] < 0:
			for n in range(abs(0 - newcoord[1])):
				for k in range(len(lake)):
					lake[k].insert(0, ['.', ''])
			coord = (coord[0], coord[1]+abs(newcoord[1]))
			newcoord = (newcoord[0], 0)
		if newcoord[0] >= len(lake):
			for n in range(newcoord[0] - len(lake) + 1):
				lake.append([['.', ''] for k in range(len(lake[0]))])
		if newcoord[1] >= len(lake[0]):
			for n in range(newcoord[1] - len(lake[0]) + 1):
				for k in range(len(lake)):
					lake[k].append(['.', ''])
		if newcoord[0] == coord[0]:
			if newcoord[1] < coord[1]:
				zip = -1
			else:
				zip = 1
			for n in range(coord[1], newcoord[1] + zip, zip):
				lake[coord[0]][n] = ['#', i[-1]]
		elif newcoord[1] == coord[1]:
			if newcoord[0] < coord[0]:
				zip = -1
			else:
				zip = 1
			for n in range(coord[0], newcoord[0] + zip, zip):
				lake[n][coord[1]] = ['#', i[-1]]
		coord = newcoord
	for i in range(len(lake)):
		for j in range(len(lake[0])):
			if lake[i][j][0] == '#':
				mapped.append([i, j])
				lake[i][j][0] = '#'
				mapped = floodfill(i+1, j+1)
				print(sum([[i[0] for i in j].count('#') for j in lake]))
				exit()
