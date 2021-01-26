from potential import potential
import numpy as np

nap = [0, 1]
t_joined_pot = potential(np.array([t, a]), None)
table = np.zeros((2, 2))
for i in nap:
    for j in nap:
        table[i, j] = clinic_potentials[t].table[i, j]\
            * clinic_potentials[a].table[j]
t_joined_pot.table = table

l_joined_pot = potential(np.array([l, s]), None)
table = np.zeros((2, 2))
for i in nap:
    for j in nap:
        table[i, j] = clinic_potentials[l].table[i, j]\
            * clinic_potentials[s].table[j]
l_joined_pot.table = table

b_joined_pot = potential(np.array([b, s]), None)
table = np.zeros((2, 2))
for i in nap:
    for j in nap:
        table[i, j] = clinic_potentials[b].table[i, j]\
            * clinic_potentials[s].table[j]
b_joined_pot.table = table

e_joined_pot = potential(np.array([e, l, t, s, a]))

table = np.zeros((2, 2, 2, 2, 2))
for i in nap:
    for j in nap:
        for k in nap:
            for m in nap:
                for n in nap:
                    table[i, j, k, m, n] = clinic_potentials[e].table[i, j, k]\
                    * clinic_potentials[l].table[j][m]\
                    * clinic_potentials[t].table[k][n]\
                    * clinic_potentials[s].table[m]\
                    * clinic_potentials[a].table[n]
e_joined_pot.table = table

x_joined_pot = potential(np.array([x, e, l, t, s, a]))
table = np.zeros((2, 2, 2, 2, 2, 2))
for i in nap:
    for j in nap:
        for k in nap:
            for m in nap:
                for n in nap:
                    for o in nap:
                        table[i, j, k, m, n, o] = clinic_potentials[x].table[i, j]\
                                                * clinic_potentials[e].table[j][k][m]\
                                                * clinic_potentials[l].table[k][n]\
                                                * clinic_potentials[t].table[m][o]\
                                                * clinic_potentials[s].table[n]\
                                                * clinic_potentials[a].table[o]
x_joined_pot.table = table

d_joined_pot = potential(np.array([d, e, b, l, t, s, a]))
table = np.zeros((2, 2, 2, 2, 2, 2, 2))
dtst = []
dtsf = []
ptsd = []
ptd = []
psd = []

plbs = []
pls = []
pbs = []

pasb = []
pab = []
pb = []

d_joined_pot = potential(np.array([d, e, l, t, s, a, b]))
table = np.zeros((2, 2, 2, 2, 2, 2, 2))
for i in nap:
    for j in nap:
        for k in nap:
            for m in nap:
                for n in nap:
                    for o in nap:
                        for p in nap:
                            table[i, j, k, m, n, o, p] = clinic_potentials[d].table[i, j, p]\
                                                * clinic_potentials[e].table[j][k][m]\
                                                * clinic_potentials[l].table[k][n]\
                                                * clinic_potentials[t].table[m][o]\
                                                * clinic_potentials[s].table[n]\
                                                * clinic_potentials[a].table[o]\
                                                * clinic_potentials[b].table[p][n]
                            if i==1 and n==1:
                                dtst.append(table[i, j, k, m, n, o, p])
                            if i==1 and n==0:
                                dtsf.append(table[i, j, k, m, n, o, p])
                            if i == 1 and m == 1:
                                ptd.append(table[i, j, k, m, n, o, p])
                            if i == 1 and n == 1:
                                psd.append(table[i, j, k, m, n, o, p])
                            if i == 1 and m == 1 and n == 1:
                                ptsd.append(table[i, j, k, m, n, o, p])
                            if k == 1 and p == 1 and n == 1:
                                plbs.append(table[i, j, k, m, n, o, p])
                            if k == 1 and n == 1:
                                pls.append(table[i, j, k, m, n, o, p])
                            if p == 1 and n == 1:
                                pbs.append(table[i, j, k, m, n, o, p])
                            if p == 1:
                                pb.append(table[i, j, k, m, n, o, p])
                            if o == 1 and n == 1 and p == 1:
                                pasb.append(table[i, j, k, m, n, o, p])
                            if o == 1 and p == 1:
                                pab.append(table[i, j, k, m, n, o, p])


d_joined_pot.table = table


try:
    assert(round(np.sum(ptsd)/np.sum(d_joined_pot.table[1]), 3) == (round((np.sum(psd)/np.sum(d_joined_pot.table[1])) * (np.sum(ptd)/np.sum(d_joined_pot.table[1])), 3)))
    print("s oraz t sa niezalezne gdy znamy d")
except:
    print("s oraz t nie sa niezalezne gdy znamy d")

try:
    assert(round(np.sum(plbs)/0.5, 3) == (round((np.sum(pls)/0.5)*(np.sum(pbs)/0.5), 3)))
    print("l oraz b sa niezalezne gdy znamy s")
except:
    print("l oraz b nie sa niezalezne gdy znamy s")

try:
    assert(round(np.sum(pasb)/np.sum(pb), 3) == (round((np.sum(pab)/np.sum(pb))*(np.sum(pbs)/np.sum(pb)), 3)))
    print("a oraz s sa niezalezne gdy znamy b")
except:
    print("a oraz s nie sa niezalezne gdy znamy b")

print("Prawdopodobienstwo d=1: {:6f}, d=0: {:6f}".format(
    np.sum(d_joined_pot.table[1]), 
    np.sum(d_joined_pot.table[0]))
    )
print("Prawdopodobienstwo d=1|s=1: {:6f}, d=1|s=0: {:6f}".format(
    np.sum(dtst)/clinic_potentials[s].table[1], 
    np.sum(dtsf)/clinic_potentials[s].table[1])
    )
print("Prawdopodobienstwo d=0|s=1: {:6f}, d=0|s=0: {:6f}".format(
    1-(np.sum(dtst)/clinic_potentials[s].table[1]), 
    1-(np.sum(dtsf)/clinic_potentials[s].table[1]))
    )
