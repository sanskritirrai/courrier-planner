import csv
def load_parcels(path):
    with open(path, "r", newline="") as file:
        return list(csv.DictReader(file))


def load_graph(path):
    graph = {}

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            source = row["from"]
            destination = row["to"]
            distance = float(row["distance_km"])

            if source not in graph:
                graph[source] = {}

            if destination not in graph:
                graph[destination] = {}

            graph[source][destination] = distance
            graph[destination][source] = distance

    return graph
