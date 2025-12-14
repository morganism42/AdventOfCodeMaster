import sys


with open('dec18.txt') as f:
	temp = [i.split(' ') for i in f.read().split('\n')]
instructs = []
directions = 'RDLU'
for i in temp:
	instructs.append([directions[int(i[-1][-2])], int(i[-1][2:-2], 16)])
lake = [[['.', '']]]
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
coords = [(0, 0)]
perim = 0
for n, i in enumerate(instructs):
	coords.append((coords[-1][0] + directions[i[0]][0] * i[1], coords[-1][1] + directions[i[0]][1] * i[1]))
	perim += i[1]
top = 0
# formula for area of an irregular polygon
for i in range(len(coords)):
	top += coords[i][0] * coords[i - 1][1] - coords[i - 1][0] * coords[i][1]
print(int(((abs(top) + perim + 2) / 2)))  # the math witches got me again
# to account for how our area is slightly larger we have to add half the perimeter and 2 and 1 since if it was a square we would lose all the peremter from top right to bottom right to bottom left, which is half +1
