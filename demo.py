import system
import room
import object
import feature

# this is a demo created on 4/30/21
# it uses hardcoded data instead of files located in gamefiles
# the following commands will not work in the demo
# loadgame
# savegame
# ask
# call
# go
# open
# use

if __name__ == '__main__':
    # instantiates the system
    sys = system.System()

    roominteractions = {
        'search': 'You take a closer look at the room, searching every nook and cranny. You do not seem to notice anything '
                  'out of the ordinary that you failed to notice on your first examination ',
        'touch': 'You touch the walls of the room, they are made of a nice wood paneling',
        'taste': 'You stick your tongue out and lick the ground...you taste dust',
        'smell': 'The smell of fresh blood is strong in this room',
        'listen': 'You hold your hand up to your ear, you can hear a faint sobbing sound coming from the upstairs hallway'
    }

    R01 = room.Room('R01','Grand Foyer',
                    'A large room with a grand staircase toward the upper floors, it has connections to the kitchen and '
                    'the library but they are both blocked by police tape.',
                    'A large grand entrance',
                    False)
    R01.add_object('O01')
    R01.add_object('O02')
    R01.add_feature('F01')
    R01.set_interactions(roominteractions)

    obj1interactions = {
        'touch': 'The candlestick is carved intricately and beatuifully, it is made of silver',
        'taste': 'The candlestick tastes metallic...this is gross',
        'smell': 'The candlestick smells dusty and old, with a metallic tinge',
        'listen': 'You hear nothing',
    }
    O01 = object.Object('O01','Candlestick','A silver candlestick with a small amount of blood on one end',
                        obj1interactions, False)

    obj2interactions = {
        'read': 'You open the letter, it says..." \n'
                'Dearest Agatha,\n'
                'I fear my time here may be cut short. I find myself becoming scared of someone in my own home.\n'
                'Let us pray we see each other again, for my sake and yours.\n'
                'Sincerely,\n'
                'Wilford',
        'touch': 'The paper this letter is written on is high quality, slightly damp from the blood',
        'taste': 'It tastes of paper...and blood',
        'smell': "A woman's perfume has been sprayed on the paper, almost as if it was purposeful",
        'listen': 'It sounds like...paper'
    }
    O02 = object.Object('O02','Letter','A letter written on fine paper with wonderfully ornate handwriting',
                        obj2interactions, True)

    feat1interactions = {
        'search': 'In the victims front pocket is a letter',
        'touch': 'the body is warm to the touch, the victim has been killed recently',
        'taste': "You reach your tongue out to taste the victim's body...then you reconsider",
        'smell': 'The victim smells of blood and heavy cologne',
        'listen': 'You cannot hear a heartbeat...he must be dead',
    }
    F01 = feature.Feature('F01',"Victim's Body",'An older gentleman lies face down on the floor in a pool of blood. His '
                                                'head has been wounded by some kind of blunt object',
                          feat1interactions, False)

    sys.add_room(R01)
    sys.add_obj(O01)
    sys.add_obj(O02)
    sys.add_feature(F01)



    print("The game is about to start, use the command 'help' if you get stuck")
    # gets a description so the user can check out stuff in the room
    sys.get_description()

    sys.game_loop()
