from scores import score_given #importujemy pojedyncza funkcje z innego pliku, ponadto nie musimy podawac jej zrodla przy wywolywaniu tej funkcji
def Brute_force_motif_search(DNA, l):
    '''
    Funkcja szukajaca motywu metoda wszystkich opcji, tworzy wszystkie mozliwe 
    kombinacje miejsc starowych i sprawdza score kazdej po kolei, zwraca 
    miejsca dla ktorych wartosc score jest najwyzsza
    Przyjmuje argumenty:
    DNA - lista sekwencji
    l - dlugosc motywu
    Testy opieraja sie na podaniu prostych sekwencji i spawdzeniu ich poprawnosci
    '''
    bestscore = 0
    starting_positions = [0 for i in DNA]
    finishing_positions = [len(DNA[0])-l for i in DNA]
    while starting_positions != finishing_positions:
        if score_given(starting_positions, DNA, l) > bestscore:
            bestscore = score_given(starting_positions, DNA, l)
            bestmotive = starting_positions[:]
        i = 0
        while 1:#stopniowe zmienianie miejsc startowych, jeżeli na danym miejscu będzie maksymalne miejsce, to zmienia to miejsce na 0 i dodaje 1 do nastepnego
            if starting_positions[i] == len(DNA[0])-l:
                starting_positions[i] = 0
                i += 1
            else:
                starting_positions[i] += 1
                break
    return bestmotive

if __name__ == "__main__":
    from tools import rewrite_places_to_sequences

    seq_test = ['tactcgtcttttg',
                'cgcgactcggcgc',
                'gttactcgtgagc',
                'aaactcgggcttt',
                'accactcgatagg',
                ]
    k_test = 5
    test_places = Brute_force_motif_search(seq_test, k_test)
    try:
        assert(test_places == [1, 4, 3, 2, 3])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['actcg', 'actcg', 'actcg', 'actcg', 'actcg'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 25)

    seq_test = ['aatgacagtaacgacccttgtg',
                'atcttggtttggactgtgacat',
                'atgagagagactcacttgaaaa',
                'attccctgcatgatgagccttg']
    k_test = 6
    test_places = Brute_force_motif_search(seq_test, k_test)
    try:
        assert(test_places == [1, 15, 0, 9])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['atgaca', 'gtgaca', 'atgaga', 'atgatg'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 20)

    seq_test = ['tgagtgtagatctgaagggaaagt',
                'gctcacagttatcgcacgtttaga',
                'gcctggttagacccgaaatataat',
                'ttgattaaacaatttaagcacgta']
    k_test = 8
    test_places = Brute_force_motif_search(seq_test, k_test)
    try:
        assert(test_places == [7, 6, 15, 9, 11, 0, 3, 1, 6, 5])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['agatctga', 'agttatcg', 'aaatataa', 'caatttaa', 'aggtccaa', 'cgatcgtg', 'cgatatca', 'cattctaa', 'agatccaa', 'acatctac'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 26)
    print("Wszystkie testy udane")