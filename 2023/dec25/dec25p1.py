from aocd import get_data, submit
import networkx as nx
from matplotlib import pyplot as plt

data = get_data(day=25, year=2023)
test = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''


def parse(raw):
	raw = raw.split('\n')
	graph = []
	for line in raw:
		line = line.split(': ')
		for point in line[1].split(' '):
			if (line[0], point) not in graph and (point, line[0]) not in graph:
				graph.append((line[0], point))
	nodes = []
	for edge in graph:
		for point in edge:
			if point not in nodes:
				nodes.append(point)
	return graph, nodes


G = nx.Graph()
graph, nodes = parse(data)

'''G.add_nodes_from(nodes)
for key in graph:
	G.add_edge(key[0], key[1])
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()'''

cut = (('fdb', 'psj'), ('nqh', 'rmt'), ('ltn', 'trh'))
start = cut[0]
for i in cut:
	if i in graph:
		graph.remove(i)
	else:
		graph.remove((i[1], i[0]))


def floodfill(graph, starting):
	visited = []
	unvisited = [starting]
	while unvisited:
		current = unvisited.pop(0)
		visited.append(current)
		for edge in graph:
			if current in edge:
				if edge[0] == current:
					if edge[1] not in visited and edge[1] not in unvisited:
						unvisited.append(edge[1])
				else:
					if edge[0] not in visited and edge[0] not in unvisited:
						unvisited.append(edge[0])
	print(visited)
	return len(set(visited))


'''G.add_nodes_from(nodes)
for key in graph:
	G.add_edge(key[0], key[1])
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

plt.show()'''

submit(floodfill(graph, start[1]) * floodfill(graph, start[0]), day=25, year=2023, part='a')
