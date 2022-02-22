
from abc import ABC, abstractmethod


"""

Hierarchy
---------
Level 0 - Base Objectives
Level 1 - Top Level Requirements
Level 2 - 


"""


class Requirement(ABC):
    """
    This abstract class provides the template for all requirements used in RocketPy!

    Abstract Properties:
    ----------
    ID : str
        Requirement unique ID
    description : str
        Description of requirement
    value : auto
        Associated value (Default None)
    level : int
        Hierarchy level of requirement
    type : str
        Type of requirement - functional or non-functional
    validation : Validator
        Validator object for requirement
    status : 
        Status of the requirement

    Notes
    -----
        - Every requirement has a validation object - interfaces with downstream requirements and/or parameters, also external libaraies


    Abstract Methods
    -------


    """

    @property
    def UID(self):
        return self._UID

    @property
    def description(self):
        return self._description

    @property
    def level(self):
        return self._level

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status


    # Setters

    @UID.setter
    def UID(self, value):
        self._UID = value
    
    @description.setter
    def description(self, value):
        self._description = value
    
    @level.setter
    def level(self, value):
        self._level = value
    
    @type.setter
    def type(self, value):
        self._type = value

    # @status.setter
    # def status(self, value):
    #     self._status = value

    
    


# Top level requirement class
class TopReq(Requirement):
    """
    Top level requirement class.

    """

    @property
    def type(self):
        return "Top"



class Constraint(Requirement):
    """
    Constraint class.

    """

    @property
    def type(self):
        return "Constraint"




