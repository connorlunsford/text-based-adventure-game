import unittest
import person
 
class TestPersonClass(unittest.TestCase):

    def setUp(self):
        id = "01"
        name = "Ralph"
        desc = "Ralph has been the groundskeeper for many years."
        sdesc = 'a man'
        interactions = {"look at": """The groundskeeper is acting nervous
            and seems to have misplaced something."""} 
        self.test_person = person.Person(id, name, desc, sdesc, interactions)

    def test_get_id(self):
        expected = "01"
        self.assertEqual(self.test_person.get_id(), expected)

    def test_get_name(self):
        expected = "Ralph"
        self.assertEqual(self.test_person.get_name(), expected)

    def test_set_name(self):
        new_name = "Bob"
        self.test_person.set_name(new_name)
        self.assertEqual(self.test_person.get_name(), new_name)

    def test_get_desc(self):
        """by default also test set_desc"""
        new_desc = """Ralph has been the groundskeeper for 
            many years. He loves his job but feels underappreciated by
            his boss."""
        self.test_person.set_desc(new_desc)
        self.assertEqual(self.test_person.get_desc(), new_desc)        

    """I realize now that Person doesn't currently have anything above and
    beyond the Interactable class attributes and there is already unit tests
    for all of those methods in test_interactable. I'm not sure that a
    separate Person test suite is even necessary at this point in time."""