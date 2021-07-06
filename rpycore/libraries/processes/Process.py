# Component superclass definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Process:
    
    def __init__(self, name="", desc="", extra_desc=""):
        
        # Defined things
        self.name = name
        self.desc = desc
        self.extra_desc = extra_desc


    def mod_desc(self, desc):
        self.desc = desc


    def mod_extra_desc(self, extra_desc):
        self.extra_desc = extra_desc
