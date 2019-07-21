def fib_naive(n):
	if n == 1 or n == 2:
		return 1
	result = fib_naive(n-1) + fib_naive(n-2)
	return result