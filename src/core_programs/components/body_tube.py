# Body tube standard template definition

from component import Component


class BodyTube(Component):
    def __init__(self,
                 name = "Body Tube",
                 top_position = [0, 0, 0],
                 material = "",
                 density = 0,
                 mass = 0,
                 length = 0,
                 InnerD = 0,
                 OuterD = 0,
                 ):

        super.__init__(
            name,
            material,
            density,
            mass,
            top_position
        )

        self.length = length
        self.InnerD = InnerD
        self.OuterD = OuterD


    # def render(self):
    #     pass