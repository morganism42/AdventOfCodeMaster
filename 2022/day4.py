assignments = ''''''
count = 0
for i in assignments:
    if (i[0] <= i[2] <= i[1]) or (i[2] <= i[0] <= i[3]) or (i[0] <= i[3] <= i[1]) or (i[2] <= i[1] <= i[3]):
        count += 1
print(count)
