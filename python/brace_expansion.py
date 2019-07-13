braces = "{a,b{c,d}}f{c,d}"

"{a, bc, bd} f {c, d}"

braces = "{a, b{c, d}}"

class Node:

	def __init__(self):
		self.data = None
		self.left = None
		self.right = None


# create a new opening bracket is encountered, create new level
#                      ,
#					/	 \
#
#
#
#
#


def recurse_string(string, length, index):
	if(index == length):
		return
	for index, element in enumerate(string):
		if (i == '{'):
			
			# string + 
			# string = run_func(recurse_string, (string[index:], length, index))

def run_func(func, args):
	func(*args)

def solve_expression():
	pass