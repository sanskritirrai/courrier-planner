
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import nearest_neighbor
from utils.data_loader import load_parcels, load_graph


def main():

    parcels = load_parcels("data/parcels.csv")
    graph = load_graph("data/locations.csv")

    print("\n========== MINI-COURIER PLANNER ==========")

    print("\n1. PARCEL INFORMATION")

    for parcel in parcels:
        print(parcel)

    print("\n2. PARCEL PRIORITIZATION")

    sorted_parcels = merge_sort(parcels)

    for parcel in sorted_parcels:
        print(
            parcel["parcel_id"],
            "| Priority:", parcel["priority"],
            "| Deadline:", parcel["deadline"]
        )

    print("\n3. OPTIMAL PACKAGE SELECTION")

    capacity = 25

    selected, total_value = knapsack(sorted_parcels, capacity)

    total_weight = 0

    for parcel in selected:
        print(
            parcel["parcel_id"],
            "| Weight:", parcel["weight"], "kg",
            "| Value:", parcel["value"]
        )

        total_weight += int(parcel["weight"])

    print("Total Weight:", total_weight, "kg")
    print("Vehicle Capacity:", capacity, "kg")
    print("Total Value:", total_value)

    print("\n4. DIJKSTRA SHORTEST PATHS")

    distances, previous = dijkstra(graph, "Depot")

    for destination in graph:

        path = get_path(previous, "Depot", destination)

        print(
            destination,
            "| Distance:", distances[destination], "km",
            "| Path:", " -> ".join(path)
        )

    print("\n5. NEAREST NEIGHBOR TSP")

    route, distance = nearest_neighbor(graph, "Depot")

    print("Delivery Route:", " -> ".join(route))
    print("Total Route Distance:", distance, "km")

    print("\n========== PLANNING COMPLETED ==========")


if __name__ == "__main__":
    main()
