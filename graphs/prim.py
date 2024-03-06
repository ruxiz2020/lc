import heapq

def prim(graph):
    # Initialize an empty set to store visited vertices
    visited = set()

    # Initialize a priority queue to store edges with their weights
    priority_queue = [(0, None, 'A')]  # (weight, parent_vertex, current_vertex)

    # Initialize a dictionary to store the MST
    mst = {}

    while priority_queue:
        weight, parent_vertex, current_vertex = heapq.heappop(priority_queue)

        # If the current vertex has been visited, skip it
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited and add it to the MST
        visited.add(current_vertex)
        if parent_vertex:
            mst.setdefault(parent_vertex, []).append((current_vertex, weight))

        # Explore neighbors of the current vertex
        for neighbor, neighbor_weight in graph[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (neighbor_weight, current_vertex, neighbor))

    return mst

# Example usage:
graph = {
    'A': {'B': 3, 'C': 4, 'D': 2},
    'B': {'A': 3, 'C': 1, 'E': 7},
    'C': {'A': 4, 'B': 1, 'E': 5},
    'D': {'A': 2, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 3, 'F': 2},
    'F': {'D': 6, 'E': 2}
}
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree (MST):", minimum_spanning_tree)
