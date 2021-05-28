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
        self._parser.load_killer("./gamefiles/killer.txt")
        self._parser.load_weapon("./gamefiles/weapon.txt")
        self._parser.load_game_dictionary("./resources/game_dictionary.txt")

    def game_loop(self):
        while True:
            print()
            print('\033[0;31;40mWhat would you like to do?')
            inp = input('\033[0;32;40m')
            print('\033[0;37;40m')
            if inp == '':
                print('\033[1;33;40mPlease type a command.\033[1;37;40m')
            else:

                # parses the input and returns a command with an interaction word and 1-2 objects
                command = self._parser.parse(inp)
                if 'verb_error' in command:
                    print('\033[1;33;40mThe game cannot determine what action you are trying to take.\033[1;37;40m')
                    print('\033[1;33;40mPlease try again using a simpler verb.\033[1;37;40m')
                    print("\033[1;33;40mTry typing 'help' for a list of commands.\033[1;37;40m")
                    pass
                elif 'object_error' in command:
                    print('\033[1;33;40mThe game cannot find the object you are trying to interacting with.\033[1;37;40m')
                    print('\033[1;33;40mTry to be more specific when talking about the object.\033[1;37;40m')
                    pass
                else:
                    if command[0] == 'use':
                        if len(command) < 3:
                            print("\033[1;33;40mYou must 'use' one object on another. Try rephrasing to 'use [object] on ["
                                  "feature]'.\033[1;37;40m")
                            pass
                        else:
                            self.use(command[1], command[2])
                    elif command[0] == 'ask':
                        if len(command) < 3:
                            print("They respond by asking, 'What did you want to ask me about?'")
                            print('\033[1;33;40mTry asking this person about an object you are carrying, a feature in the '
                                  'house, or another person.\033[1;37;40m')
                        else:
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
                        print('\033[1;33;40mSorry, the game does not understand that input.\033[1;37;40m')
                        print('\033[1;33;40mTry again with simpler language. Please make sure that you use commands and '
                              'objects that are in the game.\033[1;37;40m')
                        print("\033[1;33;40mUse the command 'help' for a list of useful phrases.\033[1;37;40m")

    def use(self, object1: str, object2: str):
        """this command takes 2 parameters, object1, which needs to be an object and is being used on object 2,
        which can be any feature, person, or object """
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
                    print('\033[1;33;40mYou cannot use the ' + self._objects[object1].get_name() + ' on the '
                          + self._features[object2].get_name() + '.\033[1;37;40m')
                    return False
            # checks if the object is a person
            elif object2 in self._people:
                print('\033[1;33;40mYou cannot use an object on a person.\033[1;37;40m')
                return False
            # checks if the object is a room
            elif object2 in self._rooms:
                print('\033[1;33;40mYou cannot use an object on a room.\033[1;37;40m')
                return False
            else:
                print('\033[1;33;40mYou cannot use that on an object that is not in the room.\033[1;37;40m')
                return False
        elif object1 in self._features:
            try:
                # prints what happens the first time you use object1 on object 2
                print(self._features[object2].get_interaction('use', object1))
                # sets the condition for the feature to True (unlocked, interacted, etc)
                self._features[object2].set_condition(True)
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot use the ' + self._objects[object1].get_name() + ' on the '
                      + self._features[object2].get_name() + '.\033[1;37;40m')
                return False
        else:
            print("\033[1;33;40mYou cannot use that object.\033[1;37;40m")
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
                    print("'Sorry, I don't know anything about that.'")
                    return False
            elif obj_id in self._features:
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry, I don't know anything about that.'")
                    return False
            elif obj_id in self._people:
                try:
                    print(self._people[person_id].get_interaction('ask', obj_id))
                    return True
                except interactable.KeyDoesNotExist:
                    print("'Sorry, I don't know anything about that.'")
                    return False
            else:
                print("'Sorry, I don't know anything about that.'")
                return False
        else:
            print("\033[1;33;40mYou can only speak with a person in this room.\033[1;37;40m")
            return False

    def call(self):
        """this command allows you to call the police when you are in the grand foyer and end the game"""
        if self._cur_room == 'R01':
            print('You pick up the phone.')
            print('\033[1;33;40mAre you sure you want to call the police? Make sure that you know the killer '
                  'and the murder weapon. (Y/N)\033[1;37;40m')
            inp = input('\033[0;32;40m').upper()
            print('\033[0;37;40m')
            if inp == 'Y' or inp == 'YES':
                # sleeps inserted for dramatic effect
                print('ring...')
                time.sleep(1)
                print('ring...')
                time.sleep(1)
                print('ring...')
                time.sleep(1)
                print('"Hello, this is Officer Christie with the Eureka Police Department. Who is this?"')
                print('You tell him your name and describe the situation.')
                print('"A murder, you say? And who did you say was the culprit?"')
                killer = input('\033[0;33;40mName of the killer: \033[0;32;40m').upper()
                print('"\033[0;37;40mAh, I see. And how did they kill this man?"')
                weapon = input('\033[0;33;40mName of the murder weapon: \033[0;32;40m').upper()
                print('\033[0;37;40m')

                # Save and format player input for later use
                killer_str = killer.title()
                weapon_str = weapon.lower()

                # Validate the killer and weapon using the respective NLP methods
                killer = self._parser.find_killer(killer)
                weapon = self._parser.find_weapon(weapon)

                print("Not long after you you make the call, the police arrive on the scene, "
                    "taking " + str(killer_str) + " into custody and the " + str(weapon_str) + " as evidence. "
                    "You return home, and life goes on, but, a week later, you come across "
                    "an article in the news that reads: ")
                if killer == 'wrong' and weapon == 'wrong':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO ALIBI AND INSUFFICIENT EVIDENCE'")
                    print("It turns out that " + str(killer_str) + " was not the killer and the " +
                        str(weapon_str) + " was not the murder weapon. You continue to follow the case in "
                        "the years that follow, but no substantial updates are ever released, and, "
                        "eventually, it's declared a cold case.")
                    print("As a result, whoever it was that killed Norman that bright Friday morning "
                          "at the retreat was able to get away.")
                    print("THE END.")
                    exit()

                # change 'correct' to the killers name in final implementation
                elif killer == 'correct' and weapon == 'wrong':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO INSUFFICIENT EVIDENCE'")
                    print("It turns out that the " + str(weapon_str) + " was not the murder weapon."
                        "You continue to follow the case in the years that follow, but no substantial "
                        "updates are ever released, and, eventually, it's declared a cold case.")
                    print("As a result, " + str(killer_str) + " was able to get away with killing Norman "
                        "that bright Friday morning at the retreat.")
                    print("THE END.")
                    exit()

                # change 'correct' to the weapon name in final implementation
                elif killer == 'wrong' and weapon == 'correct':
                    print("'SUSPECT RELEASED WITHOUT CHARGES DUE TO ALIBI'")
                    print("It turns out that " + str(killer_str) + " was not the killer. "
                        "You continue to follow the case in the years that follow, but no substantial "
                        "updates are ever released, and, eventually, it's declared a cold case.")
                    print("As a result, whoever it was that killed Norman that bright Friday morning "
                        "at the retreat was able to get away.")
                    print("THE END.")
                    exit()

                elif killer == 'correct' and weapon == 'correct':
                    print("'SUSPECT CHARGED IN THE MURDER OF NORMAN BATES'")
                    print("It seems like your information was correct! You closely follow the case"
                        "in the years that follow until one afternoon three years later, you turn on the TV "
                        "to see a guilty verdict given to " + str(killer_str) + " who, by all accounts and evidence "
                        "presented to the court, murdered Norman Bates with the " + str(
                        weapon_str) + " one bright Friday morning three years ago.")
                    print("THE END.")
                    exit()
            else:
                print('You decide you need more evidence. You set the phone down.')
        else:
            print('\033[1;33;40mSorry, you cannot call the police from this room.\033[1;37;40m')

    def read(self, obj: str):
        """this command takes an object and allows you to attempt to read it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot read this object.\033[1;37;40m')
                return False

        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot read this object.\033[1;37;40m')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('read'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot read this object.\033[1;37;40m')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            print('\033[1;33;40mYou cannot read a person. Maybe try "ask" or "look" instead.\033[1;37;40m')
            return False
        # if the object you are trying to read is the room itself
        elif obj in self._rooms:
            print('\033[1;33;40mYou cannot read a room. Try "look at [room]" or just "look" instead.\033[1;37;40m')
            return False
        # if the object is not in your room or the inventory
        else:
            print('\033[1;33;40mThe thing you are trying to read does not appear to be in this room.\033[1;37;40m')
            return False

    def open(self, obj: str):
        """this command takes an object and allows you to attempt to open it"""
        # if the object is an object
        if obj in self._objects:
            print('\033[1;33;40mYou cannot open this object.\033[1;37;40m')
            return False
        # if the object is a person
        elif obj in self._people:
            print('\033[1;33;40mYou cannot open a person.\033[1;37;40m')
            return False
        # if the object is a feature in the room
        elif obj in self._rooms[self._cur_room].get_features():
            # for certain features the condition specifies if the object is locked
            try:
                if self._features[obj].get_condition() is False:
                    print(self._features[obj].get_interaction('open', 'locked'))
                    return True
                else:
                    print(self._features[obj].get_interaction('open', 'unlocked'))
                    # checks if opening this feature allows access to some items
                    try:
                        id_list = self._features[obj].get_interaction('open', 'obj_ids')
                        for item in id_list:
                            if item in self._rooms[self._cur_room].get_objects():
                                self._objects[item].set_condition(True)
                    except interactable.KeyDoesNotExist:
                        pass
                    # checks if opening this feature allows access to some rooms
                    try:
                        id_list = self._features[obj].get_interaction('open','room_ids')
                        for room in id_list:
                            self._rooms[self._cur_room].add_connection(room[0],room[1])
                    except interactable.KeyDoesNotExist:
                        pass
                    return True
            except feature.AttributeDoesNotExist:
                print('\033[1;33;40mYou cannot open that thing.\033[1;37;40m')
        # if the object is a room
        elif obj in self._rooms:
            print('\033[1;33;40mYou cannot open a room. Try "go to [room]" or "open [door to room]" instead.\033[1;37;40m')
            return False
        # if the object is not in the room
        else:
            print('\033[1;33;40mThe thing that you are trying to open is not in this room.\033[1;37;40m')
            return False

    def search(self, obj: str):
        """this command lets you search a  given room or feature"""
        # if the search parameter is an object
        if obj in self._objects:
            print('\033[1;33;40mYou cannot search this object.\033[1;37;40m')
            return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot search that thing.\033[1;37;40m')
                return False
        # if the object you are trying to search is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot search that thing.\033[1;37;40m')
                return False
        # if the object you are trying to search is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('search'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot search that thing.\033[1;37;40m')
                return False
        # if the object is not in this room
        else:
            print('\033[1;33;40mThe thing that you are trying to search does not appear to be in this room.\033[1;37;40m')
            return False

    def touch(self, obj: str):
        """takes an object id and allows you to attempt to touch it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot touch that object.\033[1;37;40m')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot touch that object.\033[1;37;40m')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot touch that thing.\033[1;37;40m')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot touch that person.\033[1;37;40m')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('touch'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot touch that room.\033[1;37;40m')
                return False
        # if the object is not in your room or the inventory
        else:
            print('\033[1;33;40mThe thing you are trying to touch does not appear to be in this room.\033[1;37;40m')
            return False

    def taste(self, obj: str):
        """takes an object id and allows you to attempt to taste it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot taste that thing.\033[1;37;40m')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot taste that thing.\033[1;37;40m')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot taste that thing.\033[1;37;40m')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot taste that thing.\033[1;37;40m')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('taste'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mYou cannot taste that thing.\033[1;37;40m')
                return False
        # if the object is not in your room or the inventory
        else:
            print('\033[1;33;40mThe thing that you are trying to taste does not appear to be in this room.\033[1;37;40m')
            return False

    def smell(self, obj: str):
        """takes an object id and allows you to attempt to smell it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot smell that thing.\033[1;37;40m')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot smell that thing.\033[1;37;40m')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot smell that thing.\033[1;37;40m')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot smell that thing.\033[1;37;40m')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('smell'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot smell that thing.\033[1;37;40m')
                return False
        # if the object is not in your room or the inventory
        else:
            print('\033[1;33;40mThe thing that you are trying to smell does not appear to be in this room.\033[1;37;40m')
            return False

    def listen(self, obj: str):
        """takes an object id and allows you to attempt to listen to it"""
        # if the object is in your inventory
        if obj in self._player.get_inventory():
            try:
                print(self._objects[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing.')
                return False
        # if the object is in the current room
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                print(self._objects[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing.')
                return False
        # if the feature is in the current room
        elif obj in self._rooms[self._cur_room].get_features():
            try:
                print(self._features[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing.')
                return False
        # if the object you are trying to read is a person
        elif obj in self._rooms[self._cur_room].get_people():
            try:
                print(self._people[obj].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('You hear nothing.')
                return False
        # if the object you are trying to read is the room itself
        elif obj == self._cur_room:
            try:
                print(self._rooms[self._cur_room].get_interaction('listen'))
                return True
            except interactable.KeyDoesNotExist:
                print('\033[1;33;40mSorry, you cannot listen to that thing.\033[1;37;40m')
                return False
        # if the object is not in your room or the inventory
        else:
            print('\033[1;33;40mThe thing that you are trying to listen to does not appear to be in this room.\033[1;37;40m')
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
            print('\033[1;33;40mThe thing that you are trying to examine does not appear to be in this room.\033[1;37;40m')
            return False

    def look(self):
        """prints the long form description of the current room"""
        self._rooms[self._cur_room].set_visited(False)
        self.get_description()
        return True

    def go(self, room_id: str):
        """takes a room id or a direction and allows you to attempt to go there from the current room"""
        # if room_id is a direction
        if room_id in ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']:
            try:
                connections = self._rooms[self._cur_room].get_connections()
                go_to = connections[room_id]
                self._cur_room = go_to
                self.get_description()
                return True
            except KeyError:
                print('\033[1;33;40mThis room does not have a connection to the ' + room_id + '.\033[1;37;40m')
                return False
        # if the room_id is actually a room_id
        elif room_id in self._rooms[self._cur_room].get_connections().values():
            self._cur_room = room_id
            self.get_description()
            return True
        else:
            print('\033[1;33;40mYou cannot enter that room from this room.\033[1;37;40m')
            print('\033[1;33;40mPerhaps the door is locked? Try to use "open [door name]".\033[1;37;40m')
            return False

    def take(self, obj: str):
        """takes an object id and allows you to attempt to take it from the room it is currently in"""
        if obj in self._people:
            print('\033[1;33;40mYou cannot take a person.\033[1;37;40m')
            return False
        elif obj in self._features:
            print('\033[1;33;40mYou cannot take this item from the room.\033[1;37;40m')
            return False
        elif obj in self._rooms:
            print('\033[1;33;40mYou cannot take a room.\033[1;37;40m')
            return False
        elif obj in self._player.get_inventory():
            print('\033[1;33;40mThat object is already in your inventory.\033[1;37;40m')
            return False
        elif obj in self._rooms[self._cur_room].get_objects():
            try:
                if self._objects[obj].get_condition() is False:
                    print('\033[1;33;40mYou cannot pick up that object.\033[1;37;40m')
                    return False
                else:
                    print('You picked up the ' + self._objects[obj].get_name() + '.')
                    self._rooms[self._cur_room].remove_object(obj)
                    self._player.add_to_inventory(obj)
                    self._objects[obj].set_hidden(False)
                    return True
            except feature.AttributeDoesNotExist:
                print('You picked up the ' + self._objects[obj].get_name() + '.')
                self._rooms[self._cur_room].remove_object(obj)
                self._player.add_to_inventory(obj)
                self._objects[obj].set_hidden(False)
                return True
        else:
            print('\033[1;33;40mYou could not find that object in this room. Try being more specific.\033[1;37;40m')
            return False

    def drop(self, item):
        """takes one parameter, the item to drop, drops that item in the current room and returns nothing"""
        if item in self._player.get_inventory():
            self._player.remove_from_inventory(item)
            self._rooms[self._cur_room].add_object(item)
            print('You dropped the ' + self._objects[item].get_name() + '.')
            return True
        else:
            print('\033[1;33;40mThat item is not in your inventory.\033[1;37;40m')
            return False

    def help(self):
        """takes no parameters, prints out a list of commands that the player is allowed to use"""
        print('\033[1;33;40mHere are some examples of possible commands you can use:')
        print('look at [object] - allows you to examine an object, feature, or person')
        print('look - allows you to examine the room in detail')
        print('go to [room] - allows you to enter unlocked rooms connected to the current room')
        print('take [object] - allows you to pick up an object')
        print('drop [object] - allows you to drop an object in your inventory into the room')
        print('inventory - allows you to examine the contents of your inventory')
        print('savegame - allows you to save the game')
        print('loadgame - allows you to load a saved game')
        print('exit - allows you to exit the game (remember to save your progress first)')
        print('use [object] on [object/feature] - allows you to use an object on another object or feature')
        print('ask [person] about [object/feature/person] - allows you to interrogate a person about an object, '
              'a feature in the house, or another person')
        print('read [object] - allows you to read an object')
        print('open [object] - allows you to open an unlocked door or other similar object')
        print('search [object] - allows you to search through an object or room')
        print('touch [object] - allows you to feel an object; this may give you more clues')
        print('taste [object] - allows you to taste an object; this may give you more clues')
        print('smell [object] - allows you to smell an object or room; this may give you more clues')
        print('listen [object] - allows you to smell an object or room; this may give you more clues\033[1;37;40m')
        return

    def inventory(self):
        """takes no parameters, prints out the players current inventory"""
        if len(self._player.get_inventory()) == 0:
            print('\033[1;33;40mYour inventory is empty.\033[1;37;40m')
            return False
        for obj in self._player.get_inventory():
            print('\033[1;33;40m' + self._objects[obj].get_name() + '.\033[1;37;40m')
        return True

    def save(self):
        """takes no parameters, allows you to save the game"""

        print('\033[1;33;40mPlease enter a save file name (case sensitive): \033[1;37;40m')
        location = input('\033[0;32;40m')
        print('\033[0;37;40m')

        try:
            os.mkdir('saves/' + location)
            os.mkdir('saves/' + location + '/features')
            os.mkdir('saves/' + location + '/objects')
            os.mkdir('saves/' + location + '/people')
            os.mkdir('saves/' + location + '/rooms')
        except FileExistsError:
            pass

        # saves the current room
        filename = 'saves/' + location + '/cur_room.json'
        json.dump(self._cur_room, open(filename,'w'))

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

        print('\033[1;33;40mGame saved to ./saves/' + location + '.\033[1;37;40m')

        return

    def load(self):
        """takes no parameters, allows you to load the game from a save file"""

        print('\033[1;33;40mEnter the location of the save file to load the game from (case sensitive): \033[1;37;40m')
        location = input('\033[0;32;40m')
        print('\033[0;37;40m')

        if os.path.isdir('saves/' + location):

            print('\033[1;33;40mGame loading...\033[1;37;40m')
            time.sleep(1)

            # grabs the player object
            player_file = open('saves/' + location + '/player.json', 'r')
            player_json = json.load(player_file)
            player_obj = converter.player_from_json(player_json)
            self._player = player_obj

            # loads the current room
            room_file = open('saves/' + location + '/cur_room.json', 'r')
            self._cur_room = json.load(room_file)

            # grabs the list of json objects located in the rooms subdirectory
            room_files = os.listdir('saves/' + location + '/rooms')
            for room_file_name in room_files:
                room_file = open('saves/' + location + '/rooms/' + room_file_name, 'r')
                room_json = json.load(room_file)
                room_obj = converter.room_from_json(room_json)
                self._rooms[room_obj.get_id()] = room_obj

            # grabs the list of json objects located in the objects subdirectory
            object_files = os.listdir('saves/' + location + '/objects')
            for object_file_name in object_files:
                object_file = open('saves/' + location + '/objects/' + object_file_name, 'r')
                object_json = json.load(object_file)
                object_obj = converter.obj_from_json(object_json)
                self._objects[object_obj.get_id()] = object_obj

            # grabs the list of json objects located in the features subdirectory
            feature_files = os.listdir('saves/' + location + '/features')
            for feature_file_name in feature_files:
                feature_file = open('saves/' + location + '/features/' + feature_file_name, 'r')
                feature_json = json.load(feature_file)
                feature_obj = converter.feat_from_json(feature_json)
                self._features[feature_obj.get_id()] = feature_obj

            # grabs the list of json objects located in the people subdirectory
            people_files = os.listdir('saves/' + location + '/people')
            for people_file_name in people_files:
                people_file = open('saves/' + location + '/people/' + people_file_name, 'r')
                people_json = json.load(people_file)
                people_obj = converter.person_from_json(people_json)
                self._people[people_obj.get_id()] = people_obj

            print('\033[1;33;40mGame loaded from save file: ' + location + '.\033[1;37;40m')
            return True

        else:

            print('\033[1;33;40mSave file could not be found.\033[1;37;40m')
            return False

    def get_description(self):
        """gets the description of the room and all the objects/features/people in the room"""
        if self._rooms[self._cur_room].get_visited() is False:
            print(self._rooms[self._cur_room].get_desc())
            self._rooms[self._cur_room].set_visited(False)
            print('Looking around, you observe the following details:')
            for feat in self._rooms[self._cur_room].get_features():
                if self._features[feat].get_hidden() is False:
                    print(self._features[feat].get_sdesc())
            for obj in self._rooms[self._cur_room].get_objects():
                if self._objects[obj].get_hidden() is False:
                    print(self._objects[obj].get_sdesc())
            for person_id in self._rooms[self._cur_room].get_people():
                print(self._people[person_id].get_sdesc())
            self._rooms[self._cur_room].set_visited(True)
        else:
            print(self._rooms[self._cur_room].get_sdesc())
        return

    def exit(self):
        print('\033[1;33;40mAre you sure you want to quit the game? (y/n)\033[1;37;40m')
        ans = input('\033[0;32;40m').lower()
        print('\033[0;37;40m')
        if ans in ['y', 'yes', 'yeah']:
            print('\033[1;33;40mWould you like to save first? (y/n)\033[1;37;40m')
            ans = input('\033[0;32;40m').lower()
            print('\033[0;37;40m')
            if ans in ['y', 'yes', 'yeah']:
                self.save()
            print('\033[1;33;40mExiting game...\033[1;37;40m')
            exit()
        else:
            print('\033[1;33;40mReturning to game...\033[1;37;40m')
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

        os.system('color')

        print('\033[1;33;40mWould you like to load a saved game? (y/n)\033[1;37;40m')
        inp = input('\033[0;32;40m').lower()
        print('\033[0;37;40m')
        if inp in ['y', 'yes', 'yeah']:
            check = False
            # makes sure you're able to load the game
            while not check:
                check = self.load()
            self.game_loop()
        else:
            self.introduction()

            self.get_description()

            self.game_loop()

            return

    def introduction(self):
        """plays the main introduction for the game"""

        setting = "\033[1;37;40m'San Francisco, California. June 2019."
        introduction = [
            "Work has been difficult lately. "
            "Over the past six months, your boss at the detective agency has been "
            "down your neck due to an important case that, according to him, "
            "could 'make his career'. "
            "You've been living off of coffee and cold lunches and, now, with "
            "the case formally closed, you find yourself yearning for a much "
            "needed vacation and change of pace. ",
            "One afternoon, on your lunch break, you come across an advertisement "
            "in the newspaper for a digital detox retreat. The retreat is hosted "
            "over the weekend at an old, historical mansion in a remote location "
            "five hours north of the city. No cellphones, laptops, or computers "
            "of any kind are permitted. "
            "'Perfect', you think. The retreat is not too far away, and you've "
            "been looking for an excuse to finally turn off your cellphone and "
            "get away from everything. ",
            "You perform a quick Google search and learn that the mansion is owned "
            "by the descendent of an old family that became wealthy during the "
            "California Gold Rush circa the 1850s--a man by the name of Norman "
            "Bates. "
            "This piques your interest and, the next day, you call the phone "
            "number on the advertisement to book a reservation two weeks from "
            "now and request that Friday off from work. ",
            "Two weeks later, on the Friday of the first day of the retreat, "
            "you wake up at 4:00 AM to get ready and catch the bus north to "
            "the city of Eureka. "
            "From there, you follow the instructions in the reservation email "
            "to wait at the post office, and you're picked up by a man in a "
            "weathered truck who simply introduces himself as 'Todd'.",
            "Todd drives west, into the mountains that border the eastern edge "
            "of the city and, before long, you find yourself surrounded by "
            "dense, dark forests. "
            "The car ride is silent, and you begin dozing off soon after Todd "
            "exits the main road, turning onto an unmarked backroad that cuts "
            "deeper into the forest. ",
            "After an unknown amount of time, you wake up to the sound of Todd "
            "clearing his throat. You groggily look around to discover that "
            "you've arrived at a clearly old, yet seemingly well-kept mansion "
            "that matches the pictures you had seen online. "
            "You can tell that Todd is impatient, so you quickly grab your "
            "bags, thank him, and then exit the truck. Todd drives away as you "
            "stand there, still tired, examining the front of the mansion. "
            "The architecture has a distinctly Victorian style feel to it, and "
            "it looks strangely out of place this far into the forest. ",
            "You look around, but see nobody. You recall from the reservation "
            "email that you received that three other retreat participants--"
            "a man by the name of Sam Smith, a woman by the name of Heather "
            "Poirot, and another woman by the name of Ava Scarlett--"
            "were supposed to be attending the retreat along with you. "
            "The email also noted that Norman Bates' son, Adam Bates, and "
            "his assistant, Alice Stone, would be present during the retreat "
            "as well. You vaguely remember that a groundskeeper called "
            "Al Weatherby had been mentioned too. ",
            "Securing your bags, you climb the front steps and knock on the "
            "door. When no one answers, you try the doorknob. To your "
            "surprise, it's unlocked. ",
            "You open the door and enter...",
            "You quickly realize this vacation is not going to be as calming as you had hoped. A dead body is lying on the "
            "floor. You recognize it as your host, Norman Bates. Six people surround him, in various states of shock and "
            "despair. "
            "The next few minutes are a blur, but you realize that, as the only person in the house who could not be the "
            "killer, you are the only one qualified to find out who is.",
            "Search the house, talk to the suspects, and find out what happened here. As you explore you may need to pick "
            "up objects and collect evidence to enter locked rooms, interact with other objects, and question "
            "the inhabitants. When you are reasonably certain you "
            "know the killer and the murder weapon, come back to this room and call the police on the rotary phone in this "
            "room. This will end the story. (Remember at any point you can type 'help' for a list of useful commands and "
            "phrases).",
        ]

        print("")
        for char in setting:
            print(char, end="", flush=True)
            time.sleep(0.05)

        time.sleep(0.75)
        print("")

        for string in introduction:
            print(string)
            input("\033[1;33;40m(press enter to continue)\033[1;37;40m")

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
