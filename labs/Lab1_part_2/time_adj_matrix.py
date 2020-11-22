from graph import*
from prims_heap import*
from prims_unsorted_list import*
from gen import*
import time


# Creates a graph with a certain amount of vertices and edges, and performs
# prims algorithm a given amount times using a matrix min heap implementation
# Calculates the average time taken
def time_matrix_heap(g, iterations):
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY MATRIX, HEAPS")
    print(iterations, " iterations.")
    print(g.vertices, " vertices.")
    print(g.edges, " edges.")
    print("---------------------------------------------------")
    time_sum = 0
    for i in range(iterations):

        before = time.time() * 1000
        prims_matrix_h(g, g.vertices, 0)
        after = time.time() * 1000 - before
        time_sum += after
    return time_sum/iterations

# Creates a graph with a certain amount of vertices and edges, and performs
# prims algorithm a given amount times using a matrix unsorted list implementation
# Calculates the average time taken
def time_matrix_unsorted(g, iterations):
   
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY MATRIX, USING UNSORTED LISTS")
    print(iterations, " iterations.")
    print(g.vertices, " vertices.")
    print(g.edges, " edges.")
    print("\n---------------------------------------------------")

    time_sum = 0
    for i in range(iterations):

        before = time.time() * 1000
        prims_m_u(g, g.vertices, 0)
        after = time.time() * 1000 - before
        time_sum += after

    return time_sum/iterations

# Testing with increasing amount of vertices and edges, doubling each iteration
def test_ve(v_start, e_start, iterations):

    vertices = v_start
    extra_edges = e_start - vertices

    for i in range(4):
        g = matrix_generateGraph(vertices, extra_edges)
        res_hl_1 = time_matrix_heap(g, iterations)
        print("Average time: ", res_hl_1)
        res_ul_1 = time_matrix_unsorted(g, iterations)
        print("Average time: ", res_ul_1)

        vertices = vertices * 2
        extra_edges = extra_edges * 2
        
# Testing with constant amount of edges and increasing amount of vertices
def test_v(v_start, e, iterations):
    
    vertices = v_start
    extra_edges = e - vertices

    for i in range(4):
        g = matrix_generateGraph(vertices, extra_edges)
        res_hl_1 = time_matrix_heap(g, iterations)
        print("Average time: ", res_hl_1)
        res_ul_1 = time_matrix_unsorted(g, iterations)
        print("Average time: ", res_ul_1)
        vertices = vertices * 2
        extra_edges = e - vertices
        
# Testing with constant vertices and increasing edges until max edges
def test_e(vertices, iterations):

    g = matrix_generateGraph(vertices, 0)
    time_sum = 0
    per_iter = (g.max_edges - g.edges)/10
    print("per iter: ", per_iter)
    for i in range(10):
        add_edges(g, per_iter)
        res_h = time_matrix_heap(g, iterations)
        res_u = time_matrix_unsorted(g, iterations)
        print("Iteration ", i+1, ": Heap: ", res_h, ", Unsorted list: ", res_u)

# Testing with full graph, max edges
def full_test(vertices):

    g = matrix_generateFullGraph(vertices)

    before = time.time() * 1000
    prims_matrix_h(g, vertices,0)
    res_h = time.time() * 1000 - before

    before = time.time() * 1000
    prims_m_u(g, vertices, 0)
    res_u = time.time() * 1000 - before

    print("Heap: ", res_h, ", Unsorted list: ", res_u)
    

def main():

    #test_ve(500, 625, 100)
    #test_v(500, 5000, 100)
    test_e(500,100)

    #v = 5000
    #full_test(v)


    
if __name__=="__main__":
    main()


                              
