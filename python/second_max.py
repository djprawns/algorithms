import unittest

def if_number_negative(number):
	status = False
	if number[0] == '-':
		status = True
	return status

def find_greater_by_character(number1, number2, sign):
	greater = number1
	smaller = number2
	i = 0
	length = len(number1)
	while i != length:
		if sign is "positive":
			if number2[i] < number1[i]:
				greater = number2
				smaller = number1
				break
		else:
			if number2[i] > number1[i]:
				greater = number2
				smaller = number1
				break
		i+=1
	return greater, smaller

def find_greater(number1, number2):
	greater = number1
	smaller = number2
	if if_number_negative(number1) and if_number_negative(number2):
		# if both numbers are negative
		if len(number1) == len(number2): 
			greater, smaller = find_greater_by_character(number1, number2, "positive")
		elif len(number1) > len(number2):
			greater = number2
			smaller = number1
		else:
			pass
	elif not if_number_negative(number1) and not if_number_negative(number2):
		# both numbers positive
		if len(number1) == len(number2):
			greater, smaller = find_greater_by_character(number1, number2, "negative")
		elif len(number1) > len(number2):
			pass
		else:
			greater = number2
			smaller = number1
	elif if_number_negative(number1):
		# if number 1 negative
		greater = number2
		smaller = number1
	else:
		pass
		# number 2 negative
	return greater, smaller

def find_max(list):
	min_int = '-'+'9'*1024
	max = second_max = min_int
	if not list:
		return '-1'
	for number in list:
		max, smaller = find_greater(max, number)
		if smaller != max:
			second_max, smaller = find_greater(second_max, smaller)
	if min_int == second_max:
		second_max = '-1'
	return second_max

# ALTHOUGH WE COULD HAVE JUST DONE INT() OVER THE STRING TO MAKE IT NUMERIC, 
# I DID NOT WANT TO INCREASE THE OVERHEAD WHEN IT CAN BE DONE THROUGH STRINGS ITSELF.
# ALSO SINCE LEN() IS O(1) ONCE THE  MEMORY HAS BEEN ALLOCATED FOR THE STRING / NUMBER,
# WE COULD JUST ITERATE OVER THE STRING AND DETERMINE THE LARGER NUMBER.
# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY - O(1)

# PFB TEST CASES FOR THE ALGORITHM
  
class TestSecondMaxMethods(unittest.TestCase): 

	def setUp(self): 
	    pass

	def test_1(self):
		self.assertEqual(find_max(["3", "-2"]), '-2')

	def test_2(self):
		self.assertEqual(find_max(["5", "5", "4", "2"]), '4')

	def test_3(self):
		self.assertEqual(find_max(["4", "4", "4"]), '-1')

	def test_4(self):
		self.assertEqual(find_max([]), '-1')

if __name__ == '__main__': 
	unittest.main() 
