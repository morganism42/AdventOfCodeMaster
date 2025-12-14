from collections import Counter

with open('dec7.txt') as f:
	hands = f.readlines()
	for x, i in enumerate(hands):
		hands[x] = i.split(' ')
		hands[x].append(0)
		hands[x][1] = int(hands[x][1])
cardtypes = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']  # moved J to follow new value


def cus(a):
	return a[-1]


for n, hand in enumerate(hands):
	cards = Counter(list(hand[0]))
	counts = list(cards.values())

	val = [str(12 - cardtypes.index(i)) for i in hand[0]]
	rawval = ''
	for i in val:
		if int(i) < 10:
			rawval += '0' + i
		else:
			rawval += i

	# adds amount of jokers to card in hand the most
	rawval = int(rawval) / (10 ** (len(rawval)))
	if len(counts) > 1 and 'J' in cards.keys():
		counts.pop(counts.index(cards['J']))
		counts.sort()
		counts[-1] += cards['J']

	if 5 in counts:
		hands[n][-1] = 6 + rawval
	elif 4 in counts:
		hands[n][-1] = 5 + rawval
	elif 3 in counts and 2 in counts:
		hands[n][-1] = 4 + rawval
	elif 3 in counts:
		hands[n][-1] = 3 + rawval
	elif counts.count(2) == 2:
		hands[n][-1] = 2 + rawval
	elif 2 in counts:
		hands[n][-1] = 1 + rawval
	else:
		hands[n][-1] = rawval

hands.sort(key=cus)
print(sum([i[1] * (n + 1) for n, i in enumerate(hands)]))
