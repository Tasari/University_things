import matplotlib.pyplot as plt
import numpy as np

def f(x, c):#moja funkcja
    return np.arctan(2*x) + c + x

def chebydraw(x, k):
    if k == 0:
        return 1
    elif k == 1:
        return x
    else:
        return 2*x*chebydraw(x, k-1)-chebydraw(x, k-2)

def chebydraw2(x, k):
    if k == 0:
        return 1
    elif k == 1:
        return 2*x
    else:
        return 2*x*chebydraw2(x, k-1)-chebydraw2(x, k-2)

def chybyshev(x, k):#chyby 1st
    wartosci=[1, x]
    for i in range(2,k):
           wartosci.append(2*x*wartosci[i-1]-wartosci[i-2])
    return wartosci

def chybyshev2nd(x, k):#czyby 2st
    wartosci=[1, 2*x]
    for i in range(2,k+1):
           wartosci.append(2*x*wartosci[i-1]-wartosci[i-2])
    return wartosci

def chebyshev1_points(n):#Tworzy n punktów na przedziale <-1, 1> dla 1 typu cheby
    cheb_array = []
    for k in range(1, n+1):
        cheb_array.append(np.cos(np.pi*(2*k-1)/(2*n)))
    return cheb_array

def chebyshev2_points(n):#Tworzy n punktów na przedziale <-1, 1> dla 2 typu cheby
    cheb_array = []
    for k in range(1, n+1):
        cheb_array.append(np.cos((np.pi*k)/n))
    return cheb_array

xes = np.linspace(-10, 10, 100)#punkty na których rysujemy wykres
yes1 = np.zeros(100)
yes2 = np.zeros(100)
c = 2#zmienna, tam dalej do mojej funkcji
pts = 15#ilość punktów
cheby1zeros = chebyshev1_points(pts)
cheby2zeros = chebyshev2_points(pts)

zeros_range_up1 = []
for i in cheby1zeros:
    zeros_range_up1.append(0.5*(-10+10)+0.5*(10+10)*i)

val_1 = [f(x, c) for x in zeros_range_up1]

zeros_range_up2 = []
for i in cheby2zeros:
    zeros_range_up2.append(0.5*(-10+10)+0.5*(10+10)*i)

val_2 = [f(x, c) for x in zeros_range_up2]

cheby_matrix1 = [chybyshev(zeros_range_up1[i], pts) for i in range(pts)]

cheby_matrix2 = [chybyshev2nd(zeros_range_up2[i], pts-1) for i in range(pts)]

w1 = np.linalg.solve(cheby_matrix1, val_1)

w2 = np.linalg.solve(cheby_matrix2, val_2)

for i in range(100):
    for j in range(pts):
        yes1[i] += chybyshev(xes[i], pts)[j]*w1[j]

for i in range(100):
    for j in range(pts):
        yes2[i] += chybyshev2nd(xes[i], pts)[j]*w2[j]
xesc = np.linspace(-1, 1, 100)
for k in range(1, pts):
    plt.plot(xesc, chebydraw(xesc, k))
plt.show()#wykresy 1 czyby

for k in range(1, pts):
    plt.plot(xesc, chebydraw2(xesc, k))
plt.show()#wykresy 2

plt.plot(xes, f(xes, c))

plt.figure(figsize=(8,8))

plt.subplot(2,1,1)
plt.title("Czebyszew 1-szego rodzaju")
plt.plot(xes, yes1,'b-',zeros_range_up1, val_1, 'ro')

plt.subplot(2,1,2)
plt.title("Czebyszew 2-iego rodzaju")
plt.plot(xes,yes2,'r-',zeros_range_up2, val_2, 'bo')
plt.show()