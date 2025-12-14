from aocd import get_data

test = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''
data = get_data(day=9, year=2025)


def parse(Data):
	return [tuple((int(x.split(',')[0]), int(x.split(',')[1]))) for x in Data.splitlines()]


def part1(Data):
	largest = 0
	Data = parse(Data)
	for x, point1 in enumerate(Data[:-1]):
		for point2 in Data[x + 1:]:
			rect = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
			if rect > largest:
				largest = rect
	return largest


def part2(Data):
	Data = parse(Data)
	rects = []
	for x, point1 in enumerate(Data[:-1]):
		for point2 in Data[x + 1:]:
			rect = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
			rects.append((point1, point2, rect))
	rects.sort(key=lambda a: -a[2])
	Data.append(Data[0])
	for rect in rects:
		xpair = [rect[0][0], rect[1][0]]
		xpair.sort()
		ypair = [rect[0][1], rect[1][1]]
		ypair.sort()
		for x in range(len(Data) - 1):
			nxpair = [Data[x][0], Data[x + 1][0]]
			nxpair.sort()
			nypair = [Data[x][1], Data[x + 1][1]]
			nypair.sort()
			if nypair[0] == nypair[1] and ypair[0] < nypair[0] < ypair[1]:
				if xpair[0] <= nxpair[0] < xpair[1] or xpair[0] < nxpair[1] <= xpair[1] or (nxpair[0] < xpair[0] and xpair[1] < nxpair[1]):
					break
			if nxpair[0] == nxpair[1] and xpair[0] < nxpair[0] < xpair[1]:
				if ypair[0] <= nypair[0] < ypair[1] or ypair[0] < nypair[1] <= ypair[1] or (nypair[0] < ypair[0] and ypair[1] < nypair[1]):
					break
		else:
			return rect
