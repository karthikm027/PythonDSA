# Queue is a FIFO data structure 
# Can be implemented using both list or LL

# Using list, creating a circular queue
class Queue:
	def __init__(self,maxSize):
		self.items = maxSize*[None]
		self.maxSize = maxSize
		self.start = -1
		self.top = -1

	def __str__(self):
		values = [str(x) for x in self.items]
		return ' '.join(values)

	def isFull(self):
		if self.top + 1 == self.start:
			return True
		elif self.start == 0 and self.top == self.maxSize:
			return True
		else:
			return False

	def isEmpty(self):
		return True if self.top == -1 else False

	def enqueue(self, value):
		if self.isFull():
			return "The queue is full"
		else:
			if self.top + 1 == self.maxSize:
				self.top = 0
			else:
				self.top += 1
				if self.start == -1:
					self.start = 0
		self.items[self.top] = value 
		return "The element is inserted to the queue"

	def dequeue(self):
		if self.isEmpty():
			return "No elements in the queue"
		else:
			firstElement = self.items[self.start]
			start = self.start 
			# has only one element
			if self.start == self.top:
				self.start, self.top = -1, -1
			elif self.start + 1 == self.maxSize:    # already at the last
				self.start = 0
			else:
				self.start += 1 
			self.items[start] = None

	def peek(self):
		if self.isEmpty():
			return "No elements in the queue"
		else:
			return self.items[self.start]

	def delete(self):
		self.items = self.maxSize*[None]
		self.start = -1
		self.top = -1




customQ = Queue(6)
print(customQ.isFull())
customQ.enqueue(1)
customQ.enqueue(2)
customQ.enqueue(3)
customQ.enqueue(4)
customQ.enqueue(5)
customQ.enqueue(6)
customQ.enqueue(7)
#customQ.dequeue()
print(customQ.peek())
print(customQ)