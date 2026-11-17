
# Mini-Courier Planner

## Project Overview

Mini-Courier Planner is a Python-based application designed to optimize parcel delivery operations using Design and Analysis of Algorithms.

The system prioritizes parcels, selects parcels according to vehicle capacity, calculates shortest delivery paths, and generates an optimized delivery route.

## Algorithms Used

1. Merge Sort - Sorts parcels according to priority and deadline.
2. 0/1 Knapsack - Selects parcels based on vehicle capacity and parcel value.
3. Dijkstra's Algorithm - Finds the shortest path from the depot to delivery locations.
4. Nearest Neighbor TSP - Generates a delivery route visiting all locations.

## Technologies Used

- Python
- CSV
- Matplotlib
- Unittest

## Project Structure

courier-planner/
- algorithms/
  - sorting.py
  - knapsack.py
  - dijkstra.py
  - tsp.py
- data/
  - parcels.csv
  - locations.csv
- documentation/
- results/
- screenshots/
- utils/
  - data_loader.py
  - performance.py
- main.py
- test_algorithms.py
- requirements.txt
- README.md

## How to Run

Install the required libraries:

pip install -r requirements.txt

Run the main application:

python main.py

Run performance analysis:

python -m utils.performance

Run algorithm tests:

python -m unittest test_algorithms.py -v

## Output

The application displays:
- Parcel information
- Prioritized parcels
- Selected parcels
- Shortest paths from the depot
- Suggested delivery route
- Total delivery distance
- Algorithm execution times

Performance results and graphs are saved in the results folder.

## Conclusion

The Mini-Courier Planner demonstrates how algorithmic techniques can improve parcel selection, delivery prioritization, and route planning.



-------------------



# Algorithm Complexity Analysis

## 1. Merge Sort

**Purpose:** Sorts parcels according to priority and delivery deadline.

- Best Case Time Complexity: O(n log n)
- Average Case Time Complexity: O(n log n)
- Worst Case Time Complexity: O(n log n)
- Space Complexity: O(n)

## 2. 0/1 Knapsack

**Purpose:** Selects parcels to maximize total value without exceeding vehicle capacity.

- Time Complexity: O(n × W)
- Space Complexity: O(n × W)

Where:
- n = Number of parcels
- W = Vehicle capacity

## 3. Dijkstra's Algorithm

**Purpose:** Calculates the shortest distance from the depot to all delivery locations.

- Time Complexity: O(V²)
- Space Complexity: O(V²)

Where:
- V = Number of vertices or locations

## 4. Nearest Neighbor TSP

**Purpose:** Generates a delivery route by repeatedly visiting the nearest unvisited location.

- Time Complexity: O(V²)
- Space Complexity: O(V)

Where:
- V = Number of delivery locations

## 5. Overall Comparison

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack | O(n × W) | O(n × W) |
| Dijkstra | O(V²) | O(V²) |
| Nearest Neighbor TSP | O(V²) | O(V) |

## Conclusion

The project combines sorting, dynamic programming, and graph algorithms to improve parcel prioritization and delivery planning. Each algorithm solves a different optimization problem within the courier management system.
