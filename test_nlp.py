import unittest
import nlp 

class TestParserClass(unittest.TestCase):

    def setUp(self):

        self.test_parser = nlp.Parser()
        self.test_parser.add_connections("./resources/connections.txt")
        self.test_parser.add_special_commands("./resources/special_commands.txt")
        self.test_parser.add_prepositions("./resources/prepositions.txt")

        self.text1 = "This is it, my sample sentence. Oh wait, here's another..."
        self.text1_tokenized = [
            "this", "is", "it", "my", "sample", "sentence", "oh", "wait", "here",
             "s", "another"]
        self.text2 = "Pick up the earring"
        self.text2_tokenized = ["pick", "up", "the", "earring"]
        self.text2_tok_no_article = ["pick", "up", "earring"]
        self.text2_tok_no_art_or_stop = ["pick", "up", "earring"]
        self.text2_final_words = ["pick", "up", "earring"]

        self.text3 = "Take the letter"
        self.text3_tokenized = ["take", "the", "letter"]
        self.text3_tok_no_article = ["take", "letter"]
        self.text3_tok_no_art_or_stop = ["take", "letter"]
        self.text3_final_words = ["take", "letter"]
        self.text3_classified_words = ["take", "letter"]
        self.text3_resolved_command = ["take", "O09"]

        self.text4 = "Look at the candle stick"
        self.text4_tokenized = ["look", "at", "the", "candle", "stick"]
        self.text4_tok_no_article = ["look", "at", "candle", "stick"]
        self.text4_tok_no_art_or_stop = ["look", "at", "candle", "stick"]
        self.text4_final_words = ["look", "at", "candle", "stick"]
        self.text4_classified_words = ["look at", "candle stick"]
        self.text4_resolved_command = ["look at", "O01"]

        self.text5 = "Use the silver key on the lock"
        self.text5_tokenized = ["use", "the", "small", "key", "on", "the", "lock"]
        self.text5_tok_no_article = ["use", "small", "key", "on", "lock"]
        self.text5_tok_no_art_or_stop = ["use", "small", "key", "on", "lock"]
        self.text5_final_words = ["use", "small", "key", "on", "lock"]
        self.text5_classified_words = ["use", "small key", "lock"]
        # TODO: update object/id for lock once all features added to dictionary
        self.text5_resolved_command = ["use", "O02", "O04"]

        self.test_parser.load_game_verbs("./resources/game_verbs.json")
        self.test_parser.load_game_items("./resources/game_items.json")
        self.test_parser.load_articles("./resources/articles.txt")
        self.test_parser.load_stopwords("./resources/stopwords.txt")
        self.test_parser.load_killer("./resources/killer.txt")
        self.test_parser.load_weapon("./resources/weapon.txt")
        # self.test_parser.load_dictionary("game_dictionary.json")

    # test for phrase 1
    def test_tokenize(self):
        self.assertEqual(self.test_parser.tokenize(self.text1), self.text1_tokenized)

    # tests for phrase 2
    def test_tokenize2(self):
        self.assertEqual(self.test_parser.tokenize(self.text2), self.text2_tokenized)

    def test_remove_articles2(self):
        self.assertEqual(self.test_parser.remove_articles(self.text2_tokenized),
         self.text2_tok_no_article)

    def test_remove_stopwords2(self):
        self.assertEqual(self.test_parser.remove_stopwords(self.text2_tok_no_article),
         self.text2_tok_no_art_or_stop)

    def test_verify_words2(self):
        self.assertEqual(self.test_parser.verify_words(self.text2_tok_no_art_or_stop),
         self.text2_final_words)

    # tests for phrase 3
    def test_tokenize3(self):
        self.assertEqual(self.test_parser.tokenize(self.text3), self.text3_tokenized)

    def test_remove_articles3(self):
        self.assertEqual(self.test_parser.remove_articles(self.text3_tokenized),
         self.text3_tok_no_article)

    def test_remove_stopwords3(self):
        self.assertEqual(self.test_parser.remove_stopwords(self.text3_tok_no_article),
         self.text3_tok_no_art_or_stop)

    def test_verify_words3(self):
        self.assertEqual(self.test_parser.verify_words(self.text3_tok_no_art_or_stop),
         self.text3_final_words)

    def test_check_verb3(self):
        self.assertEqual(self.test_parser.resolve(self.text3_classified_words),
         self.text3_resolved_command)         

    # tests for phrase 4
    def test_tokenize4(self):
        self.assertEqual(self.test_parser.tokenize(self.text4), self.text4_tokenized)

    def test_remove_articles4(self):
        self.assertEqual(self.test_parser.remove_articles(self.text4_tokenized),
         self.text4_tok_no_article)

    def test_remove_stopwords4(self):
        self.assertEqual(self.test_parser.remove_stopwords(self.text4_tok_no_article),
         self.text4_tok_no_art_or_stop)

    def test_verify_words4(self):
        self.assertEqual(self.test_parser.verify_words(self.text4_tok_no_art_or_stop),
         self.text4_final_words)

    def test_check_verb4(self):
        self.assertEqual(self.test_parser.resolve(self.text4_classified_words),
         self.text4_resolved_command)          

    # tests for phrase 5
    def test_tokenize5(self):
        self.assertEqual(self.test_parser.tokenize(self.text5), self.text5_tokenized)

    def test_remove_articles5(self):
        self.assertEqual(self.test_parser.remove_articles(self.text5_tokenized),
         self.text5_tok_no_article)

    def test_remove_stopwords5(self):
        self.assertEqual(self.test_parser.remove_stopwords(self.text5_tok_no_article),
         self.text5_tok_no_art_or_stop)

    def test_verify_words5(self):
        self.assertEqual(self.test_parser.verify_words(self.text5_tok_no_art_or_stop),
         self.text5_final_words)

    def test_check_verb5(self):
        self.assertEqual(self.test_parser.resolve(self.text5_classified_words),
         self.text5_resolved_command)          
    
    # test full parse() functionality
    def test_parse_text5(self):
        self.assertEqual(self.test_parser.parse(self.text5), self.text5_resolved_command)

    def test_load_killer(self):
        self.assertEqual(self.test_parser._killer, "Ava Scarlett")

    def test_load_weapon(self):
        self.assertEqual(self.test_parser._weapon, "candlestick")

    ############################################################################
    # Classify Stage - Tests
    ############################################################################

    ############################################################################
    # Function: classify_input
    # Valid Cases: verb + noun, verb + adjective + noun, verb + adjectives + noun,
    # verb + noun + preposition + noun, verb + adj + noun + preposition + adj + noun,
    # verb + preposition + noun
    # Invalid Cases: verb + noun + preposition + noun + preposition + noun,
    # verb + preposition + noun + preposition + noun + preposition + noun
    ############################################################################

    def test_classify_input1(self):
        """classify_input correctly processes the case: verb + noun"""
        input = ["use", "key"]
        self.assertEqual(self.test_parser.classify_input(input), ["use", "key"])

    def test_classify_input2(self):
        """classify_input correctly processes the case: verb + adjective + noun"""
        input = ["use", "rusty", "key"]
        self.assertEqual(self.test_parser.classify_input(input), ["use", "rusty key"])

    def test_classify_input3(self):
        """classify_input correctly processes the case: verb + adjectives + noun"""
        input = ["use", "old", "rusty", "key"]
        self.assertEqual(self.test_parser.classify_input(input), ["use", "old rusty key"])

    def test_classify_input4(self):
        """classify_input correctly processes the case: verb + noun + preposition + noun"""
        input = ["use", "key", "on", "lock"]
        self.assertEqual(self.test_parser.classify_input(input), ["use", "key", "lock"])
    
    def test_classify_input5(self):
        """classify_input correctly processes the case: verb + adjective + noun + 
        preposition + adjective + noun"""
        input = ["use", "rusty", "key", "on", "brass", "lock"]
        self.assertEqual(self.test_parser.classify_input(input), ["use", "rusty key", "brass lock"])

    def test_classify_input6(self):
        """classify_input correctly processes the case: verb + preposition + noun"""
        input = ["look", "at", "painting"]
        self.assertEqual(self.test_parser.classify_input(input), ["look at", "painting"])

    def test_classify_input7(self):
        """classify_input correctly processes the case: verb + preposition + noun + preposition + noun"""
        input = ["look", "at", "painting", "on", "wall"]
        self.assertEqual(self.test_parser.classify_input(input), ["look at", "painting"])

    def test_classify_input8(self):
        """classify_input correctly processes the case: verb + noun + preposition + noun + preposition + noun"""
        input = ["use", "key", "on", "lock", "for", "fun"]
        with self.assertRaises(nlp.InvalidSentenceStructure):
            self.test_parser.classify_input(input)

    def test_classify_input9(self):
        """classify_input correctly processes the case: verb + preposition + noun + preposition + noun + preposition + noun"""
        input = ["look", "at", "painting", "on", "wall", "at", "noon"]
        with self.assertRaises(nlp.InvalidSentenceStructure):
            self.test_parser.classify_input(input)

    ############################################################################
    # Function: classify_handler
    ############################################################################

    def test_classify_handler1(self):
        input = ["look", "at", "mirror"]
        self.assertEqual(self.test_parser.classify_handler(input), ["look at", "mirror"])

    def test_classify_handler2(self):
        input = ["search", "through", "drawer"]
        self.assertEqual(self.test_parser.classify_handler(input), ["search through", "drawer"])   

    def test_classify_handler3(self):
        input = ["help"]
        self.assertEqual(self.test_parser.classify_handler(input), ["help"]) 

    def test_classify_handler4(self):
        input = ["south"]
        self.assertEqual(self.test_parser.classify_handler(input), ["go", "south"])

    def test_classify_handler5(self):
        input = ["south", "east"]
        self.assertEqual(self.test_parser.classify_handler(input), ["go", "south east"]) 

if __name__ == "__main__":
    unittest.main(verbosity=2)