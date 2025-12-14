from aocd import get_data, submit

data = get_data(day=2, year=2024)
test = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def parse(data):
	data = data.split('\n')
	data = [[int(j) for j in i.split(' ')] for i in data]
	return data

data = parse(data)
safe = 0
for report in data:
	if report[0] > report[1]:
		direction = -1
	elif report[0] < report[1]:
		direction = 1
	else:
		continue

	for i in range(len(report) - 1):
		dif = report[i] - report[i + 1]
		if 1 <= abs(dif) <= 3:
			if (dif > 0 and direction == -1) or (dif < 0 and direction == 1):
				if i == len(report) - 2:
					safe += 1
			else:
				break
		else:
			break

#submit(safe, part='a', day=2, year=2024)
def deepcheck(report):
	for i in range(-1, len(report)):
		if i != -1:
			treport = report[:i] + report[i + 1:]
		else:
			treport = report
		#above this I create a temporary report without the i-th element after checking the whole report
		if treport[0] > treport[1]:
			direction = -1
		elif treport[0] < treport[1]:
			direction = 1
		else:
			continue
		for z in range(len(treport) - 1):
			dif = treport[z] - treport[z + 1]
			if 1 <= abs(dif) <= 3:
				if (dif > 0 and direction == -1) or (dif < 0 and direction == 1):
					if z == len(treport) - 2:
						return 1
				# print(report, treport)
				else:
					print(treport[z], treport[z + 1])
					break
			else:
				print(treport[z], treport[z + 1])
				break
	return 0
safe = 0
for report in data:
	safe += deepcheck(report)

#submit(safe, part='b', day=2, year=2024)