from aocd import get_data
import hashlib

data = get_data(year=2015, day=4)


def part1(data):
	num = 0
	while True:
		input = data + str(num)
		result = hashlib.md5(input.encode())
		if result.hexdigest()[:5] == '00000':
			return num
		num += 1

def part2(data):
	num = 0
	while True:
		input = data + str(num)
		result = hashlib.md5(input.encode())
		if result.hexdigest()[:6] == '000000':
			return num
		num += 1
print(part1(data))
print(part2(data))