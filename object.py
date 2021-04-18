class Object:

    def __init__(self, id: str, name: str):
        # the ID of the feature
        self._id = id
        # the name of the feature
        self._name = name

    # methods for managing ID
    def get_id(self):
        """returns the value of self._id"""
        return self._id

    # methods for managing name
    def get_name(self):
        """returns the value of self._name"""
        return self._name

    def set_name(self, name: str):
        """changes the value of self._name to the value provided in
        the name argument"""
        self._name = name