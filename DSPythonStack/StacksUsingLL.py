# Implementing stack using linked list. 
# Create a stack and create an object of linked list class

# We update head to the new element that we add and the new nodes head to previous head

class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	#This makes out ll iterable
	def __iter__(self):
		curNode = self.head
		while curNode:
			yield curNode
			curNode = curNode.next

class Stack:
	def __init__(self):
		self.LinkedList = LinkedList()

	def __str__(self):
		values = [str(x.value) for x in self.LinkedList]
		return '\n'.join(values)

	def isEmpty(self):
		if self.LinkedList.head == None:
			return True
		else:
			return False

	def push(self, value):
		node = Node(value)
		node.next = self.LinkedList.head       #node.next = current head
		self.LinkedList.head = node 
		print("pushed an element")

	def pop(self):
		if self.LinkedList.head == None:
			return "No elements to pop"
		else:
			res = self.LinkedList.head
			self.LinkedList.head = self.LinkedList.head.next
			self.LinkedList.head = None
			return res 

	def peek(self):
		if self.isEmpty():
			return "Empty stack in peek"
		else:
			nodeValue = self.LinkedList.head.value 
			return nodeValue

	def delete(self):
		self.LinkedList.head = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
