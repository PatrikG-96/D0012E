from graph import*
from heap import*
import collections

class Edge:

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

def prims_l(G, vertices, start):

    pq = PriorityQueue(vertices)

    added = [False] * vertices
    added[start] = True
    
    add_neighbours_l(G.adj_list[start], start, pq, added)
    g = GraphL(vertices)
    wsum = 0

    while pq.size() > 0:
        e = pq.pop()
        edge = e[0]
        weight = e[1]
        if not added[edge.dst]:
            added[edge.dst] = True
            g.add_edge(edge.src, edge.dst, weight)
            wsum += weight
            node = G.adj_list[edge.dst]
            add_neighbours_l(node, edge.dst, pq, added)
    print("Wsum: ", wsum)
    return g

def add_neighbours_l(node, src, pq, added):

    while node!=None:
        if not added[node.vertex]:
            pq.push(Edge(src, node.vertex), node.weight)
        node = node.next


def prims_m(G, vertices, start):

    pq = PriorityQueue(vertices)
    added = [False] * vertices
    added[start] = True

    add_neighbours_m(G, start, pq, added)
    g = GraphM(vertices)
    wsum = 0
    while pq.size() > 0:
        e = pq.pop()
        edge = e[0]
        weight = e[1]
        if not added[edge.dst]:
            added[edge.dst] = True
            wsum+=weight
            g.add_edge(edge.src, edge.dst, weight)
            add_neighbours_m(G, edge.dst, pq, added)
    print("wsum = ", wsum)
    return g


def add_neighbours_m(G, src, pq, added):

    matrix = G.adj_matrix

    for i in range(G.vertices):
        if not added[i] and matrix[src][i] > 0:
            pq.push(Edge(src, i), matrix[src][i])

    

def main():
    g = GraphM(5)
    g.add_edge(0,1,2)
    g.add_edge(0,2,3)
    g.add_edge(1,2,4)
    g.add_edge(0,3,1)
    g.add_edge(1,4,7)
    g.add_edge(1,3,8)
    g.add_edge(2,4,5)

    g2 = prims_m(g, g.vertices, 0)

    g3 = generate_graph_l(1000,200,1,100)

    g4 = prims_l(g3, 1000, 0)
    
    #g2.traverse()

if __name__=="__main__":
    main()



            
