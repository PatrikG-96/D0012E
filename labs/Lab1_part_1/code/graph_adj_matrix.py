class EdgeNode:

    def __init__(self, vertex, weigth):
        self.vertex = vertex
        self.weight = weigth
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.adj_matrix = [[0] * vertices] * vertices
        self.vertices = vertices

    def add_edge(self, v1, v2, weight):
        if self.adj_matrix[v1][v2] != 0 or weight < 0:
            return

        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def nodes_connected(self, v1, v2):
        if self.adj_matrix[v1][v2] > 0:
            return True
        return False

g = Graph(10)
g.add_edge(1,2,5)

print(g.nodes_connected(1,2))
