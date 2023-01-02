# Topological sort
# Sorts given actions in such a way that if there is a dependency of one action on another, then the dependent action always comes later than its parent action.

# if a vertex depends on current vertex:
# 		Go to that vertex and then come back to current vertex
# else:
# 		Push current vertex to stack

from collections import defaultdict

class Graph:
	def __init__(self, numberOfVertices):
		self.graph = defaultdict(list)
		self.numberOfVertices = numberOfVertices

	def addEdge(self, vertex, edge):
		self.graph[vertex].append(edge)

	def topologicalSortUtil(self, v, visited, stack):
		visited.append(v)
		for i in self.graph[v]:
			if i not in visited:
				self.topologicalSortUtil(i, visited, stack)
		stack.insert(0,v)

	def topologicalSort(self):
		visited = []
		stack = []

		for k in list(self.graph):
			if k not in visited:
				self.topologicalSortUtil(k, visited, stack)
		print(stack)

myGraph = Graph(8)
myGraph.addEdge("A","C")
myGraph.addEdge("C","E")
myGraph.addEdge("E","H")
myGraph.addEdge("E","F")
myGraph.addEdge("F","G")
myGraph.addEdge("B","D")
myGraph.addEdge("B","C")
myGraph.addEdge("D","F")
myGraph.addEdge("A","C")
myGraph.topologicalSort()

