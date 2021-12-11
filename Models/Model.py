from gpkit import Model, Variable, Vectorize, VectorVariable, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np


class Rocket_Model(Model):
    None