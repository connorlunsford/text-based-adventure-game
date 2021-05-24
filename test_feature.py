import unittest
import feature

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Old Desk"
        test_desc = "An old wood desk."
        test_sdesc = 'a wood desk'
        test_interaction = {"look at": "The old wood desk's top is faded. It has a small center drawer."}
        test_hidden = True
        self.test_feature = feature.Feature(test_id, test_name, test_desc, test_sdesc, test_interaction, test_hidden)

    def tearDown(self):
        del self.test_feature

    # testing methods associated with the hidden attribute
    def test_get_hidden(self):
        """get_hidden successfully returns the value of the hidden attribute"""
        self.assertTrue(self.test_feature.get_hidden())

    def test_set_hidden(self):
        """set_hidden successfully sets the value of the hidden attribute to the provided value"""
        self.test_feature.set_hidden(False)
        self.assertFalse(self.test_feature.get_hidden())

    def test_switch_hidden1(self):
        """switch_hidden successfully switches the value of the hidden attribute from True to False"""
        self.test_feature.switch_hidden()
        self.assertFalse(self.test_feature.get_hidden())

    def test_switch_hidden2(self):
        """switch_hidden successfully switches the value of the hidden attribute from False to True"""
        self.test_feature.switch_hidden()
        self.test_feature.switch_hidden()
        self.assertTrue(self.test_feature.get_hidden())

    # testing methods used for managing condition
    def test_add_condition1(self):
        """add_condition successfully adds the condition attribute with the correct value"""
        self.test_feature.add_condition(True)
        self.assertTrue(self.test_feature.get_condition())

    def test_add_condition2(self):
        """add_condition successfully raises an exception when condition attribute already exists"""
        self.test_feature.add_condition(False)
        with self.assertRaises(feature.AttributeAlreadyExists):
            self.test_feature.add_condition(True)

    def test_get_condition1(self):
        """get_condition successfully returns the value of the condition attribute"""
        self.test_feature.add_condition(False)
        self.assertFalse(self.test_feature.get_condition())     

    def test_get_condition2(self):
        """get_condition successfully raises an exception when condition attribute does not exist"""
        with self.assertRaises(feature.AttributeDoesNotExist):
            self.test_feature.get_condition()

    def test_set_condition1(self):
        """set_condition successfully sets the value of the condition attribute to the provided value"""
        self.test_feature.add_condition(True)
        self.test_feature.set_condition(False)
        self.assertFalse(self.test_feature.get_condition())

    def test_set_condition2(self):
        """set_condition successfully raises an exception when condition attribute does not exist"""
        with self.assertRaises(feature.AttributeDoesNotExist):
            self.test_feature.set_condition(True)

    def test_switch_condition1(self):
        """switch_condition successfully changes the value of condition to True"""
        self.test_feature.add_condition(False)
        self.test_feature.switch_condition()
        self.assertTrue(self.test_feature.get_condition())

    def test_switch_condition2(self):
        """switch_condition successfully changes the value of condition to False"""
        self.test_feature.add_condition(True)
        self.test_feature.switch_condition()
        self.assertFalse(self.test_feature.get_condition())

    def test_switch_condition3(self):
        """switch_condition successfully raises an exception when condition attribute does not exist"""
        with self.assertRaises(feature.AttributeDoesNotExist):
            self.test_feature.switch_condition()

    def test_remove_condition1(self):
        """remove_condition successfully removes the condition attribute"""
        self.test_feature.add_condition(True)
        self.test_feature.remove_condition()
        with self.assertRaises(feature.AttributeDoesNotExist):
            self.test_feature.get_condition()

    def test_remove_condition2(self):
        """remove_condition successfully raises an exception when condition attribute does not exist"""
        with self.assertRaises(feature.AttributeDoesNotExist):
            self.test_feature.remove_condition()

if __name__ == "__main__":
    unittest.main(verbosity=2)