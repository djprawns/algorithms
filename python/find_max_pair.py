class Tree:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


a = Tree(8)
# a.data = 8
a.left = Tree(4)
a.right = Tree(5)
a.left.left = Tree(6)
a.left.right = Tree(7)
a.left.left.left = Tree(1)
a.right.left = Tree(3)
a.right.right = Tree(4)

# def inOrder(node):
# 	if node is None:
# 		return
# 	inOrder(node.left)
# 	print node.data
# 	inOrder(node.right)

# inOrder(a)


# def find_max_min(root):
# 	if root is None:
# 		return -810923821039812093812, 810923821039812093812
# 	max, min = find_max_min(root.left)
	# return find_max_min(root.next) ? 

def find_max_min(max, min, data):
	if data > max:
		max = data
	if min > data:
		min = data
	# print max, min
	# print "i am best"
	return max, min

def find_max_min2(max, min, max2, min2):
	if max > max2:
		max = max2
	if min > min2:
		min = min2
	return max, min


def findMaxMin(node):	
	if node is None:
		return 0, 810923821039812093812
	max, min = findMaxMin(node.left)
	max, min = find_max_min(max, min, node.data)
	max2, min2 = findMaxMin(node.right)
	max, min = find_max_min2(max, min, max2, min2)
	max, min = find_max_min(max, min, node.data)
	return max, min

print(findMaxMin(a))