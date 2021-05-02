import unittest
import player
import object
 
class TestPlayerClass(unittest.TestCase):

    def setUp(self):
        test_id = "F1"
        test_name = "Pearl Earring"
        test_desc = "A small pearl earring."
        test_interaction = {
            "look at": "The small pearl earring is covered in dust."}
        test_hidden = True
        self.test_object_1 = object.Object(test_id, test_name, test_desc, test_interaction, test_hidden)

        test_id = "F2"
        test_name = "paper"
        test_desc = "A piece of paper with a picture."
        test_interaction = {
            "look at": "It looks like a page torn from a book."}
        test_hidden = True
        self.test_object_2 = object.Object(test_id, test_name, test_desc, test_interaction, test_hidden)

        test_id = "F3"
        test_name = "candlestick"
        test_desc = "A silver candlestick."
        test_interaction = {
            "look at": "It looks like it might have blood on it."}
        test_hidden = True
        self.test_object_3 = object.Object(test_id, test_name, test_desc, test_interaction, test_hidden)

        self.test_player = player.Player("01")
        self.test_player.set_name("Jennifer")
        self.test_player.set_inventory([self.test_object_1, self.test_object_2])

    def test_init_get_id(self):
        expected = "01"
        self.assertEqual(self.test_player.get_id(), expected)
 
    def test_set_id(self):
        self.test_player.set_id("02")
        expected = "02"
        self.assertEqual(self.test_player.get_id(), expected)

    def test_set_name(self):
        self.test_player.set_name("Bob")
        expected = "Bob"
        self.assertEqual(self.test_player.get_name(), expected)

    def test_get_name(self):
        expected = "Jennifer"
        self.assertEqual(self.test_player.get_name(), expected)

    def test_get_inventory(self):
        """by default this is also testing set_inventory, since it is
        dependent on that method working correctly in the setUp"""
        expected = [self.test_object_1, self.test_object_2]
        self.assertEqual(self.test_player.get_inventory(), expected)

    def test_add_to_inventory(self):
        self.test_player.add_to_inventory(self.test_object_3)
        expected = [self.test_object_1, self.test_object_2, self.test_object_3]
        self.assertEqual(self.test_player.get_inventory(), expected)

    def test_delete_all_inventory(self):
        self.test_player.delete_all_inventory()
        # expected = []
        self.assertEqual(self.test_player.get_inventory(), [])

    def test_remove_from_inventory(self):
        self.test_player.remove_from_inventory(self.test_object_1)
        expected = [self.test_object_2]
        self.assertEqual(self.test_player.get_inventory(), expected)

    def test_set_inventory(self):
        self.test_player.set_inventory([self.test_object_3])
        expected = [self.test_object_3]
        self.assertEqual(self.test_player.get_inventory(), expected)

    def test_search_inventory(self):
        self.assertTrue(self.test_player.search_inventory(self.test_object_2))
