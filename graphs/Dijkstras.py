import heapq

def dijkstra(graph, source):
    # Initialize distances to all vertices as infinity except for the source vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Priority queue to store vertices with their tentative distances
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore if the current distance is greater than the distance stored in the distances dictionary
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 3, 'C': 4, 'D': 2},
    'B': {'C': 1, 'E': 7},
    'C': {'E': 5},
    'D': {'F': 6},
    'E': {'D': 3, 'F': 2},
    'F': {}
}
source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from source vertex", source_vertex, "to other vertices:", shortest_distances)
