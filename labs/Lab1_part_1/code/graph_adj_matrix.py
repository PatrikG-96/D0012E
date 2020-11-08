class EdgeNode:

    def __init__(self, vertex, weigth):
        self.vertex = vertex
        self.weight = weigth
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.vertices = vertices
    

    def add_edge(self, v1, v2, weight):
        v1-=1
        v2-=1
        if self.adj_matrix[v1][v2] != 0 or weight < 0:
            return

        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def set_weight(self, v1, v2, weight):
        v1-=1
        v2-=1
        self.adj_matrix[v1][v2] = weight

    def nodes_connected(self, v1, v2):
        if self.adj_matrix[v1][v2] > 0:
            return True
        return False

    def is_connected(self):

        visited = [False] * self.vertices
        count = 0
        for i in range(self.vertices):

            for j in range(self.vertices):

                if not visited[j] and self.adj_matrix[i][j] > 0:
                    visited[j] = True
                    count+=1
        if count == self.vertices:
            return True
        return False

    def print(self):

        for i in range(self.vertices):
            print(self.adj_matrix[i])

g = Graph(5)
g.add_edge(1,2,5)
g.add_edge(2,3,5)
g.add_edge(3,4,5)
g.add_edge(4,5,5)



print(g.nodes_connected(1,2))
print(g.is_connected())
g.print()
