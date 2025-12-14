with open('dec19.txt') as file:
	lines = file.read().split('\n\n')
flows = {}
for i in lines[0].split('\n'):
	flows[i[:i.index('{')]] = i[i.index('{') + 1:-1].split(',')
parts = []

for i in lines[1].split('\n'):
	temp = i[1:-1].split(',')
	parts.append({})
	for j in temp:
		parts[-1][j[0]] = int(j[2:])
A, R = [], []
for part in parts:
	work = 'in'
	while True:
		for check in flows[work][:-1]:
			if check[1] == '>':
				if part[check[0]] > int(check[2:check.index(':')]):
					work = check[check.index(':') + 1:]
					break
			elif check[1] == '<':
				if part[check[0]] < int(check[2:check.index(':')]):
					work = check[check.index(':') + 1:]
					break
		else:
			work = flows[work][-1]
		if work == 'A':
			A.append(part)
			break
		elif work == 'R':
			R.append(part)
			break
total = 0
for i in A:
	total += sum(i.values())
print(total)
