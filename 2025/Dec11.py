import math
import time
from functools import cache

from aocd import get_data

data = get_data(day=11, year=2025)

test1 = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''
test2 = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''


def parse(Data):
	Data = [line.split(' ') for line in Data.splitlines()]
	out = {line[0][:-1]: line[1:] for line in Data}
	return out


def part1(Data):
	@cache
	def recursive_search(position):
		out = 0
		for pos in Data[position]:
			if pos == 'out':
				out += 1
			else:
				out += recursive_search(pos)
		return out

	Data = parse(Data)
	start = 'you'
	return recursive_search(start)


def part2(Data):
	Data = parse(Data)

	@cache
	def recursive_search(position, goal, banned):
		out = 0
		banout = []
		for pos in Data[position]:
			tbanout = []
			temp = 0
			if pos == goal:
				out += 1
				break
			elif pos in banned:
				continue
			else:
				temp, tbanout = recursive_search(pos, goal, banned)
			out += temp
			banout += tbanout
		if out > 0:
			banout.append(position)
		banout = tuple(set(banout))
		return out, banout

	after = tuple()
	out1, after = recursive_search('dac', 'out', after)
	print(out1)
	out2, after = recursive_search('fft', 'dac', after)
	print(out2)
	out3, after = recursive_search('svr', 'fft', after)
	print(out3)

	return math.prod([out1, out2, out3])


tstart = time.time()
print(part2(data))
end = time.time()
print(f'Time taken: {(end - tstart) * 1000}ms')
