from aocd import get_data
from math import prod
import time

data = get_data(day=6, year=2025)

# testans 1: 4277556 2: 3263827
test = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''


def parser(Data):
	Data = Data.split('\n')
	index = 0
	problems = []
	# split into problems by empty columns
	for x in range(len(Data[0])):
		if set([Data[y][x] for y in range(len(Data))]) == {' '}:
			problems.append([Data[y][index:x] for y in range(len(Data))])
			index = x + 1
	else:
		# needed as it there is no empty column at the end of the file
		problems.append([Data[y][index:] for y in range(len(Data))])
	return problems


def part1(Data):
	ans = 0
	problems = parser(Data)
	for problem in problems:
		numbs, op = [int(x) for x in problem[:-1]], problem[-1]
		if '+' in op:
			ans += sum(numbs)
		else:
			ans += prod(numbs)
	return ans


def part2(Data):
	ans = 0
	problems = parser(Data)

	for problem in problems:
		# make list with empty spaces for numbers
		digits = len(problem[0])
		numbers = [''] * digits
		# since the first number will be the first digits etc. can take advantage of string adding
		for num in problem[:-1]:
			for n in range(digits):
				numbers[n] += num[n]
		numbers = [int(x) for x in numbers]
		if '+' in problem[-1]:
			ans += sum(numbers)
		else:
			ans += prod(numbers)

	return ans

start = time.time()
print(part2(data))
end = time.time()
print(f'Time taken: {(end - start)*1000}ms')