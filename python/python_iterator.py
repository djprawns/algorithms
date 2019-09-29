class Iter:

	def __init__(self, val):
		self.x = val

	def __iter__(self):
		if self.x:
			self.x = self.x - 1
			yield self.x
		else:
			raise StopIteration

class Test: 
  
    # Cosntructor 
    def __init__(self, limit): 
        self.limit = limit 
  
    # Called when iteration is initialized 
    def __iter__(self): 
        self.x = 10
        return self
  
    # To move to next element. In Python 3, 
    # we should replace next with __next__ 
    def next(self): 
  
        # Store current value ofx 
        x = self.x 
  
        # Stop iteration if limit is reached 
        if x > self.limit: 
            raise StopIteration 
  
        # Else increment and return old value 
        self.x = x + 1; 
        return x