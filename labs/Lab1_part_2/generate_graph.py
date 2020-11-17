from AdjacencyListGraph.py import*

def generate_graph(vertices, extra_edges, min_weight, max_weight):
    G = Graph(vertices)

    vertex_count = 1
    for i in range(2,vertices+1):
        vertex = random.randint(1, vertex_count)
        weight = random.randint(min_weight, max_weight)
        G.add_edge(i, vertex, weight)
        vertex_count += 1

    while extra_edges >= 0:
        src_vertex = random.randint(1, vertices)
        dst_vertex = random.randint(1, vertices)
        if src_vertex == dst_vertex:
            continue
        weight = random.randint(min_weight, max_weight)
        G.add_edge(src_vertex, dst_vertex, weight)
        extra_edges -= 1

    return G

g = generate_graph(100,100,1,5)

print(g.is_connected())
