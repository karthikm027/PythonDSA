class Graph:
	def __init__(self):
		self.adjacency_list = {}

	# Node of Graph
	def add_vertex(self, vertex):
		if vertex not in self.adjacency_list.keys():
			self.adjacency_list[vertex] = []
			return True
		return False

	def print_graph(self):
		for vertex in self.adjacency_list:
			print(vertex,":", self.adjacency_list[vertex])

	# To add edges between nodes
	def add_edge(self, vertex1, vertex2):
		if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
			self.adjacency_list[vertex1].append(vertex2)
			self.adjacency_list[vertex2].append(vertex1)
			return True
		return False

	# Remove edge. A -- B  The edge has to be removed from both vertices
	def remove_edge(self, vertex1, vertex2):
		if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
			try:
				self.adjacency_list[vertex1].remove(vertex2)
				self.adjacency_list[vertex2].remove(vertex1)
			except valueError:
				pass
			return True
		return False

	# Remove vertex. Need to remove edges between all other nodes. Go to all the vertices present in the edges of the vertex that needs to be deleted
	def remove_vertex(self, vertex):
		if vertex in self.adjacency_list.keys():
			for other_vertex in self.adjacency_list[vertex]:
				self.adjacency_list[other_vertex].remove(vertex)
			del self.adjacency_list[vertex]
			return True
		return False


myGraph = Graph()
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.print_graph()
print("Adding vertex C and edges between A-C and B-C :")
myGraph.add_edge("A","B")
myGraph.add_vertex("C")
myGraph.add_edge("A","C")
myGraph.add_edge("B","C")
myGraph.print_graph()
print("Removing edges between A and C :")
myGraph.remove_edge("A","C")
myGraph.print_graph()
print("Removing vertex C")
myGraph.remove_vertex("C")
myGraph.print_graph()