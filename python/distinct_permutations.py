# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# TC - O(n*n!)
# ?
# Note that there are n! permutations and it requires O(n) time to print a a permutation.

def permute(arr, start, end, dict):
	if start == end:
		stri = ''.join(str(i) for i in arr)
		if not dict.get(stri, None):
			print stri
			dict[stri] = 1
		return
	for i in xrange(start, end):
		arr[start], arr[i] = arr[i], arr[start]
		# permute(list(arr), start+1, end)          # <-------- mutable objects are passed by reference in python, so create a new list
		# arr[start], arr[i] = arr[i], arr[start]
		permute(arr, start+1, end, dict)
		arr[start], arr[i] = arr[i], arr[start]     # <-------- this backtracks the solution

