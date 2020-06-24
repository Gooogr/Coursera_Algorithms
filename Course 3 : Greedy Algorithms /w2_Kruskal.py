from collections import defaultdict, OrderedDict
from collections import deque
from math import inf

PATH_FILE = '../WeeklyTasksData/edges.txt'

data = open(PATH_FILE).read().splitlines()

number_of_nodes = int(data[0].split()[0])
number_of_edges = int(data[0].split()[1])

# Convert our data to weights sorted adjacency list format
# dict: {weight_1: [node_i, node_j], 
#		 weight_2: [node_k, node_l], 
#		 ...}

graph_dict = defaultdict(list)
for edge in data[1:]:
	edge = list(map(int, edge.split()))
	graph_dict[edge[2]].append(edge[:2])	
		
# Naive implementation of Kruskal's algorythm, using:
# O(m*logn) for sorting edges by encreasing costs;
# O(n) bfs (or dfs) routine to check for cycles inside the main for-loop 
# with m edges. So, main loop subrutione is O(m*n)
# Run-time: O(m*logn) + O(m*n) => O(m*n)

def naiveKruskal(graph):
	# Sort graph dict by key (weight)
	graph = OrderedDict(sorted(graph.items(), key=lambda x: x[0]))
	# Initialize variable
	acyclic_tree = defaultdict(list)
	treeCost = 0
	for weight in graph:
		if len(acyclic_tree) == number_of_nodes:
			break
		# Weight is graph are non-unique, we can have several edges with same cost
		for edge in graph[weight]:
			# Wake up dfs subrutine
			if not hasLoop(acyclic_tree, edge):
				acyclic_tree[edge[0]].append(edge[1])
				acyclic_tree[edge[1]].append(edge[0])
				treeCost += weight
	return treeCost
		
def hasLoop(tree, edge):
	'''
	DFS subrutine. Algorithm find all nodes linked with start node.
	After that it checks if end node belong to this explored graph.
	'''
	start, end = edge[0], edge[1]
	if (start not in tree) or (end not in tree):
		return False
	S, explored = deque(), set()
	S.append(start)
	while len(S) > 0:
		v = S.pop()
		if v not in explored:
			explored.add(v)
			for item in tree[v]:
				S.append(item)
	return (end in explored)
	
print(naiveKruskal(graph_dict))

# Union-Find Kfuskal algorythm 
def unionFindKruskal(graph):
	pass
