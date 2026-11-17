def nearest_neighbor(graph, start):

    unvisited = list(graph.keys())

    unvisited.remove(start)

    route = [start]

    total_distance = 0

    current = start
    while unvisited:

        nearest = None
        min_distance = float('inf')

        for neighbor in graph[current]:

            if neighbor in unvisited:

                distance = graph[current][neighbor]

                if distance < min_distance:

                    min_distance = distance
                    nearest = neighbor
        if nearest is None:
            print("No complete route possible!")
            return route, total_distance

        route.append(nearest)

        total_distance += min_distance

        unvisited.remove(nearest)

        current = nearest
    if start in graph[current]:

        total_distance += graph[current][start]

        route.append(start)

    return route, total_distance

if __name__ == "__main__":

    graph = {

        "Depot": {
            "A": 4,
            "B": 2,
            "C": 7
        },

        "A": {
            "Depot": 4,
            "B": 1,
            "C": 5
        },

        "B": {
            "Depot": 2,
            "A": 1,
            "C": 3
        },

        "C": {
            "Depot": 7,
            "A": 5,
            "B": 3
        }
    }

    route, distance = nearest_neighbor(graph, "Depot")

    print("Delivery Route:")

    print(" -> ".join(route))

    print("Total Route Distance:", distance, "km")
