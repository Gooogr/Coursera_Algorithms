import random

# https://www.youtube.com/watch?v=7cYgEd1I4gA
def qiuckSort_simple(arr):
	'''
	Input: array A of n distinct integers.
	Postcondition: elements of A are sorted from smallest
	to largest.
	This emplementation is very short and easy, but use excessive memory.
	It also useless for weekly programming assigment (it need specific, memory effective implementation) 
	'''
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0] # it also could be "random.choice(arr)" or whatever
		less = [item for item in arr if item < pivot]
		equal = [item for item in arr if item == pivot]
		greater = [item for item in arr if item > pivot]
		return qiuckSort_simple(less) + equal + qiuckSort_simple(greater)
		
def quickSort_memoryEffective(arr):
	'''
	Input: array A of n distinct integers.
	Postcondition: elements of A are sorted from smallest
	to largest.
	All elements are unique!
	'''
	if len(arr) < 2:
		return arr
	else:
		pivot_index = 0 #or something like "random.randint(0, len(arr) - 1)"
		i = 0
		for j in range(len(arr) - 1):
			if arr[j + 1] < arr[pivot_index]:
				arr[j + 1], arr[i + 1] = arr[i + 1], arr[j + 1]
				i += 1
		arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
		less = quickSort_memoryEffective(arr[:i])
		greater = quickSort_memoryEffective(arr[i + 1:])
		return less + [arr[i]] + greater

arr_1 = [1, 3, 0, 2, 5, 7, -4, 11]

print(qiuckSort_simple(arr_1))
print(quickSort_memoryEffective(arr_1))

