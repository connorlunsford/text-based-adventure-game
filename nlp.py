class ParserException(Exception):
    """Base exception class for the Parser class"""
    pass

class ParserMissingFile(Exception):
    """Raised when a required text file has not been added to a Parser object"""
    pass

class Parser:

    def __init__(self):
        return

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

    def parse(self, inp: str):
        """this should take a phrase and return a list containing a command in
        spot 0, and an object/feature/person id in spot 1 and potentially 2"""

        """will this be calling all the other methods in order, using the 
        previous method's output as the input? Or how are we handling all
        the various steps?"""
    
        return [inp]

    def find_killer(self, killer):
        """this should take a phrase and return either the killers name or 'WRONG'"""
        return 'WRONG'

    def find_weapon(self, weapon):
        """this should take a phrase and return either 'CANDLESTICK' or 'WRONG'"""
        return 'WRONG'

    def tokenize(self, input: str):
        """Takes user input as a string, converts to lower case, removes all
        punctuation, and tokenizes to separate individual words. Credit for this
        method: https://stackoverflow.com/questions/9797357/dividing-a-string-at-various-punctuation-marks-using-split/33393581
        This will split hyphenated words, but I don't think that's an issue
        in this game."""
        lower_input = input.lower()
        words = "".join((char if char.isalpha() else " ") for char in lower_input).split()
        return words

    def remove_articles(self, words: list):
        """ takes a list of words and removes all articles"""
        words_no_articles = []
        articles = ["a", "an", "the"]
        for word in words:
            if word not in articles:
                words_no_articles.append(word)
        # return list of words not including articles or punctuation
        return words_no_articles

    def remove_stopwords(self, words: list):
        """takes a list of words and removes stopwords"""

        # hard-coded for development and testing, will use external file later

        """ NOTE: This currently removes 's' which is useful because that will
        be leftover after tokenizing contractions. However, if we decide to 
        accept 'n', 's', 'e', and 'w' for directions then this will need to be
        adjusted. That is not part of the requirements though, so I suggest
        we don't allow them. Otherwise, at the moment, I'm not sure how to deal
        with a leftover 's' vs 's' for 'south'."""

        """TODO: are we going to have a special case for 'it' in the classify
        stage? If so, it will also need to be removed from this list"""

        stopwords = ['a', 'again', 'ain', 'all', 'am', 'an', 'and', 'any',
         'are', 'aren', 'as', 'be', 'because', 'been', 'being', 'both', 'but',
         'can', 'couldn', 'd', 'did', 'didn', 'do', 'does', 'doesn', 'doing',
         'don', 'during', 'each', 'few', 'further', 'had', 'hadn', 'has',
         'hasn', 'have', 'haven', 'having', 'he', 'her', 'here', 'hers',
         'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'is', 'isn',
         'it', 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', 'more',
         'most', 'mustn', 'my', 'myself', 'needn', 'no', 'nor', 'not', 'now',
         'o', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'own',
         're', 's', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some',
         'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them',
         'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
         'too', 've', 'very', 'was', 'wasn', 'we', 'were', 'weren', 'what',
         'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will',
         'with', 'won', 'wouldn', 'y', 'you', 'your', 'yours', 'yourself',
         'yourselves']
        words_no_stopwords = []
        for word in words:
            if word not in stopwords:
                words_no_stopwords.append(word)
        # return list of words with no articles or stopwords
        return words_no_stopwords

    def verify_words(self, clean_input: str):
        """takes a list of cleaned words and verifies that they are recognized
        by the game"""

        """ TODO: this currently only returns recognized words and will ignore
        all others. Is this how we want to handle this? Or do we want to return
        some kind of message about not understanding what the user means?"""
        
        # sample dictionary for dev/testing. 
        """ TODO: need to compose full list of words we want the game to recognize"""
        
        game_dictionary = ["get", "take", "look", "earring", "pick", "up"]
        final_words = []
        for word in clean_input:
            if word in game_dictionary:
                final_words.append(word)
        return final_words

    # Classify Stage Methods

    def classify_input(self, input:list):
        
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
        if second_word in prepositions:
            verb = verb + " " + second_word
            direct_object = input[2:]
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
                #indirect_object= " ".join(direct_object[i + 1:])
                indirect_object = direct_object[i + 1:]
                # Get the left half of the array; this is the direct object
                #direct_object = " ".join(direct_object[:i])
                direct_object = direct_object[:i]
                break

        # Make sure that there are no additional prepositions in the input
        # as this would suggest an invalid sentence structure
        if "indirect_object" in locals():
            for i in range(len(indirect_object)):
                if indirect_object[i] in prepositions:
                    raise ParserException
        else:
            for i in range(len(direct_object)):
                if direct_object[i] in prepositions:
                    raise ParserException

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
            raise ParserException

        # Analyze the sentence structure and return the result
        return self.classify_input(input)