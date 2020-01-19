def score_given(s, DNA, k):
    """
    compute the consensus SCORE of a given k-mer alignment given
    offsets into each DNA string.
    s = list of starting indices.
    DNA = list of nucleotide strings.
    k = Target Motif length
    """
    score = 0
    for i in range(k):
        cnt = dict(zip("acgt",(0,0,0,0)))
        for j, s_val in enumerate(s):
            base = DNA[j][s_val+i]
            cnt[base] += 1
        score += max(cnt.values())
    return score

def score_mine(s, DNA, k):
    '''
    funkcja liczaca score danego kmeru, robi to przepisujac s i dna na odpowiednie sekwencje, 
    a nastepnie przepisujac dane litery wszystkich sekwencji do listy, 
    i liczac ich wystapienia w danym miejscu, a nastepnie dodaje ilosc najczesciej
    wystepujacej litery do score ogolnego, ktory zwraca po przejsciu przez wszystkie miejsca.
    Przyjmuje wartosci:]
    s - lista miejsc poczatkowych
    DNA - lista sekwencji
    k - docelowa dlugosc motywu
    Testy skladaja sie ze sprawdzenia czy funkcja podaje odpowiedni score
    '''
    score = 0
    bases = ['a', 'c', 'g', 't']
    sequences = [sequence[start:start+k] for sequence, start in zip(DNA, s)]
    for i in range(k):
        place = [sequence[i] for sequence in sequences]
        counts = [place.count(base) for base in bases]
        score += max(counts)
    return score

if __name__ == "__main__":
    print("Testy tlumaczace podany score")
    s = [3, 2, 1, 0]
    k = 3
    DNA = ["aaaaaa",
            "cccccc",
            "gggggg",
            "tttttt"]
    score = 0
    for i in range(k):
        cnt = dict(zip("acgt",(0,0,0,0)))
        print("Podana funkcja tworzaca cnt tworzy slownik w ktorym przechowywane ilosci wystapien", cnt)
        print("enumarate numeruje kazda wartosc z s, gdzie pierwsza cyfra to przypisany numer a drugi to wartosc", list(enumerate(s)))
        for j, s_val in enumerate(s):# j to wa
            base = DNA[j][s_val+i]
            cnt[base] += 1
            print(base, end=' ')
        print("to zasady na miejscu {} od podanego s".format(i))
        print("Slownik ze zliczonymi wystapieniami", cnt)
        score += max(cnt.values())
        print("Score po po zliczeniu z miejsca", i, "wynosci", score)
    assert(score == 3)
    
    assert(score_given([0, 0, 0], ['aaa', 'aaa', 'aaa'], 3)==9)
    assert(score_given([3, 1, 0], ['aggatcact', 'agatatagt', 'acacagagcta'], 5)==7)
    assert(score_given([0, 0, 0, 0, 0], ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa'], 5)==25)
    assert(score_given([0, 1, 0, 1, 0], ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa'], 4)==20)
    assert(score_given([0, 1, 0, 0, 1], ['aaata', 'aaaaa', 'aaaca', 'aaaaa', 'aaaga'], 4)==17)
    assert(score_mine([0, 0, 0, 0], ['cccc', 'gggg', 'aaaa', 'tttt'], 4) == 4)
    assert(score_mine([0, 2, 2, 0], ['cggccc', 'gtaggg', 'aagata', 'tgttgt'], 4) == 7)
    assert(score_mine([5, 0, 2], ['aagatagtcgtcatccg', 'aacatcgagtcgtatcg', 'atcggtcgtcatcgaaa'], 3) == score_given([5, 0, 2], ['aagatagtcgtcatccg', 'aacatcgagtcgtatcg', 'atcggtcgtcatcgaaa'], 3))
    print("Wszystkie testy udane")