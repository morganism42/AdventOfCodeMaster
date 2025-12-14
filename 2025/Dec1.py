from aocd import get_data, submit
import time

Data = get_data(day=1, year=2025)
test = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''


def parse(parsee):
	parsee = parsee.split('\n')
	return parsee


data = parse(Data)


def P1(code):
	pointer = 50
	ans = 0
	for rot in code:
		turn = [rot[0], int(rot[1:])]

		if turn[0] == 'L':
			pointer -= int(turn[1])
		else:
			pointer += int(turn[1])
		pointer %= 100
		if pointer == 0:
			ans += 1
	print(ans)


def P2(code):
	pointer = 50
	ans = 0
	for rot in code:
		turn = [rot[0], int(rot[1:])]
		if turn[1] >= 100:
			ans += int(turn[1]) // 100
			turn[1] = turn[1] % 100

		if turn[0] == 'L':
			if int(turn[1]) > pointer != 0:
				ans += 1
			pointer -= int(turn[1])
		else:
			if int(turn[1]) + pointer > 100:
				ans += 1
			pointer += int(turn[1])
		pointer %= 100
		if pointer == 0:
			ans += 1
	return ans


start = time.time()
print(P2(data))
end = time.time()
print(f'Time taken: {(end - start) * 1000}ms')
