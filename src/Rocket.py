import pickle

class Rocket:

    def __init__ (self, name, defined_constraints={}, enforced_constraints=[]):
        self.constraints = defined_constraints
        self.name = name
        self.enf_const = enforced_constraints


    def add_constraint (self, key, value):
        self.constraints[key] = value


    def validate_rocket (self):
        None

    def save(self, path="./rockets/"):
            pickle.dump(self, open(path+self.name+".pickle", "wb"))

    # def load(self, name, path="./rockets/"):
    #     self = pickle.load(open(path+name+".pickle", "rb"))
    


