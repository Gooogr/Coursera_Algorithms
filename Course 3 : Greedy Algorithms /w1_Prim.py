'''
In this programming problem you'll code up Prim's minimum spanning tree algorithm.

This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

Your task is to run Prim's minimum spanning tree algorithm on this graph. 
You should report the overall cost of a minimum spanning tree --- an integer, 
which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) 
time implementation of Prim's algorithm should work fine.
'''
from collections import defaultdict  
from math import inf

# We use collection.defaultdict instead of dict, because we want 
# automatically initialize new keys and append to them new values (see 37-38 strings)


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


def naivePrim(graph_dict):
	'''
	Straightforward O(m*n) implementation of Primm`s algorithm
	'''
	visited_nodes = set([list(graph_dict.keys())[0]])
	weights = []
	while visited_nodes != set(list(graph_dict.keys())):
		best_node = None
		best_weight = inf
		for u in visited_nodes:
			for v in graph_dict[u]:
				if (v[0] not in visited_nodes) and (v[1] < best_weight):
					best_node = v[0]
					best_weight = v[1]
		weights.append(best_weight)
		visited_nodes.add(best_node)
	return sum(weights)
	
print(naivePrim(graph_dict))
	
	
# Answer is -3612829
	
	
	
