import random
import copy

def quickSort(arr, pivot_selection_strategy):
	'''
	Input: array A of n distinct integers.
	Postcondition: elements of A are sorted from smallest
	to largest.
	All elements are unique!
	'''
	global counter
	# ~ print('test', arr)
	if len(arr) < 2:
		return arr
	else:
		counter += len(arr) - 1
		# ~ print('before', arr)
		arr = pivot_selection_strategy(arr) 
		# ~ print('after', arr)
		i = 0
		for j in range(len(arr) - 1):
			if arr[j + 1] < arr[0]:
				arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
				i += 1
		arr[0], arr[i] = arr[i], arr[0]
		less = quickSort(arr[:i], pivot_selection_strategy)
		greater = quickSort(arr[i + 1:], pivot_selection_strategy)
		return less + [arr[i]] + greater
	
# Pivot choice strategies
def firstElement(arr):
	return arr

	
def finalElement(arr):
	'''
	Quote from the task:
	Recall from the lectures that, just before the main Partition subroutine, 
	you should exchange the pivot element (i.e., the last element) 
	with the first element!
	'''
	arr[0], arr[-1] = arr[-1], arr[0]
	return arr 


def getMedianIndex(x):
	'''
	Return median index of list x
	'''
	if len(x) % 2 == 1:
		return len(x)//2
	else:
		return len(x)//2 - 1


def medianOfThree(arr):
	min_index = 0
	max_index = -1
	median_index = getMedianIndex(arr)
	if arr[min_index] < arr[median_index] < arr[max_index]:
		arr[0], arr[median_index] = arr[median_index], arr[0]
		return  arr
	elif arr[median_index] < arr[min_index] < arr[max_index]:
		arr[0], arr[min_index] = arr[min_index], arr[0]
		return arr
	else:
		arr[0], arr[max_index] = arr[max_index], arr[0]
		return arr

file_path = '/home/grigoriy/Desktop/Repos/Coursera_Algorithms/WeeklyTasksData/QuickSort.txt'
with open(file_path, 'r') as f:
	dataList = [int(integers.strip()) for integers in f.readlines()]
	f.close()
print('Check, that all numList elements are unique:', len(dataList) == len(set(dataList)))

numList = copy.copy((dataList))
counter = 0
quickSort(numList, firstElement)
print(counter) # Should be 162085


numList = copy.copy((dataList))
counter = 0
quickSort(numList, finalElement)
print(counter) # Should be 164123

numList = copy.copy((dataList))
counter = 0 
quickSort(numList, medianOfThree)
print(counter) # Should be 138382
