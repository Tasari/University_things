import matplotlib.pyplot as plt
import numpy as np

import explosion_data_creator as data
from potential import potential
from variable import variable

amount_of_collectors = 5
data_collectors = data.create_data_collectors(amount_of_collectors)
explosion = data.explode()

std = 0.1
observations = data.observe(data_collectors, explosion, std)

accuracy=0.01
all_possible_states = np.arange(-1, 1.001, accuracy)
amount_of_states = len(all_possible_states)

variable = [variable(), variable()]

variable[0].name, variable[1].name = 'ex', 'ey'
variable[0].domain, variable[1].domain = all_possible_states, all_possible_states

potential = potential()
potential.variables = np.array([0, 1])
table = np.zeros((amount_of_states, amount_of_states))
const_1 = 1/(2*std)
const_2 = np.sqrt(np.pi*const_1)
for x in range(amount_of_states):
    for y in range(amount_of_states):
        work_e = [-1+accuracy*x, -1+accuracy*y]
        p=1
        e_distance = data.squared_distance(work_e, [0, 0])
        if e_distance<1:
            work_distances = [data.squared_distance(data_collectors[z], work_e) for z in range(amount_of_collectors)]
            distances = [1/(work_distances[x]+0.1) for x in range(amount_of_collectors)]
            work_p = [np.exp((-1/const_1)*(observations[x] - distances[x])**2)/const_2 for x in range(amount_of_collectors)]
            for z in range(amount_of_collectors):
                p = p*work_p[z]
        else:
            p=0
        table[x, y] = p

potential.table = table/np.sum(table)

maximum = np.amax(potential.table)
arg_maximum = np.argmax(potential.table)
indexes = np.unravel_index(np.argmax(potential.table), potential.table.shape)
estimated_ex = -1 + accuracy * indexes[0]
estimated_ey = -1 + accuracy * indexes[1]

x = np.arange(-1, 1.001, accuracy)
y = np.arange(-1, 1.001, accuracy)
X, Y = np.meshgrid(x, y)
plt.figure(figsize=(7, 6))
plt.contourf(Y, X, (potential.table), 20)
plt.colorbar()
plt.plot(explosion[0], explosion[1], 'D', color='yellow', label='Explosion')
plt.plot(data_collectors[:,0], data_collectors[:,1], 'ro', label='Collector')
plt.ylabel('y')
plt.xlabel('x')
plt.show()