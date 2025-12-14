from aocd import get_data, submit

data = get_data(year=2015, day=1)


def solve1(data):
	return data.count('(') - data.count(')')


def solve2(data):
	floor = 0
	for i, c in enumerate(data):
		if c == '(':
			floor += 1
		else:
			floor -= 1
		if floor == -1:
			return i + 1


print("Part 1:", solve1(data))
print("Part 2:", solve2(data))