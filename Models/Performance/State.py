from gpkit import Model, Vectorize, VectorVariable, parse_variables,  ureg as u
from gpkit.constraints.tight import Tight
from gpkit.nomials.variables import Variable
import numpy as np
# from ambiance import Atmosphere
# from .. import sealevel


class State(Model):
    """Context for evaluating flight physics

    Variables
    ---------
    V            [knots]    True Airspeed
    alt          [m]        Altitude

    """
    @parse_variables(__doc__, globals())
    def setup(self, alt):

        # Maybe better to have a vector for atmospheric states?
        
        mu = Variable("mu", Atmosphere(alt).dynamic_viscosity, "N*s/m^2", "")

        atmosphere = Atmosphere(alt.to(u.m).magnitude)
        self.rho = atmosphere.density * (u.kg / u.m**3)
        rho0 = sealevel.density * (u.kg / u.m**3)
        self.sigma = self.rho / rho0

        pass