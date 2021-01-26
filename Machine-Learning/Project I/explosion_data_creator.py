import numpy as np
import sys

def squared_distance(a, b, variables=2):
    return sum([(a[x]-b[x])**2 for x in range(variables)])

def create_data_collectors(amount):
    places = sorted([np.random.rand()*np.pi*2 for x in range(0,amount)])
    vertical = np.sin(places)
    horizontal = np.cos(places)
    return np.array([(vertical[x], horizontal[x]) for x in range(0, amount)])

def explode():
    angle = 2*np.pi*np.random.rand()
    temp = np.random.rand()+np.random.rand()
    if temp>1:
        r=2-temp
    else:
        r=temp
    return r*np.cos(angle), r*np.sin(angle)
    
def observe(data_collectors, explosion, std=0.2):
    amount = len(data_collectors)
    distances = np.array(
        [squared_distance(data_collectors[x], explosion) 
         for x in range(amount)]
    )
    observations = 1/(distances+0.1)
    return [
        observations[x] + np.random.normal(0, std) for x in range(amount)
    ]