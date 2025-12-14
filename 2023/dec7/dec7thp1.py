from collections import Counter

with open('dec7.txt') as f:
	hands = f.readlines()
	for x, i in enumerate(hands):
		hands[x] = i.split(' ')
		hands[x].append(0)
		hands[x][1] = int(hands[x][1])

# card types in descending value
cardtypes = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def cus(a):
	return a[-1]


for n, hand in enumerate(hands):
	cards = Counter(list(hand[0]))
	counts = list(cards.values())

	# converts hand into a decimal to sort by later
	val = [str(12 - cardtypes.index(i)) for i in hand[0]]
	rawval = ''
	for i in val:
		if int(i) < 10:
			rawval += '0' + i
		else:
			rawval += i
	rawval = int(rawval) / (10 ** (len(rawval)))

	# finds the most valuable handtype  that can be applied to current hand and assigns a value
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
# sorts and multiplies
hands.sort(key=cus)
print(sum([i[1] * (n + 1) for n, i in enumerate(hands)]))
