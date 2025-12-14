tinstructs = ''''''
instructs = ''''''
area = []
size = 701
rope = []
for i in range(10):
    rope.append([int(size / 2), int(size / 2)])
follow = 1
for i in range(size):
    area.append([])
    for j in range(size):
        area[-1].append(' ')
area[int(size / 2)][int(size / 2)] = '#'


def follo(H, T):
    if abs(H[0] - T[0]) > follow and H[1] - T[1] == 0:
        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -= 1
    elif H[0] - T[0] == 0 and abs(H[1] - T[1]) > follow:
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1
    elif abs(H[0] - T[0]) > follow and abs(H[1] - T[1]) > 0:
        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -= 1
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1
    elif abs(H[0] - T[0]) > 0 and abs(H[1] - T[1]) > follow:
        if H[1] > T[1]:
            T[1] += 1
        else:
            T[1] -= 1
        if H[0] > T[0]:
            T[0] += 1
        else:
            T[0] -= 1
    return H, T


def move(go, rope, area):
    for k in range(go[1]):
        if go[0] == 'R':
            rope[0][0] += 1
        elif go[0] == 'U':
            rope[0][1] += 1
        elif go[0] == 'L':
            rope[0][0] -= 1
        elif go[0] == 'D':
            rope[0][1] -= 1
        for j in range(len(rope) - 1):
            rope[j], rope[j + 1] = follo(rope[j], rope[j + 1])
        area[rope[-1][0]][rope[-1][1]] = '#'
    return rope, area


for i in instructs:
    rope, area = move(i, rope, area)

count = 0
for i in area:
    for j in i:
        if j == '#':
            count += 1

print(count)
