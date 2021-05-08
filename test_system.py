import unittest

import system
import room
import object
import player
import nlp
import feature
import interactable
import person
import object

class TestSystemClass(unittest.TestCase):

    def set_up_1(self):
        sys = system.System()
        ob1 = object.Object('O01', 'Object1', 'an object',
                            {
                                'read': 'you read the words on the page',
                                'touch': 'you touch the object',
                                'taste': 'you taste the object',
                                'smell': 'you smell the object',
                                'listen': 'you listen to the object'
                            },
                            False)
        feat1 = feature.Feature('F01', 'Feature1', 'a feature',
                              {
                                  'use': {
                                      'O01': 'you used the object on this feature'
                                  },
                                  'search': 'you search the object',
                              },
                              False)
        feat1.add_condition(False)
        per1 = person.Person('P01','Person1','a person',
                             {
                                 'ask': {
                                     'O01': 'i admit, I am the murderer',
                                     'F01': 'never heard of it!',
                                     'P02': 'she is kind of shady'
                                 }
                             })
        per2 = person.Person('P02','Person2','a second person',{})
        r1 = room.Room('R01','Room1','a room','room',False)
        r1.add_feature(feat1.get_id())
        r1.add_object(ob1.get_id())
        r1.add_person(per1.get_id())
        sys.add_obj(ob1)
        sys.add_feature(feat1)
        sys.add_person(per1)
        sys.add_person(per2)
        sys.add_room(r1)
        r2 = room.Room('R02', 'Room2', 'a room', 'room', False)
        r1.add_connection('R02')
        sys.add_room(r2)
        return sys,ob1,feat1, per1, r1

    def test_use_1(self):
        """tests use method under normal conditions"""
        sys,ob1,feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.use(ob1.get_id(),feat1.get_id()))

    def test_use_2(self):
        """tests use if we use it on a feature twice"""
        sys,ob1,feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        sys.use(ob1.get_id(),feat1.get_id())
        self.assertFalse(sys.use(ob1.get_id(), feat1.get_id()))

    def test_use_3(self):
        """tests use if we pass it an object that isn't in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.use(ob1.get_id(), feat1.get_id()))

    def test_use_4(self):
        """tests use if we pass it an object that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.use('nothing', feat1.get_id()))

    def test_use_5(self):
        """tests use if we pass it a feature that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertFalse(sys.use(ob1.get_id(), 'nothing'))

    def test_use_6(self):
        """tests use if we pass it an object and a person"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertFalse(sys.use(ob1.get_id(), per1.get_id()))

    def test_use_7(self):
        """tests use if we pass it an object and a room"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertFalse(sys.use(ob1.get_id(), r1.get_id()))

    def test_ask_1(self):
        """tests ask if we pass it an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.ask(per1.get_id(),ob1.get_id()))

    def test_ask_2(self):
        """tests ask if we pass it an object not in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.ask(per1.get_id(),ob1.get_id()))

    def test_ask_3(self):
        """tests ask if we pass it a feature"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.ask(per1.get_id(),feat1.get_id()))

    def test_ask_4(self):
        """tests ask if we pass it a person"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.ask(per1.get_id(),'P02'))

    def test_read_1(self):
        """tests read on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.read(ob1.get_id()))

    def test_read_2(self):
        """tests read on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.read(ob1.get_id()))

    def test_read_3(self):
        """tests read on a feature without the read key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.read(feat1.get_id()))

    def test_read_4(self):
        """tests read on a person without the read key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.read(per1.get_id()))

    def test_read_5(self):
        """tests read on a room without the read key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.read(r1.get_id()))

    def test_read_6(self):
        """tests read on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.read('nothing'))

    def test_search_1(self):
        """tests search on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.search(ob1.get_id()))

    def test_search_2(self):
        """tests search on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertFalse(sys.search(ob1.get_id()))

    def test_search_3(self):
        """tests search on a feature without the search key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.search(feat1.get_id()))

    def test_search_4(self):
        """tests search on a person without the search key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.search(per1.get_id()))

    def test_search_5(self):
        """tests search on a room without the search key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.search(r1.get_id()))

    def test_search_6(self):
        """tests search on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.search('nothing'))

    def test_touch_1(self):
        """tests touch on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.touch(ob1.get_id()))

    def test_touch_2(self):
        """tests touch on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.touch(ob1.get_id()))

    def test_touch_3(self):
        """tests touch on a feature without the touch key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.touch(feat1.get_id()))

    def test_touch_4(self):
        """tests touch on a person without the touch key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.touch(per1.get_id()))

    def test_touch_5(self):
        """tests touch on a room without the touch key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.touch(r1.get_id()))

    def test_touch_6(self):
        """tests touch on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.touch('nothing'))

    def test_smell_1(self):
        """tests smell on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.smell(ob1.get_id()))

    def test_smell_2(self):
        """tests smell on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.smell(ob1.get_id()))

    def test_smell_3(self):
        """tests smell on a feature without the smell key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.smell(feat1.get_id()))

    def test_smell_4(self):
        """tests smell on a person without the smell key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.smell(per1.get_id()))

    def test_smell_5(self):
        """tests smell on a room without the smell key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.smell(r1.get_id()))

    def test_smell_6(self):
        """tests smell on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.smell('nothing'))

    def test_taste_1(self):
        """tests taste on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.taste(ob1.get_id()))

    def test_taste_2(self):
        """tests taste on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.taste(ob1.get_id()))

    def test_taste_3(self):
        """tests taste on a feature without the taste key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.taste(feat1.get_id()))

    def test_taste_4(self):
        """tests taste on a person without the taste key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.taste(per1.get_id()))

    def test_taste_5(self):
        """tests taste on a room without the taste key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.taste(r1.get_id()))

    def test_taste_6(self):
        """tests taste on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.taste('nothing'))

    def test_listen_1(self):
        """tests listen on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.listen(ob1.get_id()))

    def test_listen_2(self):
        """tests listen on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.listen(ob1.get_id()))

    def test_listen_3(self):
        """tests listen on a feature without the listen key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.listen(feat1.get_id()))

    def test_listen_4(self):
        """tests listen on a person without the listen key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.listen(per1.get_id()))

    def test_listen_5(self):
        """tests listen on a room without the listen key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.listen(r1.get_id()))

    def test_listen_6(self):
        """tests listen on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.listen('nothing'))

    def test_look_at_1(self):
        """tests look_at on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.look_at(ob1.get_id()))

    def test_look_at_2(self):
        """tests look_at on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.look_at(ob1.get_id()))

    def test_look_at_3(self):
        """tests look_at on a feature without the look_at key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.look_at(feat1.get_id()))

    def test_look_at_4(self):
        """tests look_at on a person without the look_at key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.look_at(per1.get_id()))

    def test_look_at_5(self):
        """tests look_at on a room without the look_at key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.look_at(r1.get_id()))

    def test_look_at_6(self):
        """tests look_at on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.look_at('nothing'))

    def test_look_1(self):
        """tests look"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.look())

    def test_go_1(self):
        """tests go to a room that is connected"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.go('R02'))

    def test_go_2(self):
        """tests go to a room that is not connected"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.go('R02')
        self.assertFalse(sys.go('R01'))

    def test_go_3(self):
        """tests go to a room that does not exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.go('R10'))

    def test_take_1(self):
        """tests take on an object"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertTrue(sys.take(ob1.get_id()))

    def test_take_2(self):
        """tests take on an object in your inventory"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertFalse(sys.take(ob1.get_id()))

    def test_take_3(self):
        """tests take on a feature without the take key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.take(feat1.get_id()))

    def test_take_4(self):
        """tests take on a person without the take key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.take(per1.get_id()))

    def test_take_5(self):
        """tests take on a room without the take key"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.take(r1.get_id()))

    def test_take_6(self):
        """tests take on an id that doesn't exist"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.take('nothing'))

    def test_inventory_1(self):
        """tests the inventory with nothing in it"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        self.assertFalse(sys.inventory())

    def test_inventory_2(self):
        """tests the inventory with something in it"""
        sys, ob1, feat1, per1, r1 = self.set_up_1()
        sys.take(ob1.get_id())
        self.assertTrue(sys.inventory())



