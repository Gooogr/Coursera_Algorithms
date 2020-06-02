# Simple way - python set
TXT_PATH = '/home/grigoriy/Repos/Coursera_Algorithms/WeeklyTasksData/2sum.txt'

from tqdm import tqdm

def txt2dict(filename):
	with open(filename, "r") as f:
		txt_set = set()
		for line in f:
			txt_set.add(int(line))
	return txt_set
			
hash_set = txt2dict(TXT_PATH)

counter = 0
for t in tqdm(range(-10000,10001)):
	for key in hash_set:  #wordFreqDic.get("test") != None
		if (t-key) in hash_set and (t - key) != key:
			counter += 1
			break
			
print(counter) #427
	

