import sys
from dp import memoize


@memoize
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

sys.setrecursionlimit(1000)
print(fib(500))
