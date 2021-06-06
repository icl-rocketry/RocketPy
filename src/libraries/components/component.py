# Component superclass definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Component:
    
    def __init__(self, name):
        
        # Defined things
        self.name = name
        self.material = "None"

        # Derived things
        self.top_position = []                                                      # [X, r and phi] coordinate representation
        self.density = 0
        self.mass = 0
        self.parameters = {}                                                        # {Parameter_name: [value, units]}
        self.subparts = []
        self.id = None


    def load_parameters(self, parameters):
        self.parameters = self.parameters | parameters                              # For Python>=3.9 - not backwards compatible!!


    def add_subpart(self, subpart):
        self.subparts.append(subpart)                                               # List of child component objects


    def export(self, path="./exports/"):
        pickle.dump(self, open(path+self.name+"_"+self.id+".", "wb"))
