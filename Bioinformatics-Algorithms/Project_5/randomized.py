from tools import profile_creator, most_prob_kmer, rewrite_places_to_sequences #wytlumaczenie dlaczego tak w brute_force
from scores import score_given
import random

def Randomized_motif_search(DNA, motif_len):
    '''
    Wyszukuje motyw opierający sie na podanych sekwencjach DNA,
    robi to losując początkowy motyw, tworzeniu profilu na jego podstawie,
    a potem szukajac motywow w sekwencji na podstawie tego motywu, jezeli stworzony motyw
    jest lepszy od poprzedniego, to powtarza proces, w przeciwnym wypadku zwraca tuple pozycji motywu,
    metoda ma niska trafnosc, wiec trzeba ja powtorzyc wielokrotnie, a nastepnie wyciagnac
    najczesciej wystepujacy motyw
    DNA - lista sekwencji
    motif_len - dlugosc motywu
    Testy tej funkcji sa trudne do przeprowadzenia gdyz jest to algorytm losowy, i nie zawsze daje oczekiwana odpowiedz
    '''
    sequences_count = len(DNA)
    motifs = []
    places = []
    for i in DNA:
        choice = random.randint(0, len(DNA[0])-motif_len)#randint losuje integer z podanego zakresu
        motifs.append(i[choice:choice+motif_len])
        places.append(choice)
    best_places = places
    while 1:
        profile = profile_creator(motifs, mode='laplace')
        motifs_index = [most_prob_kmer(sequence, motif_len, profile) for sequence in DNA]
        motifs = rewrite_places_to_sequences(DNA, motifs_index, motif_len)
        if score_given(motifs_index,DNA,motif_len) > score_given(best_places,DNA,motif_len):
            best_places = motifs_index
        else:
            return best_places

def multiple_randomized_searches(DNA, motif_len, times):
    '''
    Funkcja wielokrotnie stosujaca metode losowa, i wyciagajaca
    wynik z najwyzszym score po wszystkich powtorzeniach który zwraca.
    Przyjmuje argumenty:
    DNA - Lista sekwencji
    motif_len - dlugosc sekwencji
    times - ilosc powtorzen losowania motywu
    Testy skladaja sie z podania prostych sekwencji i sprawdzenia poprawnosci wyniku
    '''
    best = [0 for i in DNA]
    for i in range(times):
        random = Randomized_motif_search(DNA, motif_len)
        if score_given(best, DNA, motif_len) < score_given(random, DNA, motif_len):
            best = random
    return best


if __name__ == "__main__":
    from tools import rewrite_places_to_sequences
    seq_test = [    
        'tactcgtcttttg',
        'cgcgactcggcgc',
        'gttactcgtgagc',
        'aaactcgggcttt',
        'accactcgatagg',
        ]
    k_test = 5
    test_places = multiple_randomized_searches(seq_test, k_test, 100)
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
    test_places = multiple_randomized_searches(seq_test, k_test, 100)
    try:
        assert(test_places == [1, 15, 0, 12])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['atgaca', 'gtgaca', 'atgaga', 'atgagc'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 20)
    seq_test = ['tgagtgtagatctgaagggaaagt',
                'gctcacagttatcgcacgtttaga',
                'gcctggttagacccgaaatataat',
                'ttgattaaacaatttaagcacgta',
                'ggctgcttattaggtccaaaaggt',
                'cgatcgtgtttctccctctgtggg',
                'gtgcgatatcaggccgttctctta',
                'acattctaacgctcgcttattggc',
                'ttctttagatccaaacctgttggc',
                'aaacaacatctactaacgtagtcc']
    k_test = 8
    test_places = multiple_randomized_searches(seq_test, k_test, 2500)
    try:
        assert(test_places == [7, 6, 15, 9, 11, 0, 3, 1, 6, 5])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['agatctga', 'agttatcg', 'aaatataa', 'caatttaa', 'aggtccaa', 'cgatcgtg', 'cgatatca', 'cattctaa', 'agatccaa', 'acatctac'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 55)
    print("Wszystkie testy udane")