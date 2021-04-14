import json
import room


class Converter:

    def __init__(self):
        self._objects = []
        self._features = []
        self._people = []

    def room_to_json(self, room_obj: room.Room):
        """takes a room object and converts it to a json object"""
        # a list to store the object ids
        obj_list = []
        # runs through list of objects and gets the ids
        for obj in room_obj.get_objects():
            obj_list.append(obj.get_id())
        # a list to store the feat ids
        feat_list = []
        # runs through list of features and gets the ids
        for feat in room_obj.get_features():
            feat_list.append(feat.get_id())
        # a list to store the person ids
        people_list = []
        # runs through list of people and gets the ids
        for person in room_obj.get_people():
            people_list.append(person.get_id())
        # stores everything in a dict
        room_dict = {
            'id': room_obj.get_id(),
            'desc': room_obj.get_desc(),
            'sdesc': room_obj.get_sdesc(),
            'visited': room_obj.get_visited(),
            'objects': obj_list,
            'features': feat_list,
            'people': people_list,
            'connections': room_obj.get_connections(),
        }
        # converts the dict to json file and returns it
        return json.dumps(room_dict)

    def room_from_json(self, json_room):
        """takes a json object and converts it int a room object"""
        # turns the json file into a dict
        room_dict = json.loads(json_room)
        # gets all the basic variables from the dict
        id = room_dict.get('id')
        desc = room_dict.get('desc')
        sdesc = room_dict.get('sdesc')
        visited = room_dict.get('visited')
        # creates a new room with the variables
        new_room = room.Room(id, desc, sdesc, visited)

        # creates an object list
        obj_ids = room_dict.get('objects')
        # runs through the database of objects
        for obj in self._objects:
            # if it finds an object that matches the id given
            if obj.get_id() in obj_ids:
                # removes the id from the id list
                obj_ids.remove(obj.get_id)
                # adds the object to the room
                new_room.add_object(obj)

        # adds all features, same as objects above
        feat_ids = room_dict.get('features')
        for feat in self._features:
            if feat.get_id() in feat_ids:
                feat_ids.remove(feat.get_id)
                new_room.add_feature(feat)

        # adds all people, same as objects above
        person_ids = room_dict.get('people')
        for person in self._people:
            if person.get_id() in person_ids:
                person_ids.remove(person.get_id)
                new_room.add_person(person)

        # adds all the room ids in 'connections' into self._connections
        new_room.set_connections(room_dict.get('connections'))

        # returns the new_room object as a Room object
        return new_room

    def obj_to_json(self):
        """takes an Object object and converts it to a json object"""
        return

    def obj_from_json(self):
        """takes a json object and converts it to an Object object"""
        return

    def feat_to_json(self):
        """takes a Feature object and converts it to a json object"""
        return

    def feat_from_json(self):
        """takes a json object and converts it to a Feature object"""
        return

    def person_to_json(self):
        """takes a person object and converts it to a json object"""
        return

    def person_from_json(self):
        """takes a json object and converts it to a Person object"""
        return
