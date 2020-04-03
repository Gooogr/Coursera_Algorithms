G = {
		'a': [],
		'b': [],
		'c': ['d'],
		'd': ['b'],
		'e': ['a', 'b'],
		'f': ['a', 'c']
		}

def dfs(start, g, visited, topo_result):
	'''
	Backtracking a single directed graph component.
	Add this topological track into topo_result list.
	input:
		start  - starting vertex from graph g
		g - graph, dict of adj. lists
		visited - set of visited vertexes
		topo_result - empty list with topological track
	output:
		topo_result - topological track of selected graph component
	'''
	visited.add(start)
	for vertex in g[start]:
		if vertex not in visited:
			dfs(vertex, g, visited, topo_result)
	topo_result.append(start)
		
	
def topoSort(g):
	'''
	Create complete topological sort list for all directed components
	input:
		g - graph, dict of adj. lists
	output:
		opo_result - topological track of graph
	'''
	visited = set() # In previous DFS and BFS implementations I used dict, but that was less memory effective
	topo_result = []
	for vertex in g:
		if vertex not in visited:
			dfs(vertex, g, visited, topo_result)
	return topo_result[::-1]

print(topoSort(G))