'''
Your task in this problem is to run the greedy algorithm that schedules 
jobs in decreasing order of the difference (weight - length). Recall 
from lecture that this algorithm is not always optimal. 

IMPORTANT: if two jobs have equal difference (weight - length), you 
should schedule the job with higher weight first.
'''
FILE_PATH = '../WeeklyTasksData/jobs.txt'

data = open(FILE_PATH).read().splitlines()
jobs_amount = int(data[0])
jobs_pairs = []
for job in data[1:]:
	jobs_pairs.append(list(map(int, job.split())))
	

def diff_sum(jobs):
	# sort jobs by weight-length and weight
	arr = sorted(jobs, key=lambda x: ((x[0] - x[1]), x[0]), reverse = True)
	# calculate complete operation time
	final_time, job_time = 0, 0
	for job in arr:
		job_time += job[1]
		final_time += job_time * job[0]
	return final_time

def ratio_sum(jobs):
	# sort jobs by weight-length and weight
	arr = sorted(jobs, key=lambda x: ((x[0] / x[1]), x[0]), reverse = True)
	# calculate complete operation time
	final_time, job_time = 0, 0
	for job in arr:
		job_time += job[1]
		final_time += job_time * job[0]
	return final_time
	
			
	
print('Result diff time:', diff_sum(jobs_pairs))
print('Result ratio time:', ratio_sum(jobs_pairs))

# Right answers:
# For diff_sum: 69119377652
# For ratio_sum: 67311454237

	
	
