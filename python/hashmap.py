class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class HashMap:

	capacity = 10
	load_factor = 0.7

	def __init__(self):
		self.bucket = [None]*10
		self.capacity = HashMap.capacity
		self.items = 0

	@staticmethod
	def hashcode(obj):
		return id(obj)

	def hashkey(self, obj):
		return HashMap.hashcode(obj) % HashMap.capacity

	def put(self, obj):
		key = self.hashkey(obj)
		if(not self.bucket[key]):
			self.bucket[key] = Node(obj)
			return obj
		# collision here
		next = self.bucket[key]
		curr = None
		while next:
			curr = next
			next = next.next
		curr.next = Node(obj)
		return obj

	@classmethod
	def check_if_rehash_required(cls, capacity):
		if(cls.load_factor*capacity):
			return True
		else:
			return False