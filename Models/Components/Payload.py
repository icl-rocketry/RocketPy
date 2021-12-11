from gpkit import Model, Variable, Vectorize, VectorVariable, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np


class Payload(Model):
    """Payload model

    Variables
    ---------
    M                       [kg]          Total Payload mass
    M_pax                   [kg]          Total Mass of passengers + crew
    M_luggage               [kg]          Total Mass of luggage
    g               9.81    [m/s^2]       Gravitational Acceleration
    
    """
    @parse_variables(__doc__, globals())
    def setup(self, pax=4, crew=2):
        # Constraints dictionary
        constraints = {}

        # Humans
        m_pax = Variable('m_pax', 100, 'kg', 'Assumed Passenger Weight')
        constraints.update({"Passengers + Crew Mass" : [
                    M_pax == m_pax * (pax + crew)                                    ]})

        # Luggage
        m_luggage = Variable('m_luggage', 27, 'kg', 'Assumed Luggage Weight')
        constraints.update({"Luggage Mass" : [
                    M_luggage == m_luggage * pax                                     ]})

        # Total Payload
        constraints.update({"Total Payload" : Tight([
                    M >= M_pax + M_luggage                                           ])})


        # Returning all constraints
        return constraints