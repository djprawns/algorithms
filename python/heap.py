# MIN HEAP

class MinHeap:

	def __init__(self):
		self.array = []
		self.index = 0

	def add(self, data):
		self.array.append(data)
		self.bubble_up(self.array, self.index)
		self.index += 1

	def bubble_up(self, array, index):
		parent = (index-1)/2
		# since this is root
		if parent < 0:
			return
		else:
			if self.array[index] < self.array[parent]:
				MinHeap.swap(array, index, parent)
				index = parent
				self.bubble_up(self.array, index)

	def get(self):
		MinHeap.swap(self.array, 0, self.index-1)
		largest = self.array.pop(self.index-1)
		self.bubble_down(self.array, 0)
		self.index -= 1
		return largest

	def bubble_down(self, array, index):
		left = 2*index+1
		right = 2*index+2
		swap_index = None
		if right > len(array) and array[index] > array[right]:
			swap_index = right
		if left > len(array) and array[index] > array[left]:
			swap_index = left
		if swap_index:
			MinHeap.swap(array, index, swap_index)
			self.bubble_down(self.array, swap_index)

	@staticmethod
	def swap(array, a, b):
		array[a], array[b] = array[b], array[a]



# MAX_HEAP

class MaxHeap:

	def __init__(self):
		self.array = []
		self.index = 0

	def add(self, data):
		self.array.append(data)
		self.bubble_up(self.array, self.index)
		self.index += 1

	def bubble_up(self, array, index):
		parent = (index-1)/2
		# since this is root
		if parent < 0:
			return
		else:
			if self.array[index] > self.array[parent]:
				MaxHeap.swap(array, index, parent)
				index = parent
				self.bubble_up(self.array, index)

	def get(self):
		MaxHeap.swap(self.array, 0, self.index-1)
		largest = self.array.pop(self.index-1)
		self.bubble_down(self.array, 0)
		self.index -= 1
		return largest

	def bubble_down(self, array, index):
		left = 2*index+1
		right = 2*index+2
		swap_index = None
		if right < len(array) and array[index] < array[right]:
			swap_index = right
		if left < len(array) and array[index] < array[left]:
			swap_index = left
		if swap_index:
			MaxHeap.swap(array, index, swap_index)
			self.bubble_down(self.array, swap_index)

	@staticmethod
	def swap(array, a, b):
		array[a], array[b] = array[b], array[a]


a = MaxHeap()
a.add(1)
a.add(6)
a.add(8)
a.add(3)
a.add(9)
a.add(2)
a.add(1)
a.add(1)
a.add(1)

