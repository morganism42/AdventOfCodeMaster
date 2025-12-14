with open('dec9.txt') as f:
	report = [i.split(' ') for i in f.read().split('\n')]
	for i, n in enumerate(report):
		for j, m in enumerate(n):
			report[i][j] = int(report[i][j])


def extrapolate(line):  # builds a pyramid of differences
	out = [line]
	done = False
	while done == False:
		done = True
		new = []
		for i in range(1, len(out[-1])):
			new.append(out[-1][i] - out[-1][i - 1])
			if new[-1] != 0:
				done = False
		out.append(new)
	return out


def interpolate(pyramid):  # finds the new number for each line
	pyramid = extrapolate(pyramid)
	for i in range(len(pyramid) - 1, -1, -1):
		pyramid[i - 1].insert(0, pyramid[i - 1][0] - pyramid[i][0])
	return pyramid[0][0]


print(sum([interpolate(i) for i in report]))  # sums the new numbers for each line
