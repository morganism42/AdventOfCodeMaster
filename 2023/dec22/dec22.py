from aocd import get_data, submit
from copy import deepcopy

data = get_data(day=22)
test = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''


class brick:
	def __init__(self, line, name):
		line = line.split('~')
		self.x1, self.y1, self.z1 = [int(i) for i in line[0].split(',')]
		self.x2, self.y2, self.z2 = [int(i) for i in line[1].split(',')]
		self.name = str(name)
		self.supported = 0
		self.supporters = []
		self.supporting = []

	def lower(self, area):
		free = True
		while free:
			if self.z1 == 0:
				break
			self.z1 -= 1
			self.z2 -= 1

			for x in range(self.x1, self.x2 + 1):
				for y in range(self.y1, self.y2 + 1):
					if area[x][y][self.z1 - 1] != ' ':
						free = False

		for x in range(self.x1, self.x2 + 1):
			for y in range(self.y1, self.y2 + 1):
				area[x][y][self.z2] = self.name
				if area[x][y][self.z1 - 1] != ' ' and area[x][y][self.z1 - 1] not in self.supporters and self.z1 != 0:
					self.supporters.append(area[x][y][self.z1 - 1])
		self.supported = len(self.supporters)

	def droplower(self, area):
		supported = False
		for x in range(self.x1, self.x2 + 1):
			for y in range(self.y1, self.y2 + 1):
				if area[x][y][self.z1 - 1] != ' ':
					supported = True
		if supported:
			for x in range(self.x1, self.x2 + 1):
				for y in range(self.y1, self.y2 + 1):
					area[x][y][self.z2] = self.name
			return False
		else:
			return True


	def dropchain(self, areal, brickl):
		bricklist = deepcopy(brickl)
		area = deepcopy(areal)
		dropping = 0
		for x in range(self.x1, self.x2 + 1):
			for y in range(self.y1, self.y2 + 1):
				area[x][y][self.z2] = ' '
		for b in bricklist:
			if b.z1 > self.z2:
				for x in range(b.x1, b.x2 + 1):
					for y in range(b.y1, b.y2 + 1):
						area[x][y][b.z2] = ' '
				if b.droplower(area):
					dropping += 1

		return dropping


def part1(bricks):
	bricks = bricks.split('\n')
	area = [[[' ' for z in range(len(bricks))] for y in range(10)] for x in range(10)]
	bricklist = []
	for b in bricks:
		bricklist.append(brick(b, bricks.index(b)))
	bricklist.sort(key=lambda x: x.z1)

	for b in bricklist:
		b.lower(area)
	supporters = []
	for b in bricklist:
		if b.supported == 1:
			supporters.append(b.supporters[0])
	print(len(bricklist), len(set(supporters)))
	return len(bricklist) - len(set(supporters))


def part2(bricks):
	bricks = bricks.split('\n')
	area = [[[' ' for z in range(len(bricks))] for y in range(10)] for x in range(10)]
	bricklist = []
	for b in bricks:
		bricklist.append(brick(b, bricks.index(b)))
	bricklist.sort(key=lambda x: x.z1)

	for b in bricklist:
		b.lower(area)
	bricklist.sort(key=lambda x: x.z1)
	dropchains = []
	for n, b in enumerate(bricklist):
		print(n)
		dropchains.append(b.dropchain(area, bricklist[n + 1:]))
	return sum(dropchains)


print(part2(data))
