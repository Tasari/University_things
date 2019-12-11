import Timecheck_fibonacci
import Ball
import Profile_user
import matplotlib.pyplot as plt
import numpy

fig = plt.figure(figsize=(10,10))#przygotowuje wymierzone okno w ktorym wyrysowane beda wykresy
#Sprawdzanie chwile trwa gdyz sprawdzamy 1000 razy a fibonacci rekurencyjny zajmuje duzo czasu
#Sprawdzanie czasu wykonywania Fibonacciego, wykres x = f(x)
plot = fig.add_subplot(2, 1, 1)#dodaje subplot w 1 wierszu w polu 2 wiersze x 1 kolumna
x = [i for i in range(20)]
y = [Timecheck_fibonacci.fibonacci_timecheck('Fibonacci.fibonacci_dynamiczny({})'.format(j)) for j in x]
plt.plot(x, y, label='Fibonacci dynamiczny')
y = [Timecheck_fibonacci.fibonacci_timecheck('Fibonacci.fibonacci_rekurencja({})'.format(j)) for j in x]
plt.plot(x, y, label='Fibonacci rekurencyjny')
plt.xlabel('N')#Dodaje opis osi X
plt.ylabel('Czas')#Dodaje opis osi Y
plt.title("Funkcja: k, czas(F(k))")#Dodaje tytul wykresu
plt.legend(loc="upper left")#dodaje legende stworzona z label przy rysowaniu wykresu, w miejscu loc


#Sprawdzanie czasu wykonywania Fibonacciego, wykres x = log(f(x))
plot = fig.add_subplot(2, 1, 2)#dodaje subplot w 2 wierszu w polu 2 wiersze x 1 kolumna
x = [i for i in range(20)]
y = [Timecheck_fibonacci.fibonacci_timecheck('Fibonacci.fibonacci_dynamiczny({})'.format(j)) for j in x]
plt.plot(x, numpy.log(y), label='Fibonacci dynamiczny')
y = [Timecheck_fibonacci.fibonacci_timecheck('Fibonacci.fibonacci_rekurencja({})'.format(j)) for j in x]
plt.plot(x, numpy.log(y), label='Fibonacci rekurencyjny')
plt.title('Funkcja: k, log(czas(F(k)))')
plt.xlabel('N')
plt.ylabel('Czas')
plt.legend(loc="upper left")
plt.show()
'''
Jak widzimy wykres bez logarytmu dla funkcji rekurencyjnej bardzo szybko rosnie, 
a dynamiczna rosnie podobnie do liniowej, z czego wnioskujemy ze zlozonosc funkcji dynamicznej jest liniowa,
aby ograniczyć wzrost na wykresie, uzywamy logarytmu od tego czasu,
widzimy ze funkcja rekurencyjna rosnie liniowo, z czego
mozemy wywnioskować, ze funkcja rekurencyjna nie jest optymalna,
gdyz jej zlozonosc obliczeniowa rosnie wykladniczo, poczatkowe roznice z wykresu logarytmicznego wynikaja z tego ze
rekurencyjnie funkcja od razu zwraca wartosc a dynamiczna nie
'''
fig = plt.figure(figsize=(10,5))
#Rysowanie kola w ukladzie kartezjanskim dla 3000 punktow
plot = fig.add_subplot(1, 2, 1)
Ball.circle_drawer_cartesian(3000)

#Rysowanie kola w ukladzie biegunowym dla 3000 punktow
plot = fig.add_subplot(1, 2, 2)
Ball.circle_drawer_polar(3000)
plt.show()
'''
Jak widzimy rozklad kola rysowanego w ukladzie kartezjanskim 
jest jednostajny, wynika to z tego ze losujemy punkty na 
podstawie kwadratu, dzieki czemu kazdy punkt ma po tyle samo miejsca, 
w przeciwienstwie do ukladu biegunowego, gdzie podstawa jest kolo,
w tym wypadku mamy rozklad niejednostajny, wynika to z faktu, ze 
dla tego samego stopnia, roznica odleglosci pomiedzy liniami blisko srodka,
jest znaczaco rozna od odleglosci daleko od srodka, zatem im blizej srodka
tym rozklad jest bardziej skoncentrowany, dodatkowe wytlumaczenie w pliku Addon.py
pokazane na wykresie.
'''
#Odtworzenie profilu po wylosowaniu
profile = [[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7], 
           [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2], 
           [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1], 
           [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]
after_print = 2
for i in [100, 1000, 10000]:
    #Wyliczanie sredniej
    list_of_sequences = [Profile_user.sequence_creator(profile) for k in range(i)]
    print("Srednia dla {} losowan".format(i))
    new_profile = Profile_user.profile_creator(list_of_sequences)
    for j in new_profile:
        print(j)
    #Wyliczanie odchylenia standardowego
    print("Odchylenie standardowe dla {} losowan".format(i))
    for j in Profile_user.standard_deviation(profile, new_profile):
        print(j)
    print("")#pusta linia do oddzielenia dla estetyki
'''
Jak widzimy, im wiecej punktow wylosujemy, tym dokladniej, 
losowania odzwierciedlaja poczatkowy profil, wynika to z faktu, 
ze im wieksza mamy probke z losowania tym bardziej przypadki 
odchodzace od profilu zanikaja w wielu losowaniach zgodnych z
profilem
'''