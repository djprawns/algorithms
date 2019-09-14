class LinkedList:

	def __init__(self, data):
		self.data = data
		self.next = None



head = LinkedList(20)

head.next = LinkedList(30)

head.next.next = LinkedList(40)

head.next.next.next = LinkedList(50)

head.next.next.next.next = LinkedList(60)


def iterate_over_linked_list(head):
	i = 1
	temp = head
	while temp:
		print "Node #"+str(i)+" is "+str(temp.data)
		temp = temp.next
		i += 1


def reverse_list(head):
	if head.next is None:
		return head, head
	temp, curr = reverse_list(head.next)
	temp.next = head
	return head, curr