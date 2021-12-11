from gpkit import Model, Variable, VectorVariable, Vectorize, parse_variables
from gpkit.constraints.tight import Tight
from gpkit import ureg


class Empennage(Model):
    """Empennage model

    Variables
    ---------
    M         [kg]          Mass

    """
    @parse_variables(__doc__, globals())
    def setup(self):
        constraints = []
        components = self.components = []

        # Empennage weight is sum of its components - note the tight constraint
        if len(components) > 0:
            constraints += [Tight([M >= sum(comp.M for comp in components)])]


        return [constraints, components]