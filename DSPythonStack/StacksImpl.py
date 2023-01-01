#Stack is linear data structure based LIFO

# Create stack 
# Push
# Pop
# Peek
# isEmpty
# isFull
# deleteStack

# Implementation: Python list with size limit, Python list without size limit, Using linked list'
# Using LL is optimal, but difficult to implement

class Stack:
	def __init__(self):
		self.list = []

	def __str__(self):
		values = reversed(self.list)
		values = [str(x) for x in values]
		return '\n'.join(values)

	# isEmpty
	def isEmpty(self):
		return True if self.list == [] else False

	# push
	def push(self,val):
		self.list.append(val)
		return "Element added successfully"

	# pop
	def pop(self):
		if self.isEmpty():
			return "There are no elements in the stack"
		else:
			return self.list.pop()

	def peep(self):
		if self.isEmpty():
			return "There are no elements in the stack"
		else:
			return self.list[len(self.list)-1]

	def deleteStack(self):
		self.list = None


myStack = Stack()
print(myStack.isEmpty())
print(myStack.push(8))
print(myStack.push(9))
print(myStack.push(6))
print(myStack)
print(myStack.peep())
			

#For stack using python list with size limit just include self.maxSize = maxSize in __init__