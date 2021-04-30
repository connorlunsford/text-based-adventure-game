class Parser:

    def __init__(self):
        return

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