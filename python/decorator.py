def decorator(func):
	def inner():
		print("Before execution")
		func()
		print("After execution")
	return inner


# @decorator
def hello():
	print("asdasd")

# hello()

# test = decorator(hello)

# test()