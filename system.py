import converter
import feature
import object
import parser
import person
import player
import room
import time


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
        self._parser = parser.Parser()

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
                self.look(command[1])
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
        return

    def ask(self, person_id: str, obj_id: str):
        """this command takes 2 parameters, person which is an id for a person, and object, which is an id for an
        object"""
        return

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
            print(self._objects[obj].get_interaction('read'))
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_interaction('read'))
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_interaction('read'))
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print('You cannot read a person...try "ask" or "look" instead')
            return False
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print('You cannot read a room...try "look at [room]" instead')
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
            print(self._features[obj].get_interaction('search'))
            return True
        # if the object you are trying to search is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._people[obj].get_interaction('search'))
            return True
        # if the object you are trying to search is the room itself
        elif obj == self._cur_room:
            print(self._rooms[self._cur_room].get_interaction('search'))
            return True
        # if the object is not in this room
        else:
            print('The thing you are trying to search does not appear to be in this room')
            return False

    def touch(self, obj: str):
        """takes an object id and allows you to attempt to touch it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            print(self._objects[obj].get_interaction('touch'))
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_interaction('touch'))
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_interaction('touch'))
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._features[obj].get_interaction('touch'))
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._features[obj].get_interaction('touch'))
            return True
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to touch does not appear to be in this room')
            return False

    def taste(self, obj: str):
        """takes an object id and allows you to attempt to taste it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            print(self._objects[obj].get_interaction('taste'))
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_interaction('taste'))
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_interaction('taste'))
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._features[obj].get_interaction('taste'))
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._features[obj].get_interaction('taste'))
            return True
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to taste does not appear to be in this room')
            return False

    def smell(self, obj: str):
        """takes an object id and allows you to attempt to smell it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            print(self._objects[obj].get_interaction('smell'))
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_interaction('smell'))
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_interaction('smell'))
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._features[obj].get_interaction('smell'))
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._features[obj].get_interaction('smell'))
            return True
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to smell does not appear to be in this room')
            return False

    def listen(self, obj: str):
        """takes an object id and allows you to attempt to listen to it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            print(self._objects[obj].get_interaction('listen'))
            return True
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            print(self._objects[obj].get_interaction('listen'))
            return True
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            print(self._features[obj].get_interaction('listen'))
            return True
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print(self._features[obj].get_interaction('listen'))
            return True
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print(self._features[obj].get_interaction('listen'))
            return True
        # if the object is not in your room or the inventory
        else:
            print('The thing you are trying to listen to does not appear to be in this room')
            return False

    def look(self, obj: str):
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
        print('look at [object] - allows you to examine an object, person, or room')
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


    def inventory(self):
        """takes no parameters, prints out the players current inventory"""
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
        for obj in self._rooms[self._cur_room].get_objects():
            if self._objects[obj].get_hidden is False:
                print(self._objects[obj].get_desc())
        for feat in self._rooms[self._cur_room].get_features():
            if self._features[feat].get_hidden is False:
                print(self._features[feat].get_desc())
        for person_id in self._rooms[self._cur_room].get_people():
            print(self._people[person_id].get_desc())
        return



