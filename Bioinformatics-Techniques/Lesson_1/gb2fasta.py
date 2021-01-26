import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

path_to_file = os.path.join(dir_path, "sequence.gb")

def read_gb(path_to_file):
    sequence = ''
    mode = "SeqFinder"
    with open(path_to_file, 'rt') as file:
        for line in file:
            if line.startswith('LOCUS'):
                header = '>' + ' '.join(line[5:].strip().upper().split())
            if mode == "GetSeq":
                if line.startswith('//'):
                    mode = "SeqFinder"
                else:
                    sequence += line[10:].upper().replace(' ', '') 
            elif line.startswith("ORIGIN"):
                mode = "GetSeq"
    return header, sequence

def save_fasta(header, sequence):
    with open(os.path.join(dir_path, "sequence.fasta"), 'wt') as file:
        file.write(header)
        file.write('\n')
        file.write(sequence)

if __name__ == '__main__':
    header, sequence = read_gb(path_to_file)
    print(header)
    print(sequence)
    save_fasta(header, sequence)