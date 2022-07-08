# Le module dp (dynamic programming) est disponible en annexe
from dp import timeit

def fib(n):
    if n <= 1:
        return 1
    
    return fib(n - 2) + fib(n - 1)

for n in [5, 10, 20, 30, 40, 50]:
    result, ms = timeit(fib, n)
    print(f"fib({n}) -> {result}, exécuté en {round(ms, 3)} ms")
