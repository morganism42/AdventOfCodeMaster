with open('dec15.txt') as f:
	data = f.read().split(',')
total = 0


def hash(x):  # returns the hash of a string
	temp = 0
	for i in x:
		temp += ord(i)
		temp *= 17
		temp = temp % 256
	return temp


boxes = [[] for i in range(256)]
for i in data:
	# if the instruction is to remove a lens remove it
	if i[-1] == '-':
		box = hash(i[:-1])
		for j in boxes[box]:
			if j[0] == i[:-1]:
				boxes[box].remove(j)
				break
	# if the instruction is to add a lens or change it, add it or change it
	elif i[-2] == '=':
		box = hash(i[:-2])
		for n, j in enumerate(boxes[box]):
			if j[0] == i[:-2]:
				boxes[box][n][1] = i[-1]
		else:
			boxes[box].append([i[:-2], i[-1]])

for x, box in enumerate(boxes):
	for y, lens in enumerate(box):
		total += ((1 + x) * (y + 1) * int(lens[1]))
print(total)
