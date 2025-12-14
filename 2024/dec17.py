from atexit import register

from aocd import get_data, submit

result = []
pointer = 0


def solve1(test=True):
	# Your solution code here
	global result
	global pointer
	testdata = '''Register A: 729
Register B: 0
Register C: 9

Program: 2,6'''
	testans = '4,6,3,5,6,3,5,2,1,0'
	if test:
		data = testdata
	else:
		data = get_data(day=17, year=2024)
	data = data.split('\n\n')
	registers = data[0]
	registers = registers.split('\n')
	combo = {'0': 0, '1': 1, '2': 2, '3': 3,
	         '4': int(registers[0].split(': ')[1]),
	         '5': int(registers[1].split(': ')[1]),
	         '6': int(registers[2].split(': ')[1])}
	program = data[1].split(' ')[1].split(',')
	while pointer < len(program) - 1:
		instruction = program[pointer]
		operand = program[pointer + 1]
		match instruction:
			case '0':
				adv(combo, operand)
			case '1':
				bxl(combo, operand)
			case '2':
				bst(combo, operand)
			case '3':
				jnz(combo, operand)
			case '4':
				bxc(combo, operand)
			case '5':
				out(combo, operand)
			case '6':
				bdv(combo, operand)
			case '7':
				cdv(combo, operand)
		pointer += 2
	result = ','.join(result)
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:

		print('|' + result + '|')
		submit(result, part="a", day=17, year=2024)


def adv(combo, operand):
	numerator = combo['4']
	if operand in '0123':
		denominator = 2 ** int(operand)
	else:
		denominator = 2 ** combo[operand]
	combo['4'] = numerator // denominator
	return


def bxl(combo, operand):
	combo['5'] = combo['5'] ^ int(operand)
	return


def bst(combo, operand):
	combo['5'] = combo[operand] & 7
	return


def jnz(combo, operand):
	global pointer
	if combo['4'] == 0:
		return False
	else:
		# make sure to set pointer to this value
		pointer = int(operand) - 2


def bxc(combo, operand):
	combo['5'] = combo['5'] ^ combo['6']
	return


def out(combo, operand):
	global result
	result.append(str(combo[operand] & 7))
	return


def bdv(combo, operand):
	numerator = combo['4']
	if operand in '0123':
		denominator = 2 ** int(operand)
	else:
		denominator = 2 ** combo[operand]
	combo['5'] = numerator // denominator
	return


def cdv(combo, operand):
	numerator = combo['4']
	if operand in '0123':
		denominator = 2 ** int(operand)
	else:
		denominator = 2 ** combo[operand]
	combo['6'] = numerator // denominator
	return


def solve2(test=True):
	# Your solution code here
	global result
	global pointer
	testdata = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''
	testans = 117440
	if test:
		data = testdata
	else:
		data = get_data(day=17, year=2024)
	data = data.split('\n\n')
	registers = data[0]
	registers = registers.split('\n')
	combo = {'0': 0, '1': 1, '2': 2, '3': 3,
	         '4': int(registers[0].split(': ')[1]),
	         '5': int(registers[1].split(': ')[1]),
	         '6': int(registers[2].split(': ')[1])}
	program = data[1].split(' ')[1].split(',')
	input = int('1' + ''.join(['0' for i in range(len(program) - 1)]), 8)

	while result != program:
		combo['4'] = input
		pointer = 0
		result = []
		while pointer < len(program) - 1:
			instruction = program[pointer]
			operand = program[pointer + 1]
			match instruction:
				case '0':
					adv(combo, operand)
				case '1':
					bxl(combo, operand)
				case '2':
					bst(combo, operand)
				case '3':
					jnz(combo, operand)
				case '4':
					bxc(combo, operand)
				case '5':
					out(combo, operand)
				case '6':
					bdv(combo, operand)
				case '7':
					cdv(combo, operand)
			pointer += 2
		for i in range(len(result) - 1, -1, -1):
			if result[i] != program[i]:
				input += 8 ** i
				break
	result = input
	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print("Test failed")
	elif not test:

		submit(result, part="b", day=17, year=2024)


solve2(False)
