import math
from copy import deepcopy
from collections import defaultdict

with open('test.txt') as f:
	heat = [[int(i) for i in k] for k in f.read().split('\n')]
# [distance,location,direction,steps in straight line]
unvisited = [(0, (0, 0), (0, 0), 0)]
visited = []
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
distances = {
	(i, j): defaultdict(lambda: float("inf"))
	for j in range(len(heat[0]))
	for i in range(len(heat))
}


def checkgo(movingy, movingx, goingy, goingx, line):
	if (goingy, goingx) == (-movingy, -movingx):
		return None
	elif (goingy, goingx) != (movingy, movingx):
		return 1
	elif (goingy, goingx) == (movingy, movingx):
		return line + 1


def sorting(a):
	return a[0]


rows, cols = len(heat), len(heat[0])
found = False
while unvisited:
	unvisited.sort(key=sorting)
	distance, (y, x), (dy, dx), straight = unvisited.pop(0)
	for goy, gox in directions:
		newstraight = checkgo(dy, dx, goy, gox, straight)
		if not newstraight or newstraight == 4:
			continue
		(ny, nx) = (y + goy, x + gox)
		if 0 <= ny < rows and 0 <= nx < cols:
			ndist = distance + heat[ny][nx]
			if ndist < distances[(ny, nx)][dy, dx, newstraight]:
				distances[(ny, nx)][dy, dx, newstraight] = ndist
				unvisited.append((ndist,(ny,nx),(goy,gox),newstraight))

print(min(distances[(len(heat) - 1, len(heat[0]) - 1)].values()))
