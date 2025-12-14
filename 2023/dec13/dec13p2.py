def transpose(matrix):
	tran = []
	for j in range(len(matrix[0])):
		tran.append([matrix[i][j] for i in range(len(matrix))])
	return tran


def differences(a, b):  # counts the differences between two matrices
	diff = 0
	diffs = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j] != b[i][j]:
				diffs.append([i, j])
				diff += 1

	if diff == 2: # looking for two differences as I pass the whole mirrored section twice, not both sides
		return True
	else:
		return False


file = 'dec13.txt'
with open(file) as f:
	data = [[list(j) for j in i.split('\n')] for i in f.read().split('\n\n')]
horz = 0
vert = 0
mirrors = [[0, -2], [0, 6], [2, 0], [0, 10], [4, 0], [0, -4], [4, 0], [-2, 0], [0, -2], [0, 6], [0, 6], [0, 2], [2, 0],
           [12, 0], [0, -6], [-2, 0], [0, -2], [6, 0], [0, -10], [6, 0], [-4, 0], [2, 0], [0, 12], [12, 0], [0, 4],
           [0, -8], [0, -4], [2, 0], [-2, 0], [16, 0], [2, 0], [16, 0], [0, -10], [2, 0], [0, 6], [0, 2], [0, 6],
           [-2, 0], [-2, 0], [0, -8], [-2, 0], [0, 8], [4, 0], [0, 2], [0, 2], [0, -8], [8, 0], [0, -4], [4, 0], [0, 2],
           [-2, 0], [0, 2], [-4, 0], [-2, 0], [0, 4], [-4, 0], [-6, 0], [-8, 0], [12, 0], [0, -8], [4, 0], [0, -4],
           [2, 0], [-4, 0], [-4, 0], [0, 2], [-12, 0], [2, 0], [0, -14], [0, -6], [0, -6], [0, -8], [-4, 0], [0, -16],
           [4, 0], [0, 8], [0, 6], [6, 0], [6, 0], [-4, 0], [0, -2], [2, 0], [0, -4], [2, 0], [6, 0], [0, 6], [2, 0],
           [-10, 0], [6, 0], [2, 0], [-4, 0], [4, 0], [0, -4], [-4, 0], [0, -4], [0, 6], [-14, 0], [0, 4], [0, -4],
           [-2, 0]]
for n in range(len(data)):
	horizontal = data[n]
	cont = False
	for i in range(2, len(horizontal), 2):
		temp = horizontal[:i]
		temprev = reversed(temp)
		temprev = list(temprev)
		if differences(temp, temprev):
			horz += i / 2 * 100
			cont = True
			break
	if cont: continue
	for i in reversed(range(2, len(horizontal), 2)):
		temp = horizontal[-i:]
		temprev = reversed(temp)
		temprev = list(temprev)
		if differences(temp, temprev):
			horz += (len(horizontal) - i / 2) * 100
			cont = True
			break
	if cont: continue
	vertical = transpose(data[n])
	for i in range(2, len(vertical), 2):
		temp = vertical[:i]
		temprev = reversed(temp)
		temprev = list(temprev)
		if differences(temp, temprev):
			vert += i / 2
			cont = True
			break
	if cont: continue
	for i in reversed(range(2, len(vertical), 2)):
		temp = vertical[-i:]
		temprev = reversed(temp)
		temprev = list(temprev)
		if differences(temp, temprev):
			vert += len(vertical) - i / 2
			break
total = horz + vert
print(int(total))
