from graph import*
from prims_heap import*
from prims_unsorted_list import*
import time
import random

# Creates a graph with a certain amount of vertices and edges, and performs
# prims algorithm a given amount times using a list min heap implementation
# Calculates the average time taken
def time_list_heap(g, iterations):
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY LIST, HEAPS")
    print(iterations, " iterations.")
    print(g.vertices, " vertices.")
    print(g.edges, " edges.")
    print("---------------------------------------------------")
    time_sum = 0
    for i in range(iterations):

        before = time.time() * 1000
        prims_list_h(g, g.vertices, 0)
        after = time.time() * 1000 - before
        time_sum += after
    return time_sum/iterations

def time_list_unsorted(g, iterations):
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY LIST, UNSORTED")
    print(iterations, " iterations.")
    print(g.vertices, " vertices.")
    print(g.edges, " edges.")
    print("---------------------------------------------------")
    time_sum = 0
    for i in range(iterations):

        before = time.time() * 1000
        prims_l_u(g, g.vertices, 0)
        after = time.time() * 1000 - before
        time_sum += after
    return time_sum/iterations


# Testing with increasing amount of vertices and edges, doubling each iteration
def test_ve(v_start, e_start, iterations):
    vertices = v_start
    extra_edges = e_start - vertices

    for i in range(4):
        g = generate_graph_l(vertices, extra_edges, 1, 100)
        res_hl_1 = time_list_heap(g, iterations)
        print("Average time: ", res_hl_1)
        res_ul_1 = time_list_unsorted(g, iterations)
        print("Average time: ", res_ul_1)

        vertices = vertices * 2
        extra_edges = extra_edges * 2
        
# Testing with constant amount of edges and increasing amount of vertices
def test_v(v_start, e, iterations):
    
    vertices = v_start
    extra_edges = e - vertices

    for i in range(4):
        g = generate_graph_l(vertices, extra_edges, 1, 100)
        res_hl_1 = time_list_heap(g, iterations)
        print("Average time: ", res_hl_1)
        res_ul_1 = time_list_unsorted(g, iterations)
        print("Average time: ", res_ul_1)
        vertices = vertices * 2
        extra_edges = e - vertices   

# Testing with constant vertices and increasing edges until max edges
def test_e(vertices, iterations):

    g = generate_graph_l(vertices, 0, 1, 100)
    time_sum = 0
    per_iter = int((g.max_edges - g.edges)/10)
    print("per iter: ", per_iter)
    for i in range(10):
        add_edges_helper(g, per_iter)
        res_h = time_list_heap(g, iterations)
        res_u = time_list_unsorted(g, iterations)
        print("Iteration ", i+1, ": Heap: ", res_h, ", Unsorted list: ", res_u)

# Helper function to add multiple edges to the graph
def add_edges_helper(g, edges):

    for i in range(edges):
        src = random.randint(0,g.vertices-1)
        dst = random.randint(0,g.vertices-1)
        w = random.randint(1,100)
        g.add_edge(src, dst, w)
        
# Testing with full graph, max edges
def full_test(vertices):

    e = vertices * (vertices-1)/2 - vertices
    g = generate_graph_l(vertices, e, 1, 100)
    before = time.time() * 1000
    prims_list_h(g, vertices,0)
    res_h = time.time() * 1000 - before

    before = time.time() * 1000
    prims_l_u(g, vertices, 0)
    res_u = time.time() * 1000 - before

    print("Heap: ", res_h, ", Unsorted list: ", res_u)

def main():

    #test_ve(500, 625, 10)
    #test_v(500, 5000, 10)
    #test_e(500, 10)
    v = 3000
    full_test(v)
    
if __name__=="__main__":
    main()
                              
