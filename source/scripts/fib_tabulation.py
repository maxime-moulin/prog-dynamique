from dp import ArrayLRUCache

def fib_hash(n: int) -> int:
    memo = {}
    for k in range(n+1):
        if k <= 2: f = k
        else: f = memo[k-1] + memo[k-2]
        memo[k] = f
    return memo[n]

def fib_table(n: int) -> int:
    memo = [0] * (n + 1)
    for k in range(n + 1):
        if k <= 2: f = k
        else: f = memo[k - 1] + memo[k - 2]
        memo[k] = f
    return memo[n]
        

def fib_table_lru(n: int) -> int:
    memo = ArrayLRUCache(maxsize=3)
    for k in range(n + 1):
        if k <= 2: f = k
        else: f = memo[k - 1] + memo[k - 2]
        memo[k] = f
    return memo[n]

def test(f):
    for n in list(range(10)) + [50, 200, 1000]:
        print(f"F({n}) = {f(n)}")

test(fib_hash)
test(fib_table)
test(fib_table_lru)