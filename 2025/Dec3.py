from aocd import get_data
import time
data = get_data(day=3, year=2025)

test = '''987654321111111
811111111111119
234234234234278
818181911112111'''


def parse(Data):
	Data = [[int(i) for i in n] for n in Data.splitlines()]
	return Data


# length being the quantity of batteries
def solution(Data, length):
	Data = parse(Data)
	charge = 0
	for bank in Data:
		Bank = bank
		jolt = 0
		for i in range(length):
			if i < length - 1:
				curdex = Bank.index(max(Bank[:-length + (i + 1)]))
			else:
				curdex = Bank.index(max(Bank))
			jolt *= 10
			jolt += Bank[curdex]
			Bank = Bank[curdex + 1:]
		# print(jolt)
		charge += jolt
	print(charge)



start = time.time()
solution(data, 12)
end = time.time()
print(f'Time taken: {(end - start) * 1000}ms')