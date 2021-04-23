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

    # testing methods for managing ID
    def test_get_id(self):
        test_id = "F1"
        self.assertEqual(self.test_interactable.get_id(), test_id)

    # testing methods for managing name
    def test_get_name(self):
        test_name = "Large Oak Table"
        self.assertEqual(self.test_interactable.get_name(), test_name)

    def test_set_name(self):
        test_new_name = "Oak Table"
        self.test_interactable.set_name(test_new_name)
        self.assertEqual(self.test_interactable.get_name(), test_new_name)

    # testing methods for managing descriptions
    def test_get_description(self):
        self.assertEqual(self.test_interactable.get_desc(), "A large oak table.")

    def test_set_description(self):
        self.test_interactable.set_desc("A small oak table.")
        self.assertEqual(self.test_interactable.get_desc(), "A small oak table.")

    # testing methods for managing interactions
    def test_get_interaction1(self):
        self.assertEqual(self.test_interactable.get_interaction("look at"),
        "Apart from its size, the large oak table is uninteresting.")

    def test_get_interaction2(self):
        self.assertEqual(self.test_interactable.get_interaction("sit"), None)

    def test_add_interaction1(self):
        self.test_interactable.add_interaction("sit", "You sit at the large oak table.")
        self.assertEqual(self.test_interactable.get_interaction("sit"),
        "You sit at the large oak table.")

    def test_add_interaction2(self):
        self.test_interactable.add_interaction("look at", 
        "A pile of newspapers lies on top of the large oak table.")
        self.assertEqual(self.test_interactable.get_interaction("look at"),
        "Apart from its size, the large oak table is uninteresting.")

    def test_set_interaction1(self):
        self.test_interactable.set_interaction("look at", 
        "A pile of newspapers lies on top of the large oak table.")
        self.assertEqual(self.test_interactable.get_interaction("look at"),
        "A pile of newspapers lies on top of the large oak table.")

    def test_set_interaction2(self):
        self.test_interactable.set_interaction("sit", "The table has no chairs. How odd.")
        self.assertEqual(self.test_interactable.get_interaction("sit"), None)

    def test_remove_interaction1(self):
        self.test_interactable.add_interaction("sit", "You sit at the large oak table.")
        self.test_interactable.remove_interaction("sit")
        self.assertEqual(self.test_interactable.get_interaction("sit"), None)

    def test_remove_interaction2(self):
        self.test_interactable.remove_interaction("look at")
        self.assertEqual(self.test_interactable.get_interaction("look at"), None)

    def test_get_interactions(self):
        self.assertEqual(self.test_interactable.get_interactions(), 
        {"look at": "Apart from its size, the large oak table is uninteresting."})

    def test_remove_interactions(self):
        self.test_interactable.remove_interactions()
        self.assertEqual(self.test_interactable.get_interactions(), {})

if __name__ == '__main__':
    unittest.main(verbosity=2)
