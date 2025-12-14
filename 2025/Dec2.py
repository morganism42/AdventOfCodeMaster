from aocd import get_data, submit
import time

data = get_data(day=2, year=2025)
test = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''


def parse(Data):
	return [[int(n.split('-')[0]), int(n.split('-')[1])] for n in Data.split(',')]


def part1(Data):
	Data = parse(Data)
	invalids = 0
	for region in Data:
		for n in range(region[0], region[1] + 1):
			text = str(n)
			size = len(text)
			if size % 2 == 0:
				size //= 2
				if text[:size] == text[size:]:
					invalids += n
	print(invalids)


def part2(Data):
	Data = parse(Data)
	invalids = 0
	factors = {}
	for region in Data:
		for n in range(region[0], region[1] + 1):
			size = len(str(n))
			if size not in factors.keys():
				sizes = []
				for i in range(1, size):
					if size % i == 0:
						sizes.append(i)
				factors[size] = sizes
			else:
				sizes = factors[size]
			text = str(n)
			for x in sizes:
				indx = x
				hold = text[:x]
				while indx + x <= size:
					if text[indx:indx + x] != hold:
						break
					indx += x
				else:
					invalids += n
					break
	return invalids


start = time.time()
print(part2(data))
end = time.time()
print(f'Time taken: {end - start}s')
