import unittest
import room

class TestCase(unittest.TestCase):

    def setUp(self):
        test_id = "R01"
        test_name = "Grand Foyer"
        test_desc = "A large room with marble floors and a grand staircase lies before you. \
            Afternoon light pours in from the front windows, exposing dust particles in the air."
        test_sdesc = "A large room with marble floors and a grand staircase."
        test_visited = False
        self.test_room = room.Room(test_id, test_name, test_desc, test_sdesc, test_visited)
    
    def tearDown(self):
        del self.test_room

    # testing methods used for managing ID
    def test_get_id(self):
        """get_id successfully returns the value of the id attribute"""
        self.assertEqual(self.test_room.get_id(), "R01")

    # testing methods used for managing name
    def test_get_name(self):
        """get_name successfully returns the value of the name attribute"""
        self.assertEqual(self.test_room.get_name(), "Grand Foyer")

    def test_set_name(self):
        """set_name successfully sets the value of the name attribute to the provided value"""
        self.test_room.set_name("Lobby")
        self.assertEqual(self.test_room.get_name(), "Lobby")

    # testing methods used for managing description
    def test_get_desc(self):
        """get_desc successfully returns the value of the desc attribute"""
        self.assertEqual(self.test_room.get_desc(), "A large room with marble floors and a grand staircase lies before you. \
            Afternoon light pours in from the front windows, exposing dust particles in the air.")

    def test_set_desc(self):
        """set_desc successfully sets the value of the desc attribute to the provided value"""
        self.test_room.set_desc("What once use to be a large foyer lies before you. In the darkness, \
            you can make out an old wooden staircase.")
        self.assertEqual(self.test_room.get_desc(), "What once use to be a large foyer lies before you. In the darkness, \
            you can make out an old wooden staircase.")

    # testing methods used for managing short description
    def test_get_sdesc(self):
        """get_sdesc successfully returns the value of the sdesc attribute"""
        self.assertEqual(self.test_room.get_sdesc(), "A large room with marble floors and a grand staircase.")

    def test_set_sdesc(self):
        """set_sdesc successfully sets the value of the sdesc attribute to the provided value"""
        self.test_room.set_sdesc("An old, abandoned foyer.")
        self.assertEqual(self.test_room.get_sdesc(), "An old, abandoned foyer.")

    # testing methods used for managing the correct description
    def test_get_description1(self):
        """get_description successfully returns the long description when visited is False"""
        self.assertEqual(self.test_room.get_description(), "A large room with marble floors and a grand staircase lies before you. \
            Afternoon light pours in from the front windows, exposing dust particles in the air.")        

    def test_get_description2(self):
        """get_description successfully sets the value of visited to True if it has not been visited before"""
        self.test_room.get_description()
        self.assertTrue(self.test_room.get_visited())

    def test_get_description3(self):
        """get_description successfully returns the short description when visited is True"""
        self.test_room.set_visited(True)
        self.assertEqual(self.test_room.get_description(), "A large room with marble floors and a grand staircase.")           

    # testing methods used for managing visited
    def test_get_visited(self):
        """get_visited successfully returns the value of the visited attribute"""
        self.assertFalse(self.test_room.get_visited())

    def test_set_visited(self):
        """set_visited successfully sets the value of the visited attribute to the provided value"""
        self.test_room.set_visited(True)
        self.assertTrue(self.test_room.get_visited())

    # testing methods used for managing objects
    def test_add_object1(self):
        """add_object successfully adds an object ID to the objects list"""
        self.test_room.add_object("O01")
        self.assertEqual(self.test_room.get_objects(), ["O01"])

    def test_add_object2(self):
        """add_object successfully raises an exception when the provided 
        object ID already exists in the objects list"""
        self.test_room.add_object("O01")
        with self.assertRaises(room.IDAlreadyExists):
            self.test_room.add_object("O01")

    def test_remove_object(self):
        """remove_object successfully removes an object from the objects list"""
        self.test_room.add_object("O01")
        self.test_room.add_object("O02")
        self.test_room.remove_object("O01")
        self.assertEqual(self.test_room.get_objects(), ["O02"])
    
    def test_get_objects1(self):
        """get_objects successfully returns the entire objects list with the 
        correct contents when empty"""
        self.assertEqual(self.test_room.get_objects(), [])

    def test_get_objects2(self):
        """get_objects successfully returns the entire objects list with the
        correct contents when not empty"""
        self.test_room.add_object("O01")
        self.test_room.add_object("O02")
        self.assertEqual(self.test_room.get_objects(), ["O01", "O02"])

    def test_set_objects1(self):
        """set_objects successfully sets the value of the objects list to the
        provided list when the previous list had object IDs added to it"""
        self.test_room.add_object("O01")
        self.test_room.add_object("O02")
        self.test_room.set_objects(["O01", "O02", "O03"])
        self.assertEqual(self.test_room.get_objects(), ["O01", "O02", "O03"])

    def test_set_objects2(self):
        """set_objects successfully sets the value of the objects list to the
        provided list when the previous list is empty/had no IDs added to it"""
        self.test_room.set_objects(["O01", "O02", "O03"])
        self.assertEqual(self.test_room.get_objects(), ["O01", "O02", "O03"])

if __name__ == "__main__":
    unittest.main(verbosity=2)