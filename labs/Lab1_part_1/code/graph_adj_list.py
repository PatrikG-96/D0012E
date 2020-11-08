class EdgeNode:

    def __init__(self, vertex, weight):
        self.weight = weight
        self.vertex = vertex
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * vertices

    #O(1)
    def add_edge(self, v1, v2, weight):

        if v1 > self.vertices or v2 > self.vertices or weight < 0:
            return

        node = EdgeNode(v2, weight)
        node.next = self.adj_list[v1-1]
        self.adj_list[v1-1] = node

        node = EdgeNode(v1, weight)
        node.next = self.adj_list[v2-1]
        self.adj_list[v2-1] = node
        
    # O(V)
    def nodes_connected(self, v1, v2):
        iterator = self.adj_list[v1-1]
        while iterator!=None:
            if iterator.vertex == v2:
                return True
            iterator = iterator.next

    # O(V) 
    def set_weight(self, v1, v2, weight):

        node = self.adj_list[v1-1]

        while node!=None:

            if node.vertex == v2:
                node.weight = weight
                return
            node = node.next
        
        
    # O(V+E)
    def is_connected(self):

        visited = [False] * self.vertices
        
        count = 0

        for i in range(0, self.vertices):

            node = self.adj_list[i]
            
            while node!=None:
                vertex = node.vertex
                if not visited[vertex-1]:
                    print("Visiting vertex: ", vertex)
                    visited[vertex-1]=True
                    count += 1
                node = node.next

        if count == self.vertices:
            return True
        return False

g = Graph(5)

g.add_edge(1,2,10)
g.add_edge(2,3,10)
g.add_edge(3,4,10)
#g.add_edge(4,5,10)

print(g.nodes_connected(2,1))

print(g.is_connected())
        
