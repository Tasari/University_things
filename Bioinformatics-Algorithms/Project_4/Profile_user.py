import numpy as np
def sequence_creator(profile):
    'Funkcja przyjmuje profil i zwraca sekwencje bazujaca na tym profilu'
    lenght = len(profile[0])
    seq = ''
    for i in range(lenght):
        found_random = np.random.rand(1)
        if found_random <= profile[0][i]:
            seq += 'A'
        elif found_random <= profile[1][i]+profile[0][i]:
            seq += "C"
        elif found_random <= profile[2][i]+profile[1][i]+profile[0][i]:
            seq += "G"
        else:
            seq += "T"
    return seq


def profile_creator(list_of_sequences):
    '''
    Funkcja przyjmuje liste sekwencji, liczy ilosć liter w pierwszej z nich
    (Przyjmuje ze kazda z sekwencji jest tak samo dluga)
    potem tworzy liste pustych stringow gdzie kazdy z nich odpowiada literze na danym miejscu
    nastepnie do stringa dodaje litere na danym miejscu, np. z zestawu sekwencji [TGA, AGT]
    stworzy 3 stringi ['TA', 'GG', 'AT'], nastepnie tworzy template profilu,
    a potem w odpowiednie miejsca wpisuje stosunek danej litery do wszystkich 
    liter w danym miejscu tworzac profil, ktory nastepnie zwraca
    '''
    letters_in_sequence = len(list_of_sequences[0])
    list_of_places = ['' for i in range(letters_in_sequence)]
    for sequence in list_of_sequences:
        i = 0
        for letter in sequence:
            list_of_places[i] += letter
            i += 1
    profile_out = [['' for z in range(letters_in_sequence)] for s in range(4)]
    letters = ['A', 'C', 'G', 'T']
    i = 0
    size_of_all_places = len(list_of_places[0])
    for letter in letters:
        j=0
        for place in list_of_places:
            profile_out[i][j] = '{:.3f}'.format(place.count(letter)/size_of_all_places)#formatuje string piszac podana wartosc od poczatku do konca, do 3 miejsca po przecinku
            j += 1
        i += 1 
    return profile_out

def standard_deviation(profile_start, profile_recreated):
    '''
    Funkcja wyliczajaca odchylenie standardowe dla kazdej wartosci
    z dwóch profilów
    '''
    std_dev = [['' for z in range(len(profile_start[0]))] for s in range(4)]
    letters = ['A', 'C', 'G', 'T']
    i = 0
    for letter in letters:
        j=0
        for place in std_dev[i]:
            std_dev[i][j] = '{:.3f}'.format(np.std([float(profile_start[i][j]), float(profile_recreated[i][j])]))
            j += 1
        i += 1
    return std_dev

if __name__ == "__main__":
    profile = [[1, 1, 1, 1, 1, 1, 1, 1], 
               [0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0, 0, 0]]
    list_of_sequences = [sequence_creator(profile) for k in range(100)]
    assert(list_of_sequences[58]=='AAAAAAAA')
    new_profile = profile_creator(list_of_sequences)
    assert(new_profile[0] == ['1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000'])
    print("Srednia z losowan")
    for i in new_profile:
        print(i)
    print("Odchylenie standardowe")
    dev = standard_deviation(profile, new_profile)
    for i in dev:
        print(i)
    assert(dev[0] == ['0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000'])