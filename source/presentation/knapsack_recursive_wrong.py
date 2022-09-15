def kp(P, W, C):
    if len(P) == 0:
        best_value = 0
    else:
        p_without = kp(P[1:], W[1:], C)
        p_with = kp(P[1:], W[1:], C - W[0]) + P[0]
        best_value = max(p_without, p_with)
    return best_value
    
if __name__ == '__main__':
    profits = [1, 2, 5, 6]
    weights = [2, 3, 4, 5]
    capacity = 8

    best_value = kp(profits, weights, capacity)
    print(f"best value: {best_value}")

