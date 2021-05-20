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
        # add necessary text/JSON files for natural language parser to work
        self._parser.add_connections("./resources/connections.txt")
        self._parser.add_special_commands("./resources/special_commands.txt")
        self._parser.add_prepositions("./resources/prepositions.txt")
        self._parser.load_articles("./resources/articles.txt")
        self._parser.load_stopwords("./resources/stopwords.txt")
        self._parser.load_game_verbs("./resources/game_verbs.json")
        self._parser.load_game_items("./resources/game_items.json")
        self._parser.load_game_dictionary("./resources/game_dictionary.txt")

    def game_loop(self):
        while True:
            print('What would you like to do?')
            inp = input()

            # parses the input and returns a command with an interaction word and 1-2 objects
            command = self._parser.parse(inp)
            if command[0] == 'use':
                self.use(command[1], command[2])
            elif command[0] == 'ask':
                self.ask(command[1], command[2])
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
            elif command[0] == 'exit':
                self.exit()
            elif command[0] == 'drop':
                self.drop(command[1])
            else:
                print('Sorry the game does not understand that input')
                print('Try again with simpler language')
                print("Use the command 'help' for a list of useful phrases")

    def use(self, object1: str, object2: str):
        """this command takes 2 parameters, object1, which needs to be an object and is being used on object 2,
        which can be any feature, person, or object"""
        # object1 is always the giving object
        # object 2 is always the receiving object
        # checks if the object is in the inventory
        if object1 in self._player.get_inventory():
            # checks if the second object is in the room
            if object2 in self._rooms[self._cur_room].get_features():
                try:
                    # prints what happens the first time you use object1 on object 2
                    print(self._features[object2].get_interaction('use', object1))
                    # sets the condition for the feature to True (unlocked, interacted, etc)
                    self._features[object2].set_condition(True)
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
                print('You cannot use that on an object that is not in the room')
                return False
        elif object1 in self._features:
            try:
                # prints what happens the first time you use object1 on object 2
                print(self._features[object2].get_interaction('use', object1))
                # sets the condition for the feature to True (unlocked, interacted, etc)
                self._features[object2].set_condition(True)
                return True
            except interactable.KeyDoesNotExist:
                print('You cannot use the ' + self._objects[object1].get_name() + ' on the '
                      + self._features[object2].get_name())
                return False
        else:
            print("You cannot use that object")
            return False

    def ask(self, person_id: str, obj_id: str):
        """this command takes 2 parameters, person which is an id for a person, and object, which is an id for an
        object, feature, or person"""
        # checks if the person is in the room
        if person_id in self._rooms[self._cur_room].get_people():
            # checks if the object is in the inventory
            if obj_id in self._player.get_inventory():
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry I don't know anything about that'")
                    return False
            elif obj_id in self._features:
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry I don't know anything about that'")
                    return False
            elif obj_id in self._people:
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry I don't know anything about that'")
                    return False
            else:
                print("'Sorry I don't know anything about that'")
                return False
        else:
            print("You can only speak with a person in this room")
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

                # Save and format player input for later use
                killer_str = killer.title()
                weapon_str = weapon.title()

                # Validate the killer and weapon using the respective NLP methods
                killer = self._parser.find_killer(killer)
                weapon = self._parser.find_weapon(weapon)

                print("Not long after you you make the call, the police arrive on the scene, "
                "taking " + str(killer_str) + " into custody and the " + str(weapon_str) + " as evidence. "
                "You return home, and life goes on, but, a week later, you come across "
                "an article in the news that reads: ")
                if killer == 'wrong' and weapon == 'wrong':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO ALIBI AND INSUFFICIENT EVIDENCE'")
                    print("It turns out that " + str(killer_str) + " was not the killer and that the " + 
                    str(weapon_str) + "was not the murder weapon. You continue to follow the case in "
                    "the years that follow, but no substantial updates are ever released, and, "
                    "eventually, it's declared a cold case.")
                    print("As a result, whoever it was that killed Norman that bright Saturday morning "
                    "at the retreat was able to get away.")
                    print("THE END.")
                    exit()

                # change 'correct' to the killers name in final implementation
                elif killer == 'correct' and weapon == 'wrong':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO INSUFFICIENT EVIDENCE'")
                    print("It turns out that the " + str(weapon_str) + " was not the murder weapon."
                    "You continue to follow the case in the years that follow, but no substantial "
                    "updates are ever released, and, eventually, it's declared a cold case.")
                    print("As a result, " + str(killer_str) + "  was able to get away with killing Norman "
                    "that bright Saturday morning at the retreat.")
                    print("THE END.")
                    exit()

                # change 'correct' to the weapon name in final implementation
                elif killer == 'wrong' and weapon == 'correct':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO ALIBI'")
                    print("It turns out that " + str(killer_str) + " was not the killer. "
                    "You continue to follow the case in the years that follow, but no substantial "
                    "updates are ever released, and, eventually, it's declared a cold case.")
                    print("As a result, whoever it was that killed Norman that bright Saturday morning "
                    "at the retreat was able to get away.")
                    print("THE END.")
                    exit()

                elif killer == 'correct' and weapon == 'correct':
                    print("'SUSPECT CHARGED IN THE MURDER OF NORMAN BATES'")
                    print("It seems like your information was correct! You closely follow the case")
                    ("in the years that follow until one afternoon three years later, you turn on the TV "
                    "to see a guilty verdict given to " + str(killer_str) + " who, by all accounts and evidence "
                    "presented to the court, murdered Norman Bates with the " + str(weapon_str) + " one bright "
                    "Saturday morning three years ago.")
                    print("THE END.")
                    exit()
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
                print(self._features[obj].get_interaction('read'))
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
                print(self._features[obj].get_interaction('open', 'locked'))
                return True
            else:
                print(self._features[obj].get_interaction('open', 'unlocked'))
                try:
                    id_list = self._features[obj].get_interaction('open','ids')
                    for item in id_list:
                        if item in self._rooms[self._cur_room].get_objects():
                            self._objects[item].set_condition(False)
                except interactable.KeyDoesNotExist:
                    pass
                return True
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
                print(self._rooms[self._cur_room].get_interaction('touch'))
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
                print(self._rooms[self._cur_room].get_interaction('taste'))
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
                print(self._rooms[self._cur_room].get_interaction('smell'))
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
                print('You hear nothing')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('listen'))
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
            if self._objects[obj].get_hidden() is True:
                self._objects[obj].set_hidden(False)
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_desc())
            if self._features[obj].get_hidden() is True:
                self._features[obj].set_hidden(False)
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._people[obj].get_desc())
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._rooms[obj].get_description())
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
        """takes a room id or a direction and allows you to attempt to go there from the current room"""
        # if room_id is a direction
        if room_id in ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']:
            try:
                go_to = self._rooms[self._cur_room].get_connection(room_id)
                self._cur_room = go_to
                print(self.get_description())
            except room.IDAlreadyExists:
                print('This room does not have a connection to the ' + room_id)
                return False
        # if the room_id is actually a room_id
        if room_id in self._rooms[self._cur_room].get_connections().values():
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
            try:
                if self._objects[obj].get_condition() is True:
                    print('You cannot pick up that object')
                    return False
                else:
                    print('You picked up the ' + self._objects[obj].get_name())
                    self._rooms[self._cur_room].remove_object(obj)
                    self._player.add_to_inventory(obj)
                    self._objects[obj].set_hidden(False)
                    return True
            except object.AttributeDoesNotExist:
                print('You picked up the ' + self._objects[obj].get_name())
                self._rooms[self._cur_room].remove_object(obj)
                self._player.add_to_inventory(obj)
                self._objects[obj].set_hidden(False)
                return True
        else:
            print('That object is not in the room')
            return False

    def drop(self, item):
        """takes one parameter, the item to drop, drops that item in the current room and returns nothing"""
        if item in self._player.get_inventory():
            self._player.remove_from_inventory(item)
            self._rooms[self._cur_room].add_object(item)
            print('You dropped the ' + self._objects[item].get_name())
            return True
        else:
            print('That item is not in your inventory')
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
        if len(self._player.get_inventory()) == 0:
            print('your inventory is empty')
            return False
        for obj in self._player.get_inventory():
            print(self._objects[obj].get_name())
        return True

    def save(self):
        """takes no parameters, allows you to save the game"""

        print('Please enter a save file name (case sensitive)')
        location = input()

        json_player = converter.player_to_json(self._player)
        filename = 'saves/' + location + '/player.json'
        json.dump(json_player, open(filename, 'w'))

        for feat in self._features.values():
            json_feat = converter.feat_to_json(feat)
            filename = 'saves/' + location + '/features/' + feat.get_id() + '.json'
            json.dump(json_feat, open(filename, 'w'))

        for obj in self._objects.values():
            json_obj = converter.obj_to_json(obj)
            filename = 'saves/' + location + '/objects/' + obj.get_id() + '.json'
            json.dump(json_obj, open(filename, 'w'))

        for person in self._people.values():
            json_person = converter.person_to_json(person)
            filename = 'saves/' + location + '/people/' + person.get_id() + '.json'
            json.dump(json_person, open(filename, 'w'))

        for room_obj in self._rooms.values():
            json_room = converter.room_to_json(room_obj)
            filename = 'saves/' + location + '/rooms/' + room_obj.get_id() + '.json'
            json.dump(json_room, open(filename, 'w'))

        return

    def load(self):
        """takes no parameters, allows you to load the game from a save file"""

        print('Enter the name you saved the game under (case sensitive) ')
        location = input()

        if os.path.isdir('saves/' + location):

            print('Saving Game...')
            time.sleep(1)

            # grabs the player object
            player_file = open('saves/' + location + '/player.json', 'r')
            player_json = json.load(player_file)
            player_obj = converter.player_from_json(player_json)
            self._player = player_obj

            # grabs the list of json objects located in the rooms subdirectory
            room_files = os.listdir('saves/' + location + '/rooms')
            for room_file_name in room_files:
                room_file = open(room_file_name, 'r')
                room_json = json.load(room_file)
                room_obj = converter.room_from_json(room_json)
                self._rooms[room_obj]['id'] = room_obj
                self._rooms[room_obj]['id'] = room_obj

            # grabs the list of json objects located in the objects subdirectory
            object_files = os.listdir('saves/' + location +'/objects')
            for object_file_name in object_files:
                object_file = open(object_file_name, 'r')
                object_json = json.load(object_file)
                object_obj = converter.obj_from_json(object_json)
                self._objects[object_obj]['id'] = object_obj

            # grabs the list of json objects located in the features subdirectory
            feature_files = os.listdir('saves/' + location +'/features')
            for feature_file_name in feature_files:
                feature_file = open(feature_file_name, 'r')
                feature_json = json.load(feature_file)
                feature_obj = converter.feat_from_json(feature_json)
                self._features[feature_obj]['id'] = feature_obj

            # grabs the list of json objects located in the people subdirectory
            people_files = os.listdir('saves/' + location +'/people')
            for people_file_name in people_files:
                people_file = open(people_file_name, 'r')
                people_json = json.load(people_file)
                people_obj = converter.person_from_json(people_json)
                self._people[people_obj]['id'] = people_obj

            print('Game Saved under save file: ' + location)

        else:

            print('Save file could not be found')

        return

    def get_description(self):
        """gets the description of the room and all the objects/features/people in the room"""
        if self._rooms[self._cur_room].get_visited is False:
            print(self._rooms[self._cur_room].get_description())
            print('In the room there is:')
            for feat in self._rooms[self._cur_room].get_features():
                if self._features[feat].get_hidden() is False:
                    print(self._features[feat].get_sdesc())
            for obj in self._rooms[self._cur_room].get_objects():
                if self._objects[obj].get_hidden() is False:
                    print(self._objects[obj].get_sdesc())
            for person_id in self._rooms[self._cur_room].get_people():
                print(self._people[person_id].get_sdesc())
        else:
            print(self._rooms[self._cur_room].get_description())

        return

    def exit(self):
        print('are you sure you want to quit the game? (y/n)')
        ans = input().lower()
        if ans in ['y','yes','yeah']:
            print('Exiting Game...')
            time.sleep(1)
            exit()
        else:
            print('Returning to game...')
            return


    def start(self):
        """starts the game by loading the files, playing the introduction, and starting the main gameplay loop"""
        # grabs the list of json objects located in the rooms subdirectory
        room_files = os.listdir('gamefiles/rooms')
        for room_file_name in room_files:
            room_file = open('gamefiles/rooms/' + room_file_name, 'r')
            room_json = json.load(room_file)
            room_obj = converter.room_from_json(room_json)
            self._rooms[room_obj.get_id()] = room_obj

        # grabs the list of json objects located in the objects subdirectory
        object_files = os.listdir('gamefiles/objects')
        for object_file_name in object_files:
            object_file = open('gamefiles/objects/' + object_file_name, 'r')
            object_json = json.load(object_file)
            object_obj = converter.obj_from_json(object_json)
            self._objects[object_obj.get_id()] = object_obj

        # grabs the list of json objects located in the features subdirectory
        feature_files = os.listdir('gamefiles/features')
        for feature_file_name in feature_files:
            feature_file = open('gamefiles/features/' + feature_file_name, 'r')
            feature_json = json.load(feature_file)
            feature_obj = converter.feat_from_json(feature_json)
            self._features[feature_obj.get_id()] = feature_obj

        # grabs the list of json objects located in the people subdirectory
        people_files = os.listdir('gamefiles/people')
        for people_file_name in people_files:
            people_file = open('gamefiles/people/' + people_file_name, 'r')
            people_json = json.load(people_file)
            people_obj = converter.person_from_json(people_json)
            self._people[people_obj.get_id()] = people_obj

        self.introduction()

        self.game_loop()

        return

    def introduction(self):
        """plays the main introduction for the game"""

        # insert main storyline stuff here

        # just use print statements in this, everything else will be handled outside of this class

    def add_feature(self, feat: feature.Feature):
        """adds a feature to self._features"""
        self._features[feat.get_id()] = feat
        return True

    def add_room(self, room_obj: room.Room):
        """adds a room to self._rooms"""
        self._rooms[room_obj.get_id()] = room_obj
        return True

    def add_obj(self, obj: object.Object):
        """adds a obj to self._objects"""
        self._objects[obj.get_id()] = obj
        return True

    def add_person(self, per: person.Person):
        """adds a person to self._people"""
        self._people[per.get_id()] = per
        return True

    def save_base_game_files(self):
        """takes all parameters in the system and saves
        them into the proper base gamefiles in the
        gamefiles folder. Do not use this for saving"""

        for feat in self._features.values():
            json_feat = converter.feat_to_json(feat)
            filename = 'gamefiles/features/' + feat.get_id() + '.json'
            json.dump(json_feat, open(filename, 'w'))

        for obj in self._objects.values():
            json_obj = converter.obj_to_json(obj)
            filename = 'gamefiles/objects/' + obj.get_id() + '.json'
            json.dump(json_obj, open(filename, 'w'))

        for person in self._people.values():
            json_person = converter.person_to_json(person)
            filename = 'gamefiles/people/' + person.get_id() + '.json'
            json.dump(json_person, open(filename, 'w'))

        for room_obj in self._rooms.values():
            json_room = converter.room_to_json(room_obj)
            filename = 'gamefiles/rooms/' + room_obj.get_id() + '.json'
            json.dump(json_room, open(filename, 'w'))

        return


