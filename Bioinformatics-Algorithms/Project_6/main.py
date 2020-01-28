import Speed_compare
import matplotlib.pyplot as plt
import numpy as np

'''
Kod został zakomentowany z powodu dlugiego czasu dzialania,
wyniki pod zakomentowanym kodem

'''


'''
times = 1
timesenqueue1 = []
timesenqueue2 = []
timesdequeue1 = []
timesdequeue2 = []
elements = []

for i in range(10, 17):
    print("Dzialam na 2**{} elementach".format(i))
    timeenq = Speed_compare.List_enqueue_timecheck(i, times)
    timedeq = Speed_compare.List_dequeue_timecheck(i, times)
    timesenqueue1.append(timeenq[0])
    timesenqueue2.append(timeenq[1])
    timesdequeue1.append(timedeq[0])
    timesdequeue2.append(timedeq[1])
    elements.append(2**i)

plt.loglog(elements,timesenqueue2, label="Times node based")
plt.loglog(elements,timesenqueue1, label="Times list based")
plt.xlabel("Log(Ilosc elementow)")
plt.ylabel("Log(Czas)")
plt.title("Enqueue")
plt.legend()
plt.show()

plt.loglog(elements,timesdequeue2, label="Times node based")
plt.loglog(elements,timesdequeue1, label="Times list based")
plt.xlabel("Log(Ilosc elementow)")
plt.ylabel("Log(Czas)")
plt.title("Dequeue")
plt.legend()
plt.show()
'''

elements = [2**i for i in range(10, 17)]
timesenqueue1 = [0.0005055959999822335, 0.000636742000040158, 0.0010364389999608647, 0.0020790949999991426, 0.004201899999998204, 0.008280717000047844, 0.016906439999957]
timesenqueue2 = [0.18153955299999325, 0.772298926000019, 2.5275786139999923, 10.284676378000029, 44.42744644300001, 208.00568699400003, 925.9161928810001]
timesdequeue1 = [0.0007925460000137718, 0.0017085140000290266, 0.0047587930000076994, 0.014926696999964406, 0.04988852200000338, 0.18743553000001612, 0.8115399670000443]
timesdequeue2 = [0.0012055010000153743, 0.0020113369999990027, 0.004088002999992568, 0.011558409000031133, 0.018082420000041566, 0.04156257999989066, 0.08573821899972245]


plt.subplot(2, 1, 1)
plt.loglog(elements,timesenqueue2, label="Times node based")#loglog tworzy plot ze zlogaytmowanymi wartosciami osi
plt.loglog(elements,timesenqueue1, label="Times list based")
plt.xlabel("Log(Ilosc elementow)")
plt.ylabel("Log(Czas)")
plt.title("Enqueue")
plt.legend()

plt.subplot(2, 1, 2)
plt.loglog(elements,timesdequeue2, label="Times node based")
plt.loglog(elements,timesdequeue1, label="Times list based")
plt.xlabel("Log(Ilosc elementow)")
plt.ylabel("Log(Czas)")
plt.title("Dequeue")
plt.legend()
plt.show()

'''
Z wykresow z zlogarytmowanych wartosci czasu i elementow widzimy ze 
z dodawaniem do listy zdecydowanie lepiej radzi sobie lista co wynika z faktu iz
w node podczas dodawania element jest dopasowywany do odpowiedniego miejsca
a w liscie jest wrzucany na koniec.
W wykresow dequeue widzimy ze kolejka
oparta na wezlach od pewnego momentu zaczyna sobie radzic
lepiej niz pythonowa lista, jednak to wynika z faktu
ze ma juz posortowane wartosci a wiec sciaga tylko pierwszy
element podczas gdy kolejka z listy sortuje elementy kiedy jest to wymagane
'''
