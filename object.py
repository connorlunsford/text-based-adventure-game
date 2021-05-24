from feature import Feature

class ObjectException(Exception):
    """Base exception class for the Object class"""
    pass

class AttributeDoesNotExist(ObjectException):
    """Raised when attribute does not exist"""
    pass

class AttributeAlreadyExists(ObjectException):
    """Raised when attribute already exists"""
    pass

class Object(Feature):

    def __init__(self, id: str, name: str, desc: str, sdesc: str, interactions: dict,
     hidden: bool):
        super().__init__(id, name, desc, sdesc, interactions, hidden)
