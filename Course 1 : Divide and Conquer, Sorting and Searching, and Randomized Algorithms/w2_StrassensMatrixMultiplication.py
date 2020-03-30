import numpy as np

# How to set up venv in geany: https://stackoverflow.com/questions/42013705/using-geany-with-python-virtual-environment

# Straightforward Matrix Multiplication
def matrixMultiplication_strf(X, Y):
	'''
	Straightforward approach to multiply two matrices.
	Input: 
		Two nxn integer matrices, X and Y.
	Output: 
		The matrix product X*Y.
	'''
	n = len(X)
	Z = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			Z[i][j] = 0
			for k in range(n):
				Z[i][j] += X[i][k] * Y[k][j]
	return Z
	
def matrixMultiplication_strs(X, Y):
	'''
	Strassen`s approach to multiply two matrices.
	Input: 
		Two nxn integer matrices, X and Y.
	Output: 
		The matrix product X*Y.
	We assume than n is power of two.
	'''
	n = len(X)
	# print(n)
	if n < 2:
		return X * Y
	else:
		A = X[:n//2, :n//2]
		B = X[:n//2, n//2:]
		C = X[n//2:, :n//2]
		D = X[n//2:, n//2:]
		
		E = Y[:n//2, :n//2]
		F = Y[:n//2, n//2:]
		G = Y[n//2:, :n//2]
		H = Y[n//2:, n//2:]
		
		P1 = matrixMultiplication_strs(A, (F - H))
		P2 = matrixMultiplication_strs((A + B), H)
		P3 = matrixMultiplication_strs((C + D), E)
		P4 = matrixMultiplication_strs(D, (G - E))
		P5 = matrixMultiplication_strs((A + D), (E + H))
		P6 = matrixMultiplication_strs((B - D), (G + H))
		P7 = matrixMultiplication_strs((A - C), (E + F))
		
		L1 = P5 + P4 - P2 + P6
		L2 = P3 + P4
		R1 = P1 + P2
		R2 = P1 + P5 - P3 - P7
		
		result = np.vstack([np.hstack([L1, L2]), np.hstack([R1, R2])])
		return result
			
X = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [1, 2, 3, 4]])
Y = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [1, 2, 3, 4]])

print(matrixMultiplication_strf(X, Y))
print(matrixMultiplication_strs(X, Y))


	
