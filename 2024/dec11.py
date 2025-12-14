from turtledemo.penrose import start

from aocd import get_data, submit
from collections import defaultdict
from tqdm import tqdm
import time


def solve1(test=True, q=25):
	# Your solution code here
	testdata = '''125 17'''
	testans = 55312
	if test:
		data = testdata
	else:
		data = get_data(day=11, year=2024)
	data = [int(stone) for stone in data.split(' ')]
	stones = data
	for i in tqdm(range(q)):
		newstones = []
		for stone in stones:
			if stone == 0:
				newstones.append(1)
			elif len(str(stone)) % 2 == 0:
				half = len(str(stone)) // 2
				newstones += [int(str(stone)[:half]), int(str(stone)[half:])]
			else:
				newstones.append(stone * 2024)
		stones = newstones
	result = len(stones)

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=11, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''125 17'''
	testans = 55312
	if test:
		data = testdata
	else:
		data = get_data(day=11, year=2024)
	data = {stone: 1 for stone in data.split(' ')}
	stones = data
	for i in tqdm(range(75)):
		newstones = defaultdict(int)
		for stone in stones.keys():
			if int(stone) == 0:
				newstones['1'] += stones[stone]
			elif len(stone) % 2 == 0:
				half = len(stone) // 2
				newstones[str(int(stone[:half]))] += stones[stone]
				newstones[str(int(stone[half:]))] += stones[stone]
			else:
				newstones[str(int(stone) * 2024)] += stones[stone]
		stones = newstones
	result = sum([stones[stone] for stone in stones])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=11, year=2024)


start = time.time()
solve1(test=False, q=75)
with open('brute_force.txt', 'w') as f:
	f.write(f'{time.time() - start} seconds to completion')
print("Brute force time:", time.time() - start)
