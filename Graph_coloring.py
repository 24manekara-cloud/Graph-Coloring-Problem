def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n
    if not graph_coloring_util(graph, m, color, 0):
        print("No valid coloring possible with", m, "colors.")
        return
    print("Vertex\tColor")
    for v in range(n):
        print(v + 1, "\t", color[v])


graph1 = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]


m = 3  # Number of available frequencies (colors)
print("Graph 1 Coloring:")
graph_coloring(graph1, m)


