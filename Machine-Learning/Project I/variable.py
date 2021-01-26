class variable():
    """
    Class holding data about variable
    """
    def __init__(self, name='', domain=[]):
        self.name = name
        self.domain = domain

    def __repr__(self):
        return "Name of variable: {}, list of possible outcomes: {}".format(self.name, self.domain)

if __name__=='__main__':
    illness = variable("Cancer", ['Yes', 'No'])
    print(illness)
    illness = variable()
    print(illness)
    illness.name = "Cancer"
    illness.domain = ["Yes", "No"]
    print(illness)