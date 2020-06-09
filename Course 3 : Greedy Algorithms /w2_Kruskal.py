from collections import defaultdict  
from math import inf

PATH_FILE = '../WeeklyTasksData/edges.txt'

data = open(PATH_FILE).read().splitlines()

number_of_nodes = data[0][0]
number_of_edges = data[0][1]

# Convert our data to adjacency list format
# dict: {node_1: [[node_2, weight_1], ...], 
#		 node_2: [[node_1, weight_1], ...], 
#		 ...}

graph_dict = defaultdict(list)
for edge in data[1:]:
	edge = list(map(int, edge.split()))
	graph_dict[edge[0]].append(edge[1:]) # first edge ~ [second_edge, weight]
	graph_dict[edge[1]].append([edge[0], edge[2]]) # second edge ~ [first_edge, weight]
	
print(graph_dict)


# Naive implementation of kruskal's algorythm, using:
# O(m*logn) for sorting edges by encreasing costs;
# O(n) bfs (or dfs) routine to check for cycles inside the main for-loop 
# with m edges. So, main loop subrutione is O(m*n)
# Run-time: O(m*logn) + O(m*n) => O(m*n)

def naiveKruskal(graph):
	pass
	 
def unionFindKruskal(graph):
	pass
