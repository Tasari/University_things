'''
Stwórz nić komplementarną do podanej.
Bierze po kolei każdą literkę zaczynając od ostatniej i cofając się,
zmienia ją na literkę komplementarną do niej.
Zwraca nić komplementarną.
Nić komplementarna przy użyciu replace() jest dość trudna gdyż po zmianie T na A,
gdy nastepnie zmieniamy A na T to drugi raz zmieniamy zmienione już znaki, 
podobnie z C oraz G
'''

def complementary_sequence_creator(text):
    complementary_sequence = ""
    for i in text[::-1]:#Ustawiamy krok na -1, czyli czytamy od końca
        if i == "A":
            complementary_sequence += "T"
        elif i == "T":
            complementary_sequence += "A"
        elif i == "G":
            complementary_sequence += "C"
        elif i == "C":
            complementary_sequence += "G"
    return complementary_sequence

if __name__ == "__main__":
    import file_reader
    testfile = file_reader.readDNA("oriC.fna")
    print("Sekwencja komplementarna do {} to {}".format(testfile, complementary_sequence_creator(testfile)))
    assert(complementary_sequence_creator("ACGGTAA") == "TTACCGT")