import unittest
import test_feature
import test_interactable
import test_nlp
import test_object
import test_person
import test_player
import test_room
import test_system

# Load all tests from individual modules
interactable_tests = unittest.TestLoader().loadTestsFromModule(test_interactable)
feature_tests = unittest.TestLoader().loadTestsFromModule(test_feature)
object_tests = unittest.TestLoader().loadTestsFromModule(test_object)
room_tests = unittest.TestLoader().loadTestsFromModule(test_room)
nlp_tests = unittest.TestLoader().loadTestsFromModule(test_nlp)
player_tests = unittest.TestLoader().loadTestsFromModule(test_player)
person_tests = unittest.TestLoader().loadTestsFromModule(test_person)
system_tests = unittest.TestLoader().loadTestsFromModule(test_system)

# Run all tests
print("\n**GAME SYSTEM***")
unittest.TextTestRunner(verbosity=2).run(system_tests)
print("\n***NATURAL LANGUAGE PARSER***")
unittest.TextTestRunner(verbosity=2).run(nlp_tests)
print("\n***PLAYER CLASS***")
unittest.TextTestRunner(verbosity=2).run(player_tests)
print("\n***PERSON CLASS***")
unittest.TextTestRunner(verbosity=2).run(person_tests)
print("\n***INTERACTABLE CLASS***")
unittest.TextTestRunner(verbosity=2).run(interactable_tests)
print("\n***FEATURE CLASS***")
unittest.TextTestRunner(verbosity=2).run(feature_tests)
print("\n***OBJECT CLASS***")
unittest.TextTestRunner(verbosity=2).run(object_tests)
print("\n***ROOM CLASS***")
unittest.TextTestRunner(verbosity=2).run(room_tests)
