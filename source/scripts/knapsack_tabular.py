def knapsack(profits, weights, capacity):
    N = len(profits)
    memo = [[None for _ in range(capacity + 1)] for _ in range(N + 1)]
    # initialisation du tableau de mémoïsation
    for c in range(capacity + 1):
        memo[N][c] = 0

     # on parcourt dans l'ordre décroissant de k
    for k in range(N - 1, -1, -1):
        # parcours dans l'ordre croissant de la capacité
        for c in range(capacity + 1):
            profit_without = memo[k+1][c]
            if weights[k] <= c:
                remaining = c - weights[k]
                profit_with = memo[k+1][remaining] + profits[k]
            else:
                profit_with = -1

            best_profit = max(profit_with, profit_without)
            memo[k][c] = best_profit

    return memo[0][capacity]


value_opt = knapsack(
    profits=[2600, 2600, 2600, 4500], weights=[13, 13, 13, 24], capacity=50
)
print(f"Valeur optimale: {value_opt}")
