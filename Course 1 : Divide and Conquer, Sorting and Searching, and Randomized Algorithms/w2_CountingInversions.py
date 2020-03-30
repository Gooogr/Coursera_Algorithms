def countInv_simple(arr):
	'''
	Straightforward appproach to count amount of inversions in a array.
	O = n**2
	'''
	i, j = 0, 0
	numInv = 0
	for i in range(len(arr)):
		for j in range(i, len(arr) - 1):
			if arr[i] > arr[j]:
				numInv += 1
	return numInv


# Let`s write something better	
totalInv = 0

def SortAndCountInv(arr):
	if len(arr) < 2:
		return (arr, 0)
	else:
		n = len(arr)//2
		#print('Splited arrays: ', n, arr[:n], arr[n:])
		(left_arr, left_inv) = SortAndCountInv(arr[:n])
		(right_arr, right_inv) = SortAndCountInv(arr[n:])
		(merged_arr, split_inv) = MergeAndCountInv(left_arr, right_arr)
		return (merged_arr, left_inv + right_inv + split_inv)
		
def MergeAndCountInv(left_arr, right_arr):
	global totalInv
	result = []
	i, j = 0, 0
	splitInv = 0
	#print()
	#print('Merging arrays: ', left_arr, right_arr)
	while len(left_arr) != 0 and len(right_arr) != 0:
		if left_arr[0] <= right_arr[0]:
			result.append(left_arr[0])
			left_arr.remove(left_arr[0])
		else:
			result.append(right_arr[0])
			right_arr.remove(right_arr[0])
			splitInv += len(left_arr)
	if len(left_arr) == 0:
		result += right_arr
	else:
		result += left_arr
	#print('Result: ', result)
	#print()
	return (result, splitInv)
			
	
	
arr_1 = [1, 3, 5, 2, 4, 6]

print(countInv_simple(arr_1))
print(SortAndCountInv(arr_1)[1])
