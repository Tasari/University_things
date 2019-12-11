'''
Znajdz miejsce oriC.
Szuka 3 wystąpień patternu i 3 wystąpień komplementarnego patternu
na przestrzeni 500 liter, zwraca najmniejsza i największą wartość z nich wszystkich
sprawdza 3 kolejne pozycje po kolei
'''
import reverse_dna
import Count_Pattern

def oriC_finder(sequence, pattern):
    normal_and_comp = [pattern, reverse_dna.complementary_sequence_creator(pattern)]
    all_close_positions = []
    for pattern in normal_and_comp:
        positions = Count_Pattern.count_pattern(sequence, pattern)[1]#takes only second element
        first = None
        second = None
        third = None
        for i in positions:
            if first == None:
                first = i
            elif second == None:
                second = i
            elif third == None:
                third = i
                if third - first < 500:#In case Oric is on the beginning of the sequence
                    all_close_positions.append(first)
                    all_close_positions.append(second)
                    all_close_positions.append(third)
            elif third - first < 500:
                all_close_positions.append(first)
                all_close_positions.append(second)
                all_close_positions.append(third)
            else:
                first = second
                second = third
                third = i
    all_close_positions.sort()
    return all_close_positions[0], all_close_positions[len(all_close_positions)-1]

if __name__ == "__main__":
    import file_reader
    oric_range = oriC_finder('ATCGCATTCGGCGGGCGG', 'CGG')
    print("Miejsce oric w sekwencji 'ATCGCATTCGGCGGGCGG' opierając się na sekwencji CGG został znaleziony w miejscach {}-{}".format(oric_range[0], oric_range[1]))
    oric_range = oriC_finder(file_reader.readDNA('oriC.fna'), 'ATGATCAAG')
    print("Miejsce oric w sekwencji DNA pliku oriC opierając się na sekwencji ATGATCAAG został znaleziony w miejscach {}-{}".format(oric_range[0], oric_range[1]))
    oric_range = oriC_finder(file_reader.readDNA('Vibrio.fna'), 'ATGATCAAG')
    print("Miejsce oric w sekwencji DNA pliku Vibrio opierając się na sekwencji ATGATCAAG został znaleziony w miejscach {}-{}".format(oric_range[0], oric_range[1]))
