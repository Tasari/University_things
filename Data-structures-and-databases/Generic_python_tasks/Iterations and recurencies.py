def iterated_factorial(n):
    result = n
    for i in range(2, n):
        result *= i
    return result

def recursive_factorial(n):
    if n<=1:
        return 1
    return recursive_factorial(n-1)*n

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

def recursive_GCD(a, b):
    if b>a:
        a, b = b, a
    if b == 0:
        return a
    return recursive_GCD(b, a%b)

def iterated_GCD(a, b):
    if b>a:
        a, b = b, a
    while b>0:
        a, b = b, a%b
    return a

print(iterated_factorial(5))
print(recursive_factorial(5))
print(recursive_fibonacci(6))
print(iterated_fibonacci(6))
print(recursive_GCD(56, 16))
print(iterated_GCD(56,16))