# To find the first common ancestor of 2 given nodes
# params: node 1, node 2 and the root node

def findNodeInTree(target, rootNode):
    if not rootNode:
        return False
    if target == rootNode:
        return True
    else:
        return (findNodeInTree(target, rootNode.left)) or (findNodeInTree(target, rootNode.right))

def findFirstCommonAncestor(n1, n2, root):

    #Check if n1 and n2 is on left side of the root node. Can also check on right instead of left
    n1InLeft = findNodeInTree(n1, root.left)
    n2Inleft = findNodeInTree(n2, root.left)

    # For the root node to be the common ancestor, either n1 or n2 has to be on the left subtree
    # But not both nodes on the left sub tree
    if n1InLeft ^ n2Inleft:
        return root

    # In else condition, both the nodes will be on left or right subtree
    else:
        if n1InLeft:
            return findFirstCommonAncestor(n1, n2, root.left)
        else:
            return findFirstCommonAncestor(n1, n2, root.right)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
rootNode = Node(55, node44, node77)

print(findFirstCommonAncestor(node33, node88, rootNode))