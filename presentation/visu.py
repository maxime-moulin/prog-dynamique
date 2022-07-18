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

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs


def knapsack(P, W, C):
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def kp(C, k):
        if k >= len(P):
            best_value = 0
        else:
            p_without = kp(C=C, k=k + 1)
            p_with = -1
            if W[k] <= C:
                p_with = kp(C=C - W[k], k=k + 1) + P[k]
            best_value = max(p_without, p_with)
        return best_value

    return kp(C=C, k=0)


def knapsack(P, W, C):
    N = len(P)
    memo = [[None for _ in range(C + 1)] for _ in range(N + 1)]
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def kp(c, k):
        if memo[k][c] is not None: return memo[k][c]
        if k >= N: best_value = 0
        else:
            p_without = kp(c=c, k=k + 1)
            p_with = -1
            if W[k] <= c:
                p_with = kp(c=c - W[k], k=k + 1) + P[k]
            best_value = max(p_without, p_with)
        memo[k][c] = best_value
        return best_value
    return kp(c=C, k=0)


profits = [1, 4, 4, 6]
weights = [3, 3, 5, 6]
capacity = 8

# profits = [4, 2, 1, 2, 10]
# weights = [12, 2, 1, 1, 4]
# capacity = 12

filename = "knapsack-recursive-wikipedia-instance-12"

knapsack(profits, weights, capacity)
vs.make_animation(f"{filename}.gif", delay=1)
