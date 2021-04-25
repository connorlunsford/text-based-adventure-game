import unittest
import interactable

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Large Oak Table"
        test_desc = "A large oak table."
        test_interaction = {"look at": "Apart from its size, the large oak table is uninteresting."}
        self.test_interactable = interactable.Interactable(test_id, test_name, test_desc, test_interaction)

    def tearDown(self):
        del self.test_interactable

    # testing methods used for managing ID
    def test_get_id(self):
        """get_id successfully returns the value of the id attribute"""
        self.assertEqual(self.test_interactable.get_id(), "F1")

    # testing methods used for managing name
    def test_get_name(self):
        """get_name successfully returns the value of the name attribute"""
        self.assertEqual(self.test_interactable.get_name(), "Large Oak Table")

    def test_set_name(self):
        """set_name successfully sets the value of the name attribute to the provided value"""
        self.test_interactable.set_name("Oak Table")
        self.assertEqual(self.test_interactable.get_name(), "Oak Table")

    # testing methods used for managing description
    def test_get_desc(self):
        """get_description successfully returns the value of the desc attribute"""
        self.assertEqual(self.test_interactable.get_desc(), "A large oak table.")

    def test_set_desc(self):
        """set_desc successfully sets the value of the desc attribute to the provided value"""
        self.test_interactable.set_desc("A small oak table.")
        self.assertEqual(self.test_interactable.get_desc(), "A small oak table.")

    # testing methods used for managing interactions
    def test_get_interaction1(self):
        """get_interaction successfully returns the value associated with the provided key 
        in the interactions dictionary"""
        self.assertEqual(self.test_interactable.get_interaction("look at"),
        "Apart from its size, the large oak table is uninteresting.")

    def test_get_interaction2(self):
        """get_interaction successfully raises an exception when the provided key does
        not exist in the interactions dictionary"""
        with self.assertRaises(interactable.KeyDoesNotExist):
            self.test_interactable.get_interaction("sit")

    def test_add_interaction1(self):
        """add_interaction successfully adds a key-value pair to the interactions dictionary"""
        self.test_interactable.add_interaction("sit", "You sit at the large oak table.")
        self.assertEqual(self.test_interactable.get_interaction("sit"),
        "You sit at the large oak table.")

    def test_add_interaction2(self):
        """add_interaction successfully riases an exception when the provided key already 
        exists in the interactions dictionary"""
        with self.assertRaises(interactable.KeyAlreadyExists):
            self.test_interactable.add_interaction("look at", 
            "A pile of newspapers lies on top of the large oak table.")

    def test_set_interaction1(self):
        """set_interaction successfully sets the value associated with the provided key
        in the interactions dictionary to the provided value"""
        self.test_interactable.set_interaction("look at", 
        "A pile of newspapers lies on top of the large oak table.")
        self.assertEqual(self.test_interactable.get_interaction("look at"),
        "A pile of newspapers lies on top of the large oak table.")

    def test_set_interaction2(self):
        """set_interaction successfully raises an exception when the provided key
        does not exist in the interactions dictionary"""
        with self.assertRaises(interactable.KeyDoesNotExist):
            self.test_interactable.set_interaction("sit", "The table has no chairs. How odd.")

    def test_remove_interaction1(self):
        """remove_interaction successfully removes the key-value pair associated with 
        provided key from the interactions dictionary"""
        self.test_interactable.add_interaction("sit", "You sit at the large oak table.")
        self.test_interactable.remove_interaction("sit")
        self.assertEqual(self.test_interactable.get_interactions(), 
        {"look at": "Apart from its size, the large oak table is uninteresting."})

    def test_remove_interaction2(self):
        """remove_interaction successfully removes the key-value pair associated with the
        provided key from the interactions dictionary, resulting in an empty dictionary"""
        self.test_interactable.remove_interaction("look at")
        self.assertEqual(self.test_interactable.get_interactions(), {})

    def test_remove_interaction3(self):
        """remove_interaction successfully raises an exception when the provided key 
        does not exist in the interactions dictionary"""
        with self.assertRaises(interactable.KeyDoesNotExist):
            self.test_interactable.remove_interaction("sit")

    def test_get_interactions(self):
        """get_interactions successfully returns the entire interactions dictionary"""
        self.assertEqual(self.test_interactable.get_interactions(), 
        {"look at": "Apart from its size, the large oak table is uninteresting."})

    def test_remove_interactions(self):
        """remove_interactions sucessfully removes all key-value pairs in the
        interactions dictionary, resulting in an empty dictionary"""
        self.test_interactable.remove_interactions()
        self.assertEqual(self.test_interactable.get_interactions(), {})

if __name__ == "__main__":
    unittest.main(verbosity=2)
