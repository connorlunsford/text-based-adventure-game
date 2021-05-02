import unittest
import nlp 

class TestParserClass(unittest.TestCase):

    def setUp(self):
        self.test_parser = nlp.Parser()
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
        self.text3_resolved_command = ["take", "O02"]

        self.text4 = "Look at the large silver candlestick"
        self.text4_tokenized = ["look", "at", "the", "large", "silver", "candlestick"]
        self.text4_tok_no_article = ["look", "at", "large", "silver", "candlestick"]
        self.text4_tok_no_art_or_stop = ["look", "at", "large", "silver", "candlestick"]
        self.text4_final_words = ["look", "at", "large", "silver", "candlestick"]
        self.text4_classified_words = ["look at", "large silver candlestick"]
        self.text4_resolved_command = ["look at", "O01"]

        self.text5 = "Use the silver key on the lock"
        self.text5_tokenized = ["use", "the", "silver", "key", "on", "the", "lock"]
        self.text5_tok_no_article = ["use", "silver", "key", "on", "lock"]
        self.text5_tok_no_art_or_stop = ["use", "silver", "key", "on", "lock"]
        self.text5_final_words = ["use", "silver", "key", "on", "lock"]
        self.text5_classified_words = ["use", "silver key", "lock"]
        self.text5_resolved_command = ["use", "O03", "O04"]

        self.test_parser.load_articles("articles.txt")
        self.test_parser.load_stopwords("stopwords.txt")
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