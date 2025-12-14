
snacks = ''''''
big1 = 0
big2 = 0
big3 = 0
for i in snacks:
    if sum(i) > big1:
        big3 = big2
        big2 = big1
        big1 = sum(i)
    elif sum(i) > big2:
        big3 = big2
        big2 = sum(i)
    elif sum(i) > big3:
        big3 = sum(i)

print(big1+big2+big3)
