import unittest
import feature

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Old Desk"
        test_desc = "An old wood desk."
        test_interaction = {"look at": "The old wood desk's top is faded. It has a small center drawer."}
        test_hidden = False
        self.test_feature = feature.Feature(test_id, test_name, test_desc, test_interaction, test_hidden)

    def tearDown(self):
        del self.test_feature

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