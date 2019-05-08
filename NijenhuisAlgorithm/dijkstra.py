from graphHeap import MikesGraphHeap


def dijkstra(graph, start=1):
    """
    input graph of the form {node1: {node2: distance, node3: distance, ... }, ...}
    output dictionary {node: shortest path from start to node}
    """
    X = {start}  # Vertices passed so far
    A = {start: 0}  # Computed shortest path distances
    V = set(graph.keys())
    M = MikesGraphHeap()  # stores nodes in form node = (label, key)
    # Dijkstra greedy score for nodes with edge from 1 is the values of the edges

    heapFill = V - X - set(graph[start].keys())  # all of the nodes that 1 doesnt have an edge to, to have key of inf in M
    M.heapify([(x, 10**6) for x in heapFill])
    for node in graph[start]:
        M.insert((node, graph[start][node]))

    while X != V:
        # find minimum A[v] + len(v,w) among edges (v,w) for all v in X and w not in X
        # call it (vStar, wStar)
        m = M.extract_min() # gives us (node, key)
        X.add(m[0])
        A[m[0]] = m[1]
        # for each edge (m[0], v) out of m[0], a[m[0]][v] = distance to v
        for v in graph[m[0]]:
            if v in V - X:
                M.heapList[0] = (0, 0)
                vKey = dict(M.heapList)[v]
                M.delete((v, vKey))
                vKey = min(vKey, A[m[0]] + graph[m[0]][v])
                M.insert((v, vKey))
    return A
