text = input("Podaj wyraz\n") #Podajemy tekst jaki tłumaczymy na kod ASCII
laststring = None #Definiujemy że będziemy chcieli użyć zmiennej w pętli mimo iż jeszcze jej nie mamy
for letter in text: #Dosłownie "Dla każdej <litera> w <tekst> zrób:"
    print("Litera "+ letter + " posiada kod ascii " + str(ord(letter)))#Wypisz literę i jej kod ASCII i zmieniamy typ z polecenia ord() gdyż nie można dodawać liczby i tekstu
    if laststring == None:#Jeżeli zmienna nie ma żadnej wartości to przypisz jej wartość
        laststring = str(ord(letter))#Ponownie zmieniamy typ na string bo ord() zwraca liczbę i bez tego laststring będzie wynikiem dodawania liczb a nie kodów
    else:#Jeżeli zmienna ma już wartość to dodaj do niej kolejny kod ASCII
        laststring += str(ord(letter))
print("Cały wyraz " + text +" ma kod ASCII "+ laststring)#Wypisz wynik całego dodawania kodu