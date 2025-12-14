from math import floor


def transpose(matrix):  # transposes a matrix
	tran = []
	for j in range(len(matrix[0])):
		tran.append([matrix[i][j] for i in range(len(matrix))])
	return tran


file = 'dec13.txt'
with open(file) as f:
	data = [[list(j) for j in i.split('\n')] for i in f.read().split('\n\n')]
horz = 0
vert = 0
for n in range(len(data)):
	horizontal = data[n]
	cont = False
	# iterates through all possible mirror positionsforwards
	for i in range(2, len(horizontal), 2):
		temp = horizontal[:i]
		temprev = reversed(temp)
		temprev = list(temprev)
		if temprev == temp: # section is the same flipped its the mirror
			horz += i / 2 * 100
			cont = True
			break
	if cont: continue
	for i in reversed(range(2, len(horizontal), 2)):
		temp = horizontal[-i:]
		temprev = reversed(temp)
		temprev = list(temprev)
		if temprev == temp:
			horz += (len(horizontal) - i / 2) * 100
			if (len(horizontal) - i / 2) * 100 != testlist[n]:
				print(n, i / 2 * 100, testlist[n])
			cont = True
			break
	if cont: continue
	vertical = transpose(data[n])
	for i in range(2, len(vertical), 2):
		temp = vertical[:i]
		temprev = reversed(temp)
		temprev = list(temprev)
		if temprev == temp:
			vert += i / 2
			cont = True
			break
	if cont: continue
	for i in reversed(range(2, len(vertical), 2)):
		temp = vertical[-i:]
		temprev = reversed(temp)
		temprev = list(temprev)
		if temprev == temp:
			vert += len(vertical) - i / 2
			break
total = horz + vert
print(int(total))
