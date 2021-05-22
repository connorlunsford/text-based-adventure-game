import json
import person
import feature
import object
import player
import room


def room_to_json(room_obj: room.Room):
    """takes a room object and converts it to a json object"""
    # stores everything in a dict
    room_dict = {
        'id': room_obj.get_id(),
        'name': room_obj.get_name(),
        'desc': room_obj.get_desc(),
        'sdesc': room_obj.get_sdesc(),
        'visited': room_obj.get_visited(),
        'objects': room_obj.get_objects(),
        'features': room_obj.get_features(),
        'people': room_obj.get_people(),
        'connections': room_obj.get_connections(),
        'interactions': room_obj.get_interactions()
    }
    # converts the dict to json file and returns it
    return json.dumps(room_dict)


def room_from_json(json_room):
    """takes a json object and converts it int a room object"""
    # turns the json file into a dict
    room_dict = json.loads(json_room)
    # gets all the basic variables from the dict
    id = room_dict['id']
    name = room_dict['name']
    desc = room_dict['desc']
    sdesc = room_dict['sdesc']
    visited = room_dict['visited']
    # creates a new room with the variables
    new_room = room.Room(id, name, desc, sdesc)
    # adds all the objects into the room
    new_room.set_objects(room_dict['objects'])
    # adds all the features into the room
    new_room.set_features(room_dict['features'])
    # adds all the people into the room
    new_room.set_people(room_dict['people'])
    # adds all the room ids in 'connections' into self._connections
    new_room.set_connections(room_dict['connections'])
    # sets visited
    new_room.set_visited(visited)

    # adds the verbs from 'verbs' into self._verbs
    new_room.set_interactions(room_dict['interactions'])

    # returns the new_room object as a Room object
    return new_room


def obj_to_json(object_obj: object.Object):
    """takes an Object object and converts it to a json object"""
    # store each of object_obj's atttributes in a dict
    object_dict = {
        'id': object_obj.get_id(),
        'name': object_obj.get_name(),
        'desc': object_obj.get_desc(),
        'sdesc': object_obj.get_sdesc(),
        'interactions': object_obj.get_interactions(),
        'hidden': object_obj.get_hidden()
    }

    # converts the dict to a json file and returns it
    return json.dumps(object_dict)


def obj_from_json(json_object):
    """takes a json object and converts it to an Object object"""
    # turns the json file into a dict
    object_dict = json.loads(json_object)
    # gets all the basic variables/attributes from the dict
    id = object_dict.get('id')
    name = object_dict.get('name')
    desc = object_dict.get('desc')
    sdesc = object_dict.get('sdesc')
    interactions = object_dict.get('interactions')
    hidden = object_dict.get('hidden')

    # creates a new Object object with the specified attributes
    new_object = object.Object(id, name, desc, sdesc, interactions, hidden)

    # returns the new_object object as an Object object
    return new_object


def feat_to_json(feat_obj: feature.Feature):
    """takes a Feature object and converts it to a json object"""
    # store each of feat_obj's attributes in a dict
    if hasattr(feat_obj, "_condition"):
        feature_dict = {
            'id': feat_obj.get_id(),
            'name': feat_obj.get_name(),
            'desc': feat_obj.get_desc(),
            'sdesc': feat_obj.get_sdesc(),
            'interactions': feat_obj.get_interactions(),
            'hidden': feat_obj.get_hidden(),
            'condition': feat_obj.get_condition()
        }
    else:
        feature_dict = {
            'id': feat_obj.get_id(),
            'name': feat_obj.get_name(),
            'desc': feat_obj.get_desc(),
            'sdesc': feat_obj.get_sdesc(),
            'interactions': feat_obj.get_interactions(),
            'hidden': feat_obj.get_hidden()
        }

    # converts the dict to an json file and returns it
    return json.dumps(feature_dict)


def feat_from_json(json_feature):
    """takes a json object and converts it to a Feature object"""
    # turns the json file into a dict
    feature_dict = json.loads(json_feature)
    # gets all the basic variables/attributes from the dict
    id = feature_dict.get('id')
    name = feature_dict.get('name')
    desc = feature_dict.get('desc')
    sdesc = feature_dict.get('sdesc')
    interactions = feature_dict.get('interactions')
    hidden = feature_dict.get('hidden')

    # creates a new Feature object with the specified attributes
    new_feature = feature.Feature(id, name, desc, sdesc, interactions, hidden)

    try:
        if feature_dict['condition'] is not None:
            new_feature.add_condition(feature_dict.get('condition'))
    except KeyError:
        pass

    # returns the new_feature object as a Feature object
    return new_feature


def person_to_json(person_obj: person.Person):
    """takes a Person object and converts it to a json object"""
    # stores everything in a dict
    person_dict = {
        'id': person_obj.get_id(),
        'name': person_obj.get_name(),
        'desc': person_obj.get_desc(),
        'sdesc': person_obj.get_sdesc(),
        'interactions': person_obj.get_interactions()
    }
    # converts the dict to json file and returns it
    return json.dumps(person_dict)


def person_from_json(json_person):
    """takes a json object and converts it into a Person object"""
    # turns the json file into a dict
    person_dict = json.loads(json_person)
    # gets all the basic variables from the dict
    """since we're controlling the input/json files, all attributes
    should be present, not adding validation at this time"""
    id = person_dict['id']
    name = person_dict['name']
    desc = person_dict['desc']
    sdesc = person_dict['sdesc']
    interactions = person_dict['interactions']
    # creates a new person with the variables
    new_person = person.Person(id, name, desc, sdesc, interactions)
    # returns the new_person as a Person object
    return new_person


def player_to_json(player_obj: player.Player):
    """takes a player object and converts it to a json object"""
    # stores everything in a dict
    player_dict = {
        'id': player_obj.get_id(),
        'name': player_obj.get_name(),
        'inventory': player_obj.get_inventory(),
    }
    # converts the dict to json file and returns it
    return json.dumps(player_dict)


def player_from_json(json_player):
    """takes a json object and converts it into a player object"""
    # turns the json file into a dict
    player_dict = json.loads(json_player)
    # checks to make sure there's an id in the dict
    if player_dict['id']:
        # creates a new player object using that id
        new_player = player.Player(player_dict['id'])
    else:
        """need to see if there's another way we want to handle this (print
        a message?)"""
        # cannot create a player without an id
        return False
    # checks to see if name in json/dict
    if player_dict['name']:
        # sets the name as the player's name
        new_player.set_name(player_dict['name'])
    # checks to see if inventory in json/dict
    if player_dict['inventory']:
        # sets the inventory list as the player's inventory
        new_player.set_inventory(player_dict['inventory'])
    # returns new_player as a Player object
    return new_player


