#  1 --> 2 --> 3 --> None
#  |           |
# head        tail

# Nodes are added at the end and removed from first to achive FIFO

class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self):
		self.head = None 
		self.tail = None

	def __iter__(self):
		curNode = self.head
		while curNode:
			yield curNode
			curNode = curNode.next 

class QueueLL:
	def __init__(self):
		self.LinkedList = LinkedList()

	def __str__(self):
		values = [str(x.value) for x in self.LinkedList]
		return ' '.join(values)

	def enqueue(self,value):
		newNode = Node(value)
		if self.LinkedList.head == None :
			self.LinkedList.head = newNode
			self.LinkedList.tail = newNode
		else: 
			self.LinkedList.tail.next = newNode  # current tail.next = newNode
			self.LinkedList.tail = newNode       # newly added node is the new tail

	def isEmpty(self):
		return True if self.LinkedList.head == None else False

	def deque(self):
		if self.isEmpty():
			return "No elements in the queue"
		else:
			tempNode = self.LinkedList.head
			if self.LinkedList.head == self.LinkedList.tail:
				self.LinkedList.head = None 
				self.LinkedList.tail = None 
			else:
				self.LinkedList.head = self.LinkedList.head.next 
			return tempNode

	def peek(self):
		if self.isEmpty():
			return "No elements in the queue"
		else:
			return self.LinkedList.head

	def delete(self):
		self.LinkedList.head, self.LinkedList.tail = None, None


customQueue = QueueLL() 
customQueue.enqueue(1)
customQueue.enqueue(3)
customQueue.enqueue(5)
print(customQueue)
customQueue.deque()
print(customQueue)
print(customQueue.peek())


