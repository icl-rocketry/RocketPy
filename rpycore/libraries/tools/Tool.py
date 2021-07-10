# Tool class definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Tool:
    
    def __init__(self, name, usage_notes=""):
        
        # Defined things
        self.name = name
        self.usage_notes = usage_notes
        

    def export(self, path="./exports/"):
        pickle.dump(self, open(path+self.name+"_"+self.id+".", "wb"))
