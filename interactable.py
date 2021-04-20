class Interactable:

    def __init__(self, id: str, name: str, desc: str, interactions: dict):
        # the ID of the interactable
        self._id = id
        # the name of the interactable
        self._name = name
        # a description of the interactable
        self._desc = desc
        # a dictionary of interactions associated with the interactable
        # in the form 'verb': 'result'
        # E.g., {'look at': 'A woman's silver earring.', 'eat': 'You
        # can't eat this.'}
        self._interactions = interactions

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

    # methods for managing description
    def get_desc(self):
        """returns the value of self._desc"""
        return self._desc

    def set_desc(self, desc: str):
        """changes the value of self._desc to the value provided in
        the desc argument"""
        self._desc = desc

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
