# Main component superclass

class Component:

    def __init__(self,                     # Ensure passed with completed params
                name,
                material,
                density,
                mass,
                top_position,              # [X, r and phi] coordinate representation
                **args, **kwargs           # For additional params
                ):

        self.name = name
        self.material = material
        self.density = density
        self.mass = mass
        self.top_position = top_position


    def render(self):
        pass
