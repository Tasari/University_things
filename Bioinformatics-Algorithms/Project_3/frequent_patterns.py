# -*- coding: utf-8 -*-
'''
Wyszukaj najczestszy pattern danego rozmiaru w stringu lub jeżeli nie poda się rozmiaru,
to szuka najczestrzych patternów o długości od 3 w góre zwraca słownik gdzie
kluczem jest pattern a wartością jest tupla (ilosc, [pozycje])
szuka najczestszego patternu danego rozmiaru liczac wszystkie
wystepujace patterny danego rozmiaru, i wyrzucając z pętli
najczestszy pattern danego rozmiaru, razem z ilością i pozycjami
'''
import Count_Pattern_find

def frequent_patterns(dna, kmer=0):    
    all_patterns_with_count = {}
    do_all = False
    if not kmer:
        do_all = True
        kmer = 3
    while 1: 
        all_counts = {}
        all_positions = {}
        for index in range(len(dna)-kmer):
            pattern = dna[index:index+kmer]
            if pattern not in all_counts.keys():#.keys() creates list of keys of given dictionary, and not in returns True if pattern is not counted yet
                kmer_count_and_positions = Count_Pattern_find.count_pattern(dna, pattern)#key is word and value is tuple of count and list of positions
                all_counts[pattern] = kmer_count_and_positions[0]
                all_positions[pattern] = kmer_count_and_positions[1]
        maxiumum = max(all_counts.values())
        if maxiumum == 1:
            return all_patterns_with_count
        for key, value in all_counts.items():
            if value == maxiumum:
                all_patterns_with_count[key] = (all_counts[key], all_positions[key])
        kmer += 1
        if do_all == False:
            return all_patterns_with_count            

if __name__ == "__main__":
    import file_reader

    oric_patterns = frequent_patterns(file_reader.readDNA("oriC.fna"), 3)
    for key, values in oric_patterns.items():
        print("Najczestsza sekwencja o dlugosci {} czyli  {} wystapila w podanym pliku {} razy w miejscach:".format(len(key), key, oric_patterns[key][0]))
        for value in values[1]:
            print(value, end=' ')#keyword end overwrites default end of line which is \n in python so it's prettier when printing positions
        print('')#prints \n
    print("Nie ma więcej powtarzających się patternów\n")

    oric_patterns = frequent_patterns("AAACGCAAAAAGAAAACCCCAAATTTTTTTTTGAGAGAGATATACATAGGATCATGAGAGAGAGTACACATAC")
    for key, values in oric_patterns.items():
        print("Najczestsza sekwencja o dlugosci {} czyli  {} wystapila w podanym pliku {} razy w miejscach:".format(len(key), key, oric_patterns[key][0]))
        for value in values[1]:
            print(value, end=' ')#keyword end overwrites default end of line which is \n in python so it's prettier when printing positions
        print('')#prints \n
    print("Nie ma więcej powtarzających się patternów")
