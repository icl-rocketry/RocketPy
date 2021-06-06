# Rocket class definition
# Maintained by Raihaan Usman and Luis Marques

import pickle


class Rocket:

    def __init__ (self, name, defined_constraints={}, enforced_constraints=[]):
        self.name = name
        self.constraints = defined_constraints
        self.enf_const = enforced_constraints

        # Derived
        self.components = {}
        self.interfaces = {}
        self.latest_component_id = 0                                                    # Counters - persistent with Rocket object
        self.latest_interface_id = 0


    def add_constraint(self, key, value):
        self.constraints[key] = value


    def add_component(self, component):
        self.latest_component_id += 1
        component.id = self.latest_component_id
        self.components[component.id] = component


    def show_components(self):
        [print(f"Name: {i.name}\n\
                    ID: {i.id} \n\
                    Mass: {i.mass}\n\
                    Top position: {i.top_position}\n\
                    Density: {i.density}\n") for i in self.components]
    
    
    def add_interface(self, interface):
        self.latest_interface_id += 1
        interface.id = self.latest_interface_id
        self.interfaces[interface.id] = interface


    def show_interfaces(self):
        [print(f"Name: {i.name}\n\
                    ID: {i.id} \n\
                    Mass: {i.mass}\n\
                    Top position: {i.top_position}\n\
                    Density: {i.density}\n") for i in self.components]

    
    def validate_rocket(self):
        None


    def save(self, path="./rockets/"):
            pickle.dump(self, open(path+self.name+".rpy", "wb"))

    


