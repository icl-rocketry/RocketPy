import pickle

class Rocket:

    def __init__ (self, name, defined_constraints={}, enforced_constraints=[]):
        self.constraints = defined_constraints
        self.name = name
        self.enf_const = enforced_constraints
        self.components = []
        self.interfaces = []
        self.latest_component_id = 1


    def add_constraint(self, key, value):
        self.constraints[key] = value


    def add_component(self, component):
        self.latest_component_id += 1
        component.id = self.latest_component_id
        self.components.append(component)


    def show_components(self):
        [print(f"Name: {i.name}\n\
                    ID: {i.id} \n\
                    Mass: {i.mass}\n\
                    Top position: {i.top_position}\n\
                    Density: {i.density}\n") for i in self.components]
    
    
    def add_interface(self, interface):
        self.interfaces.append(interface)

    
    def validate_rocket(self):
        None


    def save(self, path="./rockets/"):
            pickle.dump(self, open(path+self.name+".rpy", "wb"))

    # def load(self, name, path="./rockets/"):
    #     self = pickle.load(open(path+name+".pickle", "rb"))
    


