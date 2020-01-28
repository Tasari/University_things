import timeit
import random

def List_enqueue_timecheck(i, times):
    '''
    Funkcja przyjmuje potege ilosci elementow na ktorej ma przetestowac funkcje,
    1000 razy powtarza ten kod dla jednej i drugiej kolejki,
    i zwraca czas ktory zajelo im
    wykonanie enqueue 2**i elementów 1000 razy.
    Testy skladaja sie z wykonania tej funkcji dla poszegolnych i i wypisania ich czasow
    '''
    setup = '''from random import random
import Python_list_based_queue
import Node_based_queue
x = [random()for z in range(2**{})]
Queue1 = Python_list_based_queue.Priority_Queue_List()
Queue2 = Node_based_queue.Node_based_priority_queue()
'''.format(i)
    code_1 = '''
for val in x:
    Queue1.enqueue(val)
                '''
    code_2 = '''
for val in x:
    Queue2.enqueue(val)
    '''
    ile_powtorzen = times
    czas1 = timeit.timeit(setup = setup,
                        stmt = code_1,
                        number = ile_powtorzen)
    czas2 = timeit.timeit(setup = setup,
                        stmt = code_2,
                        number = ile_powtorzen)
    return czas1, czas2

def List_dequeue_timecheck(i, times):
    '''
    Funkcja przyjmuje potege ilosci elementow na ktorej ma przetestowac funkcje,
    1000 razy powtarza ten kod dla jednej i drugiej kolejki,
    i zwraca czas ktory zajelo im
    wykonanie dequeue 2**i elementów 1000 razy.
    Testy skladaja sie z wykonania tej funkcji dla poszegolnych i i wypisania ich czasow
    '''
    setup = '''from random import random
import Python_list_based_queue
import Node_based_queue
x = [random()for z in range(2**{})]
Queue1 = Python_list_based_queue.Priority_Queue_List()
Queue2 = Node_based_queue.Node_based_priority_queue()
for val in x:
    Queue1.enqueue(val)
    Queue2.enqueue(val)
'''.format(i)
    code_1 = '''
for val in x:
    Queue1.dequeue()
'''
    code_2 = '''
for val in x:
    Queue2.dequeue()
    '''
    ile_powtorzen = times
    czas1 = timeit.timeit(setup = setup,
                        stmt = code_1,
                        number = ile_powtorzen)
    czas2 = timeit.timeit(setup = setup,
                        stmt = code_2,
                        number = ile_powtorzen)
    return czas1, czas2
    
if __name__ == "__main__":
    print(List_enqueue_timecheck(1, 1))
    print(List_enqueue_timecheck(5, 1))
    print(List_enqueue_timecheck(10, 1))
    print(List_enqueue_timecheck(12, 1))
    print(List_dequeue_timecheck(1, 1))
    print(List_dequeue_timecheck(5, 1))
    print(List_dequeue_timecheck(10, 1))
    print(List_dequeue_timecheck(12, 1))