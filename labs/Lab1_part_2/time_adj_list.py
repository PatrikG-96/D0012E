from graph import*
from prims_heap import*
from prims_unsorted_list import*
import time

def time_list_heap(iterations, vertices, extra_edges, p=False):
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY LIST, HEAPS")
    print(iterations, " iterations.")
    print(vertices, " vertices.")
    print(vertices+extra_edges, " edges.")
    print("---------------------------------------------------")
    time_sum = 0
    for i in range(iterations):

        g = generate_graph_l(vertices, extra_edges, 0, 10)
        before = time.time() * 1000
        prims_list_h(g, vertices, 0)
        after = time.time() * 1000 - before
        if p:
            print("Iteration ", i+1, " took ", after, " milliseconds.")
        else:
            print(".", end="")
        time_sum += after
    print("\n---------------------------------------------------")
    return time_sum/iterations

def time_list_unsorted(iterations, vertices, extra_edges, p=False):
    time_sum = 0
    print("---------------------------------------------------")
    print("PRIMS ALGORITHM ADJACENCY LIST, USING UNSORTED LISTS")
    print(iterations, " iterations.")
    print(vertices, " vertices.")
    print(vertices+extra_edges, " edges.")
    print("\n---------------------------------------------------")
    for i in range(iterations):

        g = generate_graph_l(vertices, extra_edges, 0, 10)
        before = time.time() * 1000
        prims_l_u(g, vertices, 0)
        after = time.time() * 1000 - before
        if p:
            print("Iteration ", i+1, " took ", after, " milliseconds.")
        else:
            print(".", end="")
        time_sum += after
    print("\n---------------------------------------------------")
    return time_sum/iterations


vertices = 200
extra_edges = 50
res_hl_1 = time_list_heap(10, vertices, extra_edges)
print("Average time: ", res_hl_1)
res_ul_1 = time_list_unsorted(10, vertices, extra_edges)
print("Average time: ", res_ul_1)
vertices = 2000
extra_edges = 50
res_hl_2 = time_list_heap(10, vertices, extra_edges)
print("Average time: ", res_hl_2)
res_ul_2 = time_list_unsorted(10, vertices, extra_edges)
print("Average time: ", res_ul_2)
print("\n---------------------------------------------------")
print("Increase from previous benchmark: ")
print("Heap: ", res_hl_2/res_hl_1 * 100, "%")
print("Unsorted: ", res_ul_2/res_ul_1 * 100, "%")
print("\n---------------------------------------------------")                                          
vertices = 2000
extra_edges = 1000
res_hl_3 = time_list_heap(10, vertices, extra_edges)
print("Average time: ", res_hl_3)
res_ul_3 = time_list_unsorted(10, vertices, extra_edges)
print("Average time: ", res_ul_3)
print("\n---------------------------------------------------")
print("Increase from previous benchmark: ")
print("Heap: ", res_hl_3/res_hl_2 * 100, "%")
print("Unsorted: ", res_ul_3/res_ul_2 * 100, "%")
print("\n---------------------------------------------------")        

vertices = 60
extra_edges = vertices * (vertices - 1) - vertices
res_hl_4 = time_list_heap(10, vertices, extra_edges)
print("Average time: ", res_hl_4)
res_ul_4 = time_list_unsorted(10, vertices, extra_edges)
print("Average time: ", res_ul_4)


                              
