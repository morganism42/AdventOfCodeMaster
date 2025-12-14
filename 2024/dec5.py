from aocd import get_data, submit
from collections import defaultdict


def solve1(test=True):
	# Your solution code here
	testdata = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
	testans = 143
	if test:
		data = testdata
	else:
		data = get_data(day=5, year=2024)
	data = data.split('\n\n')
	commands = [x.split('|') for x in data[0].splitlines()]
	conditions = defaultdict(list)
	for condition in commands:
		conditions[condition[1]].append(condition[0])

	stacks = [x.split(',') for x in data[1].splitlines()]
	correct = []
	for s, stack in enumerate(stacks):
		for b, book in enumerate(stack):
			if any(x in conditions[book] for x in stack[b:]):
				break
		else:
			correct.append(stack)
	result = sum([int(x[int((len(x) - 1) / 2)]) for x in correct])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="a", day=5, year=2024)


def solve2(test=True):
	# Your solution code here
	testdata = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
	testans = 123
	if test:
		data = testdata
	else:
		data = get_data(day=5, year=2024)
	data = data.split('\n\n')
	commands = [x.split('|') for x in data[0].splitlines()]
	conditions = defaultdict(list)
	for condition in commands:
		conditions[condition[1]].append(condition[0])

	stacks = [x.split(',') for x in data[1].splitlines()]
	correct = []
	for s, stack in enumerate(stacks):
		for b, book in enumerate(stack):
			if any(x in conditions[book] for x in stack[b:]):
				correct.append(stack)
				break
	for s, stack in enumerate(correct):
		for b, book in enumerate(stack):
			for c, mag in enumerate(stack[b:], b):
				if mag in conditions[stack[b]]:
					stack[b], stack[c] = stack[c], stack[b]
					correct[s] = stack
		result = sum([int(x[int((len(x) - 1) / 2)]) for x in correct])

	if test and result == testans:
		print("Test passed")
	elif test and result != testans:
		print(correct, result)
		print("Test failed")
	elif not test:
		print(result)
		submit(result, part="b", day=5, year=2024)

