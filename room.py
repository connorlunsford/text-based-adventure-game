
class RoomException(Exception):
    """Base exception class for the Room class"""
    pass

class IDDoesNotExist(RoomException):
    """Raised when ID does not exist"""
    pass

class IDAlreadyExists(RoomException):
    """Raised when ID already exists"""
    pass

class KeyDoesNotExist(RoomException):
    """Raised when key does not exist"""
    pass

class KeyAlreadyExists(RoomException):
    """Raised when key already exists"""
    pass

class Room:

    def __init__(self, id: str, name: str, desc: str, sdesc: str):
        # contains the id for the room
        self._id = id
        # contains the name of the room
        self._name = name
        # contains the long form description for the room
        self._desc = desc
        # contains the short form description for the room
        self._sdesc = sdesc
        # contains a bool that specifies whether or not the room has been
        # visited before
        self._visited = False
        # contains a list of Object objects
        self._objects = []
        # contains a list of Feature objects
        self._features = []
        # contains a list of Person objects
        self._people = []
        # contains a dictionary of connections, with the key being a direction and the value being the room id
        self._connections = {}
        # contains a dict of possible responses for certain commands
        self._interactions = {}

    # methods for managing ID

    def get_id(self):
        """returns the value of self.id"""
        return self._id

    # methods for self._name

    def get_name(self):
        """returns the name of the room"""
        return self._name

    def set_name(self, name: str):
        """sets the given string value to the name of the room"""
        self._name = name

    # methods for managing desc

    def get_desc(self):
        """returns the value of self.desc, you probably want to use
        get_description instead"""
        return self._desc

    def set_desc(self, desc: str):
        """Takes a String and allows you to change the value stored in
        self.desc"""
        self._desc = desc

    # methods for managing sdesc

    def get_sdesc(self):
        """returns the value of self.sdesc, you probably want to use
        get_description instead"""
        return self._sdesc

    def set_sdesc(self, sdesc: str):
        """Takes a String and allows you to change the value stored in
        self.sdesc"""
        self._sdesc = sdesc

    # methods for getting the correct description

    def get_description(self):
        """If the visited bool is False, this returns desc. If the visited bool
        is True this returns sdesc"""
        if self._visited is False:
            self._visited = True
            return self._desc
        else:
            return self._sdesc

    # methods for managing the visited bool

    def get_visited(self):
        """returns the value of the visited bool"""
        return self._visited

    def set_visited(self, visited: bool):
        """sets the value of the visited bool to the given value, either True
        or False"""
        self._visited = visited

    # methods for managing self.objects

    def add_object(self, obj: str):
        """takes an Object object's ID and adds it to this rooms self.objects; if
        the ID already exists inside the list, this method raises an exception"""
        if obj not in self._objects:
            self._objects.append(obj)
        else:
            raise IDAlreadyExists

    def remove_object(self, obj: str):
        """takes an Object object's ID and attempts to remove it from this room's
        self.objects. If the ID does not exist inside the list, this method
        raises an exception"""
        if obj in self._objects:
            self._objects.remove(obj)
        else:
            raise IDDoesNotExist

    def get_objects(self):
        """returns the list of Object object IDs in self.objects"""
        return self._objects

    def set_objects(self, objects: list):
        """takes a list of ids and sets self.objects to the list"""
        self._objects = objects

    # methods for managing self.features

    def add_feature(self, feat: str):
        """takes a feature's ID and adds it to this rooms self.features; if
        the ID already exists inside the list, this method raises an exception"""
        if feat not in self._features:
            self._features.append(feat)
        else:
            raise IDAlreadyExists

    def remove_feature(self, feat: str):
        """takes a feature's ID and attempts to remove it from this room's
        self.features. If the ID does not exist inside the list, this method
        raises an exception"""
        if feat in self._features:
            self._features.remove(feat)
        else:
            raise IDDoesNotExist

    def get_features(self):
        """returns a list of Feature objects in self.features"""
        return self._features

    def set_features(self, features: list):
        """takes a list of ids and sets self.features to the list"""
        self._features = features

    # methods for managing self.people

    def add_person(self, per: str):
        """takes a person's ID and adds it to this rooms self.persons; if
        the ID already exists inside the list, this method raises an exception"""
        if per not in self._people:
            self._people.append(per)
        else:
            raise IDAlreadyExists

    def remove_person(self, per: str):
        """takes a person's ID and attempts to remove it from this rooms
        self.persons. If the ID does not exist inside the list, this method
        raises an exception"""
        if per in self._people:
            self._people.remove(per)
        else:
            raise IDDoesNotExist

    def get_people(self):
        """returns a list of Person objects in self.people"""
        return self._people

    def set_people(self, people: list):
        """takes a list of ids and sets self.people to the list"""
        self._people = people

    # methods for managing self.connections

    def add_connection(self, direction: str, connection: str):
        """takes a string which specifies a room ID and adds it to the list
        of connections to this room; if the ID already exists inside the list, 
        this method raises an exception"""
        if direction not in ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']:
            raise IDAlreadyExists
        if direction not in self._connections:
            self._connections[direction] = connection
        else:
            raise IDAlreadyExists

    def remove_connection(self, direction: str):
        """takes a string which specifies a direction and removes it from the
        list of connections to this room. If the connection is not in the dict
        it returns False. Otherwise it removes it and returns True"""
        if direction in self._connections:
            self._connections.pop(direction)
            return True

    def get_connections(self):
        """returns a dictionary of connections to this room in the form of room IDs
        stored in self.connections"""
        return self._connections

    def set_connections(self, connections: dict):
        """takes a dictionary of connections to this room in the form of room IDs
        and sets self.connections to this dict"""
        self._connections = connections

    # methods for managing self.interactions

    def set_interactions(self, interactions: dict):
        """takes a dict of interactions as keys with possible responses as the value.
        Saves that dict as the self.interactions variable"""
        self._interactions = interactions

    def get_interactions(self):
        """returns the dicts stored in the self._interactions value. Keys are all
        possible interactions/commands, value is the response for those commands"""
        return self._interactions

    def add_interaction(self, interaction: str, response: str):
        """Takes a interaction and a response, adds it to self._interactions as a key and
        a value paid"""
        if interaction not in self._interactions:
            self._interactions[interaction] = response
        else:
            raise KeyAlreadyExists

    def remove_interaction(self, interaction: str):
        """Takes a interaction and removes it and the response from self._interactions"""
        if interaction in self._interactions:
            self._interactions.pop(interaction)
        else:
            raise KeyDoesNotExist

    def get_interaction(self, interaction: str, sub1=None, sub2=None):
        """takes a interaction in reference to a room and returns the response that
        the interaction holds"""
        # interaction is the first level of the dict
        # sub1 is the second level of the dict
        # sub2 is the third level of the dict if needed
        if sub1 is None:
            # try/except will check if the interaction exists in interactions
            # if it does not it raises an error, except will then return none
            if interaction in self._interactions:
                return self._interactions[interaction]
            else:
                raise KeyDoesNotExist
        elif sub2 is None and sub1 is not None:
            if interaction in self._interactions and sub1 in self._interactions[interaction]:
                return self._interactions[interaction][sub1]
            else:
                raise KeyDoesNotExist
        else:
            if interaction in self._interactions and sub1 in self._interactions[interaction] and sub2 in self._interactions[interaction][sub1]:
                return self._interactions[interaction][sub1][sub2]
            else:
                raise KeyDoesNotExist
