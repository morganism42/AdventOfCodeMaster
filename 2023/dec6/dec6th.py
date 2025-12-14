from numpy import prod
from time import perf_counter
from math import sqrt, floor, ceil

start = perf_counter()
# get 2 lists for time and distancs
with open('dec6.txt') as f:
	data = f.readlines()
	# data = [i.replace('  ','')for i in data]
	time = [int(i) for i in data[0].split('  ')]
	distance = [int(i) for i in data[1].split('  ')]

wins = []
for i in range(len(time)):  # iterate over each race
	temp = []
	for j in range(time[i]):  # find the smallest time to press and win
		if j * (time[i] - j) > distance[i]:
			wins.append([j, time[i] - j])
			break  # math
print(f'answer:{prod([(i[1] - i[0] + 1) for i in wins])}')
print(f'naive took {perf_counter() - start}) seconds')
start = perf_counter()
wins = []
for i in range(len(time)):
	x = floor(-(-time[i] - sqrt(time[i] ** 2 - 4 * distance[i])) / 2)
	y = ceil(-(-time[i] + sqrt(time[i] ** 2 - 4 * distance[i])) / 2)
	wins.append([y, x])
print(f'answer:{prod([(i[1] - i[0] + 1) for i in wins])}')
print(f'quadratic took {perf_counter() - start}) seconds')

