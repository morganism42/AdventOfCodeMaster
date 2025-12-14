stacks = ''''''
commands = ''''''
for i in commands:
    for j in reversed(range(i[0])):
        stacks[i[2] - 1].append(stacks[i[1] - 1][-j - 1])
    del stacks[i[1] - 1][-i[0]:]
output = ''
for i in stacks:
    try:
        output += i[-1]
    except:
        print('oop')
print(output)
