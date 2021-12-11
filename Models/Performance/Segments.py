import logging
from functools import reduce

from gpkit import Model, Variable, Vectorize, VectorVariable, parse_variables, ureg as u
from gpkit.constraints.tight import Tight
import numpy as np

from .State import State


class Takeoff(Model):
    """Takeoff model

    Variables
    ---------
    TOP                             [kg/m^2]      Takeoff Parameter
    FL              fl              [m]           Field Length
    CL_max_TO                       [-]           Maximum Lift Coefficient | Takeoff
    g               9.81            [m/s^2]       Gravitational Acceleration
    
    """
    @parse_variables(__doc__, globals())
    def setup(self, M_segment, aircraft=None, CL_max=2.1, CL_clean=1.5, fl=1200):
        # Importing Aircraft() parameters - TODO: remove temporary exception
        try:
            TW          = self.TW           = aircraft.T0_W0
            WS          = self.WS           = aircraft.W0_S
            CL_max      = self.CL_max       = aircraft.CL_max
            CL_clean    = self.CL_clean     = aircraft.CL_clean

            logging.info("Aircraft() parameters are now linked")

        except AttributeError:
            logging.warning("Aircraft() object not found. Using default values.")
            
            TW          = self.TW           = Variable("TW",    "",         "Thrust to Weight ratio")
            WS          = self.WS           = Variable("WS",    "N/m^2",    "Wing Loading")
        
        # Constraints dictionary
        constraints     = self.constraints  = {}
        
        # Takeoff Parameter - TOP
        k1 = self.k1 = Variable('k', 37.5, 'ft^3/lb', 'Some Random Constant')
        constraints.update({"Takeoff Parameter" : [
                    TOP == FL / k1                                                        ]})
        
        # CL max at takeoff
        constraints.update({"Lift Coeffcient | Takeoff" : [
                    CL_max_TO == CL_clean + 0.7 * (CL_max - CL_clean)                     ]})

        # Thrust to Weight ratio
        constraints.update({"Thrust to Weight constraint" : [
                    TW >= WS / ((CL_max_TO * g * TOP) / 1.21)                             ]})

        # Fuel fraction for takeoff
        fuel_frac = self.fuel_frac = 0.97

        # Ensure M_end / aircraft.M_start == fuel_frac
        constraints.update({"Fuel Fraction | Takeoff" : [
                    M_segment[1]/M_segment[0] == fuel_frac                              ]})

        # Add bounding constraints
        self.boundaries()
        
        # Returning all constraints
        return constraints


    def boundaries(self):
        constraints = {}

        ### TODO: remove temporary bound constraints
        constraints.update({"Minimum Wing Loading" : [
                    self.WS >= 0.1 * u.N / u.m**2]})

        constraints.update({"Maximum Thrust to Weight" : [
                    self.TW <= 1]})

        self.constraints.update({"Boundaries": constraints})



