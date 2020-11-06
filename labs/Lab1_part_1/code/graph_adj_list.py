class EdgeNode:

    def __init__(self, vertex, weight):
        self.weight = weight
        self.vertex = vertex
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * vertices

    def add_edge(self, v1, v2, weight):

        if v1 > self.vertices or v2 > self.vertices or weight < 0:
            return

        node = EdgeNode(v2, weight)
        node.next = self.adj_list[v1-1]
        self.adj_list[v1-1] = node

        node = EdgeNode(v1, weight)
        node.next = self.adj_list[v2-1]
        self.adj_list[v2-1] = node
        

    def nodes_connected(self, v1, v2):
        iterator = self.adj_list[v1-1]
        while iterator!=None:
            if iterator.vertex == v2:
                return True
            iterator = iterator.next


g = Graph(10)

g.add_edge(1,2,10)

print(g.nodes_connected(2,1))
        
