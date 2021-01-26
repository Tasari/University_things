#%% Empty potentials data

from potential import potential
import numpy as np

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

#%%tests
assert(clinic_potentials[e].table[positive, positive, positive] == 1)
assert(clinic_potentials[x].table[positive, negative] == 0.05)
assert(clinic_potentials[d].table[negative, positive, negative] == 0.3)
assert(clinic_potentials[t].table[negative, negative] == 0.99)