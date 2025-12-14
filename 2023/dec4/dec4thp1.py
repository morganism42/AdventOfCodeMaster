with open('dec4.txt') as f:
	data = f.read().splitlines()
data = [i[i.find(':') + 2:].replace('  ', ' ').split(' | ') for i in data]  # formats cards

for n, i in enumerate(data):
	data[n] = [i[0].split(' '), i[1].split(' ')]  # splits cards into winning and test numbers

winnings = 0
for i in data:
	a = len(set(i[0]) & set(i[1]))
	if a > 0:
		winnings += 2 ** (a - 1)  # sums the winnings of each card

print(winnings)