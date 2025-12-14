from itertools import combinations

with open('dec11.txt') as f:
	data = [list(i) for i in f.read().split('\n')]

# find the empty rows
emprows = []
for row in range(len(data)):
	if '#' not in data[row]:
		emprows.append(row)

# find the empty columns
empcol = []
for i in range(len(data[0])):
	if not any([j[i] == '#' for j in data]):
		empcol.append(i)

# find the galaxies
galaxies = []
for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == '#':
			galaxies.append([i, j])

pairs = list(combinations(galaxies, 2))  # generate a list of galaxy pairs
expansion = 1000000  # the expansion of the universe

# if the space between 2 galaxies is empty, add the expansion-1 to the total
total = 0
for i in pairs:
	total += (abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1]))
	for j in emprows:
		if i[0][0] < j < i[1][0] or i[0][0] > j > i[1][0]:
			total += expansion - 1
	for j in empcol:
		if i[0][1] < j < i[1][1] or i[0][1] > j > i[1][1]:
			total += expansion - 1
print(total)
