import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class variable():
    """
    Class holding data about variable
    """
    def __init__(self, name='', domain=[]):
        self.name = name
        self.domain = domain

    def __repr__(self):
        return "Name of variable: {}, list of possible outcomes: {}".format(self.name, self.domain)

class potential():
    def __init__(self, variables=np.array([]), table=np.array([])):
        self.variables = variables
        self.table = table

    def __repr__(self):
        return "<Potential object: Variables: {}, table: {}>".format(self.variables, self.table)

variables_amount = 8

#All variables
a, s, b, t, l, e, x, d = (i for i in range(variables_amount))
list_of_variables = [a, s, b, t, l, e, x, d] 

#String(List) of all variables for easier filling
string_variables_list = 'asbtlexd'

'''
States of variables, i decided we can divide all variables into negative
and positive state, it enables easier filling of initial table.
e.g. Smoker? Positive (Smokes), Lung Cancer? Negative(Not ill)
'''
negative, positive = (0, 1)

clinic_variables = [variable(
   letter, [negative, positive]
   ) for letter in string_variables_list]

#Check if variable Clinic_variables[var].name = "var", to assert valid assigning
for variable, variable_str in zip(list_of_variables, string_variables_list):
   assert(clinic_variables[variable].name == variable_str)
   assert(clinic_variables[variable].domain == [0, 1])

clinic_potentials = [potential()for i in range(variables_amount)]

clinic_potentials[a].variables=np.array([a])
clinic_potentials[s].variables=np.array([s])

table = np.zeros(2)
table[negative] = 0.99
table[positive] = np.round(1 - table[negative], 2)#rounding all subtractions because d variable after subtraction was 0.30000000000000004 so it's numpy float error 
clinic_potentials[a].table = table

table = np.zeros(2)
table[negative] = 0.5
table[positive] = np.round(1 - table[negative], 2)
clinic_potentials[s].table = table

clinic_potentials[t].variables = np.array([t, a])
table = np.zeros((2, 2))
table[positive, negative] = 0.01
table[positive, positive] = 0.05
clinic_potentials[t].table = table
clinic_potentials[t].table[negative][:] = np.round(1-clinic_potentials[t].table[positive], 2)

clinic_potentials[l].variables = np.array([l, s])
table = np.zeros((2, 2))
table[positive, negative] = 0.01
table[positive, positive] = 0.1
clinic_potentials[l].table = table
clinic_potentials[l].table[negative][:] = np.round(1-clinic_potentials[l].table[positive], 2)

clinic_potentials[b].variables = np.array([b, s])
table = np.zeros((2, 2))
table[positive, negative] = 0.3
table[positive, positive] = 0.6
clinic_potentials[b].table = table
clinic_potentials[b].table[negative][:] = np.round(1-clinic_potentials[b].table[positive], 2)


clinic_potentials[e].variables = np.array([e, t, l])
table = np.zeros((2, 2, 2))
table[positive, negative, negative] = 0
table[positive, positive, negative] = 1
table[positive, negative, positive] = 1
table[positive, positive, positive] = 1
clinic_potentials[e].table = table
clinic_potentials[e].table[negative][:][:] = np.round(1-clinic_potentials[e].table[positive][:], 2)


clinic_potentials[x].variables = np.array([x, e])
table = np.zeros((2, 2))
table[positive, negative] = 0.05
table[positive, positive] = 0.98
clinic_potentials[x].table = table
clinic_potentials[x].table[negative][:] = np.round(1-clinic_potentials[x].table[positive], 2)

clinic_potentials[d].variables = np.array([d, e, b])
table = np.zeros((2, 2, 2))
table[positive, negative, negative] = 0.1
table[positive, positive, negative] = 0.7
table[positive, negative, positive] = 0.8
table[positive, positive, positive] = 0.9
clinic_potentials[d].table = table
clinic_potentials[d].table[negative][:][:] = np.round(1-clinic_potentials[d].table[positive][:], 2)

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

g = nx.DiGraph()
g.add_node('a')
g.add_node('s')
g.add_node('t')
g.add_node('l')
g.add_node('b')
g.add_node('e')
g.add_node('x')
g.add_node('d')
g.add_edge('s', 'b')
g.add_edge('s', 'l')
g.add_edge('a', 't')
g.add_edge('t', 'e')
g.add_edge('l', 'e')
g.add_edge('e', 'x')
g.add_edge('e', 'd')
g.add_edge('b', 'd')

nx.draw(g, pos=nx.kamada_kawai_layout(g), with_labels=True, node_size = 1000)
plt.show()