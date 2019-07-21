# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

def find_subset(list, index, number, avoid_list):
	number -= list[index]
	if number == 0:
		return [index]
	if number < 0:
		return
	for ind, i in enumerate(list):
		if ind not in avoid_list:
			a = find_subset(list, ind, number, avoid_list+[ind])
			if a:
				return [index] + a


def main(list, number):
	for index, i in enumerate(list):
		result = find_subset(list, index, number, [index])
		if result:
			for j in result:
				print list[j]