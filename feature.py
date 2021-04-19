class Feature:

    def __init__(self, id: str, name: str, interactions: dict, condition1=False, condition2=False):
        # the ID of the feature
        self._id = id
        # the name of the feature
        self._name = name
        # a dictionary of interactions associated with the feature
        # in the form 'action': 'result'
        # E.g., {'look at': 'A large, cluttered desk.', 'eat': 'You
        # can't eat this.'}
        self._interactions = interactions
        # an optional condition variable
        self._condition1 = condition1
        # an optional condition variable
        self._condition2 = condition2

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

    # methods for managing interactions
    def get_interaction(self, action: str):
        """returns the value associated with the key provided in the 
        action argument; if the key does not exist, this method returns
        None"""
        if action in self._interactions:
            return self._interactions[action]
        else:
            return None

    def add_interaction(self, action: str, result: str):
        """adds the key-value pair provided in the action and result
        arguments to the dictionary; if they key already exists in the 
        dictionary, this method does nothing"""
        if action not in self._interactions:
            self._interactions[action] = result

    def set_interaction(self, action: str, result: str):
        """changes the value associated with the key provided in the
        action argument to the value of the result argument; if the key 
        does not exist, this method does nothing"""
        if action in self._interactions:
            self._interactions[action] = result

    def remove_interaction(self, action: str):
        """removes the key-value pair associated with the key provided
        in the action argument; if the key does not exist, this method 
        does nothing"""
        if action in self._interactions:
           del self._interactions[action]

    def get_interactions(self):
        """returns the entire interactions dictionary"""
        return self._interactions

    def remove_interactions(self, action: str):
        """removes all key-value pairs in the interactions dictionary"""
        self._interactions.clear()
