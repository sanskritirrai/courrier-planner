import heapq

def dijkstra(graph, start):

    distances = {}

    for node in graph:
        distances[node] = float('inf')

    distances[start] = 0

    priority_queue = [(0, start)]

    previous = {}

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances, previous


def get_path(previous, start, destination):

    path = []
    current = destination

    while current != start:

        path.append(current)

        if current not in previous:
            return []

        current = previous[current]

    path.append(start)

    path.reverse()

    return path

if __name__ == "__main__":

    graph = {
        "Depot": {
            "A": 4,
            "B": 2
        },

        "A": {
            "Depot": 4,
            "B": 1,
            "C": 5
        },

        "B": {
            "Depot": 2,
            "A": 1,
            "C": 8,
            "D": 10
        },

        "C": {
            "A": 5,
            "B": 8,
            "D": 2
        },

        "D": {
            "B": 10,
            "C": 2
        }
    }

    start = "Depot"

    distances, previous = dijkstra(graph, start)

    print("Shortest Distances from", start)

    for destination in graph:

        path = get_path(previous, start, destination)

        print(
            destination,
            ": Distance =", distances[destination],
            "km | Path =", " -> ".join(path)
        )
