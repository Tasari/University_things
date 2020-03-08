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
