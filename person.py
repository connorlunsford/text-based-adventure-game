class Person:

    def __init__(self, id: str, desc: str):
        # contains id for the person (name of the person)
        self._id = id
        # contains the description of the person
        self._desc = desc
        """contains a dict of possible responses to certain verbs to
        communicate with person"""
        self._verbs = {}        
    
    # methods for managing ID

    def get_id(self):
        # returns the value of self._id
        return self._id

    def set_id(self, id: str):
        # takes a string and sets it as the value of self._id
        self._id = id

    # methods for managing desc

    def get_desc(self):
        # returns the value of self._desc
        return self._desc

    def set_desc(self, desc: str):
        # takes a string and sets it as the value of _desc
        self._desc = desc

# methods for managing verbs

    def get_verbs(self):
        """returns the dict stored in self._verbs. Keys are all
        possible verbs, value is the response for those verbs"""
        if self._verbs:
            return self._verbs
        else:
            return False

    def set_verbs(self, verbs: dict):
        """takes a dict of verbs as keys with possible responses as the value.
        Saves that dict as the self._verbs variable"""
        self._verbs = verbs

    def add_verb(self, verb: str, response: str):
        """Takes a verb and a response, adds it to self._verbs as a key and
        a value pair"""
        self._verbs[verb] = response

    def remove_verb(self, verb):
        """Takes a verb and removes it and the response from self._verbs"""
        if verb in self._verbs:
            self._verbs.pop(verb)
            return True
        else:
            return False

    def get_response(self, verb):
        """takes a verb in reference to a person and returns the response that
        the verb holds"""
        if verb in self._verbs:
            return self._verbs[verb]
        else:
            return False
