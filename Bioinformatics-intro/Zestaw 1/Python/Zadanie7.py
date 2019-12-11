from math import sqrt
def prime_checker(b):
    x=2
    while x <= sqrt(b):
        if b%x == 0:
            return False
        else:
            x += 1
    return True

primes_list = []
for anything in range(2, int(input("Podaj liczbę do której chcesz wypisać liczby pierwsze\n"))+1):
     if prime_checker(anything):
          primes_list.append(anything)
print(primes_list)