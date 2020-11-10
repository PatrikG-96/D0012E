import random

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

def generate_graph(vertices, extra_edges, min_weight, max_weight):
    G = Graph(vertices)

    vertex_count = 1
    for i in range(2,vertices+1):
        vertex = random.randint(1, vertex_count)
        weight = random.randint(min_weight, max_weight)
        #print("Creating edge from ", i, " to ", vertex, " with weight ", weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1

    while extra_edges >= 0:
        src_vertex = random.randint(1, vertices)
        dst_vertex = random.randint(1, vertices)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        extra_edges -= 1

    return G


# Connected graph example
g = Graph(5)
g.add_edge(1,2,10)
g.add_edge(2,3,10)
g.add_edge(3,4,10)
g.add_edge(4,5,10)

print("Node 2 and 1 connected? ", g.nodes_connected(2,1))
print("Is g a connected graph? ",g.is_connected())

#Disconnected graph example
g1 = Graph(5)

g1.add_edge(1,2,10)
g1.add_edge(2,3,10)
g1.add_edge(3,4,10)

print("Is g1 a connected graph? ",g1.is_connected())

#Generated connected graph
g2 = generate_graph(1000, 1000, 1, 10)

print("Is g2 a connected graph? ", g2.is_connected())
