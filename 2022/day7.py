commands = ''''''   # input data
commandst = ''''''  # example data
datastruc = {}


def diresize(directory, totalsize, bigdec):
    size = 0
    targetsize = 30000000 - (70000000 - 47442399)
    for j in directory:
        if j[0] == 'dir':
            x, totalsize, bigdec = diresize(datastruc[j[1]], totalsize, bigdec)
            size += x
        else:
            size += int(j[0])
    if size <= 100000:
        totalsize += size
    if bigdec > size > targetsize:
        bigdec = size
    return size, totalsize, bigdec


state = 0
loc = []
for i in commands:
    if i[0] == '$cd':
        state = 0
        if i[1] != '..':
            loc.append(i[1])
            datastruc[str(loc)] = []
        elif i[1] == '..':
            del loc[-1]
    elif i[0] == '$ls':
        state = 1
    elif state == 1:
        if i[0] == 'dir':
            temp = loc.copy()
            temp.append(i[1])
            datastruc[str(loc)].append([i[0], str(temp)])
        else:
            datastruc[str(loc)].append(i)

print(datastruc)
print(diresize(datastruc["['/']"], 0, 999999999999999999999999999999999999999999999))
