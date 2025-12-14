from aocd import get_data

data = get_data(year=2015, day=2).split('\n')
data = [list(map(int, x.split('x'))) for x in data]
print(data)


def part1(data):
	total = 0
	for box in data:
		l, w, h = box
		sides = [l * w, w * h, h * l]
		total += sum(sides) * 2 + min(sides)
	return total


def part2(data):
	total = 0
	for box in data:
		box.sort()
		total += box[0] * 2 + box[1] * 2 + box[0] * box[1] * box[2]
	return total


print(part1(data))
print(part2(data))
