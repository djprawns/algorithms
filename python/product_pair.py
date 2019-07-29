# https://www.geeksforgeeks.org/pair-with-given-product-set-1-find-if-any-pair-exists/
#Efficient Solution ( O(n) ): We can improve time complexity to O(n) using hashing. Below are steps.
#Create an empty hash table
#Traverse array elements and do following for every element arr[i].
#	If arr[i] is 0 and x is also 0, return true, else ignore arr[i].
#	If x % arr[i] is 0 and x/arr[i] exists in table, return true.
#	Insert arr[i] into the hash table.
#Return false

def find_pair(arr, k):
	map = {}
	for i in arr:
		if i is not 0 and (not k % i):
			if map.get(i, None):
				return True
			else:
				map[k/i] = 1
			print map
	return False