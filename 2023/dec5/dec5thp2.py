from time import perf_counter as watch
start = watch()
with open('dec5.txt') as f:
	data = f.read()
	data = data.split('\n\n')
seeds = data[0][data[0].find(':') + 2:].split(' ')
seeds = [int(i) for i in seeds]
seedpacks = []
# turns each seed and instruction pair into a pair of first and last seed
for i in range(0, len(seeds), 2):
	seedpacks.append([seeds[i], seeds[i] + seeds[i + 1] - 1])
# parses map into sets of instructions
field = []
for i in range(1, len(data)):
	field.append(data[i][data[i].find(':') + 2:].split('\n'))
	for j, n in enumerate(field[i - 1]):
		field[i - 1][j] = n.split(' ')

# makes map values integers
for i in range(len(field)):
	for j in range(len(field[i])):
		for n in range(len(field[i][j])):
			field[i][j][n] = int(field[i][j][n])

# for each set of instructions run all the seed packs thorugh those instructions and replace the seedpack
for intructs in field:
	packstemp = []
	for pack in seedpacks:
		for instruct in intructs:
			# if both seeds are between the edges of the seeds that need to be moved, move them all
			if instruct[2] + instruct[1] > pack[0] >= instruct[1] and instruct[2] + instruct[1] > pack[1] >= instruct[
				1]:
				packstemp.append([pack[0] - (instruct[1] - instruct[0]), pack[1] - (instruct[1] - instruct[0])])
				pack = []
				break
			# if only one is, then move all withing to a new seed pack, and keep the current pack
			elif instruct[2] + instruct[1] > pack[0] >= instruct[1]:
				packstemp.append([pack[0] - (instruct[1] - instruct[0]), instruct[0] + (instruct[2] - 1)])
				pack = [instruct[1] + instruct[2], pack[1]]
			elif instruct[2] + instruct[1] > pack[1] >= instruct[1]:
				packstemp.append([instruct[0], pack[1] - (instruct[1] - instruct[0])])
				pack = [pack[0], instruct[1] - 1]

		if len(pack) > 0:
			packstemp.append(pack)
	seedpacks = packstemp
print(min([i[0] for i in seedpacks]))
print(f'completed in {watch()-start} seconds')
