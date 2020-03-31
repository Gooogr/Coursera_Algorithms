'''
See w1_BFSShortestPath.py

The idea is to use an outer loop to make a single pass over the vertices, 
invoking BFS as a subroutine whenever the algorithm encounters a 
vertex that it has never seen before.
'''

from collections import deque
import numpy as np

example_graph = {
				's': ['a', 'b'],
				'b': ['s', 'c', 'd'],
				'a': ['s', 'c'],
				'c': ['b', 'a', 'e'],
				'd': ['b', 'e'],
				'e': ['c', 'd'],
				
				'f': ['g', 'h'],
				'g': ['f', 'h'],
				'h': ['f', 'g']
				}
				
def UCC(g):
	'''
	Function amount of disconnected parts in graph
	Input:
		g - graph in incidence lists, dict form: {'vertex':[vertex1, vertex2, ...], ...}
	Output:
		numCC - number of independent sub-graphs, int
	'''
	# initialize variables
	explored_dict = dict(zip(list(g.keys()), [False]*len(g)))
	numCC = 0 # amout of disconnected graph`s parts
	
	for vertex in explored_dict.keys():
		if explored_dict[vertex] == False:
			numCC += 1
			# Initialize variables for BFS
			explored_dict[vertex] = True
			queue = deque()
			queue.append(vertex)
			# BFS loop
			while len(queue) > 0:
				v = queue.popleft()
				for w in g[v]:
					if explored_dict[w] == False:
						explored_dict[w] = True
						queue.append(w)
	return(numCC)

print(UCC(example_graph))			
