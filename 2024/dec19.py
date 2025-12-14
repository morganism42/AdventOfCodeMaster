from aocd import get_data, submit
import functools



def solve1(test=True):
	def patternfinder(pattern):
		if len(pattern) == 0:
			return True
		for towel in towels:
			if pattern.startswith(towel) and len(towel) <= len(pattern):
				if patternfinder(pattern[len(towel):]):
					return True
		return False

	# Your solution code here
	testdata = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
	testans = 6
	if test:
		data = testdata
	else:
		data = get_data(day=19, year=2024)
	towels, patterns = data.split('\n\n')
	towels = towels.split(', ')
	patterns = patterns.split('\n')
	result = 0
	for pattern in patterns:
		if patternfinder(pattern):
			result += 1
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=19, year=2024)


def solve2(test=True):
	@functools.cache
	def patternfinder(pattern):
		count = 0
		if len(pattern) == 0:
			return 1
		for towel in towels:
			if pattern.startswith(towel) and len(towel) <= len(pattern):
				count += patternfinder(pattern[len(towel):])
		return count

	# Your solution code here
	testdata = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
	testans = 16
	if test:
		data = testdata
	else:
		data = get_data(day=19, year=2024)
	towels, patterns = data.split('\n\n')
	towels = towels.split(', ')
	patterns = patterns.split('\n')
	result = 0
	for pattern in patterns:
		result += patternfinder(pattern)
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=19, year=2024)
solve2(False)