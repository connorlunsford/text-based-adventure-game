class Parser:

    def __init__(self):
        return

    def parse(self, inp: str):
        """this should take a phrase and return a list containing a command in
        spot 0, and an object/feature/person id in spot 1 and potentially 2"""
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
        This will split hyphenated words though."""
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
        stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
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
        
        game_dictionary = ["get", "take", "look", "earring", "pick"]
        final_words = []
        for word in clean_input:
            if word in game_dictionary:
                final_words.append(word)
        return final_words     