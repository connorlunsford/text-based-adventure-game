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

    def test_tokenize(self):
        self.assertEqual(self.test_parser.tokenize(self.text1), self.text1_tokenized)

    def test_tokenize2(self):
        self.assertEqual(self.test_parser.tokenize(self.text2), self.text2_tokenized)

    def test_remove_articles(self):
        self.assertEqual(self.test_parser.remove_articles(self.text2_tokenized),
         self.text2_tok_no_article)

    def test_remove_stopwords(self):
        self.assertEqual(self.test_parser.remove_stopwords(self.text2_tok_no_article),
         self.text2_tok_no_art_or_stop)

    def test_verify_words(self):
        self.assertEqual(self.test_parser.verify_words(self.text2_tok_no_art_or_stop),
         self.text2_final_words)