import random
import time
import os
''' TODO
Początek: 
wylosowac slowo z pliku!
określicz ilość liter
zakodować hasło
określić nieużyte litery
dać użytkownikowi życia

Gra:
Input użytkownika
Sprawdzić czy dana litera jest w słowie lub jest cheatem
Jeżeli udało się zgadnąć to poinformować gracza, jeżeli nie, odebrać życie
zaktualizować niużyte litery
powtarzać 
Zakończenie, poinformować gracza że wygrał/przegrał

'''
#początek
def wypisanie_tablicy(tablica):
    wyraz = ''
    for litera in tablica:
        wyraz += litera
    print(wyraz)

plik = open('slowa.txt','r', encoding='utf-8')
plik_odczyt = plik.read()
baza = plik_odczyt.split()
slowo = baza[random.randrange(0,len(baza) - 1)]
dlugosc_slowa = len(slowo)
print("Twoje slowo ma dlugosc {}".format(dlugosc_slowa))
zakodowane = ["*"] * dlugosc_slowa
niuzyte_litery = ['a', 'ą', 'b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','r','s','t','u','v','w','x','y','z', 'ż', 'ź']
zycie = 10
halp_count = 0
#Gra
while zycie > 0 or '*' in zakodowane:
    os.system("cls")
    print("Całkowita liczba liter w słowie to {}".format(len(slowo)))
    if zycie == 9:
        print("Masz jeszcze 9 żyć, NYAN")
    else:
        print("Masz jeszcze {} żyć".format(zycie))
    if zycie > len(niuzyte_litery):
        print("Już nie masz jak przegrać wariaciku, oszuście, więc kończymy grę, za 5 sekund dostaniesz informację jakie słowo dostałeś")
        time.sleep(5)
        while 1:
            print("BEZTALENCIE")
    print("Aktualny stan twojego słowa to:")
    wypisanie_tablicy(zakodowane)
    print("Pozostały Ci litery {}".format(niuzyte_litery))
    wybor = input("Podaj litere jaką chcesz odgadnąć\n").lower()
    if wybor == 'zycko':
        zycie += 10
        continue
    elif wybor == 'im stupid':
        halp_count = 0
    elif wybor == 'halp plox':
        halp_count += 1
        if halp_count == 3:
            print("Nie zrobie tego za Ciebie imbecylu")
            time.sleep(5)
            break
        xd = 0
        while 1:
            if zakodowane[xd] == '*':
                wybor = slowo[xd]
                break
            else:
                xd += 1
    if wybor in niuzyte_litery:
        if wybor in slowo:
            i = 0
            for litera in slowo:
                if litera == wybor:
                    zakodowane[i] = wybor
                i += 1
                if wybor in niuzyte_litery:
                    niuzyte_litery.remove(wybor)
        else:
            zycie -= 1
            if wybor in niuzyte_litery:
                niuzyte_litery.remove(wybor)
    
    else:
        print("Nie ma tej litery w nieuzytych\n\n")
        continue
    if zycie < 1:
        print('Przegrałeś twoje słowo: {}'.format(slowo))
        break
    elif '*' not in zakodowane:
        print("Wygrałeś")
        break