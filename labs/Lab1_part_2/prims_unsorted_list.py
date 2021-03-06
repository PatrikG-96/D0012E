from graph import*
import collections
import sys

def find_min(keys, picked):

    minimum = sys.maxsize
    min_index = 0
    for i in range(len(keys)):

        if keys[i] < minimum and not picked[i]:
            minimum = keys[i]
            min_index = i
    return min_index
        

def prims_l_u(G, vertices, start):

    weight = [sys.maxsize] * vertices  # n
    parent = [-1] * vertices
    inMST = [False] * vertices #n
    weight[0] = 0

    for i in range(vertices):
   
        vertex = find_min(weight, inMST)

        inMST[vertex] = True
        node = G.adj_list[vertex]

        while node!=None:
            if not inMST[node.vertex] and weight[node.vertex] > node.weight:
                weight[node.vertex] = node.weight
                parent[node.vertex] = vertex
            node = node.next

    return (parent, weight)
    

def prims_m_u(G, vertices, start):
    weight = [sys.maxsize] * vertices  # n
    parent = [-1] * vertices
    inMST = [False] * vertices #n
    weight[0] = 0

    for i in range(vertices):
   
        vertex = find_min(weight, inMST)

        inMST[vertex] = True
        matrix_row = G.adj_matrix[vertex]

        for i in range(vertices):
            v_weight = matrix_row[i]
            if  v_weight > 0:
                if not inMST[i] and weight[i] > v_weight:
                    weight[i] = v_weight
                    parent[i] = vertex
               
    return (parent, weight)



def print_mst(parent, key):

    for i in range(1, len(parent)):
        print("Edge from ", parent[i], " to ", i, " with weight ", key[i])

    print("Total of ", (len(parent)-1), " edges")





def main():

    g = GraphL(5)
    g.add_edge(0,1,2)
    g.add_edge(0,2,3)
    g.add_edge(1,2,4)
    g.add_edge(0,3,1)
    g.add_edge(1,4,7)
    g.add_edge(1,3,8)
    g.add_edge(2,4,5)

    g2 = prims_l_u(g, g.vertices, 0)

    print_mst(g2[0], g2[1])

    g3 = GraphM(5)
    g3.add_edge(0,1,10)
    g3.add_edge(0,2,3)
    g3.add_edge(1,2,4)
    g3.add_edge(0,3,1)
    g3.add_edge(1,4,7)
    g3.add_edge(1,3,8)
    g3.add_edge(2,4,5)

    g4 = prims_m_u(g3, g3.vertices, 0)

    print_mst(g4[0], g4[1])

if __name__=="__main__":
    main()



            
