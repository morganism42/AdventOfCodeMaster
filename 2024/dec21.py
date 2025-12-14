from aocd import get_data, submit

def manhattan(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def keypad(code):
	keypad = {
		"1": (0, 1),
		"2": (1, 1),
		"3": (2, 1),
		"4": (0, 2),
		"5": (1, 2),
		"6": (2, 2),
		"7": (0, 3),
		"8": (1, 3),
		"9": (2, 3),
		"0": (1, 0),
		"A": (2, 0),

	}
	position = keypad["A"]
	keydirecs0 = ''
	for c in code:
		dif = (keypad[c][0] - position[0], keypad[c][1] - position[1])
		if dif[0] < 0:
			keydirecs0 += "<" * (-dif[0])
		if dif[1] < 0:
			keydirecs0 += "v" * (-dif[1])
		if dif[1] > 0:
			keydirecs0 += "^" * dif[1]
		if dif[0] > 0:
			keydirecs0 += ">" * dif[0]




		keydirecs0 += "A"
		position = keypad[c]
	return keydirecs0


def direcpad(code):
	direcpad = {
		"<": (0, 0),
		">": (2, 0),
		"^": (1, 1),
		"v": (1, 0),
		"A": (2, 1)
	}
	position = direcpad["A"]
	keydirecs = ''
	for key in code:
		dif = (direcpad[key][0] - position[0], direcpad[key][1] - position[1])

		if dif[0] > 0:
			keydirecs += ">" * dif[0]



		if dif[1] < 0:
			keydirecs += "v" * (-dif[1])

		if dif[0] < 0:
			keydirecs += "<" * (-dif[0])
		if dif[1] > 0:
			keydirecs += "^" * dif[1]

		keydirecs += "A"
		position = direcpad[key]
	return keydirecs


def solve1(test=True):
	# Your solution code here
	testdata = '''029A
980A
179A
456A
379A'''
	testans = 126384
	if test:
		data = testdata
	else:
		data = get_data(day=21, year=2024)
	data = data.split("\n")

	result = 0
	for code in data:

		keydirecs = keypad(code)
		keydirecs1 = direcpad(keydirecs)
		keydirecs2 = direcpad(keydirecs1)
		print(keydirecs, keydirecs1, keydirecs2)
		print(len(keydirecs2), int(code[:-1]))
		result += len(keydirecs2) * int(code[:-1])
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=21, year=2024)


solve1()
