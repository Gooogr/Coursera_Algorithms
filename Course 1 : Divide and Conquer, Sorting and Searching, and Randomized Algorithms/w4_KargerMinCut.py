'''
Your task is to code up and run the randomized contraction algorithm 
for the min cut problem and use it on the above graph to compute 
the min cut.
'''
import random
from tqdm import tqdm

FILE_PATH = '/home/grigoriy/Desktop/Repos/Coursera_Algorithms/WeeklyTasksData/kargerMinCut.txt'
N = 200

def load_graph(file_path):
	with open(file_path, 'r') as f:
		vertices_raw = [list(map(int, integers[:].strip().split('\t'))) for integers in f.readlines()] 
		vertices = [item[1:] for item in vertices_raw ]#cut off labels
		data_dict= dict(zip(range(1, 201), vertices))
		f.close()
	return data_dict
			
def merge_edge(v, u):
	global data
	# relpace u by v in all list
	for key in data.keys():
		data[key] = [v if item == u else item for item in data[key]]
	# merge u and v vertices, remove loops
	data[v] = list(data[v] + data[u])
	data[v] = [item for item in data[v] if item != v]
	# remove u
	del data[u]

results = []

for i in tqdm(range(N)):
	data = load_graph(FILE_PATH)
	while len(data) > 2:
		u = random.choice(list(data.keys()))
		v = random.choice(data[u])
		merge_edge(v, u)
	results.append(len(list(data.items())[0][1]))
	
print(min(results))
		
	


