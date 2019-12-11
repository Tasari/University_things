import numpy as np
import matplotlib.pyplot as plt

def circle_drawer_cartesian(numpoints):
    '''a
    Funkcja tworzy losowe punkty w zakresie [-1, 1), a nastepnie, nanosi je na wykres,
    jezeli punkt znajduje sie w polu kola o r = 1 i punkcie startowym = [0, 0]
    to koloruje go na czerwono, a jezeli nie to koloruje go na niebiesko, zwraca
    tuple slownikow, gdzie pierwszy element to punkty nalezace do kola, a drugi element to punkty,
    które do niego nie naleza. Przyjmuje ilosc punktow jaka ma wylosowac jako argument
    '''
    #Uniform dziala podobnie do rand, jednak zamiast zakresu [0, 1) losuje z podanego zakresu
    x_axis, y_axis = list(np.random.uniform(-1, 1, numpoints)), list(np.random.uniform(-1, 1, numpoints))
    red = {}
    blue = {}
    for x, y in zip(x_axis, y_axis):
        if x*x+y*y<1:
            red[x] = y
        else:
            blue[x] = y
    plt.scatter(blue.keys(), blue.values(), color = "blue", label = 'Kolo')
    plt.scatter(red.keys(), red.values(), color = "red", label = 'Poza kolem')
    plt.legend(loc = 'upper right')
    return red, blue

def circle_drawer_polar(numpoints):
    '''
    Funkcja tworzy r w zakresie [0, 1), 
    a potem kat w zakresie [0, 360) w jakim ma obliczyć wartosć
    zwraca liste list x i y, gdzie punkty to (x[0], y[0]), (x[1], y[1]) itd.
    Przyjmuje ilosc punktow jaka ma wylosowac jako argument
    '''
    r = np.random.rand(numpoints, 1)
    fi = list(np.random.uniform(0, 360, numpoints))
    x=[]
    y=[]
    for i in range(numpoints):
        x.append(r[i][0]*np.cos(fi[i]))
        y.append(r[i][0]*np.sin(fi[i]))
    plt.scatter(x, y, label = "Wylosowane punkty")
    plt.legend(loc = 'upper right')
    return [x, y]

if __name__ == "__main__":
    print("Testy rysowania w ukladzie kartezjanskim")
    print("Rysowanie dla 2000 punktow")
    circle_drawer_cartesian(2000)
    plt.show()
    print("Rysowanie dla 10000 punktow")
    circle_drawer_cartesian(10000)
    plt.show()
    print("Testy rysowania w ukladzie biegunowym")
    print("Rysowanie dla 2000 punktow")
    circle_drawer_polar(2000)
    plt.show()
    print("Rysowanie dla 10000 punktow")
    circle_drawer_polar(10000)
    plt.show()