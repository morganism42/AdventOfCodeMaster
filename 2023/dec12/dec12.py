from functools import cache
from time import perf_counter

start = perf_counter()
file = 'dec12.txt'
with open(file) as f:
	lines = [i.split(' ') for i in f.read().split('\n')]
for i in range(len(lines)):
	while '..' in lines[i][0]:
		lines[i][0] = lines[i][0].replace('..', '.')
	lines[i][1] = [int(j) for j in lines[i][1].split(',')]
for i in range(len(lines)):
	new = '?' + lines[i][0]
	ne2 = lines[i][1].copy()
	for j in range(4):
		lines[i][0] += new
		for z in ne2:
			lines[i][1].append(z)


@cache  # remembers all inputs and their outputs
# recursive function that finds all possible places to put the current spring and then passes the next spring for each of those spaces
def findplace(line, numbers,count=0):
	if len(numbers) == 1:  # if last number in list
		if len(line) < sum(numbers) + len(numbers) - 1:
			return count
		for i in range(len(line)):
			if len(line[i:]) < sum(numbers) + len(
					numbers) - 1:  # if there is not enough space left to fit the rest of the numbers regardless of placement
				return count
			disp = line[i:]
			if line[i] == '.':
				continue
			elif line[i] == '#':
				tp = line[i + numbers[0]:]
				tp2 = line[i:i + numbers[0]]
				if '#' not in line[i + numbers[0]:] and '.' not in line[i:i + numbers[0]]:
					count += 1
				break
			else:
				if '#' not in line[i + numbers[0]:] and '.' not in line[i:i + numbers[0]]:
					count += 1
	else:
		for i in range(len(line)):
			if len(line[i:]) < sum(numbers) + len(
					numbers) - 1:  # if there is not enough space left to fit the rest of the numbers regardless of placement
				return count
			if line[i] == '.':
				continue
			elif line[i] == '#':
				# basically if you can't be placed farther than here
				if line[i + numbers[0]] != '#' and '.' not in line[i:i + numbers[0]]:
					count += findplace(line[i + numbers[0] + 1:], numbers[1:])
				return count
			else:
				if line[i + numbers[0]] != '#' and '.' not in line[i:i + numbers[0]]:
					count += findplace(line[i + numbers[0] + 1:], numbers[1:])
	return count


total = 0
bong = 0
for entry in lines:
	bong += 1
	bing = findplace(tuple(entry[0]), tuple(entry[1]))
	total += bing
print(total, perf_counter() - start)
