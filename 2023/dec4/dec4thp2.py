def timing(self):
	import time
	start_time = time.time()
	self.implement()
	end_time = time.time()
	print(f'Time taken: {end_time - start_time} seconds')


timing()
with open('dec4.txt') as f:
	data = f.read().splitlines()
data = [i[i.find(':') + 2:].replace('  ', ' ').split(' | ') for i in data]

for n, i in enumerate(data):
	data[n] = [i[0].split(' '), i[1].split(' ')]  # splits card into winning numbers and test numbers
	data[n].append(1)  # adds a card count to the end of each card

for n, i in enumerate(data):
	a = len(set(i[0]) & set(i[1]))
	if a > 0:
		for j in range(a):
			if n + j + 1 >= len(data):
				break
			data[n + j + 1][-1] += data[n][-1]

# sums the card counts
print(sum([i[-1] for i in data]))
