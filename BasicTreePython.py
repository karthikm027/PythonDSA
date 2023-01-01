# Tree - Non-linear data structure 

#             Drinks 
#             /    \
#           hot    cold

class TreeNode:
	def __init__(self, data, children = []):
		self.data = data
		self.children = children

	def __str__(self, level=0):
		ret = '|' + '--' * level + str (self.data) + '\n'
		for child in self.children:
			ret += child.__str__(level+1)
		return ret 

	def addChild(self, TreeNode):
		self.children.append(TreeNode)


tree = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('tea', [])
coffee = TreeNode('coffee', [])
hot.addChild(tea)
hot.addChild(coffee)
alcoholic = TreeNode('Alcoholic', [])
nonAlcoholic = TreeNode('Non-Alcoholic', [])
cold.addChild(alcoholic)
cold.addChild(nonAlcoholic)
print(tree)