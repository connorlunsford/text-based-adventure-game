import unittest
import object

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Pearl Earring"
        test_desc = "A small pearl earring."
        test_interaction = {"look at": "The small pearl earring is covered in dust."}
        test_hidden = True
        self.test_object = object.Object(test_id, test_name, test_desc, test_interaction, test_hidden)

    def tearDown(self):
        del self.test_object

    # testing methods for managing hidden
    def test_get_hidden(self):
        self.assertEqual(self.test_object.get_hidden(), True)

    def test_set_hidden(self):
        self.test_object.set_hidden(False)
        self.assertEqual(self.test_object.get_hidden(), False)

    def test_switch_hidden1(self):
        self.test_object.switch_hidden()
        self.assertEqual(self.test_object.get_hidden(), False)

    def test_switch_hidden2(self):
        self.test_object.switch_hidden()
        self.test_object.switch_hidden()
        self.assertEqual(self.test_object.get_hidden(), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
