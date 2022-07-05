from time import time

def timeit(f, n):
    t0 = time()
    result = f(n)
    t1 = time()
    return result, (t1 - t0) * 1000

def fib(n):
    if n <= 1:
        return 1
    
    return fib(n - 2) + fib(n - 1)

for n in [5, 10, 20, 30, 40, 50]:
    r, ms = timeit(fib, n)
    print(f"fib({n}) exécuté en {round(ms, 3)} ms")
