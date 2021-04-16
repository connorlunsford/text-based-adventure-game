class Person:

    def __init__(self, id: str, desc: str):
        # contains id for the person (name of the person)
        self._id = id
        # contains the description of the person
        self._desc = desc
    
    # methods for managing ID

    def get_id(self):
        # returns the value of self._id
        return self._id

    def set_id(self, id: str):
        # takes a string and sets it as the value of self._id
        return self._id        

    # methods for managing desc

    def get_desc(self):
        # returns the value of self._desc
        return self._desc

    def set_desc(self, desc: str):
        # takes a string and sets it as the value of _desc
        self._desc = descgit 