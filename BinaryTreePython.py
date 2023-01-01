# Using linked list with all traversals

from queue import Queue 

class TreeNode:
	def __init__(self,data):
		self.data = data 
		self.leftChild = None
		self.rightChild = None

	def __str__(self, level=0):
		ret = '|' + '--' * level + str (self.data) + '\n'
		for child in self.children:
			ret += child.__str__(level+1)
		return ret 

def preOrderTraversal(rootNode):
	if not rootNode:
		return
	print(rootNode.data, end="-> ")
	preOrderTraversal(rootNode.leftChild)
	preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
	if not rootNode:
		return
	postOrderTraversal(rootNode.leftChild)
	postOrderTraversal(rootNode.rightChild)
	print(rootNode.data, end="-> ")

def inOrderTraversal(rootNode):
	if not rootNode:
		return
	inOrderTraversal(rootNode.leftChild)
	print(rootNode.data, end="-> ") 
	inOrderTraversal(rootNode.rightChild) 

def levelOrderTraversal(rootNode):
	if not rootNode:
		return 
	else:
		customQueue = []
		customQueue.append(rootNode)
		while len(customQueue)>0:
			root = customQueue.pop(0)
			print(root.data, end="->")
			if root.leftChild:
				customQueue.append(root.leftChild)
			if root.rightChild:
				customQueue.append(root.rightChild)



newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftleft = TreeNode("Tea")
leftright = TreeNode("Coffee")
leftChild.leftChild = leftleft
rightChild.rightChild = rightChild
rightleft = TreeNode("Soda")
rightright = TreeNode("Cola")
rightChild.leftChild = rightleft
rightChild.rightChild = rightright
print("preOrderTraversal:")
print(preOrderTraversal(newBT))
print("inOrderTraversal:")
print(inOrderTraversal(newBT))
print("postOrderTraversal:")
print(postOrderTraversal(newBT))
print("levelOrderTraversal:")
print(levelOrderTraversal(newBT))