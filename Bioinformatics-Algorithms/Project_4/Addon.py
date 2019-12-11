'''
Dodatkowy plik ktory ma za zadanie lepiej wytlumaczyc 
niejednostajny rozklad punktow w ukladzie biegunowym
'''
import numpy as np
import matplotlib.pyplot as plt
def circle_drawer_polar(numpoints , r, fi, color):
    '''
    Alternatywna wersja rysowania w ukladzie biegunowym
    nie losuje punktu tylko dorysowuje podany w podanym kolorze
    '''
    x=[]
    y=[]
    for i in range(numpoints):
        x.append(r*np.cos(fi))
        y.append(r*np.sin(fi))
    plt.scatter(x, y, color='{}'.format(color))

circle_drawer_polar(1, 0.1, 0, 'b')
circle_drawer_polar(1, 0.1, 45, 'b')
circle_drawer_polar(1, 1, 0, 'r')
circle_drawer_polar(1, 1, 45, 'r')
plt.show()
'''
Jak widzimy punkty niebieskie majace ten sam maly r lecz rozny kat
sa blizej siebie niz punkty czerwone majace ten sam duzy r lecz rozny kat
z tego faktu wynika to ze rozklad jest niejednostajny 
'''