import threading
from collections import OrderedDict
	
# def synchronized(func):

# 	func.__lock__ = threading.Lock()

# 	def synced_func(*args, **kws):
# 		with func.__lock__:
# 			return func(*args, **kws)

# 	return synced_func


class SetHandler:

	sets = []

	# @synchronized
	def add(self, set_id=None, key=0, score=-1):
		if key == 0:
			return "Must be positive integer"
		set_id, status = self.find_set(set_id)
		if status:
			diction = {key:score}
			# if()
			# if find_dict(set_id, key):
			# 	status = False
			# 	for i in SetHandler.sets[set_id]:
			# 		if key in i.keys():
			# 			status = True
			# 			break
			# # if SetHandler.sets[set_id]
			SetHandler.sets[set_id].append(diction)
			return set_id
		else:
			diction = {key:score}
			SetHandler.sets.append([diction])
			return len(SetHandler.sets[-1]) - 1

	def find_dict(self, set_id, key):
		return any(key in d for d in SetHandler.sets[set_id])


	# def remove_key(self, set_id, key):
	# 	set_id = self.find_set(set_id):
	# 	if set_id:
	# 		SetHandler.sets


	def find_set(self, set_id):
		if set_id is None:
			return False, False
		if set_id <= len(SetHandler.sets)-1:
			return set_id, True
		else:
			return False, False