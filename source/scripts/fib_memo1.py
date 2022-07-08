from dp import timeit
memo = {}   # dictionnaire global servant à stocker les valeurs déjà calculées
def fib_memo1(n):
    if n <= 1: return n
    if n not in memo: memo[n] = fib_memo1(n - 1) + fib_memo1(n - 2)
    return memo[n]
    
for n in [5, 10, 20, 200]:
    result, ms = timeit(fib_memo1, n)
    print(f"fib({n}) -> {result}, exécuté en {round(ms, 3)} ms")

