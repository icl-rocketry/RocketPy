class Interface:
    def __init__(self, 
                 component_IDs, 
                 name="None"):

        self.name = name
        self.attaching = component_IDs

    
    def enforce(self):
        None