class Climb(Model):
    """Climb model (general)
    Variables
    ---------
    CL                              [-]           Lift Coefficient | Climb
    CDi_climb                       [-]           Induced Drag Coefficient | Climb

    """
    @parse_variables(__doc__, globals())
    def setup(self, M_segment, dCd0, de, climb_gradient, aircraft=None, CL_max=2.1, CL_clean=1.5, goAround=False):
        # Importing Aircraft() parameters - TODO: remove temporary exception
        try:
            self.aircraft = aircraft

            TW          = self.TW           = aircraft.T0_W0
            CL_max      = self.CL_max       = aircraft.CL_max
            CL_clean    = self.CL_clean     = aircraft.CL_clean
            AR          = self.AR           = aircraft.AR
            e           = self.e            = aircraft.e
            Cd0         = self.Cd0          = aircraft.Cd0
        
            logging.info("Aircraft() parameters are now linked")
        
        except AttributeError:
            logging.warning("Aircraft() object not found. Using default values.")

            TW          = self.TW           = Variable("TW",    "",     "Thrust to Weight ratio")
            AR          = self.AR           = Variable("AR",    "",     "Aspect Ratio")
            e           = self.e            = Variable("e",     "",     "Oswald Efficiency")
            Cd0         = self.Cd0          = Variable("Cd0",   "",     "Zero-Lift Drag Coefficient")

        Cd0_climb   = self.Cd0_climb   = Variable("Cd0_climb",      Cd0 + dCd0,     "",     "Variation in Cd0")
        e_climb     = self.e_climb     = Variable("e_climb",        e + de,         "",     "Variation in Oswald efficiency")
        
        constraints = self.constraints = {}
        
        # Switch between initial climb vs go-around climb
        CL_climb = {"Go-around CL|CLimb" : [CL == CL_max]} if goAround else {"Initial CL|Climb" : [CL == CL_clean + 0.7 * (CL_max - CL_clean)]}
        constraints.update(CL_climb)

        # Induced Drag Coefficient
        constraints.update({"Induced Drag Coefficient | Climb" : [
                    CDi_climb == (CL ** 2)/(np.pi * AR * e_climb)                                              ]})


        constraints.update({"Thrust to Weight constraint" : [
                    TW >= (Cd0_climb + CDi_climb) / CL + climb_gradient/100                                    ]})

        # Fuel Fraction for climb
        fuel_frac = self.fuel_frac = 0.985

        # Ensure M_end / aircraft.M_start == fuel_frac
        constraints.update({"Fuel Fraction | Climb" : [
                    M_segment[1]/M_segment[0] == fuel_frac                                                   ]})

        # Add bounding constraints
        self.boundaries()
        
        return constraints

    
    def boundaries(self):
        constraints = []

        ### TODO: remove temporary lower bound constraints
        constraints += [self.Cd0_climb >= 1e-6]
        constraints += [self.TW <= 1]
        # constraints += [self.AR <= 50]

        self.constraints.update({"Boundaries": constraints})



class Climb_GoAround(Climb):
    def setup(self, M_segment, dCd0, de, climb_gradient, aircraft):
        return super().setup(M_segment, dCd0, de, climb_gradient, aircraft, goAround=True)



