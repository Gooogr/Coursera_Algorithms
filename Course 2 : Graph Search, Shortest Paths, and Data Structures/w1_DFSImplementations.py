from collections import deque
import numpy as np 

example_graph = {
				's': ['a', 'b'],
				'b': ['s', 'c', 'd'],
				'a': ['s', 'c'],
				'c': ['b', 'a', 'e'],
				'd': ['b', 'e'],
				'e': ['c', 'd']
				}

# Iterative DFS implementation
def iterativeDFS(g, start_vertex):
	'''
	Iterative implementation of DFS algorithm.
	Input:
		g - graph in incidence lists form: {'vertex':[vertex1, vertex2, ...], ...}
		s - starting vertex
	Output:
		explored_dict - dict with {'vertex': explored (True, False)}.
	You can check graph integrity by boolean explored label.
	The main difference between DFS and BFS - DFS uses stack, not queue.
	'''
	S = deque()
	S.append(start_vertex)
	explored_dict = dict(zip(list(g.keys()), [False] * len(g)))
	while len(S) > 0:
		v = S.pop()
		if explored_dict[v] == False:
			explored_dict[v] = True
			for item in g[v]:
				S.append(item)
	return explored_dict
	
print(iterativeDFS(example_graph, 'e'))			
	

# Recurrent DFS implementation
exp_dict = dict(zip(list(example_graph.keys()), 
					[False] * len(example_graph)))

def recurrentDFS(g, start_vertex):
	'''
	Recurrent implementation of DFS algorithm.
	Input:
		g - graph in incidence lists form: {'vertex':[vertex1, vertex2, ...], ...}
		s - starting vertex
	Output:
		explored_dict - dict with {'vertex': explored (True, False)}.
	You can check graph integrity by boolean explored label.
	You have to initialize explored dictionary like global variable!
	'''
	global exp_dict
	exp_dict[start_vertex] = True
	for v in g[start_vertex]:
		if exp_dict[v] == False:
			recurrentDFS(g, v)
			
recurrentDFS(g = example_graph, start_vertex = 'e')			
print(exp_dict)
				
