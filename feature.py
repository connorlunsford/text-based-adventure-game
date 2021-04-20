from interactable import Interactable
from object import Object

class Feature(Object):

    def __init__(self, id: str, name: str, desc: str, interactions: dict, hidden: bool):
        super().__init__(id, name, desc, interactions, hidden)

    # methods for managing the optional condition variable
    def add_condition(self, condition: bool):
        """adds an optional condition attribute to the object with the value
        provided in the condition argument if self._condition does not already
        exist; otherwise, this method does nothing"""
        if not hasattr(self, "_condition"):
            self._condition = condition

    def get_condition(self):
        """returns the value of self._condition if self._condition exists;
        otherwise, this method does nothing"""
        if hasattr(self, "_condition"):
            return self._condition

    def set_condition(self, condition: bool):
        """changes the value of self._condition to the value provided in
        the condition argument if self._condition exists; otherwise,
        this method does nothing"""
        if hasattr(self, "_condition"):
            self._condition = condition

    def switch_condition(self):
        """changes the value of self._condition to the opposite of its
        current Boolean value if self._condition exists; otherwise, 
        this method does nothing"""
        if hasattr(self, "_condition"):
            if self._condition:
                self._condition = False
            else:
                self._condition = True

    def remove_condition(self):
        """removes the optional condition attribute from an object if
        self._condition exists; otherwise, this method does nothing"""
        if hasattr(self, "_condition"):
            del(self._condition)
