# Rocket class definition
# Maintained by Raihaan Usman and Luis Marques

from libraries.components.Component import Component as Component
import pickle, os


class Rocket:

    def __init__ (self, name, defined_constraints={}, enforced_constraints=[]):
        self.name = name
        self.constraints = defined_constraints                                          # Constraints defined in Mission Analyser
        self.enf_const = enforced_constraints                                           # List of required constraints (IDs) derived from rocket objectives

        # Derived
        self.components = []
        self.interfaces = []
        self.latest_component_id = 0                                                    # Counters - persistent with Rocket object
        self.latest_interface_id = 0


    # Constraint methods
    def add_constraint(self, key, value):
        self.constraints[key] = value

    
    # Component methods
    def create_component(self, name):
        component = Component(name)
        self.latest_component_id += 1
        component.id = self.latest_component_id
        self.components[component.id] = component


    def show_components(self):
        [print(f"Name: {i.name}\n\
                    ID: {i.id} \n\
                    Mass: {i.mass}\n\
                    Top position: {i.top_position}\n\
                    Density: {i.density}\n") for i in self.components]
    

    # Interface methods
    def add_interface(self, interface):
        self.latest_interface_id += 1
        interface.id = self.latest_interface_id
        self.interfaces[interface.id] = interface


    def show_interfaces(self):
        [print(f"Type: {i.name}\n\
                    Attached component IDs: {i.attached} \n\
                    Attached component names: {self.components[i.attached]}") for i in self.interfaces]

    
    # Rocket self-validation method
    def validate_rocket(self):
        None


    # Save!
    def save(self, path="./rockets/"):
        try:
            pickle.dump(self, open(path+self.name+"/"+self.name+".rpy", "wb"))
        
        except FileNotFoundError:
            os.mkdir(path+self.name)
            pickle.dump(self, open(path+self.name+"/"+self.name+".rpy", "wb"))
