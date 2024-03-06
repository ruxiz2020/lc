from collections import defaultdict, deque

def topological_sort(graph):
    # Count in-degrees of all vertices
    in_degree = {vertex: 0 for vertex in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    print(in_degree)

    # Initialize a queue to store vertices with zero in-degree
    queue = deque([vertex for vertex in graph if in_degree[vertex] == 0])

    # Initialize a list to store the topological ordering
    topological_ordering = []

    # Perform topological sorting
    while queue:
        current_vertex = queue.popleft()
        topological_ordering.append(current_vertex)

        # Reduce in-degree of adjacent vertices and enqueue them if in-degree becomes zero
        for neighbor in graph[current_vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If there are still vertices left with non-zero in-degree, the graph has a cycle
    if len(topological_ordering) != len(graph):
        raise ValueError("The graph contains a cycle")

    return topological_ordering

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}
try:
    result = topological_sort(graph)
    print("Topological Ordering:", result)
except ValueError as e:
    print(e)
