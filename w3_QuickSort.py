import random

# https://www.youtube.com/watch?v=7cYgEd1I4gA
def qiuckSort(arr):
	'''
	Input: array A of n distinct integers.
	Postcondition: elements of A are sorted from smallest
	to largest.
	'''
	if len(arr) < 2:
		return arr
	else:
		pivot = random.choice(arr)
		less = [item for item in arr if item < pivot]
		equal = [item for item in arr if item == pivot]
		greater = [item for item in arr if item > pivot]
		return qiuckSort(less) + equal + qiuckSort(greater)

arr_1 = [1, 3, 5, 2, 4, 6]
print(qiuckSort(arr_1))
