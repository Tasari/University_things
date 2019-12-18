import numpy as np
import matplotlib.pyplot as plt

def funkcja(x, c):
    return np.arctan(2*x) + c + x

def pochodna(x):
    return 2/(4*(x*x)+1)+1

def pprzegiecia(x):
    return (-16*x)/pow(1+4*pow(x, 2),2)

def metoda_newtona(x, c):
    return x - funkcja(x, c)/pochodna(x)

def punkt_staly(x, c):
    return -np.arctan(2*x)-c

def pochodna_stalego(x):
    return -2/(1+4*x*x)

show_data = 1

epsilon = 1.0e-7
bstart = 5
astart = 0.5
dystart = 0.1
imax = 1000
istart = 0
c = -4
pi = np.pi
metody = ["newtona", "bisekcji", "punktu stalego"]
xes = np.arange(astart, bstart, 0.01)

for metoda in metody:
    a=astart
    b=bstart
    dy=dystart
    i = istart
    if metoda == "newtona":
        if a > b:
            print("Początek przedziału nie może być większy od jego konca")
            exit(1)
        elif funkcja(a, c)*funkcja(b, c)>0:
            print('Brak jednego miejsca zerowego w przedziale')
            exit(1)
        elif pochodna(a)*pochodna(b)<0:
            print("pierwsza pochodna nie ma stałego znaku wiec newton nie działa")
            continue
        elif pprzegiecia(a)*pprzegiecia(b)<0:
            print("druga pochodna nie ma stałego znaku wiec newton nie działa")
            continue

        while dy > epsilon and i < imax:
            x = metoda_newtona(a, c)
            if show_data:
                print(x)
            dy = abs(funkcja(x, c))
            a = x
            i += 1

    elif metoda == "bisekcji":
        if a > b:
            print("Początek przedziału nie może być większy od jego konca")
            exit(10)
        elif funkcja(a, c)*funkcja(b, c)>0:
            print('Brak jednego miejsca zerowego w przedziale')
            exit(1)
        while dy > epsilon and i < imax:
            x = (a+b)/2
            if funkcja(a, c) * funkcja(x, c) < 0:
                b = x
            elif funkcja(a, c) * funkcja(x, c) > 0:
                a = x
            if show_data:
                print(x)
            dy = abs(b-a)
            i += 1            

    elif metoda == "punktu stalego":
        if a > b:
            print("Początek przedziału nie może być większy od jego konca")
            exit(10)
        elif funkcja(a, c)*funkcja(b, c)>0:
            print('Brak jednego miejsca zerowego w przedziale')
            exit(1)
        while dy > epsilon and i < imax:
            z = punkt_staly(a, c)
            if show_data:
                print(z)
            dy = abs(a-z)
            a = z
            i += 1   
    print("Miejsce zerowe z podaną dokładnością minimalną używając metody {} znajduje sie w miejscu {} po {} krokach".format(metoda, a, i))



fig, axs = plt.subplots(2, 2)
full = np.arange(-6, 6, 0.01)
axs[0, 0].plot(full, funkcja(full, c))
axs[0, 1].plot(full, pochodna(full))
axs[1, 0].plot(full, pprzegiecia(full))
axs[1, 1].plot(xes, funkcja(xes, c))
axs[1, 1].axvline(a, color="red")
axs[0, 0].set(title="Arctan(2x)+x+c")
axs[0, 1].set(title="2/(4*(x*x)+1)+1")
axs[1, 0].set(title="(-16*x)/pow(1+4*pow(x, 2),2)")
axs[1, 1].set(title="Rozwiązanie pokazane na przedziale (a, b)")
axs[0, 0].grid(True)
axs[1, 0].grid(True)
axs[0, 1].grid(True)
axs[1, 1].grid(True)
plt.show()
plt.plot(full, full)
plt.plot(full, punkt_staly(full, c))
plt.grid(True)
plt.show()
plt.plot(np.arange(-100, 100, 0.01), pochodna_stalego(np.arange(-100, 100, 0.01)))
plt.grid(True)
plt.show()