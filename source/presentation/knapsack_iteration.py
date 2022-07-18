# Author: Bishal Sarang, https://github.com/Bishalsarang/Recursion-Tree-Visualizer/

import sys

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs


config = {
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey",
}

def knapsack(P, W, C):
    N = len(P)
    memo = [[None for _ in range(C + 1)] for _ in range(N + 1)]
    for c in range(0, C+1): memo[N][c] = 0

    # itération au lieu de récursion (k allant de N-1 à 0)
    for k in range(N - 1, -1, -1):
        for c in range(0, C+1):
            p_without = memo[k+1][c]
            p_with = -1
            if W[k] <= c:
                p_with = memo[k+1][c - W[k]] + P[k]
            best_value = max(p_without, p_with)
            memo[k][c] = best_value
    return memo[0][c]

# profits = [1, 4, 4]
# weights = [3, 3, 5]
# capacity = 6
profits = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8

optimal_profit = knapsack(profits, weights, capacity)
print(f"Optimal profit: {optimal_profit}")
