from aocd import get_data, submit
from copy import deepcopy
from collections import defaultdict

data = get_data(day=23).split('\n')
test = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''.split('\n')
start = (0, 1)

unvisted = [(0, start, 0)]


def genmap(data, start):
	end = (len(data) - 1, len(data[0]) - 2)
	pathmap = {(0, 1): {}}
	arrows = {(1, 0): '^<>', (-1, 0): 'v<>', (0, 1): '<v^', (0, -1): '>v^'}
	directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
	intersections = [[start, [(1, 0)]]]
	mapped = []
	while intersections:
		enter = intersections.pop(0)
		mapped.append(enter[0])
		if enter[0] == end:
			break
		for way in enter[1]:
			path = [enter[0]]
			ny = enter[0][0] + way[0]
			nx = enter[0][1] + way[1]
			legal = True
			pathing = True
			while legal:
				path.append((ny, nx))
				count = 0
				poss = []
				if (ny, nx) == end:
					poss = [(ny, nx)]
					count = 2
				else:
					for d in directions:
						if data[ny + d[0]][nx + d[1]] == '#' or (ny + d[0], nx + d[1]) in path:
							continue
						if data[ny][nx] in arrows[d]:
							pathing = False
						poss.append((ny + d[0], nx + d[1]))
						count += 1

				if count == 0:
					break
				else:
					ny = poss[0][0]
					nx = poss[0][1]
				if count > 1 or (ny, nx) == end:
					if pathing:
						pathmap[enter[0]][path[-1]] = len(path) - 1
					if path[-1] == end:
						break
					if path[-1] not in mapped and path[-1] not in [i[0] for i in intersections]:
						intersections.append([path[-1], []])
						pathmap[path[-1]] = {}
						for d in directions:
							if data[path[-1][0] + d[0]][path[-1][1] + d[1]] != '#':
								intersections[-1][1].append(d)
					break
	return pathmap, end
def genmap2(data, start):
	end = (len(data) - 1, len(data[0]) - 2)
	pathmap = {(0, 1): {}}
	directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
	intersections = [[start, [(1, 0)]]]
	mapped = []
	while intersections:
		enter = intersections.pop(0)
		mapped.append(enter[0])
		if enter[0] == end:
			break
		for way in enter[1]:
			path = [enter[0]]
			ny = enter[0][0] + way[0]
			nx = enter[0][1] + way[1]
			legal = True
			pathing = True
			while legal:
				path.append((ny, nx))
				count = 0
				poss = []
				if (ny, nx) == end:
					poss = [(ny, nx)]
					count = 2
				else:
					for d in directions:
						if data[ny + d[0]][nx + d[1]] == '#' or (ny + d[0], nx + d[1]) in path:
							continue
						poss.append((ny + d[0], nx + d[1]))
						count += 1

				if count == 0:
					break
				else:
					ny = poss[0][0]
					nx = poss[0][1]
				if count > 1 or (ny, nx) == end:
					if pathing:
						pathmap[enter[0]][path[-1]] = len(path) - 1
					if path[-1] == end:
						break
					if path[-1] not in mapped and path[-1] not in [i[0] for i in intersections]:
						intersections.append([path[-1], []])
						pathmap[path[-1]] = {}
						for d in directions:
							if data[path[-1][0] + d[0]][path[-1][1] + d[1]] != '#':
								intersections[-1][1].append(d)
					break
	return pathmap, end

def search(node, distance, end, pathmap, path):
	global maxdistance
	if node == end:
		if distance > maxdistance:
			maxdistance = distance
			print(maxdistance)
		return distance
	temp = [0]
	for i in list(pathmap[node].keys()):
		if i not in path:
			temp.append(search(i, distance + pathmap[node][i], end, pathmap, path.copy() + [i]))
	return max(temp)

maxdistance = 0
pathmap, end = genmap(test, start)
distance = search(start, 0, end, pathmap, [start])
print(distance)
maxdistance = 0
pathmap, end = genmap2(data, start)
distance = search(start, 0, end, pathmap, [start])
print(distance)