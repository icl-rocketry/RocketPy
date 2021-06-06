# Interface class definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Interface:
    def __init__(self, 
                 component_IDs, 
                 name="None"):

        self.name = name
        self.attaching = component_IDs
        self.id = None

    
    def enforce(self):
        None

    
    def save(self, path="./interfaces/"):
        pickle.dump(self, open(path+self.name+"_"+self.id+".", "wb"))