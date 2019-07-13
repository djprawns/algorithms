class Node():

	def __init__(self):
		self.data = None
		self.next = None
		self.prev = None

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev