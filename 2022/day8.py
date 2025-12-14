forest = ''''''
tforest = '''30373
25512
65332
33549
35390'''
best = 0
data = [[]]
visible = []
sight = []
for i in forest:
    if i == '\n':
        data.append([])
    else:
        data[-1].append(int(i))
for i in range(len(data)):
    visible.append([])
    for j in range(len(data[0])):
        visible[-1].append(0)

for i in range(len(data)):
    check = -1
    for j in range(len(data[i])):
        if data[i][j] > check:
            visible[i][j] = 1
            check = data[i][j]
    check = -1
    for j in reversed(range(len(data[i]))):
        if data[i][j] > check:
            visible[i][j] = 1
            check = data[i][j]
for i in range(len(data)):
    check = -1
    for j in range(len(data[i])):
        if data[j][i] > check:
            visible[j][i] = 1
            check = data[j][i]
    check = -1
    for j in reversed(range(len(data[i]))):
        if data[j][i] > check:
            visible[j][i] = 1
            check = data[j][i]
print(sum([sum(i) for i in visible]))

for i in range(len(data)):
    sight.append([])
    for j in range(len(data[0])):
        sight[-1].append(1)

for x in range(len(data)):
    for y in range(len(data)):
        see = 0
        if x > 0:
            for i in range(1, x + 1):
                if data[x][y] > data[x - i][y]:
                    see += 1
                elif data[x][y] <= data[x - i][y]:
                    see += 1
                    break
        sight[x][y] *= see
        see = 0
        if x < len(data) - 1:
            for i in range(1, len(data) - x):
                if data[x][y] > data[x + i][y]:
                    see += 1
                elif data[x][y] <= data[x + i][y]:
                    see += 1
                    break
        sight[x][y] *= see
        see = 0
        if y > 0:
            for i in range(1, y + 1):
                if data[x][y] > data[x][y-i]:
                    see += 1
                elif data[x][y] <= data[x][y-i]:
                    see += 1
                    break
        sight[x][y] *= see
        see = 0
        if y < len(data) - 1:
            for i in range(1, len(data) - y):
                if data[x][y] > data[x][y+i]:
                    see += 1
                elif data[x][y] <= data[x][y+i]:
                    see += 1
                    break
        sight[x][y] *= see
        if sight[x][y] > best:
            best = sight[x][y]
print(best)
