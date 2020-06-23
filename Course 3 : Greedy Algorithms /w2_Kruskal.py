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
	# Sort graph dict by key
	graph = OrderedDict(sorted(graph.items(), key=lambda x: x[0]))
	# Initialize variable
	acyclic_tree = defaultdict(list)
	treeCost = 0
	while len(acyclic_tree) < number_of_nodes: #Результат не зависит от порога !?
		for weight in graph:
			# Weight is graph are non-unique, we can have several edges with same cost
			for edge in graph[weight]:
				# Wake up dfs subrutine
				if not hasLoop(acyclic_tree, edge):
					acyclic_tree[edge[0]].append(edge[1])
					acyclic_tree[edge[1]].append(edge[0])
					treeCost += weight
	return treeCost
		
# ~ def hasLoop(tree, edge):
	# ~ start, end = edge[0], edge[1]
	# ~ if (start not in tree) or (end not in tree):
		# ~ return False
	# ~ S, explored = deque(), set()
	# ~ S.append(start)
	# ~ while len(S) > 0:
		# ~ v = S.pop():
			# ~ if # ???
	
	
def hasLoop(graph, edge):

	#if u or v not in tree, no path exists b/w them, thus edge (u, v) can be added to MST
	start, end = edge[0], edge[1]
	if start not in graph or end not in graph:
		return False

	#init
	explored = [False] * number_of_nodes
	queue, explored[-1 * start] = [start], True

	#loop until queue is empty
	while queue:
		v = queue.pop(0)
		for w in graph[v]:
			if not explored[-1 * w]:
				explored[-1 * w] = True
				queue.append(w)

	return explored[-1 * edge[1]]	
	
	

print(naiveKruskal(graph_dict))

# Union-Find Kfuskal algorythm 
def unionFindKruskal(graph):
	pass
