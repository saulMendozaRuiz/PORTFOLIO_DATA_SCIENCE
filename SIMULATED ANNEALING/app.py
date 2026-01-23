"""
Traveling Salesman Problem (TSP) solved using Simulated Annealing (SA).

- Cities are loaded from a JSON file (latitude, longitude).
- The algorithm operates strictly on permutations of indices.
- Distance evaluation is fully vectorized using NumPy.
- Multiple neighbor samples are evaluated at each temperature level.
- Initial temperature is NOT estimated: it emerges from the first ΔE > 0.
"""

import numpy as np
import os
import json
from typing import Tuple

app_path = os.path.dirname(__file__)
json_path = os.path.join(app_path, "cities.json")


# ------------------------ Utility Functions --------------------------

def load_n_cities(n: int) -> Tuple[np.ndarray, list]:
    """
    Load n random cities from the JSON dataset.

    Returns
    -------
    coords : np.ndarray of shape (n, 2)
        City coordinates (lat, lon)
    names : list[str]
        City names in the same order as coords
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    idx = np.random.choice(len(data), size=n, replace=False)

    coords = np.array(
        [
            (
                round(float(data[i]["latitude"]), 6),
                round(float(data[i]["longitude"]), 6),
            )
            for i in idx
        ],
        dtype=np.float64,
    )

    names = [f'{data[i]["city"]}, {data[i]["state"]}' for i in idx]

    return coords, names

def evaluate_tour(tour: np.ndarray) -> float:
    shifted = np.roll(tour, -1, axis=0)
    deltas = tour - shifted
    sq_dist = np.sum(deltas ** 2, axis=1)
    return float(np.sqrt(sq_dist).sum())

def simulated_annealing(
    route: np.ndarray,
    cities: np.ndarray,
    cooling_rate: float,
    max_iter: int,
    samples_per_temp: int,
) -> np.ndarray:
    """
    Simulated Annealing over index permutations with emergent temperature.

    Parameters
    ----------
    route : np.ndarray of shape (N,)
        Initial permutation of city indices
    cities : np.ndarray of shape (N, 2)
        Fixed city coordinates
    """

    current_route = route.copy()
    current_distance = evaluate_tour(cities[current_route])

    best_route = current_route.copy()
    best_distance = current_distance

    temp = None  # temperature emerges from first ΔE > 0

    for _ in range(max_iter):

        for _ in range(samples_per_temp):
            i, j = np.random.choice(len(route), size=2, replace=False)

            new_route = current_route.copy()
            new_route[i], new_route[j] = new_route[j], new_route[i]

            new_distance = evaluate_tour(cities[new_route])
            delta = new_distance - current_distance

            # set temperature from first uphill move
            if temp is None and delta > 0:
                temp = delta

            if temp is None:
                accept = True  # T → ∞ phase
            else:
                accept = delta < 0 or np.random.rand() < np.exp(-delta / temp)

            if accept:
                current_route = new_route
                current_distance = new_distance

                if current_distance < best_distance:
                    best_route = current_route.copy()
                    best_distance = current_distance

        if temp is not None:
            temp *= cooling_rate

    return best_route

# --------------------------------------------------
if __name__ == "__main__":

    n = int(input("Enter number of cities to load: "))

    cities, names = load_n_cities(n)

    print("\nLoaded cities:")
    print(*names, sep="\n")

    route = np.random.permutation(len(cities))
    initial_distance = evaluate_tour(cities[route])

    print("\nInitial tour distance:", initial_distance)

    optimized_route = simulated_annealing(
        route=route,
        cities=cities,
        cooling_rate=0.95,
        max_iter=2000,
        samples_per_temp=30,
    )

    optimized_distance = evaluate_tour(cities[optimized_route])

    print("\nOptimized tour distance:", optimized_distance)
    print("Improvement:", initial_distance - optimized_distance)