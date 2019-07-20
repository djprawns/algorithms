# https://www.geeksforgeeks.org/count-ofdifferent-ways-express-n-sum-1-3-4/

def count134(n):
	if n<0:
		return 0
	if n==0:
		return 1
	return count134(n-1) + count134(n-3) + count134(n-4)