class AdjNode:
	def __init__(self, x):
		self.vertex = x
		self.link = None



class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	
	def edge(self, source, destination):
		
		node = AdjNode(destination)
		node.link = self.graph[source]
		self.graph[source] = node

		node = AdjNode(source)
		node.link = self.graph[destination]
		self.graph[destination] = node

	
	def display_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.link
			print(" \n")



if __name__ == "__main__":
	V = 5
	graph = Graph(V)
	graph.edge(0, 1)
	graph.edge(0, 4)
	graph.edge(1, 2)
	graph.edge(1, 3)
	graph.edge(1, 4)
	graph.edge(2, 3)
	graph.edge(3, 4)

	graph.display_graph()