class Cruise(Model):
    """Cruise model
    
    Variables
    ---------
    beta                            [-]             Thrust Lapse
    LD                              [-]             Optimum Lift-Drag | Cruise
    R           cruise_range        [km]            Cruise Range
    M_end                           [kg]            End Mass | Cruise

    """
    @parse_variables(__doc__, globals())
    def setup(self, M_segment, cruise_range=2700*u.km, alpha=0.955, n=1, state=None, aircraft=None):
        # Importing Aircraft() parameters - TODO: remove temporary exception
        try:
            self.aircraft = aircraft

            TW          = self.TW           = aircraft.T0_W0
            AR          = self.AR           = aircraft.AR
            e           = self.e            = aircraft.e
            Cd0         = self.Cd0          = aircraft.Cd0
            WS          = self.WS           = aircraft.W0_S

            logging.info("Aircraft() parameters are now linked")
        
        except AttributeError:
            logging.warning("Aircraft() object not found. Using default values.")

            TW          = self.TW           = Variable("TW",    "",         "Thrust to Weight ratio")
            AR          = self.AR           = Variable("AR",    "",         "Aspect Ratio")
            e           = self.e            = Variable("e",     "",         "Oswald Efficiency")
            Cd0         = self.Cd0          = Variable("Cd0",   "",         "Zero-Lift Drag Coefficient")
            WS          = self.WS           = Variable("WS",    "N/m^2",    "Wing Loading")
        
        # Held in State but initialised in the 'parent' Segment() class - Variable type
        try:
            rho             = state.rho
            sigma           = state.sigma
            V_inf           = state.V_inf
            alt             = state.alt
            climb_rate      = state.climb_rate
        except AttributeError:
            rho             = Variable("rho",          1.22,            "kg/m^3",    "Density")
            sigma           = Variable("sigma",        0.246,           "",          "Aggregate fuel fraction")
            V_inf           = Variable("V_inf",        220,             "m/s",       "Cruising Velocity")
            alt             = Variable("alt",          40000,           "ft",        "Altitude")
            climb_rate      = Variable("climb_rate",   0,               "m/s",       "Climb Rate")

        constraints = {}
        
        # Switch Thrust Lapse calculations depending on altitude
        beta_Calculated = {"Thrust Lapse Troposphere" : [beta == sigma ** 0.7]} if alt <= 11000*u.m else {"Thrust Lapse Stratosphere" : [beta == 1.439 * sigma ]}
        constraints.update(beta_Calculated)

        term1 = (1.0 / V_inf) * climb_rate

        # Neglect term 2 of S 2.2.9        

        term3 = (0.5 * rho * (V_inf**2) * Cd0) / (alpha * WS)
        term4 = (alpha * (n**2) * WS) / (0.5 * rho * (V_inf**2) * np.pi * AR * e)

        # Applying constraint
        constraints.update({"Thrust to Weight Constraint | Cruise" : [
                    TW >= (alpha / beta) * (term1 + term3 + term4)                                                 ]})


        # Fuel fraction for cruise - Breguet Range relation (S 1.3-2)
        constraints.update({"Optimum LD": [LD  == 0.866 * aircraft.LD_max]})
        c   = self.c    = aircraft.str_engine.sfc_cruise

        # 4th order taylor approximation for e^x - because apparently e^x is not allowed in GP :(        
        ln_breguet      = R * c / (V_inf * LD)
        fuel_frac       = self.fuel_frac = 1 + reduce(lambda x,y: x+y, [ln_breguet**i/np.math.factorial(i) for i in range(1, 10)])

        # Ensure M_end / aircraft.M_start == fuel_frac -----> EXCEPTION HERE!!! -ve sign in Breguet
        constraints.update({"Fuel Fraction | Cruise" : Tight([
                    M_segment[0]/M_segment[1] >= fuel_frac                                                          ])})

        return constraints

    # For reference, the following is the original code
    # def __Breguet_range(self, segment_state, c, LD):
    #     '''Evaluates weight fraction for a given flight regime'''

    #     # Equation S 1.3-2 - Breguet range
    #     return np.exp(-segment_state["Range"] * c / (segment_state["Speed"] * LD))

    
    # def __Breguet_endurance(self, segment_state, c, LD):
    #     return np.exp(- segment_state["Endurance"] * c / LD )



class Landing(Model):
    """Landing model

    Variables
    ---------
    V_stall                              [m/s]         Target Stall Speed | Landing
    FL                   1200            [m]           Field Length | Landing
    SL_density           1.225           [kg/m^3]      Sea Level Density | Landing

    """
    @parse_variables(__doc__, globals())
    def setup(self, M_segment, aircraft=None, CL_max=2.1):
        # Importing Aircraft() parameters - TODO: remove temporary exception
        try:
            WS          = aircraft.W0_S
            CL_max      = aircraft.CL_max
        
        except AttributeError:
            WS          = Variable("WS",        "N/m^2",    "Wing Loading")
            CL_max      = Variable("CL_max",    "",         "Maximum Lift Coefficient")
        
        # Define emprical constant
        k = Variable('k', 0.5136, 'ft/kts^2', 'Landing Empirical Constant')

        # Define the constraint dictionary
        constraints =  {}

        # Define V_stall
        constraints.update({"Target Stall Speed" : [
                    V_stall == (FL / k) ** 0.5         ]})

        # Max Wing Loading constraint
        constraints.update({"Max Wing Loading" : [
                    WS <= (0.5 * SL_density * (V_stall**2) * CL_max)      ]})

        # Fuel Fraction for landing
        fuel_frac = self.fuel_frac = 0.995

        # Ensure M_end / aircraft.M_start == fuel_frac
        constraints.update({"Fuel Fraction | Landing" : [
                    M_segment[1]/M_segment[0] == fuel_frac                                                         ]})
        
        # Returning all constraints
        return constraints


# TODO: Implement following models
# Descent
# Loiter


# General Segment model - couples flight segment with the aircraft model and state
class Segment(Model):
    def setup(self, Aircraft):
        constraints = []
        return [constraints]
