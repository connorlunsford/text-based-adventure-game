import json

class ParserException(Exception):
    """Base exception class for the Parser class"""
    pass

class ParserMissingFile(ParserException):
    """Raised when a required text file has not been added to a Parser object"""
    pass

class InvalidInput(ParserException):
    """Riased when the input is invalid"""
    pass

class InvalidSentenceStructure(ParserException):
    """Raised when an input has an invalid sentence structure"""
    pass  

class Parser:

    def __init__(self):
        return

    # load name of killer from file
    def load_killer(self, filepath: str):
        # read killer id from file as a string
        with open(filepath, "r") as fp:
            if not hasattr(self, "_killer"):
                self._killer = fp.read()
                fp.close()
            else:
                fp.close()
                raise ParserException    

    # load weapon from file
    def load_weapon(self, filepath: str):
        # read weapon id from file as a string
        with open(filepath, "r") as fp:
            # articles = list(fp.read().split())
            if not hasattr(self, "_weapon"):
                self._weapon = fp.read()
                fp.close()
            else:
                fp.close()
                raise ParserException          

    # load the articles text file
    def load_articles(self, filepath: str):
        # read each line/word from the file and create a list
        with open(filepath, "r") as fp:
            articles = list(fp.read().split())
        if not hasattr(self, "_articles"):
            self._articles = articles
            fp.close()
        else:
            fp.close()
            raise ParserException      

    # load the stopwords text file
    def load_stopwords(self, filepath: str):
        # read each line/word from the file and create a list
        with open(filepath, "r") as fp:
            stopwords = list(fp.read().split())
        if not hasattr(self, "_stopwords"):
            self._stopwords = stopwords
            fp.close()
        else:
            fp.close()
            raise ParserException  

    # load the verbs dictionary with all aliases
    def load_game_verbs(self, filepath: str):
        fp = open(filepath, "r")
        if not hasattr(self, "_game_verbs"):
            self._game_verbs = json.load(fp)
            fp.close()
        else:
            fp.close()
            raise ParserException              

    # load the game items dictionary. inludes all rooms, objects, people,
    # features, and directions
    def load_game_items(self, filepath: str):
        fp = open(filepath, "r")
        if not hasattr(self, "_game_items"):
            self._game_items = json.load(fp)
            fp.close()
        else:
            fp.close()
            raise ParserException  

    # load full game dictionary for verify_words step. inludes all rooms, 
    # objects, people, features, verbs, special commands, directions, and
    # prepositions
    def load_game_dictionary(self, filepath: str):
        fp = open(filepath, "r")
        if not hasattr(self, "_game_dictionary"):
            self._game_dictionary = fp.read()
            fp.close()
        else:
            fp.close()
            raise ParserException  

    # methods for managing a prepositions text file
    def add_prepositions(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_prepositions"):
            self._prepositions = file_contents
            #setattr(self, attribute_name, file_contents)
            fp.close()
        else:
            fp.close()
            raise ParserException

    def set_prepositions(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_prepositions"):
            self._prepositions = file_contents
            #setattr(self, attribute_name, file_contents)
            fp.close()
        else:
            fp.close()
            raise ParserException        

    def delete_prepositions(self):
        if hasattr(self, "_prepositions"):
            del(self._prepositions)
            #delattr(self, attribute_name)
        else:
            raise ParserException

    # methods for managing a special commands text file
    def add_special_commands(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_special_commands"):
            self._special_commands = file_contents
            fp.close()
        else:
            fp.close()
            raise ParserException

    def set_special_commands(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_special_commands"):
            self._special_commands = file_contents
            fp.close()
        else:
            fp.close()
            raise ParserException        

    def delete_special_commands(self):
        if hasattr(self, "_special_commands"):
            del(self._special_commands)
        else:
            raise ParserException

    # methods for managing a connections text file
    def add_connections(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_connections"):
            self._connections = file_contents
            fp.close()
        else:
            fp.close()
            raise ParserException

    def set_connections(self, filepath: str):
        fp = open(filepath, "r")
        file_contents = fp.read()
        if not hasattr(self, "_connections"):
            self._connections = file_contents
            fp.close()
        else:
            fp.close()
            raise ParserException        

    def delete_connections(self):
        if hasattr(self, "_connections"):
            del(self._connections)
        else:
            raise ParserException

    # killer and weapon methods
    # TODO: refactor to remove repitition

    def find_killer(self, killer: str):
        """this should take a phrase and return either "correct" or "wrong" """

        # check all aliases to see if player's guess resolves to a person
        for i in range(len(self._game_items)):
            for obj_set in self._game_items[i]:
                key_list = list(self._game_items[i].keys())
                value_list = list(self._game_items[i].values())
                # if it resolves to a person, check to see if it is the killer
                if killer.lower() in value_list[0]:
                    if key_list[0] == self._killer:
                        return "correct"
                    else:
                        return "wrong"
        
        # if it gets this far, it has searched the entire game_items dictionary
        # and the player's input does not resolve to a person
        return "wrong"


    def find_weapon(self, weapon: str):
        """this should take a phrase and return either "correct" or "wrong" """

        # check all aliases to see if player's guess resolves to an object
        for i in range(len(self._game_items)):
            for obj_set in self._game_items[i]:
                key_list = list(self._game_items[i].keys())
                value_list = list(self._game_items[i].values())
                # if it resolves to an object, check to see if it is the correct object/weapon
                if weapon.lower() in value_list[0]:
                    if key_list[0] == self._weapon:
                        return "correct"
                    else:
                        return "wrong"

        # if it gets this far, it has searched the entire game_items dictionary
        # and the player's input does not resolve to a recognized object/weapon
        return "wrong"

    # Lexical Parsing Stage Methods        

    def tokenize(self, input: str):
        """Takes user input as a string, converts to lower case, removes all
        punctuation, and tokenizes to separate individual words. Credit for this
        method: https://stackoverflow.com/questions/9797357/dividing-a-string-at-various-punctuation-marks-using-split/33393581
        This will split hyphenated words, but I don't think that's an issue
        in this game."""
        lower_input = input.lower()
        words = "".join((char if char.isalpha() else " ") for char in lower_input).split()
        # returns list of individual words
        return words

    def remove_articles(self, words: list):
        """ takes a list of words and removes all articles, returns a list"""
        words_no_articles = []
        for word in words:
            if word not in self._articles:
                words_no_articles.append(word)
        # return list of words not including articles or punctuation
        return words_no_articles

    def remove_stopwords(self, words: list):
        """takes a list of words and removes stopwords, returns a list"""

        words_no_stopwords = []
        for word in words:
            if word not in self._stopwords:
                words_no_stopwords.append(word)
        # return list of words with no articles or stopwords
        return words_no_stopwords

    def verify_words(self, clean_input: list):
        """takes a list of cleaned words and verifies that they are recognized
        by the game"""

        """ TODO: this currently only returns recognized words and will ignore
        all others. Is this how we want to handle this? Or do we want to return
        some kind of message about not understanding what the user means?"""
        

        # TODO: implement error checking/exception for unrecognized/misspelled words
        # this should probably be done as part of the resolver?
        
        final_words = []
        for word in clean_input:
            if word in self._game_dictionary:
                final_words.append(word)
        return final_words

    def lexical_handler(self, input: str):
        # 1st: converts to all lower case, remove punctuation, tokenize words
        # 2nd: removes articles from the list
        # 3rd: removes stopwords from the list
        # 4th: verifies words are recognized by the game

        # returns clean list of words, ready to be classified
        return self.verify_words(self.remove_stopwords(self.remove_articles(self.tokenize(input))))

    # Classify Stage Methods

    def classify_input(self, input:list):
        """analyzes the grammatical structure of an input and attempts to assign 
        grammatical classifications, such as verb, direct object, or indirect object,
        based upon this structure"""
        
        # Get all prepositions
        if hasattr(self, "_prepositions"):
            prepositions = self._prepositions
        else:
            raise ParserMissingFile

        # First word is always the verb
        verb = input[0]
        
        # Second word is either a preposition or a direct object/part of a direct object
        second_word = input[1]
        
        # If second word is a preposition, combine it with the verb
        # Consider everything after the preposition to be the direct object
        verb_modifier = False
        if second_word in prepositions:
            verb = verb + " " + second_word
            direct_object = input[2:]
            verb_modifier = True
        # If the second word is not a preposition, consider everything after
        # the verb to be the direct object
        else:
            direct_object = input[1:]

        # Search for any prepositions in the remaining input as this would 
        # indicate the presence of an indirect object
        for i in range(len(direct_object)):
            # If a preposition is found
            if direct_object[i] in prepositions:
                # Get the second half of the array; this is the indirect object
                indirect_object = direct_object[i + 1:]
                # Get the left half of the array; this is the direct object
                direct_object = direct_object[:i]
                break

        # Make sure that there are no additional prepositions in the input
        # as this would suggest an invalid sentence structure
        if "indirect_object" in locals():
            for i in range(len(indirect_object)):
                if indirect_object[i] in prepositions:
                    raise InvalidSentenceStructure
        else:
            for i in range(len(direct_object)):
                if direct_object[i] in prepositions:
                    raise InvalidSentenceStructure

        # Handle case: verb + preposition + noun + preposition + noun
        # E.g., "look at painting on wall"
        # In this case, the wall is no longer an indirect object, so everything after the second
        # preposition should be removed OR it should be considered part of the direct object
        # In this instance, I opted to remove it as it keeping it would require
        # the tracking of more object aliases.
        if verb_modifier and "indirect_object" in locals():
            del indirect_object

        # Concatenate the direct object array into a single string
        direct_object = " ".join(direct_object)

        # Add the verb and direct object to the result list
        result = [verb, direct_object]

        # If an indirect_object is present, concatenate its array
        # into a single string and add it to the result list
        if "indirect_object" in locals():
            indirect_object = " ".join(indirect_object)
            result.append(indirect_object)

        return result

    def classify_handler(self, input: list):
        """handles the classify stage of the natural language parser, including 
        special cases (e.g., direction, single word commands) and passing the 
        input to the method responsible for analyzing the grammatical structure"""

        if input == []:
            raise InvalidInput

        # Get all connections
        if hasattr(self, "_connections"):
            connections = self._connections
        else:
            raise ParserMissingFile
        
        # Get all special (single-word) commands
        if hasattr(self, "_special_commands"):
            single_commands = self._special_commands
        else:
            raise ParserMissingFile

        # Check for the presence of a single command
        if len(input) == 1 and input[0] in single_commands:
            return input[:1]

        # Check for the presence of a connection without a "go" verb
        if " ".join(input) in connections:
            return ["go", " ".join(input)]

        # Input that reaches this point should be longer than one word long;
        # raise an exception if it is not
        if len(input) == 1:
            raise InvalidInput

        # Analyze the sentence structure and return the result
        try:
            return self.classify_input(input)
        except:
            raise ParserException


    # Resolve Stage Methods

    def resolve(self, input: list):
        """will receive a list of strings that are words or phrases: [verb, direct 
        object, indirect object (opt)] (each can be 1 or more words)"""
        
        # at least one "word" will be returned
        input_verb = input[0]
        # if not a single word command, then next is direct object
        if len(input) >= 2:
            input_direct = input[1]
        else:
            input_direct = None
        # if third, then indirect object
        if len(input) == 3:
            input_indirect = input[2]
        else:
            input_indirect = None            

        resolved_verb = None
        resoved_direct_obj = []
        resoved_indirect_obj = []
        # list of resolved ["verb", direct_object_id, indirect_object_id] to
        # returned to game system
        resolved_command = []

        # RESOLVE VERB: can be single verb word or "verb prep" combo

        # first word in the "verb" location of the list will always be the verb
        verb_words = input_verb.split()
        verb = verb_words[0]
        # if there's a second word, it's a preposition
        if len(verb_words) == 2:
            prep = verb_words[1]
        else:
            prep = None

        # check against all verbs game dictionary
        for i in range(len(self._game_verbs)):
            for verb_set in self._game_verbs[i]:
                key_list = list(self._game_verbs[i].keys())
                value_list = list(self._game_verbs[i].values())
                if verb in value_list[0]:
                    resolved_verb = key_list[0]

        # error checking if player uses an unrecognized verb
        # the game system will default to saying it doesn't understand input
        if resolved_verb == None:
            return ["error"]

        # the only preposition that should be returned to the game system with 
        # the verb is "at" for "look at", so checking for this special case
        # all/any other prepostions will just be ignored
        if prep != None:
            if resolved_verb == "look" and prep == "at":
                resolved_verb = "look at"
        
        # add verb/phrase to command to be returned
        resolved_command.append(resolved_verb)

        # RESOLVE DIRECT OBJECT: can be one or more words
        # TODO: refactor to remove repitition

        # check each word in direct object against game dictionary
        if input_direct != None:
            # direct_words = input_direct.split()
            # for i in range(len(direct_words)):
            for j in range(len(self._game_items)):
                for obj_set in self._game_items[j]:
                    key_list = list(self._game_items[j].keys())
                    value_list = list(self._game_items[j].values())
                    # if direct_words[i] in value_list[0]:
                    if input_direct in value_list[0]:
                        resoved_direct_obj.append(key_list[0])

            # concats list of resolved direct object words and returns string
            resolved_command.append(" ".join(resoved_direct_obj))

        # RESOLVE INDIRECT OBJECT: can be one or more words

        # if an indirect object, check against game dictionary
        if input_indirect != None:
            # indirect_words = input_indirect.split()
            # for i in range(len(indirect_words)):
            for j in range(len(self._game_items)):
                for obj_set in self._game_items[j]:
                    key_list = list(self._game_items[j].keys())
                    value_list = list(self._game_items[j].values())
                    # if indirect_words[i] in value_list[0]:
                    if input_indirect in value_list[0]:
                        resoved_indirect_obj.append(key_list[0])

            # concats list of resolved indirect object words and returns string
            resolved_command.append(" ".join(resoved_indirect_obj))

        # return list of resolved words
        return resolved_command
    
    def parse(self, inp: str):
        """this should take a phrase and return a list containing a command in
        spot 0, and an object/feature/person id in spot 1 and potentially 2"""

        # takes input from user and completes the lexical parsing stage to 
        # parse and clean input
        parsed_input = self.lexical_handler(inp)
        # takes parsed input and completes the classify stage to break input
        # into verb, direct object, and indirect object
        try:
            classified_input = self.classify_handler(parsed_input)
        except:
            return ["error"]
        # takes classified input and resolves it to game verbs, objects or 
        # features
        final_command = self.resolve(classified_input)
    
        # returns [verb, direct object id (opt), indirect object id(opt)]
        return final_command
    
