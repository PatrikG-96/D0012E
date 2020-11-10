import random 

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

    #O(1)
    def add_edge(self, v1, v2, weight):

        if v1 > self.vertices or v2 > self.vertices or weight < 0:
            return

        node = EdgeNode(v2, weight)
        node.next = self.adj_list[v1-1]
        self.adj_list[v1-1] = node
    # O(V)
    def nodes_connected(self, v1, v2):
        iterator = self.adj_list[v1-1]
        while iterator!=None:
            if iterator.vertex == v2:
                return True
            iterator = iterator.next
        iterator = self.adj_list[v2-1]
        while iterator!=None:
            if iterator.vertex == v1:
                return True
            iterator = iterator.next
        return False
    # O(V) 
    def set_weight(self, v1, v2, weight):

        node = self.adj_list[v1-1]

        while node!=None:

            if node.vertex == v2:
                node.weight = weight
                return
            node = node.next
    
    def dfs(self, vertex, visited, counter):
        
        print("DFS for vertex ", vertex)

        visited[vertex] = True

        node = self.adj_list[vertex]

        while node!=None:
            if not visited[node.vertex-1]:
                counter+=1
                return self.dfs(node.vertex, visited, counter)
            node = node.next

        return counter == self.vertices
        

    def is_connected_rec(self):
        
        visited = [False] * self.vertices

        return self.dfs(0, visited, 0)
        
    # O(V+E)
    def is_connected(self):

        visited = [False] * self.vertices
        
        count = 0
        counter = 0
        for i in range(0, self.vertices):

            counter += 1
            node = self.adj_list[i]
            
            while node!=None:
                vertex = node.vertex
                if not visited[vertex-1]:
                    visited[vertex-1]=True
                    count += 1
                node = node.next
                counter += 1

        print("Iterations: ", counter)
        print("Count=", count)
        if count+1 == self.vertices:
            return True
        return False

def generate_graph(vertices, edges_excess, min_weight, max_weight):
    G = Graph(vertices)

    vertex_count = 1
    for i in range(2,vertices+1):
        vertex = random.randint(1, vertex_count)
        weight = random.randint(min_weight, max_weight)
        #print("Creating edge from ", i, " to ", vertex, " with weight ", weight)
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


g = Graph(5)

g.add_edge(1,2,10)
g.add_edge(2,3,10)
g.add_edge(3,4,10)
g.add_edge(4,5,10)

#print(g.nodes_connected(2,1))

#print(g.is_connected())
        
g2 = generate_graph(1000, 1000, 1, 10)

print(g.is_connected_rec())
print(g2.is_connected())
print(g.is_connected())