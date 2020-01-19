import tools
import greedy
import randomized
import scores

sequences = [
    'tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
    'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
    'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
    'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
    'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
    'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
    'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta',
    'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
    'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
    'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg'
    ]

#Czesc kodu ktora wypisuje score osiagniety przez metode, maksymalny score, ich stosunek do siebie, oraz dlugosc sekwencji na ktorej pracuje, 
#jego wykonanie zajmuje ponad 60 sekund, omowienie jego wynikow pod kodem

for length in range(3, len(sequences[0])):
    score = scores.score_given(greedy.Greedy_motif_search(sequences, length), sequences, length)
    print("Greedy - Score {}, max Score {}, stosunek {}, dlugosc {}".format(score, length*10, score/(length*10), length))
    score = scores.score_given(randomized.multiple_randomized_searches(sequences, length, 100), sequences, length)
    print("Randomized - Score {}, max Score {}, stosunek {}, dlugosc {}\n".format(score, length*10, score/(length*10), length))
'''
Stosunek score zaczyna znaczaco spadac przy przejsciu z dlugosci 10 na dlugosc 11

Greedy - Score 72, max Score 80, stosunek 0.9, dlugosc 8
Randomized - Score 72, max Score 80, stosunek 0.9, dlugosc 8

Greedy - Score 80, max Score 90, stosunek 0.8888888888888888, dlugosc 9
Randomized - Score 80, max Score 90, stosunek 0.8888888888888888, dlugosc 9

Greedy - Score 89, max Score 100, stosunek 0.89, dlugosc 10
Randomized - Score 89, max Score 100, stosunek 0.89, dlugosc 10

Greedy - Score 91, max Score 110, stosunek 0.8272727272727273, dlugosc 11
Randomized - Score 91, max Score 110, stosunek 0.8272727272727273, dlugosc 11

Greedy - Score 94, max Score 120, stosunek 0.7833333333333333, dlugosc 12
Randomized - Score 95, max Score 120, stosunek 0.7916666666666666, dlugosc 12

Z tego wynika ze najlepszym motywem bedzie ten o dlugosci 10, czyli odpowiednio sekwencje:

Dla greedy:
tagatctgaa
tggatccgaa
tagacccgaa
taaatccgaa
taggtccaaa
tagattcgaa
cagatccgaa
tagatccgta
tagatccaaa
tcgatccgaa

Dla randomized:
tagatctgaa
tggatccgaa
tagacccgaa
taaatccgaa
taggtccaaa
tagattcgaa
cagatccgaa
tagatccgta
tagatccaaa
tcgatccgaa
'''