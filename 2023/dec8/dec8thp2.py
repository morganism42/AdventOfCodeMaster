import numpy as np

with open('dec8.txt') as f:
	data = f.read().split('\n')
	instructs = data[0]
	temp = data[2:]
Map = {}
for i in temp:
	Map[i[:3]] = [i[-9:-6], i[-4:-1]]

locations = []
for i in Map.keys(): # finds all start locations
	if i[-1] == 'A':
		locations.append(i)
steps = 0


def allz(x):
	for i in x:
		if i[-1] != 'Z':
			return False
	return True


paths = []
nothere = True
for x, location in enumerate(locations): # for each start location
	paths.append(0)
	steps = 0
	path = []
	Znotfound = True
	nothere = True
	while nothere:
		for i in instructs:
			steps += 1
			if i == 'L':
				location = Map[location][0]
			elif i == 'R':
				location = Map[location][1]
			if location[-1] == 'Z': # find first time you encounter a location ending in Z
				paths[-1] = steps
				nothere = False
				break
			path.append(location)


print(np.lcm.reduce(paths, dtype='int64')) #due to the length from start to Z being the same as the length from Z to Z LCM just works

