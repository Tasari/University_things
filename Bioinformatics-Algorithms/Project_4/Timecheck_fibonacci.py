'''Uznalem ze czytelniej bedzie zrobić osobny plik sprawdzajacy czas,
gdyz funkcja sprawdzajaca czas nie jest konieczna przy samym liczeniu
wartosci n-tego wyrazu ciagu.
'''
import timeit
def fibonacci_timecheck(funkcja):
    '''
    Funkcja przyjmuje string funkcji ktora ma przetestowac,
    powtarza go 1000 razy, i zwraca czas ktory zajelo jej
    wykonanie tej funkcji 1000 razy.
    '''
    mysetup = 'import Fibonacci'
    mycode = '''
{}
'''.format(funkcja)
    ile_powtorzen = 1000
    czas = timeit.timeit(setup = mysetup,
                        stmt = mycode,
                        number = ile_powtorzen)
    return czas