from graph import*
from heap import*
import collections
import sys

class Edge:

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst



def prims_list(G, vertices, start):

    key = [sys.maxsize] * vertices
    parent = [-1] * vertices
    pq = PriorityQueue(vertices * (vertices-1))
    inMST = [False] * vertices

    pq.push(start, 0)

    while pq.size() > 0:
        vertex = pq.pop()[0]

        inMST[vertex] = True

        node = G.adj_list[vertex]

        while node!=None:
        
            if not inMST[node.vertex] and key[node.vertex] > node.weight:
                key[node.vertex] = node.weight
                pq.push(node.vertex, node.weight)
                parent[node.vertex] = vertex
            node = node.next
    #print_mst(parent, key)
    return (parent, key)


def prims_matrix(G, vertices, start):
    key = [sys.maxsize] * vertices
    parent = [-1] * vertices
    pq = PriorityQueue(vertices * (vertices-1))
    inMST = [False] * vertices

    pq.push(start, 0)

    while pq.size() > 0:

        vertex = pq.pop()[0]

        inMST[vertex] = True

        matrix_row = G.adj_matrix[vertex]

        for i in range(vertices):
            weight = matrix_row[i]
            if  weight > 0:
                if not inMST[i] and key[i] > weight:
                    key[i] = weight
                    pq.push(i, weight)
                    parent[i] = vertex
                    
    #print_mst(parent, key)
    return (parent, key)

def print_mst(parent, key):

    for i in range(1, len(parent)):
        print("Edge from ", parent[i], " to ", i, " with weight ", key[i])

    print("Total of ", (len(parent)-1), " edges")




def main():
    g = GraphM(5)
    g.add_edge(0,1,2)
    g.add_edge(0,2,3)
    g.add_edge(1,2,4)
    g.add_edge(0,3,1)
    g.add_edge(1,4,7)
    g.add_edge(1,3,8)
    g.add_edge(2,4,5)

    prims_matrix(g, 5, 0)

    g = GraphL(5)
    g.add_edge(0,1,1)
    g.add_edge(0,2,2)
    g.add_edge(0,3,3)
    g.add_edge(0,4,4)
    g.add_edge(4,3,10)
    g.add_edge(3,2,10)
    g.add_edge(2,1,10)

    prims_list(g, 5, 0)

    g = generate_graph_l(500, 200, 1, 100)

    t = prims_list(g, g.vertices, 0)
    print_mst(t[0], t[1])

if __name__=="__main__":
    main()



            
