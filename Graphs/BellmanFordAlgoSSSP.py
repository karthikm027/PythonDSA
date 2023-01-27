# Dijkstra algorithm doesn't work for graphs containing negative cycle. 
# All types of graphs can be solved using Bellman Ford Algorithm

# iterates over edges 

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []            # [A,C,6], [A,D,-6]
        self.nodes = []            # [A,B,C,D,E]

    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])

    def addNode(self,value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex : Distance from source")
        for k,v in dist.items():
            print(" "+ k, ": ", v)

    def bellmanFord(self, source):
        dist = {i : float("inf") for i in self.nodes}
        dist[source] = 0

        for _ in range(self.V - 1):
            for s,d,w in self.graph:
                if dist[s] != float("inf") and dist[s]+w < dist[d]:
                    dist[d] = dist[s] + w 

        # V-1 iterations because, to reach any node in a graph, we may atmost traverse through V-1 nodes
        # Vth iteration for checking the negative cycle
        for s,d,w in self.graph:
            if dist[s] != float("inf") and dist[s]+w < dist[d]:
                print("Graph contains negative cycle")
                return
        
        self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.add_edge("A","C",6)
g.add_edge("A","D",6)
g.add_edge("B","A",3)
g.add_edge("C","D",1)
g.add_edge("D","C",2)
g.add_edge("D","B",1)
g.add_edge("E","B",4)
g.add_edge("E","D",2)

g.bellmanFord("E")