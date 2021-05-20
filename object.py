from interactable import Interactable

class ObjectException(Exception):
    """Base exception class for the Object class"""
    pass

class AttributeDoesNotExist(ObjectException):
    """Raised when attribute does not exist"""
    pass

class AttributeAlreadyExists(ObjectException):
    """Raised when attribute already exists"""
    pass

class Object(Interactable):

    def __init__(self, id: str, name: str, desc: str, sdesc: str, interactions: dict,
     hidden: bool):
        super().__init__(id, name, desc, sdesc, interactions)
        # the visible/hidden status of the object
        self._hidden = hidden

    # methods for managing object
    def get_hidden(self):
        """returns the value of self._hidden"""
        return self._hidden

    def set_hidden(self, hidden: bool):
        """changes the value of self._hidden to the value provided in
        the hidden argument"""
        self._hidden = hidden

    def switch_hidden(self):
        """changes the value of self._hidden to the opposite of its
        current Boolean value"""
        if self._hidden:
            self._hidden = False
        else:
            self._hidden = True

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
