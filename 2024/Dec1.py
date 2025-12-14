from aocd import get_data, submit

data = get_data(day=1, year=2024)
test = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''


def parse(data):
	data = data.split('\n')
	data = [i.split('   ') for i in data]
	list1 = [i[0] for i in data]
	list2 = [i[1] for i in data]
	list1.sort()
	list2.sort()
	return list1, list2


list1, list2 = parse(data)
distances = []
for i in range(len(list1)):
	distances.append(abs(int(list1[i]) - int(list2[i])))
#submit(sum(distances), part='a', day=1, year=2024)
fullscore = 0
for i in list1:
	score = 0
	for j in list2:
		if i == j:
			score += 1
	fullscore += score * int(i)
#submit(fullscore, part='b', day=1, year=2024)
