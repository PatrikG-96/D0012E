import random 
import collections

class EdgeNode:

    def __init__(self, vertex, weight):
        self.weight = weight
        self.vertex = vertex
        self.next = None

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * vertices
        self.dbg_count = 0
        self.c = 0

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
        

    def is_connected_bfs(self):
        fifo = collections.deque()
        visited = [False] * self.vertices

        fifo.append(0)
        count = 0
        while len(fifo) > 0:
            vertex = fifo.popleft()
            node = self.adj_list[vertex]
            if not visited[vertex]:
                visited[vertex] = True
                count += 1
                while node!=None:
                    fifo.append(node.vertex-1)
                    node = node.next
        
        return count == self.vertices

    
def generate_graph(vertices, edges_excess, min_weight, max_weight):
    G = Graph(vertices)

    vertex_count = 1
    for i in range(2,vertices+1):
        vertex = random.randint(1, vertex_count)
        weight = random.randint(min_weight, max_weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1

    while edges_excess >= 0:
        src_vertex = random.randint(1, vertices)
        dst_vertex = random.randint(1, vertices)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        edges_excess -= 1

    return G


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

#Generated connected graph
g2 = generate_graph(1000, 1000, 1, 10)

print("Is g2 a connected graph? ", g2.is_connected_bfs())


g3 = Graph(7)

g3.add_edge(1,2,0)
g3.add_edge(2,3,0)
g3.add_edge(3,1,0)
g3.add_edge(4,5,0)
g3.add_edge(5,6,0)
g3.add_edge(6,4,0)
g3.add_edge(6,7,0)
#g3.add_edge(7,1,0)

print(g3.is_connected_bfs())