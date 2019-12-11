'''
Wyszukaj pattern, policz ile razy i gdzie sie wystepuje.
Liczy ilość wystąpień oraz ich lokalizacje i je zwaca.
Robi to tworząc po kolei patterny o danej długości w całej sekwencji
'''

def count_pattern(Text, Pattern):
    zlicz = 0
    gdzie = []
    kmer = len(Pattern)
    for i in range(len(Text)-kmer+1):#bez +1 nie działało, gdy sekwencja znajdowała się na końcu stringa
        if (Text[i:(i+kmer)] == Pattern):
            zlicz += 1
            gdzie.append(i)
    return zlicz, gdzie

if __name__ == "__main__":
    import file_reader
    dna = file_reader.readDNA('oriC.fna')
    how_many, where = count_pattern(dna, 'AAG')
    for i in range(how_many):
        print(where[i], dna[where[i]:where[i]+3])

    second = "ATCGCATTCGGCGGGCGG"
    how_many, where = count_pattern(second, 'CGG')
    for i in range(how_many):
        print(where[i], second[where[i]:where[i]+3])

    assert(count_pattern("AAAAA", "AA") == (4, [0, 1, 2, 3]))
