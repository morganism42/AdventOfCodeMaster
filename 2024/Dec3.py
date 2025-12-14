from aocd import get_data, submit
import re
data = get_data(day=3, year=2024)
test = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''


def regexanswer(data):
	step1 = re.findall(r'''^.+?don't\(\)|do\(\).+?don't\(\)|do\(\).+$''', data, re.DOTALL)
	step2 = []
	for chunk in step1:
		step2 += re.findall(r'''mul\(\d+,\d+\)''', chunk)
	total = 0
	for mul in step2:
		temp = mul[4:-1].split(',')
		total += int(temp[0]) * int(temp[1])
	return total


def solvea(data):
	inputs = 0
	digit1 = ''
	digit2 = ''
	value = 0
	answers = 0
	for n, i in enumerate(data):
		# if any of these aren't involved it can't be a mul command
		if i not in 'mul(),0987654321':
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
		# horible way to check for mul
		elif i == 'm':
			past = 'm'
			digit1 = ''
			digit2 = ''
			inputs = 0
		elif i == 'u' and past == 'm':
			past = 'u'
		elif i == 'l' and past == 'u':
			past = 'l'
		elif i == '(' and past == 'l':
			past = '('
			inputs = 1
		#finds the first until it finds a comma, then it finds the second number
		elif i.isdigit() and inputs == 1:
			digit1 += i
			inputs = 1
		elif i == ',' and inputs == 1:
			inputs = 2
		elif i.isdigit() and inputs == 2:
			digit2 += i
		#once it finds the second number it multiplies them and resets the values
		elif i == ')' and inputs == 2:
			value += int(digit1) * int(digit2)
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
			answers += 1
		else:
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
	print(answers)
	return value


def solveb(data):
	inputs = 0
	digit1 = ''
	digit2 = ''
	value = 0
	answers = 0
	do = True
	for n, i in enumerate(data):
		#only difference between a and b is here
		if not do and i == 'd' and data[n:n + 4] == 'do()':
			do = True
		elif do and i == 'd' and data[n:n + 7] == "don't()":
			do = False
		#end of difference
		elif i not in 'mul(),0987654321' or not do:
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
		elif i == 'm':
			past = 'm'
			digit1 = ''
			digit2 = ''
			inputs = 0
		elif i == 'u' and past == 'm':
			past = 'u'
		elif i == 'l' and past == 'u':
			past = 'l'
		elif i == '(' and past == 'l':
			past = '('
			inputs = 1
		elif i.isdigit() and inputs == 1:
			digit1 += i
			inputs = 1
		elif i == ',' and inputs == 1:
			inputs = 2
		elif i.isdigit() and inputs == 2:
			digit2 += i
		elif i == ')' and inputs == 2:
			value += int(digit1) * int(digit2)
			print(f'{digit1} * {digit2} = {int(digit1) * int(digit2)}')
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
			answers += 1

		else:
			inputs = 0
			digit1 = ''
			digit2 = ''
			past = ''
	print(answers)
	return value
