import Count_Pattern
import distances
import file_reader
import frequent_patterns
import reverse_dna
import skew

dna = file_reader.readDNA("Vibrio.fna")
reverse = reverse_dna.complementary_sequence_creator(dna)
print("Szukam ATGATCAAG")
counted1st = Count_Pattern.count_pattern(dna, "ATGATCAAG")
print("Szukam CTCTTGATC")
counted2nd = Count_Pattern.count_pattern(dna, "CTCTTGATC")
print("Szukam TCTTGATCA")
counted3rd = Count_Pattern.count_pattern(dna, 'TCTTGATCA')
print("Szukam CTTGATCAT")
counted4th = Count_Pattern.count_pattern(dna, 'CTTGATCAT')
print("Szukam oriC na podstawie sekwencji 'ATGATCAAG'\n")
oric_place = distances.oriC_finder(dna, 'ATGATCAAG')

print("Sekwencja 'ATGATCAAG' zostala znaleziona w pliku {} razy na miejscach:".format(counted1st[0]))
for miejsce in counted1st[1]:
    print(miejsce, end=" ")
print("\n")
print("Sekwencja 'CTCTTGATC' zostala znaleziona w pliku {} razy na miejscach:".format(counted2nd[0]))
for miejsce in counted2nd[1]:
    print(miejsce, end=" ")
print("\n")
print("Sekwencja 'TCTTGATCA' zostala znaleziona w pliku {} razy na miejscach:".format(counted3rd[0]))
for miejsce in counted3rd[1]:
    print(miejsce, end=" ")
print("\n")
print("Sekwencja 'CTTGATCAT' zostala znaleziona w pliku {} razy na miejscach:".format(counted4th[0]))
for miejsce in counted4th[1]:
    print(miejsce, end=" ")
print("\n")
print("OriC zostal znaleziony w miejscu {}-{}".format(oric_place[0], oric_place[1]))
print("Najmniejsza wartość diagramu skośności została znaleziona na miejscu {}".format(skew.skew(dna, 500000)))