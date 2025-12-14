from itertools import combinations
with open('dec11.txt') as f:
	data = [list(i) for i in f.read().split('\n')]
rowmap = []
for row in data:
	if '#' not in row:
		rowmap.append(['.'] * len(row))
	rowmap.append(row)
empcol = []
for i in range(len(rowmap[0])):
	column = [rowmap[j][i] for j in range(len(rowmap))]
	if '#' not in column:
		empcol.append(i)
colmap = []
for j in rowmap:
	colmap.append([])
	for i in range(len(j)):
		if i in empcol:
			colmap[-1].append('.')
		colmap[-1].append(j[i])
galaxies = []
for i in range(len(colmap)):
	for j in range(len(colmap[i])):
		if colmap[i][j] == '#':
			galaxies.append([i, j])

pairs = list(combinations(galaxies, 2))
lengths = 0
for i in pairs:
	lengths += abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
print(lengths)