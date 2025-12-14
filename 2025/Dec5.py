from aocd import get_data, submit
import time

data = get_data(day=5, year=2025)

test = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''


def parser(Data):
	ranges, ingredients = Data.split('\n\n')
	return [[int(chunk.split('-')[0]), int(chunk.split('-')[1])] for chunk in ranges.splitlines()], [int(x) for x in ingredients.splitlines()]


def part1(Data):
	# I mean I just check if its in one of the ranger what do you want
	Data = parser(Data)
	ans = 0
	Fresh, ingredients = Data
	for veg in ingredients:
		for s, e in Fresh:
			if s <= veg <= e:
				ans += 1
				break
	print(ans)
	return ans



def part2(Data):
	Data = parser(Data)
	area = Data[0]
	area.sort(key=lambda a: a[0])
	newarea = [area[0]]
	# first I get the true ranges by checking for overlaps and accounting for them
	for i in range(1, len(area)):
		if area[i][0] <= newarea[-1][1] < area[i][1]:
			newarea[-1][1] = area[i][1]
		elif area[i][0] > newarea[-1][1]:
			newarea.append(area[i])
	ans = 0
	# than I count the numbers in each range
	for zone in newarea:
		ans += zone[1] - zone[0] + 1
	print(ans)


start = time.time()
print(part2(data))
end = time.time()
print(f'Time taken: {(end - start)*1000}ms')
