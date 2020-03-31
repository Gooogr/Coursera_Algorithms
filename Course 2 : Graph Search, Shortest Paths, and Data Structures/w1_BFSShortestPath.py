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
				
def findShortestPath(g, s):
	'''
	Function compute distnace from edge s to every edge in grapg g. 
	Also it checks graph integrity.
	Input:
		g - graph in incidence lists form: {'vertex':[vertex1, vertex2, ...], ...}
		s - starting vertex
	Output:
		explored_dict - dict with {'vertex': [explored (True, False), distance]}.
	You can check graph integrity by boolean explored label. If some vertex has False label - you can`t 
	get from vertex s to this vertex.
	'''
	# initialize variables
	explored_dict = dict(zip(list(g.keys()), [[False, np.inf]]*len(g)))
	explored_dict[s] = [True, 0]
	queue = deque()
	queue.append(s)
	
	while len(queue) > 0:
		v = queue.popleft()
		d_v = explored_dict[v][1] #distance from s to v
		for w in g[v]:
			if explored_dict[w][0] == False:
				explored_dict[w] = [True, d_v + 1]
				queue.append(w)
	return(explored_dict)
	 
	
print(findShortestPath(g, s = 'e'))


