data = ''''''
pl = 14  # uniqueness length required
count = pl - 1
for i in range(pl - 1, len(data)):
    count += 1
    if len(set(data[i - (pl - 1):i + 1])) == pl:
        break
print(count)
