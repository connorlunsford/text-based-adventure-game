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
        self.test_room = room.Room(test_id, test_name, test_desc, test_sdesc)
    
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

    def test_remove_object1(self):
        """remove_object successfully removes an object ID from the objects list"""
        self.test_room.add_object("O01")
        self.test_room.add_object("O02")
        self.test_room.remove_object("O01")
        self.assertEqual(self.test_room.get_objects(), ["O02"])

    def test_remove_object2(self):
        """remove_object successfully raises an exception when the provided
        object ID does not exist in the objects list"""
        with self.assertRaises(room.IDDoesNotExist):
            self.test_room.remove_object("O01")
    
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
        provided list when the previous list had no IDs added to it"""
        self.test_room.set_objects(["O01", "O02", "O03"])
        self.assertEqual(self.test_room.get_objects(), ["O01", "O02", "O03"])

    # testing methods for managing features
    def test_add_feature1(self):
        """add_feature successfully adds a feature ID to the features list"""
        self.test_room.add_feature("F01")
        self.assertEqual(self.test_room.get_features(), ["F01"])

    def test_add_feature2(self):
        """add_feature successfully raises an exception when the provided 
        feature ID already exists in the feature list"""
        self.test_room.add_feature("F01")
        with self.assertRaises(room.IDAlreadyExists):
            self.test_room.add_feature("F01")

    def test_remove_feature1(self):
        """remove_feature successfully removes a feature ID from the 
        features list"""
        self.test_room.add_feature("F01")
        self.test_room.add_feature("F02")
        self.test_room.remove_feature("F01")
        self.assertEqual(self.test_room.get_features(), ["F02"])

    def test_remove_feature2(self):
        """remove_feature successfully raises an exception when the provided
        feature ID does not exist in the features list"""
        with self.assertRaises(room.IDDoesNotExist):
            self.test_room.remove_feature("F01")
    
    def test_get_features1(self):
        """get_features successfully returns the entire features list with the 
        correct contents when empty"""
        self.assertEqual(self.test_room.get_features(), [])

    def test_get_features2(self):
        """get_features successfully returns the entire features list with the
        correct contents when not empty"""
        self.test_room.add_feature("F01")
        self.test_room.add_feature("F02")
        self.assertEqual(self.test_room.get_features(), ["F01", "F02"])

    def test_set_features1(self):
        """set_features successfully sets the value of the features list to the
        provided list when the previous list had IDs added to it"""
        self.test_room.add_feature("F01")
        self.test_room.add_feature("F02")
        self.test_room.set_features(["F01", "F02", "F03"])
        self.assertEqual(self.test_room.get_features(), ["F01", "F02", "F03"])

    def test_set_features2(self):
        """set_features successfully sets the value of the features list to the
        provided list when the previous list had no IDs added to it"""
        self.test_room.set_features(["F01", "F02", "F03"])
        self.assertEqual(self.test_room.get_features(), ["F01", "F02", "F03"])

    # testing methods for managing persons
    def test_add_person1(self):
        """add_person successfully adds a person ID to the persons list"""
        self.test_room.add_person("P01")
        self.assertEqual(self.test_room.get_people(), ["P01"])

    def test_add_person2(self):
        """add_person successfully raises an exception when the provided 
        person ID already exists in the persons list"""
        self.test_room.add_person("P01")
        with self.assertRaises(room.IDAlreadyExists):
            self.test_room.add_person("P01")

    def test_remove_person1(self):
        """remove_person successfully removes a person ID from the 
        persons list"""
        self.test_room.add_person("P01")
        self.test_room.add_person("P02")
        self.test_room.remove_person("P01")
        self.assertEqual(self.test_room.get_people(), ["P02"])

    def test_remove_person2(self):
        """remove_person successfully raises an exception when the provided
        person ID does not exist in the persons list"""
        with self.assertRaises(room.IDDoesNotExist):
            self.test_room.remove_person("P01")
    
    def test_get_people1(self):
        """get_people successfully returns the entire persons list with the 
        correct contents when empty"""
        self.assertEqual(self.test_room.get_people(), [])

    def test_get_people2(self):
        """get_people successfully returns the entire persons list with the
        correct contents when not empty"""
        self.test_room.add_person("P01")
        self.test_room.add_person("P02")
        self.assertEqual(self.test_room.get_people(), ["P01", "P02"])

    def test_set_people1(self):
        """set_people successfully sets the value of the persons list to the
        provided list when the previous list had IDs added to it"""
        self.test_room.add_person("P01")
        self.test_room.add_person("P02")
        self.test_room.set_people(["P01", "P02", "P03"])
        self.assertEqual(self.test_room.get_people(), ["P01", "P02", "P03"])

    def test_set_people2(self):
        """set_people successfully sets the value of the persons list to the
        provided list when the previous list had no IDs added to it"""
        self.test_room.set_people(["P01", "P02", "P03"])
        self.assertEqual(self.test_room.get_people(), ["P01", "P02", "P03"])

    # testing methods for managing connections
    def test_add_connection1(self):
        """add_connection successfully adds a room ID to the connections list"""
        self.test_room.add_connection("north","R01")
        self.assertEqual(self.test_room.get_connections(), {'north':"R01"})

    #
    # this test is depreciated since connections is a dict now
    #
    # def test_add_connection2(self):
    #     """add_connection successfully raises an exception when the provided
    #     room ID already exists in the connections list"""
    #     self.test_room.add_connection("north","R01")
    #     with self.assertRaises(room.IDAlreadyExists):
    #         self.test_room.add_connection("north","R01")

    # def test_remove_connection1(self):
    #     """remove_connection successfully removes a room ID from the
    #     connections list"""
    #     self.test_room.add_connection("north","R01")
    #     self.test_room.add_connection("west","R02")
    #     self.test_room.remove_connection("R01")
    #     self.assertEqual(self.test_room.get_connections(), {'west':"R02"})

    def test_remove_connection2(self):
        """remove_connection successfully raises an exception when the provided
        room ID does not exist in the connections list"""
        with self.assertRaises(room.IDDoesNotExist):
            self.test_room.remove_connection("R01")
    
    def test_get_connections1(self):
        """get_connections successfully returns the entire connections list
        with the correct contents when empty"""
        self.assertEqual(self.test_room.get_connections(), {})

    def test_get_connections2(self):
        """get_connections successfully returns the entire connections list
        with the correct contents when not empty"""
        self.test_room.add_connection("north","R01")
        self.test_room.add_connection("west","R02")
        self.assertEqual(self.test_room.get_connections(), {'north':"R01",'west': "R02"})

    def test_set_connections1(self):
        """set_connections successfully sets the value of the connections list
        to the provided list when the previous list had IDs added to it"""
        self.test_room.add_connection("north","R01")
        self.test_room.add_connection("west","R02")
        self.test_room.set_connections({'north':"R01",'west': "R02", 'east': "R03"})
        self.assertEqual(self.test_room.get_connections(), {'north':"R01",'west': "R02", 'east': "R03"})

    def test_set_connections2(self):
        """set_connections successfully sets the value of the connections list
        to the provided list when the previous list had no IDs added to it"""
        self.test_room.set_connections({'north':"R01",'west': "R02", 'east': "R03"})
        self.assertEqual(self.test_room.get_connections(), {'north':"R01",'west': "R02", 'east': "R03"})

    # testing methods for managing connections
    def test_add_interaction1(self):
        """add_interaction successfully adds a key-value pair to the interactions dict"""
        self.test_room.add_interaction("key1", "value1")
        self.assertEqual(self.test_room.get_interactions(), {"key1": "value1"})

    def test_add_interaction2(self):
        """add_interaction successfully raises an exception when the provided 
        key already exists in the interactions dict"""
        self.test_room.add_interaction("key1", "value1")
        with self.assertRaises(room.KeyAlreadyExists):
            self.test_room.add_interaction("key1", "value1")

    def test_remove_interaction1(self):
        """remove_interaction successfully removes a key-value pair from the 
        interactions dict"""
        self.test_room.add_interaction("key1", "value1")
        self.test_room.add_interaction("key2", "value2")
        self.test_room.remove_interaction("key1")
        self.assertEqual(self.test_room.get_interactions(), {"key2": "value2"})

    def test_remove_interaction2(self):
        """remove_interaction successfully raises an exception when the provided
        key does not exist in the connections list"""
        with self.assertRaises(room.KeyDoesNotExist):
            self.test_room.remove_interaction("key1")

    def test_get_interaction1(self):
        """get_interaction successfully returns an interaction that contains
        no nesting"""
        self.test_room.add_interaction("key1", "value1")
        self.assertEqual(self.test_room.get_interaction("key1"), "value1")

    def test_get_interaction2(self):
        """get_interaction successfully raises an exception when the provided
        key does not exist in the interactions dict (no nesting)"""
        self.test_room.add_interaction("key1", "value1")
        with self.assertRaises(room.KeyDoesNotExist):
            self.test_room.get_interaction("key2")

    def test_get_interaction3(self):
        """get_interaction successfully returns an interaction that contains
        single-level nesting"""
        self.test_room.add_interaction("key1", {"sub1": "subvalue1"})
        self.assertEqual(self.test_room.get_interaction("key1", "sub1"), "subvalue1")

    def test_get_interaction4(self):
        """get_interaction successfully raises an exception when the provided
        key does not exist in the interactions dict (single-level nesting)"""
        self.test_room.add_interaction("key1", {"sub1": "subvalue1"})
        with self.assertRaises(room.KeyDoesNotExist):
            self.test_room.get_interaction("key1", "sub2")

    def test_get_interaction5(self):
        """get_interaction successfully returns an interaction that contains
        double-level nesting"""
        self.test_room.add_interaction("key1", {"sub1": {"subsub1": "subsubvalue1"}})
        self.assertEqual(self.test_room.get_interaction("key1", "sub1", "subsub1"), "subsubvalue1")

    def test_get_interaction6(self):
        """get_interaction successfully raises an exception when the provided
        key does not exist in the interactions dict (double-level nesting)"""
        self.test_room.add_interaction("key1", {"sub1": {"subsub1": "subsubvalue1"}})
        with self.assertRaises(room.KeyDoesNotExist):
            self.test_room.get_interaction("key1", "sub1", "subsub2")

    def test_set_interactions1(self):
        """set_interactions successfully sets the value of the interactions dict
        to the provided dict when the previous dict had IDs added to it"""
        self.test_room.add_interaction("key1", "value1")
        self.test_room.add_interaction("key2", "value2")
        self.test_room.set_interactions({"key1": "value1", "key2": "value2"})
        self.assertEqual(self.test_room.get_interactions(), {"key1": "value1", "key2": "value2"})

    def test_set_interactions2(self):
        """set_connections successfully sets the value of the interactions dict
        to the provided dict when the previous dict had no IDs added to it"""
        self.test_room.set_interactions({"key1": "value1", "key2": "value2"})
        self.assertEqual(self.test_room.get_interactions(), {"key1": "value1", "key2": "value2"})

    def test_get_interactions1(self):
        """get_interactions successfully returns the entire interactions dict
        with the correct contents when empty"""
        self.assertEqual(self.test_room.get_interactions(), {})

    def test_get_interactions2(self):
        """get_connections successfully returns the entire interactions dict
        with the correct contents when not empty"""
        self.test_room.add_interaction("key1", "value1")
        self.test_room.add_interaction("key2", "value2")
        self.assertEqual(self.test_room.get_interactions(), {"key1": "value1", "key2": "value2"})

if __name__ == "__main__":
    unittest.main(verbosity=2)