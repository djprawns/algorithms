# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# TC - O(n*n!)
# ?
# Note that there are n! permutations and it requires O(n) time to print a a permutation.

def permute(arr, start, end):
	if start == end:
		print ''.join(str(i) for i in arr)
		return
	for i in xrange(start, end):
		arr[start], arr[i] = arr[i], arr[start]
		permute(arr, start+1, end)

