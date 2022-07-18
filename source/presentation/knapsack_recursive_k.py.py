def kp(P, W, C, k=0):
    if k >= len(P):
        best_value = 0
    else:
        p_without = kp(P, W, C, k + 1)
        p_with = -1
        if W[k] <= C:
            p_with = kp(P, W, C - W[k], k + 1) + P[k]
        best_value = max(p_without, p_with)
    return best_value
    
if __name__ == '__main__':
    profits = [1, 2, 5, 6]
    weights = [2, 3, 4, 5]
    capacity = 8

    best_value = kp(profits, weights, capacity)
    print(f"best value: {best_value}")