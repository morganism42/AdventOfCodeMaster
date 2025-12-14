from aocd import get_data, submit


def solve1(test=True):
	# Your solution code here
	testdata = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''
	testans = 480
	acost, bcost = 3, 1
	if test:
		data = testdata
	else:
		data = get_data(day=13, year=2024)
	data = data.split("\n\n")
	machines = []
	for machine in data:
		machine = machine.split("\n")
		machine = [line.split(": ")[1].split(", ") for line in machine]
		machine[0] = [int(machine[0][0][2:]), int(machine[0][1][2:])]
		machine[1] = [int(machine[1][0][2:]), int(machine[1][1][2:])]
		machine[2] = [int(machine[2][0][2:]), int(machine[2][1][2:])]
		machines.append(machine)
	'''a*X1 +b*X2 = X
	a*Y1 +b*Y2 = Y
	a = -(YX2-XY2)/(X1Y2-X2Y1)
	b = (YX1-XY1)/(X1Y2-X2Y1)'''
	result = 0
	for machine in machines:
		X1, Y1 = machine[0]
		X2, Y2 = machine[1]
		X, Y = machine[2]
		a = -(Y * X2 - X * Y2) / (X1 * Y2 - X2 * Y1)
		b = (Y * X1 - X * Y1) / (X1 * Y2 - X2 * Y1)
		if a < 0 or b < 0:
			continue
		if a.is_integer() and b.is_integer():
			result += a * acost + b * bcost
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(int(result), part="a", day=13, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''
	testans = 480
	acost, bcost = 3, 1
	if test:
		data = testdata
	else:
		data = get_data(day=13, year=2024)
	data = data.split("\n\n")
	machines = []
	for machine in data:
		machine = machine.split("\n")
		machine = [line.split(": ")[1].split(", ") for line in machine]
		machine[0] = [int(machine[0][0][2:]), int(machine[0][1][2:])]
		machine[1] = [int(machine[1][0][2:]), int(machine[1][1][2:])]
		machine[2] = [int(machine[2][0][2:])+10000000000000, int(machine[2][1][2:])+10000000000000]
		machines.append(machine)
	'''a*X1 +b*X2 = X
	a*Y1 +b*Y2 = Y
	a = -(YX2-XY2)/(X1Y2-X2Y1)
	b = (YX1-XY1)/(X1Y2-X2Y1)'''
	result = 0
	for machine in machines:
		X1, Y1 = machine[0]
		X2, Y2 = machine[1]
		X, Y = machine[2]
		a = -(Y * X2 - X * Y2) / (X1 * Y2 - X2 * Y1)
		b = (Y * X1 - X * Y1) / (X1 * Y2 - X2 * Y1)
		if a < 0 or b < 0:
			continue
		if a.is_integer() and b.is_integer():
			result += a * acost + b * bcost
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(int(result), part="b", day=13, year=2024)
solve2(False)