from .Payload       import *

from gpkit import Model, Vectorize, VectorVariable, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np


class RocketPerformance(Model):
    """Rocket performance model

    Variables
    ---------

    """
    @parse_variables(__doc__, globals())
    def setup(self, rocket, state):
        self.rocket     = rocket
        self.state      = state
        perf_models     = self.perf_models  = []

        perf_models     += None
        

        # W               = rocket.W
        # S               = rocket.wing.S
        # V               = state.V
        # rho             = state.rho
        
        return {"Performance": perf_models}


class Rocket(Model):
    """The rocket model

    Variables
    ---------
    M_0                         [kg]          Total Mass
    M_fuel                      [kg]          Starting Fuel Mass
    M_dry                       [kg]          rocket Dry Mass


    """
    @parse_variables(__doc__, globals())
    def setup(self, CL_max=2.1, CL_clean=1.5, AR=7.5, e=0.9):
        components      = self.components   = []
        systems         = self.systems      = []
        constraints     = self.constraints  = {}

        # Hyperparameters from the user - TODO: remove these
        # self.CL_max     = CL_max
        # self.CL_clean   = CL_clean
        # self.AR         = AR
        # self.e          = e

        payload         = self.payload      = Payload()
        
        components      += [payload]
        
        constraints.update({"Dry Mass" : Tight([
                    M_dry >= sum(c.M for c in self.components) + sum(s.M for s in systems)])})
        
        constraints.update({"Total Mass" : Tight([
                    M_0 >= M_fuel + M_dry])}) 

        # Add bounding constraints - temporary
        self.boundingConstraints()

        return [constraints, components]

    # Dynamic performance model - clones rocketPerformance()
    dynamic = RocketPerformance


    def boundingConstraints(self):
        constraints = {}

        ### TODO: remove temporary lower bound constraints

        # constraints.update({"Minimum Fuel Mass" : [
        #             self.M_fuel >= 10 * u.kg, self.M_fuel <= 100000 * u.kg]})

        # # Minimum Cd0
        # constraints.update({"Minimum Cd0" : [
        #             self.Cd0 >= 1e-6]})

        # self.constraints.update({"Boundary Constraints": constraints})
