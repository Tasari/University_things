def iterated_fibonacci(k):
    if k<=2:
        return 1
    n=1
    m=1
    while k>2:
        n, m = m, n+m
        k -= 1
    return m

def recursive_fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
 
