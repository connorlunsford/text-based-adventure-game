from interactable import Interactable

class ObjectException(Exception):
    """Base exception class for the Object class"""
    pass

class Object(Interactable):

    def __init__(self, id: str, name: str, desc: str, interactions: dict,
     hidden: bool):
        super().__init__(id, name, desc, interactions)
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
