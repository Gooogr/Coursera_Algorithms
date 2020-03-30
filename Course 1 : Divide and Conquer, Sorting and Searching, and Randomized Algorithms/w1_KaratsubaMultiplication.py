def KaratsbaMult_str(x, y):
	'''
	Input:
		two n-digit positive integers x and y
	Output:
		the product x*y
	We assume that n is powers of n
	'''
	if len(str(x)) != len(str(y)):
		delta = abs(len(str(x)) - len(str(y)))
		if len(str(x)) > len(str(y)):
			y = '0' * delta + str(y)
		else:
			x = '0' * delta + str(x)
	n = len(str(x))
	if n == 1:
		return x * y
	else:
		a, b = int(str(x)[:n/2]), int(str(x)[n/2:])
		c, d = int(str(y)[:n/2]), int(str(y)[n/2:])
		p = a + b
		q = c + d
		ac = KaratsbaMult_str(a, c)
		bd = KaratsbaMult_str(b, d)
		pq = KaratsbaMult_str(p, q)
		adbc = pq - ac - bd
		result = 10**n*ac + 10**(n/2)*adbc + bd
		return result
		

def KaratsbaMult_int(x,y):
	'''
	Input:
		two n-digit positive integers x and y
	Output:
		the product x*y
	We assume that n is powers of n
	'''
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = KaratsbaMult_int(a,c)
		bd = KaratsbaMult_int(b,d)
		ad_plus_bc = KaratsbaMult_int(a+b,c+d) - ac - bd
        
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod


num_1 = 3141592653589793238462643383279502884197169399375105820974944592

num_2 = 2718281828459045235360287471352662497757247093699959574966967627

print(KaratsbaMult_str(num_1, num_2))
print(KaratsbaMult_int(num_1, num_2))


