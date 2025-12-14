file = open('../sample.txt', 'r')
data = file.read()
file.close()
temp = data.split('\n')
engine = []
for i in temp:
    engine.append(list(i))


def left(x, y, n):
    if engine[x][y - 1] in nsymbs[:-1]:
        n = engine[x][y - 1] + n
        n = left(x, y - 1, n)
    return n


def right(x, y, n):
    if y + 1 == len(engine[x]):
        return n
    if engine[x][y + 1] in nsymbs[:-1]:
        n = n + engine[x][y + 1]
        n = right(x, y + 1, n)
    return n


def findnum(x, y):
    if engine[x][y] == '.':
        return '0'
    n = left(x, y, engine[x][y])
    n = right(x, y, n)
    return n


nsymbs = '1234567890.'
numbs = []
for x, row in enumerate(engine):
    for y, i in enumerate(row):

        if i not in nsymbs:
            numbs.append([])
            n = findnum(x, y + 1)
            if n != '0':
                numbs[-1].append(n)
            n = findnum(x, y - 1)
            if n != '0':
                numbs[-1].append(n)
            n = findnum(x + 1, y)
            if n == '0':
                n = findnum(x + 1, y + 1)
                if n != '0':
                    numbs[-1].append(n)
                n = findnum(x + 1, y - 1)
                if n != '0':
                    numbs[-1].append(n)
            else:
                numbs[-1].append(n)

            n = findnum(x - 1, y)
            if n == '0':
                n = findnum(x - 1, y + 1)
                if n != '0':
                    numbs[-1].append(n)
                n = findnum(x - 1, y - 1)
                if n != '0':
                    numbs[-1].append(n)
            else:
                numbs[-1].append(n)
            if len(numbs[-1]) == 0:
                numbs.pop(-1)
numbs = [[int(j) for j in i] for i in numbs]
print(f'part 1:{sum([sum(i) for i in numbs])}')
ratios = 0

# part 2
numbs = []
for x, row in enumerate(engine):
    for y, i in enumerate(row):

        if i == '*':   #<- change from part 1
            numbs.append([])
            n = findnum(x, y + 1)
            if n != '0':
                numbs[-1].append(n)
            n = findnum(x, y - 1)
            if n != '0':
                numbs[-1].append(n)
            n = findnum(x + 1, y)
            if n == '0':
                n = findnum(x + 1, y + 1)
                if n != '0':
                    numbs[-1].append(n)
                n = findnum(x + 1, y - 1)
                if n != '0':
                    numbs[-1].append(n)
            else:
                numbs[-1].append(n)

            n = findnum(x - 1, y)
            if n == '0':
                n = findnum(x - 1, y + 1)
                if n != '0':
                    numbs[-1].append(n)
                n = findnum(x - 1, y - 1)
                if n != '0':
                    numbs[-1].append(n)
            else:
                numbs[-1].append(n)
            if len(numbs[-1]) == 0:
                numbs.pop(-1)
numbs = [[int(j) for j in i] for i in numbs]

#find the *s with 2 and multiply than add
for i in numbs:
    if len(i) == 2:
        ratios += i[0] * i[1]
print(f'part 2:{ratios}')
