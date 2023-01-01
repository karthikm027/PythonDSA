# Single source shortest path problem 
# Dijkstra's algorithm      ( Doesn't work for negative cycles)

# Heap will be used to get the node with lowest distance
import heapq

# Edge: start ----> target     where start and target are vertices/nodes

class Edge:
	def __init__(self, weight, start_vertex, target_vertex):
		self.weight = weight
		self.start_vertex = start_vertex
		self.target_vertex = target_vertex


class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.neighbours = []
		self.min_distance = float("inf")

	def __lt__(self, other):
		return self.min_distance < other.min_distance

	def addEdge(self, weight, destination_vertex):
		edge = Edge(weight, self, destination_vertex)       # Will pass self as start_vertex
		self.neighbours.append(edge)


class Dijkstra:
	def __init__(self):
		self.heap = []

	def calculate(self, start_vertex):
		start_vertex.min_distance = 0
		heapq.heappush(self.heap, start_vertex)
		while self.heap:
			# pop element with lowest distance
			actual_vertex = heapq.heappop(self.heap)
			if actual_vertex.visited:
				continue

			# Consider the neighbours
			for edge in actual_vertex.neighbours:                            # Edge will be like  start -----> target
				start = edge.start_vertex                                    # start and target will be nodes
				target = edge.target_vertex
				new_distance = start.min_distance + edge.weight
				if new_distance < target.min_distance:
					target.min_distance = new_distance
					target.predecessor = start

					# Update the heap 
					heapq.heappush(self.heap, target)
			actual_vertex.visited = True

	def get_shortest_path(self, vertex):
		print(f"The shortest path to the vertex is : {vertex.min_distance}")
		actual_vertex = vertex
		while actual_vertex is not None:                                     # We keep asking who's told you until we find the original node
			print(actual_vertex.name, end=" ")
			actual_vertex = actual_vertex.predecessor  
		print("\n----")

# step 1 - Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# step 2 - add edge
nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(5, nodeH)
nodeC.addEdge(21, nodeG)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

# step 3 - calculate SSSP
algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)
