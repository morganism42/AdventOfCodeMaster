from aocd import get_data

data = get_data(day=12, year=2025)
test = '''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''


def parse(Data):
	Data = Data.split('\n\n')
	pieces = {int(piece[0]): piece.splitlines()[1:] for piece in Data[:6]}
	instructs = [[instr.split(':')[0], instr.split(':')[1].split(' ')] for instr in Data[-1].splitlines()]
	return pieces, instructs


def part1(Data):
	ans = 0
	ans2 = 0
	pieces, instructs = parse(Data)
	piecesum = {0: 9, 1: 9, 2: 9, 3: 9, 4: 9, 5: 9}
	for instr in instructs:
		nums = instr[0].split('x')
		nums = int(nums[0]) * int(nums[1])
		summ = 0
		summ2 = 0
		numbs = [int(i) for i in instr[1][1:]]
		# is their space for all the pieces within each piece?
		for i in range(6):
			summ += piecesum[i] * numbs[i]
		# is there space if each piece was full?
		for i in range(6):
			summ2 += 9 * numbs[i]
		if nums >= summ:
			ans += 1
		if nums >= summ2:
			ans2 += 1
	return ans, ans2  # these being the same means there is either definitively too little space or way more than necessary


def part2(Data):
	return 'Merry Christmas'


print(part1(data))
print(part2(data))
