from aocd import get_data, submit
from itertools import combinations
from z3 import *

data = get_data(day=24)
test = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''


def parse(intake):  # turn each hail into [[x y z], [dx dy dz]]
	intake = intake.split('\n')
	hails = []
	for line in intake:
		line = line.split(' @ ')
		hails.append([[int(i) for i in line[0].split(', ')], [int(i) for i in line[1].split(', ')]])
	return hails


def crosstest2d(a, b, area):
	# find the slope and intercept of each line in the x y plane
	slopea = a[1][2] / a[1][0]
	inta = -slopea * a[0][0] + a[0][2]
	slopeb = b[1][2] / b[1][0]
	intb = -slopeb * b[0][0] + b[0][2]
	if slopea == slopeb:  # check if parallel
		return False
	x = (intb - inta) / (slopea - slopeb)  # find the x and calculate y from x
	y = slopea * x + inta
	point = (x, y)
	for n in point:  # check if within bounding box
		if n < area[0] or n > area[1]:
			return False
	# make sure it's in the correct direction
	for n in range(2):
		if (point[n] < a[0][n] and a[1][n] > 0) or (point[n] > a[0][n] and a[1][n] < 0) or (
				point[n] < b[0][n] and b[1][n] > 0) or (point[n] > b[0][n] and b[1][n] < 0):
			return False
	return True


def part1():
	hails = parse(data)
	pairs = combinations(hails, 2)  # get each possible pair of hailstones
	total = 0
	for i in pairs:
		if crosstest2d(i[0], i[1], (200000000000000, 400000000000000)):
			total += 1
	print(total)


def part2(data):
	hails = parse(data)
	x, y, z, t0, t1, t2, dx, dy, dz = Ints('x y z t0 t1 t2 dx dy dz')
	# declare variables for unknowns, origin and slope of rock, and time of intersections with 3 hail
	# only need 3 hail cause a line that intercepts them will also intercept all other hail
	answer = Int('answer')
	# solve as a linear equation
	s = Solver()
	s.add(x + dx * t0 == hails[0][0][0] + hails[0][1][0] * t0)
	s.add(y + dy * t0 == hails[0][0][1] + hails[0][1][1] * t0)
	s.add(z + dz * t0 == hails[0][0][2] + hails[0][1][2] * t0)
	s.add(x + dx * t1 == hails[1][0][0] + hails[1][1][0] * t1)
	s.add(y + dy * t1 == hails[1][0][1] + hails[1][1][1] * t1)
	s.add(z + dz * t1 == hails[1][0][2] + hails[1][1][2] * t1)
	s.add(x + dx * t2 == hails[2][0][0] + hails[2][1][0] * t2)
	s.add(y + dy * t2 == hails[2][0][1] + hails[2][1][1] * t2)
	s.add(z + dz * t2 == hails[2][0][2] + hails[2][1][2] * t2)
	s.add(t0 >= 0)
	s.add(answer == x + y + z)
	s.check()
	m = s.model()
	return int(m[answer].as_long())


submit(part2(data), day=24)
