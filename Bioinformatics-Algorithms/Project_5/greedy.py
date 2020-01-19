from tools import profile_creator, most_prob_kmer #wytlumaczenie dlaczego tak w brute_force
from scores import score_given
def Greedy_motif_search(DNA, motif_len):
    '''
    Wyszukuje motyw danej dlugosci opierajac podanych sekwencjach,
    robi to tworzac wszystkie mozliwe kmery w pierwszej sekwencji, 
    a nastepnie dla kazdego kolejnego kmeru tworzy profil metoda laplace, na podstawie
    ktorego szuka najbardziej prawdopodobny kmer z nastepnej sekwencji,
    potem tworzy na podstawie tych kmerow nowy profil, i powtarza to,
    dla kazdej sekwencji z dna, potem powtarza to zaczynajac od kolejnego
    kmeru z 1 sekwencji, przy czym sprawdza score każdej kombinacji, zwraca
    liste pozycji z najwyzszym score.
    Lista parametrów:
    DNA - Lista sekwencji 
    motif_len - dlugosc motywu
    testy składają się z podania prostych sekwencji i sprawdzenia poprawnosci umiejscowienia motywow
    '''
    sequences_count = len(DNA)
    bestmotive = [0 for seq in DNA]
    all_motifs_of_first_sequence = [DNA[0][i:i+motif_len] for i in range(len(DNA[0])-motif_len+1)]
    actual_motif = 0
    for motif in all_motifs_of_first_sequence:
        i = 1
        motifes = [motif]
        actual_places = [0 for z in range(len(DNA))]
        actual_places[0] = actual_motif
        while i < sequences_count:
            profile = profile_creator(motifes, mode='laplace')
            place_of_most_prob_kmer = most_prob_kmer(DNA[i], motif_len, profile)
            motifes.append(DNA[i][place_of_most_prob_kmer:place_of_most_prob_kmer+motif_len])
            actual_places[i] = most_prob_kmer(DNA[i], motif_len, profile)
            i += 1
        if score_given(actual_places, DNA, motif_len) > score_given(bestmotive, DNA, motif_len):
            bestmotive = actual_places
        actual_motif += 1
    return bestmotive

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
    test_places = Greedy_motif_search(seq_test, k_test)
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
    test_places = Greedy_motif_search(seq_test, k_test)
    try:
        assert(test_places == [1, 15, 0, 9])
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
    test_places = Greedy_motif_search(seq_test, k_test)
    try:
        assert(test_places == [7, 6, 15, 9, 11, 0, 3, 1, 6, 5])
        motifs_test = rewrite_places_to_sequences(seq_test, test_places, k_test)
        assert(motifs_test == ['agatctga', 'agttatcg', 'aaatataa', 'caatttaa', 'aggtccaa', 'cgatcgtg', 'cgatatca', 'cattctaa', 'agatccaa', 'acatctac'])
    except AssertionError:
        print("Wystapil blad assercji, tak dlugo jak nie ma bledu score, tak dlugo nie trzeba zwracac uwagi na ten blad, gdyz score moze byc taki sam dla kilku motywow")
    score = score_given(test_places, seq_test, k_test)
    assert(score == 55)
    print("Wszystkie testy udane")