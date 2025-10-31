def is_safe(node, graph, color, c):
    """
    Check if it's safe to assign color c to node.
    """
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    """
    Recursive utility to try assigning colors using backtracking.
    """
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    """
    Main function to solve the graph coloring problem.
    """
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0):
        print("No solution exists with", m, "frequencies.")
        return None
    print("Frequency assignment to cells:", color)
    return color

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
graph_coloring(graph, m)