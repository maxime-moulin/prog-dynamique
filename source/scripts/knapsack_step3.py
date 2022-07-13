def knapsack(profits, weights, capacity, k):
    if k >= len(profits):
        return 0

    profit_without = knapsack(profits, weights, capacity, k + 1)
    if weights[k] <= capacity:
        remaining = capacity - weights[k]
        profit_with = knapsack(profits, weights, remaining, k + 1) + profits[k]
    else:
        profit_with = -1

    return max(profit_with, profit_without)

value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50, k=0
)
print(f"Valeur optimale: {value_opt}")
