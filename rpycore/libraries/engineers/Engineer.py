# Engineer class definition
# Maintained by Raihaan Usman and Krish Nair

import pickle


class Engineer:
    
    def __init__(self, name, shortcode, year=1, tools=[], exp=0):

        #Defined
        self.name = name
        self.shortcode = shortcode
        self.year = year
        self.tools = tools
        self.exp = exp


    def export(self, path="./libraries/engineers/"):
        pickle.dump(self, open(path+self.name+"_"+self.id+".", "wb"))



