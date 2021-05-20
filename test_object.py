import unittest
import object

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Pearl Earring"
        test_desc = "A small pearl earring."
        test_sdesc = 'a round earring'
        test_interaction = {"look at": "The small pearl earring is covered in dust."}
        test_hidden = True
        self.test_object = object.Object(test_id, test_name, test_desc, test_sdesc, test_interaction, test_hidden)

    def tearDown(self):
        del self.test_object

    # testing methods associated with the hidden attribute
    def test_get_hidden(self):
        """get_hidden successfully returns the value of the hidden attribute"""
        self.assertTrue(self.test_object.get_hidden())

    def test_set_hidden(self):
        """set_hidden successfully sets the value of the hidden attribute to the provided value"""
        self.test_object.set_hidden(False)
        self.assertFalse(self.test_object.get_hidden())

    def test_switch_hidden1(self):
        """switch_hidden successfully switches the value of the hidden attribute from True to False"""
        self.test_object.switch_hidden()
        self.assertFalse(self.test_object.get_hidden())

    def test_switch_hidden2(self):
        """switch_hidden successfully switches the value of the hidden attribute from False to True"""
        self.test_object.switch_hidden()
        self.test_object.switch_hidden()
        self.assertTrue(self.test_object.get_hidden())

if __name__ == "__main__":
    unittest.main(verbosity=2)
