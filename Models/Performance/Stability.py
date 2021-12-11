from gpkit import Model, Variable, VectorVariable, Vectorize, parse_variables
from gpkit.constraints.tight import Tight
from gpkit import ureg as u
import numpy as np


class Stability(Model):
    """Stability model

    Variables
    ---------

    """
    @parse_variables(__doc__, globals())
    def setup(self):
        constraints = self.constraints  = []

        return [constraints]


    def calc_static_margin(x_np, x_cg, c_bar, aircraft):
        """calc_static_margin
            Arguments:  longitudinal position of neutral point,
                        longitudinal position of centre of gravity,
                        mean chord of the wing,

            Return: static margin of aircraft without thrust, SM of AC with thrust
        """

        return None