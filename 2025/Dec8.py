from aocd import get_data
from math import sqrt
import time

data = get_data(day=8, year=2025)

test = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''


def parse(Data):
	return tuple(tuple(int(x) for x in box.split(',')) for box in Data.splitlines())


def distance(box1, box2):
	return (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2


def part1(Data, depth=1000):
	Data = parse(Data)
	distances = []
	for x, box1 in enumerate(Data[:-1]):
		for box2 in Data[x + 1:]:
			distances.append((box1, box2, distance(box1, box2)))
	distances.sort(key=lambda a: a[2])
	circuits = [{distances[0][0], distances[0][1]}]
	for x in range(1, depth):
		newcircuits = []
		newcircuit = {distances[x][0], distances[x][1]}
		for y, circ in enumerate(circuits):
			if distances[x][0] in circ:
				newcircuit.update(circ)
			elif distances[x][1] in circ:
				newcircuit.update(circ)
			else:
				newcircuits.append(circ)
		newcircuits.append(newcircuit)
		circuits = newcircuits
	circuits.sort(key=lambda a: -len(a))
	print(circuits)
	return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part2(Data):
	Data = parse(Data)
	distances = []
	for x, box1 in enumerate(Data[:-1]):
		for box2 in Data[x + 1:]:
			distances.append((box1, box2, distance(box1, box2)))
	distances.sort(key=lambda a: a[2])
	x = 0
	circuits = [{distances[0][0], distances[0][1]}]
	while len(circuits[0]) < len(Data):
		x += 1
		newcircuits = []
		newcircuit = {distances[x][0], distances[x][1]}
		for y, circ in enumerate(circuits):
			if distances[x][0] in circ:
				newcircuit.update(circ)
			elif distances[x][1] in circ:
				newcircuit.update(circ)
			else:
				newcircuits.append(circ)
		newcircuits.append(newcircuit)
		circuits = newcircuits
	return distances[x][0][0] * distances[x][1][0]


start = time.time()
print(part2(data))
end = time.time()
print(f'Time taken: {(end - start) * 1000}ms')
