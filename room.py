import object
import feature
import person
import interactable

class RoomException(Exception):
    """Base exception class for the Room class"""
    pass

class IDDoesNotExist(RoomException):
    """Raised when ID does not exist"""
    pass

class IDAlreadyExists(RoomException):
    """Raised when ID already exists"""
    pass

class Room:

    def __init__(self, id: str, name: str, desc: str, sdesc: str, visited: bool):
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
        self._visited = visited
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
        return True

    # methods for managing self.features

    def add_feature(self, feat: str):
        """takes a feature object and adds it to this rooms self.features,
            returns True"""
        self._features.append(feat)
        return True

    def remove_feature(self, feat: str):
        """takes a feature object and attempts to remove it from this rooms
        self.features. If it fails it returns False, if it succeeds it returns
        True"""
        if feat in self._features:
            self._features.remove(feat)
            return True
        else:
            return False

    def get_features(self):
        """returns a list of Feature objects in self.features"""
        return self._features

    def set_features(self, features: list):
        """takes a list of ids and sets self.features to the list"""
        self._features = features
        return True

    # methods for managing self.people

    def add_person(self, per: str):
        """takes a person object and adds it to this rooms self.persons,
            returns True"""
        self._people.append(per)
        return True

    def remove_person(self, per: str):
        """takes a person object and attempts to remove it from this rooms
        self.persons. If it fails it returns False, if it succeeds it returns
        True"""
        if per in self._people:
            self._people.remove(per)
            return True
        else:
            return False

    def get_people(self):
        """returns a list of Person objects in self.people"""
        return self._people

    def set_people(self, people: list):
        """takes a list of ids and sets self.people to the list"""
        self._people = people
        return True

    # methods for managing self.connections

    def add_connection(self, direction: str, connection: str):
        """takes a string which specifies a room ID and adds it to the list
        of connections to this room"""
        if str not in ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']:
            return False
        self._connections[direction] = connection
        return True

    def remove_connection(self, direction: str):
        """takes a string which specifies a direction and removes it from the
        list of connections to this room. If the connection is not in the dict
        it returns False. Otherwise it removes it and returns True"""
        if direction in self._connections:
            self._connections.pop(direction)
            return True
        else:
            return False

    def get_connections(self):
        """returns a dictionary of connections to this room in the form of room IDs
        stored in self.connections"""
        return self._connections

    def set_connections(self, connections: dict):
        """takes a dictionary of connections to this room in the form of room IDs
        and sets self.connections to this dict"""
        self._connections = connections
        return True

    # methods for managing self.interactions

    def set_interactions(self, interactions: dict):
        """takes a dict of interactions as keys with possible responses as the value.
        Saves that dict as the self.interactions variable"""
        self._interactions = interactions
        return True

    def get_interactions(self):
        """returns the dicts stored in the self._interactions value. Keys are all
        possible interactions/commands, value is the response for those commands"""
        return self._interactions

    def add_interaction(self, interaction: str, response: str):
        """Takes a interaction and a response, adds it to self._interactions as a key and
        a value paid"""
        self._interactions[interaction] = response
        return True

    def remove_interaction(self, interaction: str):
        """Takes a interaction and removes it and the response from self._interactions"""
        self._interactions.pop(interaction)
        return True

    def get_interaction(self, interaction: str, sub1=None, sub2=None):
        """takes a interaction in reference to a room and returns the response that
        the interaction holds"""
        # interaction is the first level of the dict
        # sub1 is the second level of the dict
        # sub2 is the third level of the dict if needed
        if sub1 is None:
            # try/except will check if the interaction exists in interactions
            # if it does not it raises an error, except will then return none
            try:
                return self._interactions[interaction]
            except KeyError:
                raise interactable.KeyDoesNotExist
        elif sub2 is None and sub1 is not None:
            try:
                return self._interactions[interaction][sub1]
            except KeyError:
                raise interactable.KeyDoesNotExist
        else:
            try:
                return self._interactions[interaction][sub1][sub2]
            except KeyError:
                raise interactable.KeyDoesNotExist
