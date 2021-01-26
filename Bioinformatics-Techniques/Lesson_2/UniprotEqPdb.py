import json
import requests

from sys import argv


def getdatafromAPI(uniprot_id):
    api_url = f'https://www.ebi.ac.uk/proteins/api/proteins/{uniprot_id}'

    response = requests.get(api_url, headers={'Accept': 'application/json'})

    if response.ok:
        return response.text
    else:
        return False

def get_data_from_API_pdb(pdb_id):
    api_url = f'https://files.rcsb.org/view/{pdb_id}.pdb'

    response = requests.get(api_url, headers={'Accept': 'application/json'})

    if response.ok:
        return response.text
    else:
        return False

def get_aa_sequence_from_pdb_data(pdb_data):
    protein = ''
    chain = ''
    for line in pdb_data.splitlines():
        if line.startswith("SEQRES"):
            if chain == '':
                chain = line[11]
            if line[11] == chain:
                protein += line[19:]
    protein = protein.split()
    return protein

def translate3to1(aa_seq, aa_codes):
    newseq = ""
    for aa in aa_seq:
        newseq += aa_codes[aa]
    return newseq

def check_if_uniprot_and_pdb_have_eq_data(uniprot_id):
    data = getdatafromAPI(uniprot_id)
    if data:
        data = json.loads(data)
        uniprot_data = data['sequence']['sequence']
        for reference in data['dbReferences']:
            reference_type = reference['type']
            if reference_type == 'PDB':
                pdb_id = reference['id']
                pdb = get_data_from_API_pdb(pdb_id)
                aa_seq = get_aa_sequence_from_pdb_data(pdb)
                pdb_data = translate3to1(aa_seq, aa_codes)
    return uniprot_data == pdb_data

aa_codes = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}



if __name__ == '__main__':
    try:
        try:
            data_dict = {}
            print("Processing...")
            with open(argv[1], 'rt') as uniprot_ids:
                for uniprot_id in uniprot_ids:
                    uniprot_id = uniprot_id.strip('\n').strip()
                    print("Processing {}".format(uniprot_id))
                    data_dict[uniprot_id] = check_if_uniprot_and_pdb_have_eq_data(uniprot_id)
                print(data_dict)
        except IndexError:
            uniprot_id = input("Uniprot ID of the sequence you want to check: ")
            print(uniprot_id + ':',check_if_uniprot_and_pdb_have_eq_data(uniprot_id))
    except UnboundLocalError:
        print("Given Uniprot ID doesn't exist or has no PDB database reference")