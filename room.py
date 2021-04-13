import object
import feature
import person


class Room:

    def __init__(self, id: str, desc: str, sdesc: str, visited: bool):
        # contains the id for the room
        self._id = id
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
        # contains a list of connections in the form of Room ids
        self._connections = []

    # methods for managing ID

    def get_id(self):
        """returns the value of self.id"""
        return self._id

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

    def add_object(self, obj: object.Object):
        """takes an Object object and adds it to this rooms self.objects,
        returns True"""
        self._objects.append(obj)
        return True

    def remove_object(self, obj: object.Object):
        """takes an Object object and attempts to remove it from this rooms
        self.objects. If it fails it returns False, if it succeeds it returns
        True"""
        if object in self._objects:
            self._objects.remove(obj)
            return True
        else:
            return False

    def get_objects(self):
        """returns the list of Object objects in self.objects"""
        return self._objects

    # methods for managing self.features

    def add_feature(self, feat: feature.Feature):
        """takes a feature object and adds it to this rooms self.features,
            returns True"""
        self._features.append(feat)
        return True

    def remove_feature(self, feat: feature.Feature):
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

    # methods for managing self.people

    def add_person(self, per: person.Person):
        """takes a person object and adds it to this rooms self.persons,
            returns True"""
        self._people.append(per)
        return True

    def remove_person(self, per: person.Person):
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

    # methods for managing self.connections

    def add_connection(self, connection: str):
        """takes a string which specifies a room ID and adds it to the list
        of connections to this room"""
        self._connections.append(connection)
        return True

    def remove_connection(self, connection: str):
        """takes a string which specifies a room ID and removes it from the
        list of connections to this room. If the connection is not in the list
        it returns False. Otherwise it removes it and returns True"""
        if connection in self._connections:
            self._connections.remove(connection)
            return True
        else:
            return False

    def get_connections(self):
        """returns a list of connections to this room in the form of room IDs
        stored in self.connections"""
        return self._connections

    def set_connections(self, connections: list):
        """takes a list of connections to this room in the form of room IDs
        and sets self.connections to this list"""
        self._connections = connections
        return True