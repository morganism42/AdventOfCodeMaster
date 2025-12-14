from aocd import get_data, submit
from itertools import permutations, combinations_with_replacement, product, repeat


def solve1(test=True):
    # Your solution code here
	testdata = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
	testans = 3749
	if test:
		data = testdata
	else:
		data = get_data(day=7, year=2024)
	data = data.splitlines()
	data = [[int(row[0]), [int(x) for x in row[1].split(' ')]] for row in [row.split(": ") for row in data]]
	operators = ['+','*']
	result = 0
	for row in data:
		ops = len(row[1])-1

		for perm in product(operators,repeat=ops):
			value = row[1][0]
			for i in range(ops):
				if perm[i] == '+':
					value += row[1][i+1]
				else:
					value *= row[1][i+1]
			if value == row[0]:
				result += row[0]
				break
    
    
    
    
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=7, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
	testans = 11387
	if test:
		data = testdata
	else:
		data = get_data(day=7, year=2024)
	data = data.splitlines()
	data = [[int(row[0]), [int(x) for x in row[1].split(' ')]] for row in [row.split(": ") for row in data]]
	operators = ['+', '*','||']
	result = 0

	for row in data:
		ops = len(row[1]) - 1

		for perm in product(operators, repeat=ops):
			value = row[1][0]
			for i in range(ops):
				if perm[i] == '+':
					value += row[1][i + 1]
				elif perm[i] == '*':
					value *= row[1][i + 1]
				else:
					value = int(str(value) + str(row[1][i + 1]))
			if value == row[0]:
				result += row[0]
				break

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=7, year=2024)