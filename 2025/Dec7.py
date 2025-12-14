from aocd import get_data
from collections import defaultdict
import time
from tqdm import tqdm
from functools import cache

data = get_data(day=7, year=2025)

test = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''


def part1(Data):
	Data = [list(row) for row in Data.splitlines()]
	lasers = [{Data[0].index('S')}]
	ans = 0
	for row in Data:
		lasers.append(set())
		for beam in lasers[-2]:
			if row[beam] == '^':
				ans += 1
				lasers[-1].add(beam + 1)
				lasers[-1].add(beam - 1)
			else:
				lasers[-1].add(beam)
	return ans


def part2(Data):
	Data = [list(row) for row in Data.splitlines()]
	lasers = {Data[0].index('S'): 1}
	for row in Data[1:]:
		newlasers = defaultdict(int)
		for beam, amount in lasers.items():
			if row[beam] == '^':
				newlasers[beam + 1] += amount
				newlasers[beam - 1] += amount
			else:
				newlasers[beam] += amount
		lasers = newlasers
	return sum([i for i in lasers.values()])


def visualize(Data):
	Data = [list(row) for row in Data.splitlines()]
	lasers = [{Data[0].index('S'): 1}]
	visual = [Data[0].copy()]
	print(''.join(visual[-1]))
	for row in Data[1:]:
		lasers.append(defaultdict(int))
		visual.append(row.copy())
		for beam, amount in lasers[-2].items():
			if row[beam] == '^':
				lasers[-1][beam + 1] += amount
				lasers[-1][beam - 1] += amount
			else:
				lasers[-1][beam] += amount
		for beam in lasers[-1].keys():
			visual[-1][beam] = '|'
		print(''.join(visual[-1]))
	return sum([i for i in lasers[-1].values()])


def DFS(Data):
	Data = [list(row) for row in Data.splitlines()]

	@cache
	def recursive_DFS(x=Data[0].index('S'), y=0):
		ans = 0
		for row in range(y + 1, len(Data)):
			if Data[row][x] == '^':
				ans += recursive_DFS(x + 1, row) + recursive_DFS(x - 1, row)
				return ans
		else:
			return 1

	return recursive_DFS(Data[0].index('S'), 0)


start = time.time()

print(DFS(data))
end = time.time()
print(f'Time taken: {(end - start) * 1000}ms')
