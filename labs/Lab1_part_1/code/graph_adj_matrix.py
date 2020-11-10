import random
import collections

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

    def is_connected_bfs(self):
        fifo = collections.deque()
        visited = [False] * self.vertices

        fifo.append(0)
        count = 0
        while len(fifo) > 0:
            #print(fifo)
            vertex = fifo.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                count += 1
                for i in range(self.vertices):
                    if self.adj_matrix[vertex][i] > 0:
                        fifo.append(i)

        return count == self.vertices


# Connected graph example
g = Graph(5)
g.add_edge(1,2,10)
g.add_edge(2,3,10)
g.add_edge(3,4,10)
g.add_edge(4,5,10)

print("Node 2 and 1 connected? ", g.nodes_connected(2,1))
print("Is g a connected graph? ",g.is_connected_bfs())

#Disconnected graph example
g1 = Graph(5)

g1.add_edge(1,2,10)
g1.add_edge(2,3,10)
g1.add_edge(3,4,10)

print("Is g1 a connected graph? ",g1.is_connected_bfs())
g1.is_connected_bfs()

g3 = Graph(7)

g3.add_edge(1,2,5)
g3.add_edge(2,3,5)
g3.add_edge(3,1,5)
g3.add_edge(4,5,5)
g3.add_edge(5,6,5)
g3.add_edge(6,4,5)
g3.add_edge(6,7,5)
#g3.add_edge(7,1,5)

print("Is g3 a connected graph? ",g3.is_connected_bfs())