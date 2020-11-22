from graph import *
from prims_heap import*
import random
import time

# Generate a full graph using adjacency matrix. Weights are pseudo random
def matrix_generateFullGraph(vertices):

    graph = GraphM(vertices)

    for i in range(vertices):

        for j in range(i, vertices):

            if i!=j:
                w = random.randint(1,100)
                graph.adj_matrix[i][j] = w
                graph.adj_matrix[j][i] = w

    return graph


# Generate a connected graph with a specified amount of edges beyond the requiered V-1
# Used for testing purposes, will only generate the same type of graph every time
def matrix_generateGraph(vertices,edges):

    graph = GraphM(vertices)

    for i in range(vertices):
        w = random.randint(1,100)
        if i < vertices-1:

            graph.add_edge(i, i+1, w)

        else:

            graph.add_edge(i, 0, w)
    if edges > 0:
        add_edges(graph, edges)

    return graph

def add_edges(graph, edges):
    vertices = graph.vertices
    for i in range(vertices):

        for j in range(i, vertices):

            if edges == 0:
                break
            if i!=j and graph.adj_matrix[i][j]==0:
                w = random.randint(1,100)
                graph.add_edge(i,j,w)
                edges-=1
                
# Generates an adjacency list graph for testing purposes. Can contain duplicate edges
# but this does not matter when testing performance
def generate_graph_l(vertices, extra_edges, min_weight, max_weight):
    G = GraphL(vertices)
    vertex_count = 0
    for i in range(1,vertices):
        vertex = random.randint(0, vertex_count)
        weight = random.randint(min_weight, max_weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1
    while extra_edges >= 0:
        src_vertex = random.randint(0, vertices-1)
        dst_vertex = random.randint(0, vertices-1)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        extra_edges -= 1

    return G

# Scuffed old version of generating matrix graphs, still here for reference
# Problem is that duplicates do not work for testing purposes in a matrix
# representation
def generate_graph_m(vertices, extra_edges, min_weight, max_weight):
    G = GraphM(vertices)
    vertex_count = 0
    for i in range(1,vertices):
        vertex = random.randint(0, vertex_count)
        weight = random.randint(min_weight, max_weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1
    while extra_edges >= 0:
        src_vertex = random.randint(0, vertices-1)
        dst_vertex = random.randint(0, vertices-1)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        extra_edges -= 1

    return G


