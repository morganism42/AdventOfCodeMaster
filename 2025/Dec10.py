import math
from aocd import get_data
import itertools
from scipy.optimize import linprog

test = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''
data = get_data(day=10, year=2025)


def parse(Data):
	Data = Data.splitlines()
	Data = [x.split(' ') for x in Data]
	newData = []
	for x, row in enumerate(Data):
		lights = []
		for light in row[0][1:-1]:
			if light == '#':
				lights.append(1)
			else:
				lights.append(0)
		buttons = row[1:-1]
		for n, button in enumerate(buttons):
			buttons[n] = tuple(int(i) for i in button[1:-1].split(','))
		buttons = tuple(buttons)
		jolts = tuple([int(i) for i in row[-1][1:-1].split(',')])
		newData.append([lights, buttons, jolts])
	return newData


def part1(Data):
	Data = parse(Data)
	ans = 0
	for light, wires, jolt in Data:
		ans += findpresseslights(wires, light)

	return ans


def findpresseslights(wires, lights):
	linwires = []
	for x in lights:
		linwires.append([])
		for y in wires:
			linwires[-1].append(0)
	for x in range(len(wires)):
		for y in range(len(lights)):
			if y in wires[x]:
				linwires[y][x] = 1
	presses = [set()]
	for wire in range(len(wires)):
		presses[-1].add(tuple([0] * wire + [1] + [0] * (len(wires) - (wire + 1))))

	for buttons in presses[-1]:
		count = 0
		for light, wire in enumerate(linwires):
			if lights[light] == sum([(wire[ind] * buttons[ind]) for ind in range(len(wire))]) % 2:
				count += 1
		if count == len(lights):
			return 1
	for ans in itertools.count(1, 1):
		presses.append(set())
		for press in presses[ans - 1]:
			for wire in range(len(wires)):
				new_press = list(press)
				new_press[wire] += 1
				presses[-1].add(tuple(new_press))
		for buttons in presses[-1]:
			count = 0
			for light, wire in enumerate(linwires):
				if lights[light] == sum([(wire[ind] * buttons[ind]) for ind in range(len(wire))]) % 2:
					count += 1
			if count == len(lights):
				return ans + 1


def findpressesjolts(wires, jolts):
	linwires = []
	for x in jolts:
		linwires.append([])
		for y in wires:
			linwires[-1].append(0)
	for x in range(len(wires)):
		for y in range(len(jolts)):
			if y in wires[x]:
				linwires[y][x] = 1
	c = [1] * len(wires)
	b = jolts
	solved = linprog(c, A_eq=linwires, b_eq=b, integrality=c)
	count = math.ceil(sum(solved.x))
	return count


def part2(Data):
	Data = parse(Data)
	ans = 0
	for light, wires, jolt in Data:
		ans += findpressesjolts(wires, jolt)
	return ans


print(part2(data))
