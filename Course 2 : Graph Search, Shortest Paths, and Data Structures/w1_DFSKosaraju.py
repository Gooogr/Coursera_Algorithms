G = {
		0: [1, 4, 3],
		1: [],
		2: [0],
		3: [2],
		4: [1, 3]
		}
from copy import copy

def transposeGraph(g):
	# Convert dict to lists structure. 
	# Because i didn`t find a right way to operate with dict
	adj= [[]] * len(g)
	for key in g.keys():
		adj[key] = g[key]
	
	# Create transposed adj.lists
	tr = [[]for i in range(len(g))] 
	for i in range(len(g)):
		for j in range(len(adj[i])):
			tr[adj[i][j]].append(i)
			
	# Rebuild transposed adj, dict
	gt = {key: tr[key] for key in range(len(tr))}
	
	return gt
	
	
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
	
	
def kisaraju(g):
	g_visited = set()
	gt_visited = set()
	# create transposed graph
	gt = transposeGraph(g)
	# Get topoogical sorting of transposed graph
	gt_topo = topoSort(gt)
	
	
		 

	
				
			
transposeGraph(G)