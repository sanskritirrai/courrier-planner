
import unittest
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import nearest_neighbor

class TestAlgorithms(unittest.TestCase):

    def test_merge_sort(self):
        parcels = [
            {"priority": 2, "deadline": "12:00"},
            {"priority": 5, "deadline": "10:00"},
            {"priority": 3, "deadline": "09:00"}
        ]

        result = merge_sort(parcels)

        self.assertEqual(
            [p["priority"] for p in result],
            [5, 3, 2]
        )

    def test_knapsack(self):
        parcels = [
            {"weight": "5", "value": "100"},
            {"weight": "4", "value": "80"},
            {"weight": "6", "value": "120"}
        ]

        selected, total_value = knapsack(parcels, 10)

        self.assertEqual(total_value, 200)

    def test_dijkstra(self):
        graph = {
            "A": {"B": 4, "C": 2},
            "B": {"A": 4, "C": 1},
            "C": {"A": 2, "B": 1}
        }

        distances, previous = dijkstra(graph, "A")

        self.assertEqual(distances["B"], 3)
        self.assertEqual(distances["C"], 2)
        self.assertEqual(get_path(previous, "A", "B"), ["A", "C", "B"])

    def test_nearest_neighbor(self):
        graph = {
            "A": {"B": 2, "C": 5},
            "B": {"A": 2, "C": 3},
            "C": {"A": 5, "B": 3}
        }

        route, distance = nearest_neighbor(graph, "A")

        self.assertEqual(route[0], "A")
        self.assertEqual(route[-1], "A")
        self.assertEqual(distance, 10)

if __name__ == "__main__":
    unittest.main()
