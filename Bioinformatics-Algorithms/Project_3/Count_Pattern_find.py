'''
Funkcja count pattern z użyciem wbudowanej funkcji find
po znalezieniu patternu szuka dalej od następnej pozycji,
aby nie utknąć w nieskonczonej petli
'''
def count_pattern(tekst, szukana):
    wszystkie = []
    gdzie = tekst.find(szukana)
    wszystkie.append(gdzie)
    while gdzie > -1:
        gdzie = tekst.find(szukana, gdzie+1)
        if gdzie > -1:
            wszystkie.append(gdzie)
    return len(wszystkie), wszystkie

if __name__ == "__main__":
    import file_reader
    
    assert(count_pattern("AAAAA", "AA") == (4, [0, 1, 2, 3]))

    dna = file_reader.readDNA('oriC.fna')
    how_many, where = count_pattern(dna, 'AAG')
    for i in range(how_many):
        print(where[i], dna[where[i]:where[i]+3])

    second = "ATCGCATTCGGCGGGCGG"
    how_many, where = count_pattern(second, 'CGG')
    for i in range(how_many):
        print(where[i], second[where[i]:where[i]+3])