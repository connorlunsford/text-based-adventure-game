from interactable import Interactable
from object import Object

class FeatureException(Exception):
    """Base exception class for the Feature class"""
    pass

class AttributeDoesNotExist(FeatureException):
    """Raised when attribute does not exist"""
    pass

class AttributeAlreadyExists(FeatureException):
    """Raised when attribute already exists"""
    pass

class Feature(Object):

    def __init__(self, id: str, name: str, desc: str, sdesc: str, interactions: dict, hidden: bool):
        super().__init__(id, name, desc, sdesc, interactions, hidden)

    # methods for managing the optional condition variable
    def add_condition(self, condition: bool):
        """adds an optional condition attribute to the object with the value
        provided in the condition argument if self._condition does not already
        exist; if self._condition already exists, this method raises an exception"""
        if not hasattr(self, "_condition"):
            self._condition = condition
        else:
            raise AttributeAlreadyExists

    def get_condition(self):
        """returns the value of self._condition if self._condition exists;
        if self._condition does not exist, this method raises an exception"""
        if hasattr(self, "_condition"):
            return self._condition
        else:
            raise AttributeDoesNotExist

    def set_condition(self, condition: bool):
        """sets the value of self._condition to the value provided in
        the condition argument if self._condition exists; if self._condition
        does not exist, this method raises an exception"""
        if hasattr(self, "_condition"):
            self._condition = condition
        else:
            raise AttributeDoesNotExist

    def switch_condition(self):
        """changes the value of self._condition to the opposite of its
        current Boolean value if self._condition exists; if self._condition
        does not exist, this method raises an exception"""
        if hasattr(self, "_condition"):
            if self._condition:
                self._condition = False
            else:
                self._condition = True
        else:
            raise AttributeDoesNotExist

    def remove_condition(self):
        """removes the optional condition attribute from an object if
        self._condition exists; if self._condition does not exist,
        this method raises an exception"""
        if hasattr(self, "_condition"):
            del(self._condition)
        else:
            raise AttributeDoesNotExist
