class Node():

	def __init__(self, data):
		self.data = data
		self.next = None


class HashMap():

	capacity = 10
	load_factor = 0.7

	def __init__(self):
		self.bucket = [None]*10
		self.capacity = capacity
		self.items = 0

	def put(self, obj):
		key = hashkey(obj)
		if(!self.bucket[key]):
			self.bucket[key] = Node(obj)
			return obj
		next = self.bucket[key]
		curr = None
		while next:
			curr = next
			next = next.next
		curr.next = Node(obj)
		return obj

	def hashkey(self, obj):
		return self.hashcode(obj) % HashMap.capacity

	def hashcode(obj):
		return id(obj)

	@classmethod
	def check_if_rehash_required(cls, capacity):
		if(cls.load_factor*capacity)