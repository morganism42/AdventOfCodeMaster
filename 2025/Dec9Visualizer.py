from aocd import get_data
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon, Rectangle
from sympy.abc import alpha

data = get_data(day=9, year=2025)
test = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''


def parse(Data):
	return [tuple((int(x.split(',')[0]), int(x.split(',')[1]))) for x in Data.splitlines()]


def matplotgrapher(Largest, Current, Bounds, num=0):
	boundary = Polygon(Bounds, closed=True, color='b')
	large = Rectangle(Largest[0], Largest[1][0] - Largest[0][0], Largest[1][1] - Largest[0][1], color='g')
	curr = Rectangle(Current[0], Current[1][0] - Current[0][0], Current[1][1] - Current[0][1], color='r')
	L = (boundary, large)
	C = (boundary, curr)
	L = PatchCollection(L, alpha=0.4)
	C = PatchCollection(C, alpha=0.4)
	L.set_clim((0, 100))
	colors = np.array([40, 70])
	L.set_array(colors)
	C.set_clim((0, 100))
	colors = np.array([40, 90])
	C.set_array(colors)
	fig, (ax1, ax2) = plt.subplots(2)
	ax1.add_collection(L)
	ax2.add_collection(C)
	maxval = max([max(x) for x in Bounds]) + 2
	ax1.set(xlim=(0, maxval), ylim=(0, maxval))
	ax2.set(xlim=(0, maxval), ylim=(0, maxval))
	plt.savefig(f'pngdump/{num}.png')
	plt.close()


def part1(Data):
	Data = parse(Data)
	rects = []
	largest = [0, 0, 0]
	for x, point1 in enumerate(Data[:-1]):
		for point2 in Data[x + 1:]:
			rect = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
			rects.append((point1, point2, rect))
	for x in tqdm(range(len(rects))):
		rect = rects[x]
		if rect[0][0] == rect[1][0] or rect[0][1] == rect[1][1]:
			continue
		elif rect[2] > largest[2]:
			largest = rect
			matplotgrapher(largest, rect, Data, x)
		elif x % 1000 == 0:
			matplotgrapher(largest, rect, Data, x)


part1(data)
