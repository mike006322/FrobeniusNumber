from NijenhuisAlgorithm.dijkstra import *


def nijenhuis(*generators):
    """
    input integers
    output Frobenius Number, i.e. the largest number not a linear combination of inputs
    """
    # 1. Create the Nijenhuis graph.

    def make_nijenhuis_graph(generators):
        """
        output is in form {node1: {node2: distance, node3: distance, ... }, ...}
        """
        g = {}
        m = min(generators)
        for i in range(m):
            g[i] = {}
            for n in generators:
                if (i + n) % m not in g[i]:
                    g[i][(i + n) % m] = n
                elif g[i][(i + n) % m] > n:
                    g[i][(i + n) % m] = n
        return g

    graph = make_nijenhuis_graph(generators)

    # 2. Calculate the shortest paths from the 0 vertex to each non-zero vertex

    shortest_paths = dijkstra(graph, 0)

    # 3. Return the maximum shortest path minus min(generators)

    v = max(shortest_paths, key=shortest_paths.get)
    return shortest_paths[v] - min(generators)
