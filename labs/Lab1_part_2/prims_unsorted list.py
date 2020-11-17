from graph import*
import collections

class Edge:

    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.w = w

def prims_l(G, vertices, start):

    lst = []
    added = [False] * vertices
    added[start] = True

    add_neighbours_l(G.adj_list[start], start, lst, added)
    g = GraphL(vertices)
    wsum = 0
    while len(lst) > 0:
        i = find_min(lst)
        e = lst[i]
        lst.remove(e)
        if not added[e.dst]:
            added[e.dst] = True
            g.add_edge(e.src, e.dst, e.w)
            node = G.adj_list[e.dst]
            wsum += e.w
            add_neighbours_l(node, e.dst, lst, added)
            
    print("wsum: ", wsum)
    return g
    


def add_neighbours_l(node, src, lst, added):

    while node!=None:
        if not added[node.vertex]:
            lst.append(Edge(src, node.vertex, node.weight))
        node = node.next


def prims_m(G, vertices, start):
    lst = []
    added = [False] * vertices
    added[start] = True

    add_neighbours_m(G.adj_matrix[start], start, lst, added)
    g = GraphM(vertices)
    wsum = 0
    while len(lst) > 0:
        i = find_min(lst)
        e = lst[i]
        lst.remove(e)
        if not added[e.dst]:
            added[e.dst] = True
            g.add_edge(e.src, e.dst, e.w)
            wsum += e.w
            add_neighbours_m(G.adj_matrix[e.dst], e.dst, lst, added)
    print("wsum: ", wsum)
    return g


def add_neighbours_m(matrix_row, src, lst, added):

    for i in range(0, len(matrix_row)):
        if matrix_row[i] > 0 and not added[i]:
            lst.append(Edge(src, i, matrix_row[i]))
    

def print_list(lst):
    print("[", end="")
    for i in lst:
        if i!=None:
            print(i.w, end= ", ")
    print("]")

def find_min(lst):

    minimum = lst[0].w
    i = 0
    min_index = 0
    while i < len(lst):

        if lst[i].w < minimum:
            minimum = lst[i].w
            min_index = i
        i += 1
    return min_index




def main():

    g = GraphL(5)
    g.add_edge(0,1,2)
    g.add_edge(0,2,3)
    g.add_edge(1,2,4)
    g.add_edge(0,3,1)
    g.add_edge(1,4,7)
    g.add_edge(1,3,8)
    g.add_edge(2,4,5)

    g2 = prims_l(g, g.vertices, 0)

    g3 = GraphM(5)
    g3.add_edge(0,1,2)
    g3.add_edge(0,2,3)
    g3.add_edge(1,2,4)
    g3.add_edge(0,3,1)
    g3.add_edge(1,4,7)
    g3.add_edge(1,3,8)
    g3.add_edge(2,4,5)

    g4 = prims_m(g3, g3.vertices, 0)

if __name__=="__main__":
    main()



            
