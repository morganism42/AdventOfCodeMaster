from aocd import get_data
import re

data = get_data(year=2015, day=5)


def part1(data):
	hits = re.findall(
		r"(?=^.*(.)\1+.*$)(?=^.*[aeiou].*[aeiou].*[aeiou].*$)(?!^.*ab.*$)(?!^.*cd.*$)(?!^.*pq.*$)(?!^.*xy.*$)", data,
		re.MULTILINE)
	return len(hits)


def part2(data):
	hits = re.findall(r"(?=^.*(.).\1.*$).*(..).*\2.*", data,
	                  re.MULTILINE)
	return len(hits)


print(part1(data))
print(part2(data))
