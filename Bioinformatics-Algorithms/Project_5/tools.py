def rewrite_places_to_sequences(DNA, places, kmer):
    '''
    Przepisuje miejsca na sekwencje, zwraca liste sekwencji ktore 
    powstaly z czytania danej sekwencji dna od danego miejsca.
    Przyjmuje argumenty:
    DNA - Lista sekwencji
    places - Lista miejsc od ktorych zaczyna przepisywac sekwencje
    kmer - dlugosc sekwencji jaka chcemy otrzymac
    Testy skladaja sie z podania prostych miejsc startowych, i prostych sekwencji dna, 
    i sprawdzenia poprawnosci ich przepisania
    '''
    sequence_number = 0
    sequences = []
    for sequence in DNA:
        sequences.append(DNA[sequence_number][places[sequence_number]:places[sequence_number]+kmer])
        sequence_number += 1
    return sequences

def most_prob_kmer(sequence, kmer, profile):
    '''
    Tworzy najbardziej prawdopodobny kmer na podstawie profilu, 
    robi to tworzac wszystkie mozliwe kmery
    i sprawdzanie calkowitego prawdopodobiensta ich wystapienia,
    zwraca miejsce poczatku kmeru ktorego prawdopodobienstwo bedzie najwieksze.
    Przyjmuje argumenty:
    sequence - sekwencja w ktorej ma byc znaleziony najbardziej prawdopodobny kmer
    kmer - dlugosc jaka ma uzyskac kmer
    profile - profil na podstawie ktorego ma powstac kmer
    Testy skladaja sie z podania prostej sekwencji, i prostego profilu oraz sprawdzeniu poprawnosci
    wyniku
    '''
    kmer_list = [sequence[i:i+kmer] for i in range(len(sequence)-kmer+1)]
    bestprob = 0
    bestkmerpos = 0
    kmerpos = 0
    for seq in kmer_list:
        prob = 1
        place = 0
        for letter in seq:
            if letter == 'a':
                prob *= profile[0][place]
            elif letter == 'c':
                prob *= profile[1][place]
            elif letter == 'g':
                prob *= profile[2][place]
            elif letter == 't':
                prob *= profile[3][place]
            place += 1
        if prob > bestprob:
            bestprob = prob
            bestkmerpos = kmerpos
        kmerpos += 1
    return bestkmerpos

def profile_creator(list_of_seq, mode='normal'):
    '''
    Tworzy profil opierajac sie na sekwencjach i go zwraca
    Przyjmuje parametry:
    list_of_seq - lista sekwencji z ktorych ma zostac zbudowany profil
    mode - domyslnie ma wartosc 'normal', ktora tworzy profil normalna metoda,
    mozna zmienic ten argument na 'laplace', aby stworzyc profil metoda laplace'a
    Testy skladaja sie ze stworzenia prostych sekwencji i sprawdzeniu poprawnosci wyniku
    '''
    if mode == 'normal':
        mode = 0
    elif mode == "laplace":
        mode = 1
    profile = [[mode for i in range(len(list_of_seq[0]))] for i in range(4)]
    for seq in list_of_seq:
        letter_position = 0
        for letter in seq:
            if letter == 'a':
                profile[0][letter_position] += 1
            elif letter == 'c':
                profile[1][letter_position] += 1 
            elif letter == 'g':
                profile[2][letter_position] += 1
            elif letter == 't':
                profile[3][letter_position] += 1
            letter_position += 1
    row = 0
    for a in profile:
        column = 0
        for b in a:
            profile[row][column] = round(profile[row][column]/(len(list_of_seq)+(4*mode)), 2)#round zaokragla liczbe do podanego miejsca po przecinku
            column += 1
        row += 1
    return profile

if __name__ == "__main__":
    assert(rewrite_places_to_sequences(['aaaca', 'ctata', 'taaag'], [0, 1, 2], 3) == ['aaa', 'tat', 'aag'])
    assert(rewrite_places_to_sequences(['ttttcccaaagg','gggaaatgtgtg'], [5, 2], 5) == ['ccaaa', 'gaaat'] )
    
    assert(most_prob_kmer('aaagaaacgac', 5, [[0.0, 0.8, 0.5, 0.5, 0.3],
                                            [0.2, 0.1, 0.3, 0.3, 0.5],
                                            [0.7, 0.0, 0.2, 0.2, 0.1],
                                            [0.1, 0.1, 0.0, 0.0, 0.1]]) == 3)
    assert(most_prob_kmer('aagagtagtatacgac', 5, [[0.0, 0.8, 0.5, 0.5, 0.3],
                                            [0.2, 0.1, 0.3, 0.3, 0.5],
                                            [0.7, 0.0, 0.2, 0.2, 0.1],
                                            [0.1, 0.1, 0.0, 0.0, 0.1]]) == 10)
    
    assert(profile_creator(['aaa', 'aaa', 'aaa']) == [[1.0, 1.0, 1.0], 
                                                    [0.0, 0.0, 0.0], 
                                                    [0.0, 0.0, 0.0], 
                                                    [0.0, 0.0, 0.0]])
    assert(profile_creator(['acga', 'ggta', 'ttac', 'tgtg', 'tgaa'], mode='laplace') == [[0.22, 0.11, 0.33, 0.44], 
                                                                                        [0.11, 0.22, 0.11, 0.22], 
                                                                                        [0.22, 0.44, 0.22, 0.22], 
                                                                                        [0.44, 0.22, 0.33, 0.11]])
    print("Wszystkie testy udane")