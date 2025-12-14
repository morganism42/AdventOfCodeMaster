moves = ''''''
score = 0
for i in moves:
    if i[0] == 'A':
        if i[1] == 'X':
            score += 3
        elif i[1] == 'Y':
            score += 4
        else:
            score += 8
    elif i[0] == 'B':
        if i[1] == 'X':
            score += 1
        elif i[1] == 'Y':
            score += 5
        else:
            score += 9
    else:
        if i[1] == 'X':
            score += 2
        elif i[1] == 'Y':
            score += 6
        else:
            score += 7
print(score)
