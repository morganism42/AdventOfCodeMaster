input = ''''''
tinput = ''''''
data = input
i = 0
j = 0
x = 2
count = 0
out = [[]]
while True:
    if 0 <= (x - i) <= 2:
        out[-1].append('#')
        i += 1
    else:
        out[-1].append('.')
        i += 1
    if i == 40:
        i = 0
        out.append([])
    if data[j][0] == 'addx':
        if 0 <= (x - i) <= 2:
            out[-1].append('#')
            i += 1
        else:
            out[-1].append('.')
            i += 1
        if i == 40:
            i = 0
            out.append([])
        x += data[j][1]
        j += 1

    else:
        j += 1
    if j == len(data):
        break

    if i == 40:
        i = 0
        out.append([])
for i in out:
    txt = ''
    for j in i:
        txt += j
    print(txt)
print(count)
