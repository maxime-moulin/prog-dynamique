# Author: Bishal Sarang, https://github.com/Bishalsarang/Recursion-Tree-Visualizer/

import sys

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

from knapsack_recursive_wrong import kp
#from knapsack_recursive_ok import kp as kp_rec_ok

functions = {
    'kp_rec_wrong': kp,
    #'kp_rec_ok': kp_rec_ok,
}

config = {
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey",
}

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs

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

profits = [1, 4, 4]
weights = [3, 3, 5]
capacity = 6
# profits = [1, 4, 4, 6]
# weights = [3, 3, 5, 6]
# capacity = 8

filename = 'knapsack-memo-small'

knapsack(profits, weights, capacity)
vs.make_animation(f"{filename}.gif", delay=1)
