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
		
	
distances = readUndirectedGraphToDict(FILE_PATH)
nodes = list(distances.keys())
	
unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 1
currentDistance = 0
unvisited[current] = currentDistance	

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)

check_list = [7,37,59,82,99,115,133,165,188,197]
answer = [visited[key] for key in check_list]

print(answer)



