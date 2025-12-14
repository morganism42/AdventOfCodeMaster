sacks = ''''''
sacktest = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
copies = []
i = 0
while i < len(sacks):
    for j in sacks[i]:
        if j in sacks[i+1] and j in sacks[i+2]:
            copies.append(j)
            print(j)
            break
    i += 3
value = 0
for i in copies:
    if ord(i) > 96:
        value += ord(i) - 96
    else:
        value += ord(i) - 38
print(value)
