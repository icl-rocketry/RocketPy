from gpkit import Model, Variable, VectorVariable, Vectorize, parse_variables
from gpkit.constraints.tight import Tight
from gpkit import ureg


class Cabin(Model):
    """Cabin model

    Variables
    ---------
    M                      [kg]        Mass

    """
    @parse_variables(__doc__, globals())
    def setup(self):
        constraints = []
        components = self.components = []

        # Fuselage weight is sum of its components - note the tight constraint means equality
        if len(components) > 0:
            constraints += [Tight([M >= sum(comp.M for comp in components)])]

        return [constraints, components]



class Fuselage(Model):
    """Fuselage model

    Variables
    ---------
    M  [kg]   Mass
    t  [in]   wall thickness
    b  [in]   width
    h  [in]   height

    """
    @parse_variables(__doc__, globals())
    def setup(self):
        constraints = []
        components  = self.components   = []

        cabin       = self.cabin        = Cabin()
        components  += [cabin]

        # Fuselage weight is sum of its components - note the tight constraint means equality
        if len(components) > 0:
            constraints += [Tight([M >= sum(comp.M for comp in components)])]

        return [constraints, components]
