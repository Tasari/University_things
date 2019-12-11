# -*- coding: utf-8 -*-
'''
Wczytaj plik.
Pobiera nazwę pliku i otwiera ją w trybie czytającym,
sciąga z niego linie, a nastepnie zbija je w string,
który zwraca
'''

def readDNA(plik):
    try:
        file_opened = open(plik, "r" )
    except IOError:
        print("Pliku {} nie udalo sie otworzyc\n".format(plik))
        exit(1)
    print("Analizuje plik {}".format(plik))#format dostosowuje zmienna do wyswietlenia w stringu i wrzuca ja w miejce {}
    lines = file_opened.readlines()
    dna = ""
    for line in lines:
        dna += line[:-1]#Z tablicy string tworze tablice bez ostatniego elementu, czyli '\n' gdyż \ łączy się z n tworząc jeden znak - znak końca linii, jest tak w systemie Windows, gdy otwieramy plik, w trybie tekstowym a nie binarnym
    file_opened.close()
    return dna

if __name__ == "__main__":
    print(readDNA('oriC.fna'))
    print(readDNA('Vibrio.fna'))
    print(readDNA('cola.fna'))
    