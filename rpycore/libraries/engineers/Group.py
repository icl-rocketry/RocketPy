# Group superclass definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Group:
    
    def __init__(self, group_id, engineers=[]):
        
        # Defined things
        self.group_id = group_id
        self.engineers = engineers


    def export(self, path="./exports/"):
        pickle.dump(self, open(path+self.name+"_"+self.id+".", "wb"))
