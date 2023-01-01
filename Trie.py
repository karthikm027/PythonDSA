

class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfString = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insertString(self,word):
		current = self.root 
		for i in word:
			ch = i 
			node = current.children.get(ch)
			if node == None:
				node = TrieNode()
				current.children.update({ch:node})
			current = node 
		current.endOfString = True
		print("Successfully inserted")

	def searchString(self, word):
		currentNode = self.root
		for i in word:
			node = currentNode.children.get(i)
			if node == None:
				return False
			currentNode = node 

		return True if currentNode.endOfString == True else False


# Delete method for Trie has to be defined outside the class
# root is the parent node and current node is the children 

def deleteString(root, word, index):
	ch = word[index]
	currentNode = root.children.get(ch)
	canThisNodeBeDeleted = False

	if len(currentNode.children) > 1:
		deleteString(currentNode, word, index + 1)
		return False

	# Our word has exhausted but not the Trie path
	if index == len(word)-1:
		if len(currentNode.children) >= 1:
			currentNode.endOfString = False
			return False
		else:
			root.children.pop(ch)        # Doesn't have any children, so pop from the ROOT node
			return True                  # Deleted successfully

	if currentNode.endOfString:
		deleteString(currentNode, word, index + 1)
		return False

	canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
	if canThisNodeBeDeleted:
		root.children.pop(ch)
		return True
	else:
		return False


newTrie = Trie()
newTrie.insertString("APP")
newTrie.insertString("APPI")
deleteString(newTrie.root, "APP", 0)
print(newTrie.searchString("APP"))