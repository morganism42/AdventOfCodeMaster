from aocd import get_data, submit

data = get_data(year=2024, day=4)


def part1(data):
	data = data.splitlines()
	directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
	hits = 0
	for x, row in enumerate(data):
		for y, letter in enumerate(row):
			if letter == 'X':
				for dx, dy in directions:
					try:  # probably not best practice but in this scenario it has no downsides
						if data[x + dx][y + dy] == 'M' and data[x + 2 * dx][y + 2 * dy] == 'A' and data[x + 3 * dx][
							y + 3 * dy] == 'S':
							hits += 1
					except:
						pass
	return hits


def part2(data):
	data = data.splitlines()
	total = 0
	for x, row in enumerate(data):
		for y, letter in enumerate(row):
			if letter == 'A':
				if x == 0 or x == len(data) - 1 or y == 0 or y == len(data[0]) - 1:
					continue
				elif (data[x + 1][y + 1] == 'M' and data[x - 1][y - 1] == 'S') or (
						data[x - 1][y - 1] == 'M' and data[x + 1][y + 1] == 'S'):
					if (data[x + 1][y - 1] == 'M' and data[x - 1][y + 1] == 'S') or (
							data[x - 1][y + 1] == 'M' and data[x + 1][y - 1] == 'S'):
						total += 1
	return total


submit(part1(data), part=1)
