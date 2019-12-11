import matplotlib.pyplot as plt
from numpy import arange#importowana do stworzenia array, czyli listy z C
"""
Funkcja znajdująca oriC, na podstawie diagramu skośności,
rysuje wykres, a gdy dlugosc jest mniejsza od 75, to za oś x 
podstawia odpowiednie litery pod wartości, zwraca indeks 
najniższej ze wszystkich wartości
Ilość G rośnie od momentu w którym znajduje się oric
wynika to z deaminacji
algorytm przeszukuje cały text aby ustalić wartość jaką ma przyjąć 
wartość w danym punkcie dodaje 1 gdy znajduje G, a odejmuje gdy znajduje C
"""
def skew(text, start=0):#przy niepodaniu startu, przyjmuje ze start to 0
    wartosc = 0
    lista = [0]
    try:
        assert(start<len(text)+1)    
    except AssertionError:
        print("Start nie może być większy od długości textu")
        return -1
    dystans = arange(start, len(text)+1)
    for i in text[start:]:
        if i == "C":
            wartosc -= 1
        elif i == "G":
            wartosc += 1
        lista.append(wartosc)
    if len(text)-start < 75:
        plt.xticks(dystans[:-1], text)#Zastępowanie zmiennych osi x, na inne wartości, w tym wypadku text
    plt.ylabel("Skew")
    i=0
    last = 0
    if len(text)< 100:
        lista = lista[1:]
        for x in dystans:
            if x+1 < len(dystans):
                if lista[i]>last:
                    plt.plot([dystans[i], dystans[i+1]], [last, lista[i]], "g-o")
                elif lista[i]<last:
                    plt.plot([dystans[i], dystans[i+1]], [last, lista[i]], "r-o")
                elif lista[i]==last:
                    plt.plot([dystans[i], dystans[i+1]], [last, lista[i]], "k-o")
            try:
                last = lista[i]
            except IndexError:
                last = None
            i += 1
    else:
        plt.plot(dystans, lista)
    plt.show()
    return lista.index(min(lista))+start

if __name__ == "__main__":
    import file_reader
    assert(skew("CCCCCGGGGGG") == 4)
    print('Indeks najniższej wartości w danym tekscie to {}'.format(skew('CATGGGCATCGGCCATACGCC')))
    print('Indeks najniższej wartości w danym tekscie to {}'.format(skew("AAAACCGGGGGGTCCAAATTTGCGTCTGCGGCCAACCTATATATAGGGGAA")))
    print('Indeks najniższej wartości w danym tekscie to {}'.format(skew(file_reader.readDNA('cola.fna'), 2000000)))