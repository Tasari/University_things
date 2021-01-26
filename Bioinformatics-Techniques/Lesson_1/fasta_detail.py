import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

path_to_file = os.path.join(dir_path, "sequence.fasta")

def read_fasta(path_to_file):
    sequence = ''
    total_len = 0 
    with open(path_to_file, 'rt') as file:
        for line in file:
            if line.startswith('>'):
                continue
            sequence += line
            total_len += len(line)
    return sequence, total_len
    
def count_bases(sequence):
    A = 0
    C = 0
    G = 0
    T = 0
    for letter in sequence:
        if letter == "A":
            A += 1
        elif letter == "C":
            C += 1
        elif letter == "G":
            G += 1
        elif letter == "T":
            T += 1
    return (A, C, G, T)

def create_complementary(sequence, to_reverse=0):
    complementary = ''
    if to_reverse:
        sequence = sequence[::-1]
    for i, nucleotide in enumerate(sequence):
        if nucleotide == 'G':
            complementary += 'C'
        elif nucleotide == 'C':
            complementary += 'G'
        elif nucleotide == 'A':
            complementary += 'T'
        elif nucleotide == 'T':
            complementary += 'A'
        if i%60 == 0:
            complementary += '\n'
    return complementary

def create_mrna(sequence):
    complementary = create_complementary(sequence, 1)
    mrna = complementary.replace("T", "U")
    return mrna

if __name__ == "__main__":
    sequence, total_len = read_fasta(path_to_file)
    A, C, G, T = count_bases(sequence)
    complementary = create_complementary(sequence, 1)
    mrna = create_mrna(sequence)
    print(
        "Sekwencja wczytana posiada {} zasad A ({}% calosci), {} zasad T ({}%), {} zasad C ({}%) oraz {} zasad G({}%)\n".format(
            A, round(A/total_len * 100, 2), 
            T, round(T/total_len * 100, 2),
            C, round(C/total_len * 100, 2),
            G, round(G/total_len * 100, 2),)
    )
    print(
        "Sekwencja komplementarna do wczytanej to {}\n".format(complementary)
    )
    print(
        "Sekwencja mRNA zbudowana na wczytanej sekwencji to {}\n".format(mrna)
    )