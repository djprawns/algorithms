rows = 5
cols = 5
arr = [[0]*cols]*rows

# for i in range(rows):
# 	for j in range(cols):
# 		print arr[i][j]


def count_ways(row, col):
	if row is rows and col is cols:
		return 1
	if row is rows:
		return 0
	if col is cols:
		return 0
	if row is not rows:
		a = count_ways(row+1, col)
	if col is not cols:
		b = count_ways(row, col+1)