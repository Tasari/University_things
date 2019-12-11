#sprawdzanie czasu w pliku Timecheck_fibonacci.py
def fibonacci_rekurencja(n):
    '''a
    Funkcja wyliczajaca n-ty wyraz ciagu fibonacciego, 
    robi to rekurencyjnie, przyjmuje argument n,
    a zwraca wartosc danego wyrazu.
    Testy skladaja sie z assertów 
    poszczególnych wartosci dla danego n
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rekurencja(n-1)+fibonacci_rekurencja(n-2) 

def fibonacci_dynamiczny(n):
    '''
    Funkcja wyliczajaca n-ty wyraz ciagu fibonacciego, 
    zapisuje wyniki w liscie z której korzysta w obliczaniu,
    kolejnych n, index listy to n-ty wyraz.
    Testy skladaja sie z assertów 
    poszczególnych wartosci dla danego n
    '''
    all_n = [0, 1]
    for i in range(2, n+1):
        all_n.append(all_n[i-1] + all_n[i-2])
    return all_n[n]
if __name__ == "__main__":
    '''
    Testy funkcji rekurencyjnej
    '''
    assert(fibonacci_rekurencja(3)==2)
    assert(fibonacci_rekurencja(5)==5)
    assert(fibonacci_rekurencja(9)==34)
    '''
    Testy funkcji dynamicznej
    '''
    assert(fibonacci_dynamiczny(11)==89)
    assert(fibonacci_dynamiczny(9)==34)
    assert(fibonacci_dynamiczny(8)==21)
    assert(fibonacci_dynamiczny(55)==139583862445)