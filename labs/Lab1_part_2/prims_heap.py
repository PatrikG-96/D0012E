from graph import*
from heap import*
import collections
import sys
import time


def prims_list(G, vertices, start):

    key = [sys.maxsize] * vertices  # n
    parent = [-1] * vertices        # n
    inHeap = [True] * vertices      # n

    minheap = MinHeap(vertices)     # n
    minheap.insert(0,0)             # insert starting vertex with weight 0, represents initial choice

    # Insert other vertices with a temporary max value as weight
    for i in range(1,vertices):
        minheap.insert(i, sys.maxsize)

    while minheap.size() > 0: # n

        vertex = minheap.extract_min()[0]    # get vertex with minimum weight from heap
        inHeap[vertex] = False               # set this vertex to not be in heap

        node = G.adj_list[vertex]            # get linked list from the graph

        # Loop through all adjacent edges to vertex
        while node!=None:
            # If the vertex is still in heap and it's weight is less than current stored weight for that vertex
            if inHeap[node.vertex] and key[node.vertex] > node.weight:
                key[node.vertex] = node.weight  # update weight
                parent[node.vertex] = vertex    # set the parent of this vertex as vertex from heap
                minheap.decreaseWeight(node.vertex, node.weight)  # decrease weight of this vertex in heap
            node = node.next
    return (parent, key)


def prims_matrix(G, vertices, start):
    key = [sys.maxsize] * vertices
    parent = [-1] * vertices
    inHeap = [True] * vertices

    minheap = MinHeap(vertices)     # n
    minheap.insert(0,0)             # insert starting vertex with weight 0, represents initial choice

    # Insert other vertices with a temporary max value as weight
    for i in range(1,vertices):
        minheap.insert(i, sys.maxsize)

    while minheap.size() > 0:

        vertex = minheap.extract_min()[0]

        inHeap[vertex] = False

        matrix_row = G.adj_matrix[vertex]

        for i in range(vertices):
            weight = matrix_row[i]
            if  weight > 0:
                if inHeap[i] and key[i] > weight:
                    key[i] = weight
                    parent[i] = vertex
                    minheap.decreaseWeight(i, weight)
                    
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

    t = prims_matrix(g, 5, 0)

    print_mst(t[0], t[1])

    g = GraphL(5)
    g.add_edge(0,1,1)
    g.add_edge(0,2,2)
    g.add_edge(0,3,6)
    g.add_edge(0,4,4)
    g.add_edge(4,3,10)
    g.add_edge(3,2,10)
    g.add_edge(2,1,10)
    g.add_edge(1,3,1)

    t = prims_list(g, 5, 0)

    print_mst(t[0], t[1])

if __name__=="__main__":
    main()



            
