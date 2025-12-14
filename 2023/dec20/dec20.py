from aocd import get_data, submit
from copy import deepcopy
from numpy import lcm

data = get_data(day=20)
test = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''


class FlipFlop:
	def __init__(self, output):
		self.mem = -1
		self.sends = tuple(output)

	def pulse(self, val, source):
		if val == -1:
			self.mem = self.mem * -1
			return self.sends, self.mem
		else:
			return [], 0


class Conjunction:
	def __init__(self, inputs, outputs):
		self.inputs = inputs
		self.outputs = tuple(outputs)

	def pulse(self, val, source):

		self.inputs[source] = val
		if sum(list(self.inputs.values())) == len(list(self.inputs.values())):
			return self.outputs, -1
		else:
			return self.outputs, 1


def parse(data):
	conjucts = []
	data = data.split('\n')

	gates = {}
	for line in data:
		temp = line[1:].split(' -> ')
		if line[0] == '%':
			gates[temp[0]] = FlipFlop(temp[1].split(', '))
		elif line[0] == '&':
			conjucts.append([temp[0], temp[1].split(', ')])
		elif line[0] == 'b':
			broadcast = temp[1].split(', ')
	for con in conjucts:
		temp = {}
		for line in data:
			temp2 = line[1:].split(' -> ')
			if con[0] in temp2[1].split(', '):
				temp[temp2[0]] = -1
		gates[con[0]] = Conjunction(temp.copy(), con[1])
	return gates, broadcast


def part1(gates, broadcast, repeats=1000):
	high = 0
	low = 0
	pulses = []  # my broadcast signals
	for n in range(repeats):
		low += len(broadcast) + 1
		for i in broadcast:
			outputs, val = gates[i].pulse(-1, 'broadcast')  # send out the button pulses and count them
			for k in outputs:
				pulses.append([k, val, i])
				if val > 0:
					high += 1
				else:
					low += 1

		while pulses:
			new_pulses = []
			for pulse in pulses:
				# print(pulse[2], pulse[1], pulse[0])
				if pulse[0] not in gates.keys():
					continue
				outputs, val = gates[pulse[0]].pulse(pulse[1], pulse[
					2])  # push the pulse through the module and track the outputs
				if outputs:
					for k in outputs:
						new_pulses.append([k, val, pulse[0]])
						if val > 0:
							high += 1
						else:
							low += 1
				outputs = None
			pulses = deepcopy(new_pulses)  # new pulses become the current pulses
	# print('\n')
	print(high, low)
	return high * low


def part2(gates, broadcast):
	high = 0
	low = 0
	pulses = []
	n = 0
	toggles = []
	toggled = []
	while True:
		n += 1
		low += len(broadcast) + 1
		for i in broadcast:
			outputs, val = gates[i].pulse(-1, 'broadcast')
			for k in outputs:
				pulses.append([k, val, i])
				if val > 0:
					high += 1
				else:
					low += 1

		while pulses:
			new_pulses = []
			for pulse in pulses:
				# print(pulse[2], pulse[1], pulse[0])
				if pulse[0] == 'zp' and pulse[1] == 1:  # find the cycles for the appropriate modules
					if pulse[2] not in toggles:
						toggles.append(pulse[2])
						toggled.append(n)
						print(n, toggles)
						if len(toggles) >= 4:
							return lcm.reduce(toggled, dtype='int64')  # find the lcm of the cycles to get the answer
				if pulse[0] not in gates.keys():
					continue
				outputs, val = gates[pulse[0]].pulse(pulse[1], pulse[2])
				if outputs:
					for k in outputs:
						new_pulses.append([k, val, pulse[0]])
						if val > 0:
							high += 1
						else:
							low += 1
				outputs = None
			pulses = deepcopy(new_pulses)


modules, broadcast = parse(data)
print(part1(modules, broadcast))
print(part2(modules, broadcast))
