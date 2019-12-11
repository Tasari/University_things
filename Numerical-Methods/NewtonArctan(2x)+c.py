import numpy as np
import matplotlib.pyplot as plt

def funkcja(x, c):
    return np.arctan(2*x) + c

def pochodna(x):
    return 2/(4*(x*x)+1)

def pprzegiecia(x):
    return (-16*x)/pow(1+4*pow(x, 2),2)

def metoda_newtona(x, c):
    return x - funkcja(x, c)/pochodna(x)

print("Aby metoda Newtona zadziałała dla funkcji arctan(2x)+c, c musi mieścić się w przedziale <-pi/2, pi/2>\\0")

epsilon = 1.0e-10
b = 5
a = 0.1
dy = 0.1
imax = 1000000
i = 0
c = -1
pi = np.pi

if a > b:
    print("Początek przedziału nie może być większy od jego konca")
elif c > pi/2:
    print("funkcja arctan(2x)+c nie ma miejsc zerowych dla c wiekszego od pi/2" )
    exit(1)
elif c < -pi/2:
    print("funkcja arctan(2x)+c nie ma miejsc zerowych dla c mniejszego od -pi/2" )
    exit(2)
elif c == 0:
    print('''funkcja arctan(2x)+c nie ma miejsc zerowych dla c = 0, 
    gdyż druga pochodna tej funkcji zmienia swój znak w tym miejscu,
    i jeśli nie wybierzemy przedziału <-a, 0> lub <0,b>, znak nie bedzie stały, 
    jednak jeżeli to zrobimy to 1 warunek czyli a*b<0 nie będzie spełniony''' )
    exit(3)
elif c < 0 and a < 0:
    print("funkcja arctan(2x)+c musi mieć a > 0 aby spełnić 3 warunek dla twojego c" )
    exit(4)
elif c > 0 and b > 0:
    print("funkcja arctan(2x)+c musi mieć b < 0 aby spełnić 3 warunek dla twojego c" )
    exit(5)

xes = np.arange(a, b, 0.01)

while dy > epsilon and i < imax:
    x = metoda_newtona(a, c)
    print(x)
    dy = abs(funkcja(x, c))
    a = x
    i += 1
    if np.isnan(x):
        print("Zawęź przedział, przestrzeliłeś szeryfie")
        exit(420)
print("Miejsce zerowe z podaną dokładnością minimalną znajduje sie w miejscu {}".format(a))
plt.plot(xes, funkcja(xes, c))
plt.axvline(a)
plt.show()
