import random 
import collections

class EdgeNode:

    def __init__(self, vertex, weight):
        self.weight = weight
        self.vertex = vertex
        self.next = None

class GraphL:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [None] * vertices
        self.edges = 0
        self.max_edges = vertices * (vertices-1) / 2

    def add_edge(self, v1, v2, weight):

        if v1 > self.vertices or v2 > self.vertices or weight < 0:
            return

        node = EdgeNode(v2, weight)
        node.next = self.adj_list[v1]
        self.adj_list[v1] = node

        node = EdgeNode(v1, weight)
        node.next = self.adj_list[v2]
        self.adj_list[v2] = node
        self.edges += 1

    def nodes_connected(self, v1, v2):
        iterator = self.adj_list[v1]
        while iterator!=None:
            if iterator.vertex == v2:
                return True
            iterator = iterator.next

    def set_weight(self, v1, v2, weight):

        node = self.adj_list[v1]

        while node!=None:

            if node.vertex == v2:
                node.weight = weight
                return
            node = node.next

    def traverse(self):
        fifo = collections.deque()
        visited = [False] * self.vertices

        fifo.append(0)
        while len(fifo) > 0:
            vertex = fifo.popleft()
            node = self.adj_list[vertex]
            if not visited[vertex]:
                print("Visiting node ", vertex)
                visited[vertex] = True
                while node!=None:
                    fifo.append(node.vertex)
                    node = node.next

    def is_connected(self):
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
                    fifo.append(node.vertex)
                    node = node.next
        
        return count == self.vertices


class GraphM:

    def __init__(self, vertices):
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.vertices = vertices
        self.edges = 0
        self.max_edges = vertices * (vertices-1) / 2
    

    def add_edge(self, v1, v2, weight):
        if self.adj_matrix[v1][v2] != 0 or weight < 0:
            return

        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight
        self.edges += 1

    def set_weight(self, v1, v2, weight):
        self.adj_matrix[v1][v2] = weight

    def nodes_connected(self, v1, v2):
        if self.adj_matrix[v1][v2] > 0:
            return True
        return False

    def is_connected(self):
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



