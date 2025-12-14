from aocd import get_data

data = get_data(year=2015, day=3)


def parse(data):
	moves = []
	for move in data:
		match move:
			case '^':
				moves.append((0, 1))
			case 'v':
				moves.append((0, -1))
			case '<':
				moves.append((-1, 0))
			case '>':
				moves.append((1, 0))
	return moves


def part1(data):
	moves = parse(data)
	visited = {(0, 0)}
	x, y = 0, 0
	for dx, dy in moves:
		x += dx
		y += dy
		visited.add((x, y))
	return len(visited)


def part2(data):
	moves = parse(data)
	visited = {(0, 0)}
	robo = False
	x, rx, y, ry = 0, 0, 0, 0
	for dx, dy in moves:
		if robo:
			rx += dx
			ry += dy
			visited.add((rx, ry))
			robo = False
		else:
			robo = True
			x += dx
			y += dy
			visited.add((x, y))
	return len(visited)


print(part1(data))
print(part2(data))