import numpy as np

class potential():
    def __init__(self, variables=np.array([]), table=np.array([])):
        self.variables = variables
        self.table = table

    def __repr__(self):
        return "<Potential object: Variables: {}, table: {}>".format(self.variables, self.table)

if __name__ == "__main__":
    cancer = 2
    cancer_domain = ['Present', 'Not present']
    cancer_present = 1
    cancer_not_present = 0
    chance_of_cancer_presence = 0.35

    cancer_potential = potential(
        np.array([cancer]), 
        np.array([chance_of_cancer_presence, 1-chance_of_cancer_presence]),
    )
    print(cancer_potential)