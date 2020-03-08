def iterated_factorial(n):
    result = n
    for i in range(2, n):
        result *= i
    return result

def recursive_factorial(n):
    if n<=1:
        return 1
    return recursive_factorial(n-1)*n 
