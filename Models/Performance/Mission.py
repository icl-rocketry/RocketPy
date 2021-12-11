from gpkit import Model, Vectorize, VectorVariable, constraints, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np
from functools import reduce

from .Segments import *


class Mission(Model):
    """A sequence of flight segments according to Target Mission Profile

    Variables
    ---------
    aggregate           [-]         End / Takeoff Mass ratio

    """
    @parse_variables(__doc__, globals())
    def setup(self, aircraft=None):
        self.aircraft   = aircraft
        constraints     = self.constraints   = []
        mission         = self.mission       = []

        # TODO: 8 is hardcoded. This should be a parameter!
        M_segments = VectorVariable(7, "M", "kg", "Mass at end of each segment")
        constraints += [M_segments[0] == aircraft.M_0]
        # All M_segments[i] must be greater than M_segments[i-1]
        constraints += [M_segments[i] <= M_segments[i-1] for i in range(1, 7)]
        
        # Final mass must be greater than M_dry
        # constraints += [M_segments[-1] >= aircraft.M_dry]
        
        # TODO: link to Streamlit frontend - session_state.mission_profile
        takeoff = self.takeoff  = Takeoff(M_segments[:2], aircraft=aircraft) 
        climb   = self.climb    = Climb(M_segments[1:3], 0.04, 0.05, 0.1, aircraft=aircraft)
        cruise  = self.cruise   = Cruise(M_segments[2:4], aircraft=aircraft)
        # descent = self.descent  = Descent(aircraft=aircraft)
        climb2  = self.climb2   = Climb_GoAround(M_segments[3:5], 0.04, 0.05, 0.1, aircraft=aircraft)
        cruise2 = self.cruise2  = Cruise(M_segments[4:6], aircraft=aircraft)
        # loiter  = self.loiter   = Loiter(aircraft=aircraft)
        landing = self.landing  = Landing(M_segments[5:], aircraft=aircraft)

        mission += [takeoff, climb, cruise, climb2, cruise2, landing]

        # Aggregate fuel fraction
        # ag = reduce(lambda x, y: x * y, [fs.fuel_frac for fs in mission])
        # constraints += Tight([M_segments[0] >= M_segments[-1] + aircraft.M_fuel/1.01])
        constraints += Tight([M_segments[-1] >= aircraft.M_dry * 1.06])

        return {"Top-level constraints": constraints}, mission
