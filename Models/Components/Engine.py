from gpkit import Model, Vectorize, VectorVariable, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np


class EnginePerformance(Model):
    """Engine performance model

    Variables
    ---------


    """
    @parse_variables(__doc__, globals())
    def setup(self, engine):
        return None


class Engine(Model):
    """Engine model

    Variables
    ---------
    M               1500       [kg]            Mass
    sfc_cruise      0.8        [1/hr]          Specific Fuel Consumption at Cruise
    sfc_loiter      0.7        [1/hr]          Specific Fuel Consumption at Loiter
    
    """
    @parse_variables(__doc__, globals())
    def setup(self):
        constraints = self.constraints  = []
        components  = self.components   = []

        # Engine weight is sum of its components - note the tight constraint
        # constraints += [Tight([W >= sum(comp.W for comp in components)])]


        return [constraints, components]


# Aliases
class Starboard_Engine(Engine):
    def setup(self): return super().setup()


class Port_Engine(Engine):
    def setup(self): return super().setup()
