from gpkit import Model, Variable, VectorVariable, Vectorize, parse_variables
from gpkit.constraints.tight import Tight
from gpkit import ureg


class Regulations(Model):
    """FAR25 airworthiness regualtions - for commercial transport aircraft 

    Variables
    ---------------

    """
    def setup(self, aircraft):

        # All operational constraints go here - returned at end


        return []