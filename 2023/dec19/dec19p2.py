from copy import deepcopy
from aocd import get_data, submit

data = get_data(day=19)
lines = data.split('\n\n')
flows = {}
for i in lines[0].split('\n'):
	flows[i[:i.index('{')]] = i[i.index('{') + 1:-1].split(',')
parts = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
total = 0


def test(part, flow):
	global total
	if flow == 'A':
		temp = 1
		for k in part.keys(): temp *= part[k][1] - part[k][0] + 1
		total += temp
		return
	elif flow == 'R':
		return
	for check in flows[flow][:-1]:
		if check[1] == '>':
			if part[check[0]][1] > int(check[2:check.index(':')]):
				newpart = deepcopy(part)
				newpart[check[0]][0] = int(check[2:check.index(':')]) + 1
				part[check[0]][1] = int(check[2:check.index(':')])
				test(newpart, check[check.index(':') + 1:])
		elif check[1] == '<':
			if part[check[0]][0] < int(check[2:check.index(':')]):
				newpart = deepcopy(part)
				newpart[check[0]][1] = int(check[2:check.index(':')]) - 1
				part[check[0]][0] = int(check[2:check.index(':')])
				test(newpart, check[check.index(':') + 1:])
	test(part, flows[flow][-1])


test(parts, 'in')
print(total)
submit(total, day=19, year=2023, part='b')

