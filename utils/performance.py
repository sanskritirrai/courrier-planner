
import csv
import time
from pathlib import Path
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"

def measure(function, *args):
    times = []

    for _ in range(3):
        start = time.perf_counter()
        function(*args)
        end = time.perf_counter()
        times.append(end - start)

    return sum(times) / len(times)

def generate_parcels(size):
    parcels = []

    for i in range(size):
        parcels.append({
            "parcel_id": f"P{i}",
            "priority": (i * 7) % 5 + 1,
            "deadline": f"{(i * 13) % 24:02d}:00",
            "weight": (i * 3) % 10 + 1,
            "value": (i * 97) % 1000 + 100
        })

    return parcels

def generate_graph(size):
    graph = {}
    nodes = ["Depot"] + [f"Location{i}" for i in range(1, size)]

    for i in range(size):
        graph[nodes[i]] = {}

        for j in range(size):
            if i != j:
                distance = ((i * 7 + j * 3) % 20) + 1
                graph[nodes[i]][nodes[j]] = distance

    return graph

def run_performance_tests():
    RESULTS_DIR.mkdir(exist_ok=True)

    results = []

    parcel_sizes = [10, 50, 100, 200, 500]

    for size in parcel_sizes:
        parcels = generate_parcels(size)

        sorting_time = measure(merge_sort, parcels)
        knapsack_time = measure(knapsack, parcels, 50)

        results.append(["Merge Sort", size, sorting_time])
        results.append(["Knapsack", size, knapsack_time])

    graph_sizes = [5, 10, 20, 30, 40]

    for size in graph_sizes:
        graph = generate_graph(size)

        dijkstra_time = measure(dijkstra, graph, "Depot")
        tsp_time = measure(nearest_neighbor, graph, "Depot")

        results.append(["Dijkstra", size, dijkstra_time])
        results.append(["Nearest Neighbor TSP", size, tsp_time])

    output_file = RESULTS_DIR / "runtime_results.csv"

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Input Size", "Execution Time (seconds)"])
        writer.writerows(results)

    print("\n========== PERFORMANCE ANALYSIS ==========")

    for algorithm, size, execution_time in results:
        print(f"{algorithm} | Input Size: {size} | Time: {execution_time:.8f} seconds")

    print("\nResults saved to:", output_file)

    try:
        import matplotlib.pyplot as plt

        parcel_algorithms = ["Merge Sort", "Knapsack"]
        graph_algorithms = ["Dijkstra", "Nearest Neighbor TSP"]

        for algorithms, filename, title in [
            (parcel_algorithms, "parcel_performance.png", "Parcel Algorithm Performance"),
            (graph_algorithms, "graph_performance.png", "Graph Algorithm Performance")
        ]:
            plt.figure()

            for algorithm in algorithms:
                selected = [row for row in results if row[0] == algorithm]
                sizes = [row[1] for row in selected]
                times = [row[2] for row in selected]
                plt.plot(sizes, times, marker="o", label=algorithm)

            plt.xlabel("Input Size")
            plt.ylabel("Execution Time (seconds)")
            plt.title(title)
            plt.legend()
            plt.grid(True)
            plt.savefig(RESULTS_DIR / filename)
            plt.close()

        print("Performance graphs saved in results folder.")

    except ImportError:
        print("Matplotlib is not installed. Graphs were not generated.")

if __name__ == "__main__":
    run_performance_tests()
