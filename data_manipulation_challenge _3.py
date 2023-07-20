import heapq

def dijkstra(graph, start):
    # Function to find the shortest path from a given start node to all other nodes in the graph
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    # Challenge: Find the shortest path from a given start node to all other nodes in the graph
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'C': 1, 'D': 7},
        'C': {'D': 3},
        'D': {'A': 5},
    }
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Shortest Distances from Node", start_node)
    for node, distance in shortest_distances.items():
        print(f"To Node {node}: {distance}")

if __name__ == "__main__":
    main()
