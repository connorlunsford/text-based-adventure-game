# python modules
import time
import os
import json

# our modules
import converter
import feature
import object
import person
import player
import room
import nlp
import interactable


class System:

    def __init__(self):
        # insert functionality to get this from the converter
        # contains a dict with rooms, the key is the id, the value is the room object
        self._rooms = {}
        # contains a dict with features, the key is the id, the value is the feature object
        self._features = {}
        # contains a dict with object, the key is the id, the value is the Object object
        self._objects = {}
        # contains a dict with people, the key is the id, the value is the person object
        self._people = {}
        # contains the player
        self._player = player.Player('player')
        # contains the id for the room the player is currently in
        self._cur_room = 'R01'
        # contains the natural language parser
        self._parser = nlp.Parser()
        # add necesary text files for natural language parser to work
        self._parser.add_connections("./resources/connections.txt")
        self._parser.add_special_commands("./resources/special_commands.txt")
        self._parser.add_prepositions("./resources/prepositions.txt")
        self._parser.load_articles("./resources/articles.txt")
        self._parser.load_stopwords("./resources/stopwords.txt")

    def game_loop(self):
        while True:
            print('What would you like to do?')
            inp = input()

            # parses the input and returns a command with an interaction word and 1-2 objects
            command = self._parser.parse(inp)
            if command[0] == 'use':
                self.use(command[1],command[2])
            elif command[0] == 'ask':
                self.ask(command[1],command[2])
            elif command[0] == 'call':
                self.call()
            elif command[0] == 'read':
                self.read(command[1])
            elif command[0] == 'open':
                self.open(command[1])
            elif command[0] == 'search':
                self.search(command[1])
            elif command[0] == 'touch':
                self.touch(command[1])
            elif command[0] == 'taste':
                self.taste(command[1])
            elif command[0] == 'smell':
                self.smell(command[1])
            elif command[0] == 'listen':
                self.listen(command[1])
            elif command[0] == 'look':
                self.look()
            elif command[0] == 'look at':
                self.look_at(command[1])
            elif command[0] == 'go':
                self.go(command[1])
            elif command[0] == 'take':
                self.take(command[1])
            elif command[0] == 'help':
                self.help()
            elif command[0] == 'inventory':
                self.inventory()
            elif command[0] == 'savegame':
                self.save()
            elif command[0] == 'loadgame':
                self.load()

    def use(self, object1: str, object2: str):
        """this command takes 2 parameters, object1, which needs to be an object and is being used on object 2,
        which can be any feature, person, or object"""
        # object1 is always the giving object
        # object 2 is always the receiving object
        # checks if the object is in the inventory
        if object1 in self._player.get_inventory():
            # checks if the second object is in the room
            if object2 in self._rooms[self._cur_room].get_features:
                try:
                    # prints what happens the first time you use object1 on object 2
                    print(self._features[object2].get_interaction('use',object1))
                    # sets the condition for the feature to True (unlocked, interacted, etc)
                    self._features[object2].set_condition(True)
                    # removes the interaction from the dictionary
                    self._features[object2].remove_nested_interaction('use',object1)
                    return True
                except interactable.KeyDoesNotExist:
                    print('You cannot use the ' + self._objects[object1].get_name() + ' on the '
                          + self._features[object2].get_name())
                    return False
            # checks if the object is a person
            elif object2 in self._people:
                print('You cannot use an object on a person')
                return False
            # checks if the object is a room
            elif object2 in self._rooms:
                print('You cannot use an object on a room')
                return False
            else:
                print('You cannot use an object that is not in the room')
                return False
        else:
            print("You cannot use an object that isn't in your inventory")
            return False

    def ask(self, person_id: str, obj_id: str):
        """this command takes 2 parameters, person which is an id for a person, and object, which is an id for an
        object"""
        # checks if the person is in the room
        if person_id in self._rooms[self._cur_room].get_people():
            # checks if the object is in the inventory
            if obj_id in self._player.get_inventory():
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry I don't know anything about that object'")
                    return False
            else:
                print('You cannot ask someone about an object that is not in your inventory')
                return False
        else:
            print("You cannot speak with something that isn't a person")
            return False

    def call(self):
        """this command allows you to call the police when you are in the grand foyer and end the game"""
        if self._cur_room == 'R01':
            print('You pick up the phone')
            print('Are you sure you want to call the police? Make sure you know the killer and the murder weapon (Y/N)')
            inp = input().upper()
            if inp == 'Y' or inp == 'YES':
                # sleeps inserted for dramatic effect
                print('ring...')
                time.sleep(1)
                print('ring...')
                time.sleep(1)
                print('ring...')
                time.sleep(1)
                print('"Hello, this is Officer Christie with the Police Department, who is this"')
                print('You tell him your name and the situation')
                print('"A murder you say! And who did you say was the culprit?"')
                killer = input('Who is the killer: ').upper()
                print('"Ah I see, and how did they kill this man?"')
                weapon = input('What was the murder weapon: ').upper()

                # NOTE:

                # at this point we need to add some sort of validation for the killer and weapon

                # the best way to handle this might be the language parser

                killer = self._parser.find_killer(killer)
                weapon = self._parser.find_weapon(weapon)

                if killer == 'WRONG' and weapon == 'WRONG':
                    pass
                    # insert lose scenario #1
                    # both killer and weapon is wrong
                    #
                # change 'CORRECT' to the killers name in final implementation
                elif killer == 'CORRECT' and weapon == 'WRONG':
                    pass
                    #
                    # insert lose scenario #2
                    #
                # change 'CORRECT' to the weapon name in final implementation
                elif killer == 'WRONG' and weapon == 'CORRECT':
                    pass
                    #
                    # insert lose scenario #3
                    #
                # change 'CORRECT' to the killers name in final implementation
                # change 'CORRECT' to the weapon name in final implementation
                elif killer == 'CORRECT' and weapon == 'CORRECT':
                    pass
                    #
                    # insert win scenario
                    #
            else:
                print('You decide you need more evidence. You set the phone down')
        else:
            print('Sorry you cannot call the police from this room')

    def read(self, obj: str):
        """this command takes an object and allows you to attempt to read it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot read this object')
                return False

        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot read this object')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._objects[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot read this object')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print('You cannot read a person...try "ask" or "look" instead')
            return False
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print('You cannot read a room...try "look at [room]" or just "look" instead')
            return False
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to read does not appear to be in this room')
            return False

    def open(self, obj: str):
        """this command takes an object and allows you to attempt to open it"""
        # if the object is an object
        if obj in self._objects:
            print('you cannot open this object')
            return False
        # if the object is a person
        elif obj in self._people:
            print('You cannot open a  person')
            return False
        # if the object is a feature in the room
        elif obj in self._rooms[self._cur_room].get_features():
            # for certain features the condition specifies if the object is locked
            if self._features[obj].get_condition() is True:
                print(self._features[obj].get_interaction('open','locked'))
            else:
                print(self._features[obj].get_interaction('open', 'unlocked'))
        # if the object is a room
        elif obj in self._rooms:
            print('You cannot open a room, try "go to [room]" or "open [door to room]" instead')
            return False
        # if the object is not in the room
        else:
            print('The thing you are trying to open is not in this room')
            return False

    def search(self, obj: str):
        """this command lets you search a  given room or feature"""
        # if the search parameter is an object
        if obj in self._objects:
            print('You cannot search this object')
            return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot search that thing')
                return False
        # if the object you are trying to search is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot search that thing')
                return False
        # if the object you are trying to search is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot search that thing')
                return False
        # if the object is not in this room
        else:
            print('The thing you are trying to search does not appear to be in this room')
            return False

    def touch(self, obj: str):
        """takes an object id and allows you to attempt to touch it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot touch that object')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot touch that object')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot touch that thing')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot touch that person')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._objects[self._cur_room].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot touch the room')
                return False
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to touch does not appear to be in this room')
            return False

    def taste(self, obj: str):
        """takes an object id and allows you to attempt to taste it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot taste that thing')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot taste that thing')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot taste that thing')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot taste that thing')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._objects[self._cur_room].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot taste that thing')
                return False
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to taste does not appear to be in this room')
            return False

    def smell(self, obj: str):
        """takes an object id and allows you to attempt to smell it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot smell that thing')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot smell that thing')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot smell that thing')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot smell that thing')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._objects[self._cur_room].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot smell that thing')
                return False
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to smell does not appear to be in this room')
            return False

    def listen(self, obj: str):
        """takes an object id and allows you to attempt to listen to it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot listen to that thing')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot listen to that thing')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot listen to that thing')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot listen to that thing')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._objects[self._cur_room].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('Sorry you cannot listen to that thing')
                return False
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to listen to does not appear to be in this room')
            return False

    def look_at(self, obj: str):
        """takes an object id and allows you to look at / examine it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            print(self._objects[obj].get_desc())
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_desc())
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_desc())
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._features[obj].get_desc())
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._features[obj].get_description())
            return True
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to examine does not appear to be in this room')
            return False

    def look(self):
        """prints the long form description of the current room"""
        self._rooms[self._cur_room].set_visited = False
        self.get_description()
        return True

    def go(self, room_id: str):
        """takes a room id and allows you to attempt to go there from the current room"""
        if room_id in self._rooms[self._cur_room].get_connections():
            self._cur_room = room_id
            print(self.get_description())
            return True
        else:
            print('You cannot currently enter that room from this room')
            return False

    def take(self, obj: str):
        """takes an object id and allows you to attempt to take it from the room it is currently in"""
        if obj in self._people:
            print('You cannot take a person')
            return False
        elif obj in self._features:
            print('You cannot take this from the room')
            return False
        elif obj in self._rooms:
            print('You cannot take a room')
            return False
        elif obj in self._player.get_inventory():
            print('That object is already in your inventory')
            return False
        elif obj in self._rooms[self._cur_room].get_objects():
            print('You picked up the ' + self._objects[obj].get_name())
            self._rooms[self._cur_room].remove_object(obj)
            self._player.add_to_inventory(obj)
            return True
        else:
            print('That object is not in the room')
            return False

    def help(self):
        """takes no parameters, prints out a list of commands that the player is allowed to use"""
        print('Here are some examples of possible commands you can use')
        print('look at [object] - allows you to examine an object, feature, or person')
        print('look - allows you to examine the room')
        print('go to [room] - allows you to enter unlocked rooms connected to the current room')
        print('take [object] - allows you to pick up an object')
        print('inventory - allows you to examine the contents of your inventory')
        print('savegame - allows you to save the game')
        print('loadgame - allows you to load the game')
        print('use [object1] on [object2] - allows you to use an object on another object')
        print('ask [person] about [object] - allows you to interrogate a person about an object')
        print('read [object] - allows you to read an object')
        print('open [object] - allows you to open an unlocked door or other similar object')
        print('search [object] - allows you to search through an object or room')
        print('touch [object] - allows you to feel an object, may give you more clues')
        print('taste [object] - allows you to taste an object, may give you more clues')
        print('smell [object] - allows you to smell an object or room, may give you more clues')
        print('listen [object] - allows you to smell an object or room, may give you more clues')
        return

    def inventory(self):
        """takes no parameters, prints out the players current inventory"""
        for obj in self._player.get_inventory():
            print(self._objects[obj].get_name())
        return

    def save(self):
        """takes no parameters, allows you to save the game"""
        return

    def load(self):
        """takes no parameters, allows you to load the game from a save file"""
        return

    def get_description(self):
        """gets the description of the room and all the objects/features/people in the room"""
        print(self._rooms[self._cur_room].get_description())
        print('In the room there is:')
        for feat in self._rooms[self._cur_room].get_features():
            if self._features[feat].get_hidden() is False:
                print(self._features[feat].get_desc())
        for obj in self._rooms[self._cur_room].get_objects():
            if self._objects[obj].get_hidden() is False:
                print(self._objects[obj].get_desc())
        for person_id in self._rooms[self._cur_room].get_people():
            print(self._people[person_id].get_desc())
        return

    def start(self):
        """starts the game by loading the files, playing the introduction, and starting the main gameplay loop"""
        # grabs the list of json objects located in the rooms subdirectory
        room_files = os.listdir('gamefiles/rooms')
        for room_file_name in room_files:
            room_file = open(room_file_name,'r')
            room_json = json.load(room_file)
            room_obj = converter.room_from_json(room_json)
            self._rooms[room_obj]['id'] = room_obj

        # grabs the list of json objects located in the objects subdirectory
        object_files = os.listdir('gamefiles/objects')
        for object_file_name in object_files:
            object_file = open(object_file_name,'r')
            object_json = json.load(object_file)
            object_obj = converter.obj_from_json(object_json)
            self._objects[object_obj]['id'] = object_obj

        # grabs the list of json objects located in the features subdirectory
        feature_files = os.listdir('gamefiles/features')
        for feature_file_name in feature_files:
            feature_file = open(feature_file_name,'r')
            feature_json = json.load(feature_file)
            feature_obj = converter.feat_from_json(feature_json)
            self._features[feature_obj]['id'] = feature_obj

        # grabs the list of json objects located in the people subdirectory
        people_files = os.listdir('gamefiles/people')
        for people_file_name in people_files:
            people_file = open(people_file_name,'r')
            people_json = json.load(people_file)
            people_obj = converter.person_from_json(people_json)
            self._people[people_obj]['id'] = people_obj

        self.introduction()

        self.game_loop()

        return

    def introduction(self):
        """plays the main introduction for the game"""

        # insert main storyline stuff here

        # just use print statements in this, everything else will be handled outside of this class

    def add_feature(self,feature):
        """adds a feature to self._features"""
        self._features[feature.get_id()] = feature
        return True

    def add_room(self,room):
        """adds a room to self._rooms"""
        self._rooms[room.get_id()] = room
        return True

    def add_obj(self,obj):
        """adds a obj to self._objects"""
        self._objects[obj.get_id()] = obj
        return True

    def add_person(self,person):
        """adds a person to self._people"""
        self._people[person.get_id()] = person
        return True
