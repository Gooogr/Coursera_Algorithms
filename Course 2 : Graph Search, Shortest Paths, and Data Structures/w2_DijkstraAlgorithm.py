FILE_PATH = '/root/Desktop/Repos/Coursera_Algorithms/WeeklyTasksData/dijkstraData.txt'

# https://www.youtube.com/watch?v=IG1QioWSXRI  https://pastebin.com/3Q9rqGHA
# https://www.youtube.com/watch?v=Ub4-nG09PFw  https://gist.github.com/amitabhadey/37af83a84d8c372a9f02372e6d5f6732
# https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python   First Answer. Really good one!

def readUndirectedGraphToList(filename): 
	'''
	Convert raw file from practice assigmnent to the adjustmnet list structure:
	[[end_vertex_label, edge_weight], ...]
	Positions of list elements equal to labels of starting vertex.
	input:
		Path to txt file
	output:
		Adjustment list of underected graph with weights.
	'''
	adjlist = []
	lines = open(filename).read().splitlines()
	for line in lines:
		adjlist.append([])
		data = line.split()
		v = int(data[0]) - 1 # because we want to count from 0
		
		for tpl in data[1:]:
			ts, ws = tpl.split(',')
			t = int(ts) - 1
			w = int(ws)
			adjlist[v].append((t, w))

	return adjlist
	
def readUndirectedGraphToDict(filename): 
	'''
	Convert raw file from practice assigmnent to the adjustmnet dict structure:
	{starting_vertex: {end_vertex_label1: edge_weight1, ...},	...}
	input:
		Path to txt file
	output:
		Adjustment dict of underected graph with weights.
	'''
	adjdict = {}
	lines = open(filename).read().splitlines()
	for line in lines:
		data = line.split()
		label_vertex = int(data[0])
		temp_dict = {}
		for pair in data[1:]:
			vertex, weight = pair.split(',')
			temp_dict[int(vertex)] = int(weight)
		adjdict[label_vertex] = temp_dict
	return adjdict

# find picture of this graph here: https://www.youtube.com/watch?v=K_1urzWrzLs		
testGraph = {
						'A': {'B': 2, 'C': 4, 'D': 7, 'F': 5},
						'B': {'A': 2, 'D': 6, 'E': 3, 'G': 8},
						'C': {'A': 4, 'F': 6},
						'D': {'A': 7, 'B': 6, 'F': 1, 'G': 6},
						'E': {'B': 3, 'G': 7},
						'F': {'A': 5, 'C': 6, 'D': 1,'G': 6},
						'G': {'B': 8, 'D': 6, 'E': 7, 'F': 6}
					  }
						
def getDijkstraPathes(graph, start_vertex):

	# initialization
	nodes = list(graph.keys())
	unvisited = {node: 1e6 for node in nodes} #use 1e6 as inf
	visited = {}
	current = start_vertex
	currentDistance = 0
	unvisited[current] = currentDistance	

	while True:
		for neighbour, distance in graph[current].items():
			print(neighbour, distance)
			# Check, if we aleady visit neighbour of current vertex
			if neighbour not in unvisited: 
				continue
			# Calculate new distance to unvisited neighbour. Replace if it less then previous value
			newDistance = currentDistance + distance
			if unvisited[neighbour] > newDistance:
				unvisited[neighbour] = newDistance
			print(unvisited)
			
		# Update dict if visited nodes with their distances
		visited[current] = currentDistance
		# Remove visited vertex from unvisited 
		del unvisited[current]
		
		# check if we still have unvisied nodes. If not - break the while loop and return result
		if not unvisited: 
			break
			
		#greedly choose new vertex with the smallest  distance
		candidates = [node for node in unvisited.items()]
		current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

	return visited


print('Test example:', getDijkstraPathes(testGraph, 'A'))

assignmnet_graph = readUndirectedGraphToDict(FILE_PATH)
vertex_dict = getDijkstraPathes(assignmnet_graph, 1)

check_list = [7,37,59,82,99,115,133,165,188,197]
answer = [vertex_dict[key] for key in check_list]
print('Assigmnet answer:', answer)



