import system
import room
import interactable
import object
import feature
import person
import converter

# DESC
# This python file will use everything from the system to generate the json files for the game
# simply instantiate the rooms and interactables you want to create, then add them to the system
# the system will then call a command to save the base gamefiles you have created

# list of possible interactions for reference
# interactions = {
#     'use': {
#         'object_id': 'insert how this object would interact with this feature',
#     },
#     'ask': {
#         'object_id': 'insert in character response for the player asking them about this object',
#         'feature_id': 'insert in character response for the player asking them about this feature',
#         'person_id': 'insert in character response for the player asking them about this person',
#     },
#     'read': 'insert the text that would be on this object IE: the letter says "dearest Ava..."',
#     'open': {
#         'locked': 'insert what happens if the player tries to open this object while it is locked',
#         'unlocked': 'insert what happens if the player tries to open this object while it is unlocked',
#     },
#     'search': 'insert what the player finds if they search through the feature',
#     'touch': 'insert what the player feels when they touch this object',
#     'taste': 'insert what the player tastes when they lick this object',
#     'smell': 'insert what the player smells when they sniff this object',
#     'listen': 'insert what the players can hear when they listen to this object',
# }

if __name__ == '__main__':
    # instantiates the system
    sys = system.System()

    # R01 The Grand Foyer

    # creates the grand foyer
    R01 = room.Room('R01', 'Grand Foyer',
                    'The large empty expanse of the Grand Foyer stretches out in front of you. Impressively clean '
                    'marble floors, dark stained wood-paneled walls, and a large double sided curved staircase make '
                    'up the architecture of this massive entrance room. The walls are decorated in several paintings, '
                    'some of which look to be quite expensive. \n'
                    'To the south is the entrance to the house, you know you cannot leave until the murder has been '
                    'solved.\n'
                    'To the west through an open arch appears to be the entrance to a gleaming white kitchen.\n'
                    'To the east through a massive set of open double doors seems to be a Library of sorts.\n'
                    'Going up the staircase would take you to the top floor of the house.',
                    'The Grand Foyer stretches out in front of you. To the west is the kitchen, to the east is the '
                    'library, and going up the staircase would take you to the top floor.')
    # sets the connections for the room
    R01.set_connections({
        'west': 'R02',  # kitchen
        'east': 'R03',  # library
        'staircase': 'R11'  # hallway
    })
    # sets the objects in the room
    R01.set_objects(['O02',  # rusty key
                     ])
    # sets the features in the room
    R01.set_features(['F01R01',  # victims body
                      'F02R01',  # side table
                      'F03R01',  # rotary phone
                      ])
    # no people so no need to set the people list
    # sets the interactions
    R01.set_interactions({
        'search': "You walk around the room inspecting every nook and cranny, as far as you can tell, "
                  "the only things in the room are the victim's body and some gaudy old furniture",
        'touch': 'You run your hands along the ground, careful to walk around the puddle of blood, it feels cold '
                 'to the touch. Placing your hands upon the wood paneling of the wall reveals it is sturdy dark wood. '
                 'This building was clearly quite expensive to construct.',
        'taste': 'You get on all fours and lean down to touch the marble to your tongue. It tastes similar to some '
                 'kind of floor polish or cleaning solution.',
        'smell': 'For the first time since entering the room you notice the smell of the blood. It smells acrid '
                 'and metallic. You recoil and turn your nose out of surprise.',
        'listen': 'You can hear the creaks and groans of an old house. You sit in silence for a minute before you '
                  'hear someone speaking in the library. You cannot make out what they are saying',
    })

    sys.add_room(R01)

    # F01R01 the victims body
    F01R01 = feature.Feature('F01R01', "Victim's Body",
                             'You turn the body over for a minute, careful not to touch the blood. '
                             'Examining his face closely you can tell he is an older man in his 50s '
                             'with graying hair and wrinkles. In life he may have been quite handsome, '
                             'but the shock of death has left him pale white with a purple tinge around his lips. ',
                             "The Victim's Body lays face down on the floor in the middle of the room. He is wearing "
                             "a green sweater with gray slacks. Judging by the large gash on the back of his head, "
                             "he was likely struck by some sort of object. A small pool of blood has surrounded "
                             "him, slowly congealing on the cold floor.",
                             {
                                 'search': 'You pat the body down, searching his pockets for any belongings he may '
                                           'have been carrying. You quickly discover in his front left pocket is a '
                                           'rusty metal key',
                                 'touch': "You place your hands on the victim's neck. He is still slightly warm. "
                                          "You are unable to locate a pulse",
                                 'taste': "You place two fingers in the pool of blood around the victim. Touching "
                                          "them to your tongue immediately confirms this is blood...you may want "
                                          "to get tested when you get home",
                                 'smell': 'Smelling the body reveals it is coated in a deep musky cologne. Although,'
                                          'you can detect hints of another less powerful smell, one that is more '
                                          'flowery and delicate.',
                                 'listen': "You place your ear to the victim's chest. You can hear no heartbeat.",
                             },
                             False)

    sys.add_feature(F01R01)

    # F02R01 the end table
    F02R01 = feature.Feature('F02R01', "End Table",
                             'Examining the end table closer reveals nothing out of the ordinary at first. You '
                             'open the window to get a closer look which allows a beam of light to enter the room. '
                             'The light reveals a thin layer of dust on the table almost imperceptible. Next to the '
                             'candlestick is a ring of clean table where a similar object appears to have been removed.',
                             'A small end table sits in the corner of the room near the entrance to the kitchen, '
                             'a single candlestick sits atop it.',
                             {
                                 'touch': 'You run a finger on the top of the end table, you feel a little bit of '
                                          'dust between your fingers.',
                                 'taste': 'You bend down and run your tongue along the table. It tastes as if it has '
                                          'not been cleaned in a little while.',
                                 'smell': 'The table smells dusty, you recoil as you begin to sneeze',
                             },
                             False)

    sys.add_feature(F02R01)

    # F03R01 the rotary phone

    F03R01 = feature.Feature('F03R01', "Rotary Phone",
                             'You examine the phone closely. It is an older model of phone, maybe from the 50s or 60s. '
                             'It is a shiny black, though it shows its age through the dulling of the gloss on its surface.',
                             'A rotary phone sits on a table near the front door of the house.',
                             {
                                 'touch': 'You touch the handle of the earpiece. A layer of dust has settled on it, clearly '
                                          'the victim has not called anyone in quite a while.',
                                 'taste': 'You raise the earpiece and run your tongue over the end you talk into. You '
                                          'realize that doing this may seem a bit weird to others',
                                 'smell': 'The phone has no distinct smell',
                                 'listen': 'You bring the earpiece to your ear and listen for a second. A harsh dialtone '
                                           'rings in your ear as you realize you may need to input a number into the phone.'
                                           '(Try the "call" command to call the police and end the game).'
                             },
                             False)

    sys.add_feature(F03R01)

    # O02 the rusty key

    O02 = object.Object('O02', 'Rusty Key',
                        'The key is quite old, examining it in your hands reveals it is made of some sort of metal. '
                        'Nearly the entire key has been coated in rust. It is smaller than a normal door key.',
                        'A rusty key sits on the ground',
                        {
                            'touch': 'The key is old and rough, the years have been unkind to it as rust has eaten '
                                     'through the top layer of metal.',
                            'taste': 'The key feels rough on your tongue and feels metallic, the only question '
                                     'running through your mind is "Am I up to date on my Tetanus shot?"',
                            'smell': 'The key lacks any distinct smell',
                        },
                        True)

    sys.add_obj(O02)

    # R02 The Kitchen

    R02 = room.Room('R02', 'Kitchen',
                    "The bright white of the kitchen almost blinds you in this room. Under different circumstances "
                    "this would excite you for a weekend of great meals. However due to the retreat owner's "
                    "untimely demise, the kitchen just seems cold and empty. Large stainless steel appliances sit "
                    "unused next to the white marble counters.\n"
                    "To the west is an open door you suspect leads to the garage.\n"
                    "To the southeast is an archway that leads back to the grand foyer.\n"
                    "To the northeast are clear glass french doors that look into a dining room.",
                    'You enter the kitchen, glancing around to see the white counter tops and stainless steel '
                    'appliances. A door to the west leads to the garage, an archway to the southeast leads to '
                    'the grand foyer, and some french doors to the northeast leads to the dining room.'
                    )
    R02.set_connections({
        'west': 'R08',  # garage
        'southeast': 'R01',  # grand foyer
        'northeast': 'R05'  # dining room
    })
    R02.set_features(['F01R02',  # the pantry
                      'F02R02',  # the dishes
                      ])
    R02.set_people(['P06',  # Ava Scarlett (the killer)
                    ])
    R02.set_interactions({
        'search': "You walk around the room opening cabinet doors and drawers. The cabinets are filled with various "
                  "cooking utensils and dishes. You do not sense anything out of the ordinary.",
        'touch': 'You run your hands along the cold marble counters and the warm metal top of the stove. The room has '
                 'been impeccably cleaned besides a small pile of dishes, not a spot of grease to be found.',
        'taste': 'You place your tongue on the marble counter top and lick, confirming that the marble has recently '
                 'been cleaned.',
        'smell': 'The room has recently been used to cook. You can smell hints of garlic and butter wafting from the'
                 ' dishes near the sink.',
        'listen': 'You can hear the electric buzz of the appliances and not much else.',
    })

    sys.add_room(R02)

    # F01R02 pantry

    F01R02 = feature.Feature('F01R02', "Pantry",
                             'Opening the door to the pantry and switching on the light you can see the kitchen is well '
                             'stocked. Every kind of food imaginable is stored in this pantry; boxes of pasta, bags of '
                             'potatoes, a bin of onions and garlic, and several large sacks of flour. Those who live '
                             'in the house full time clearly do not go hungry.',
                             'The door to a large open pantry is cracked, you can see many boxes of food inside.',
                             {
                                 'search': 'You take a minute to comb through every box and bag in the pantry. You do not '
                                           'notice anything out of the ordinary stored in here.',
                                 # NOTE: May need to change this and put an item in search
                                 'touch': 'You touch a few of the boxes in the pantry. It appears to be normal food.',
                                 'taste': 'You open up a box of crackers and take one out. Examining it reveals that '
                                          'it is a normal water cracker. You take a bite and determine it is a little '
                                          'bland.',
                                 'smell': 'The pantry smells of dried food that has been stored for quite a while.',
                                 'listen': 'You do not hear anything out of the ordinary in the pantry',
                             },
                             False)

    sys.add_feature(F01R02)

    # F02R02 dishes

    F02R02 = feature.Feature('F02R02', "Dishes",
                             'Examining the pile of dishes closely you can see they were recently used to cook a full '
                             'meal. You see several pans that have been used to cook many different things.',
                             'A pile of dirty dishes sits by the sink, recently used',
                             {
                                 'search': 'You look through the pile of dirty dishes, absentmindedly searching for '
                                           'something. You see several substances cooked into the pans, bits of meat, '
                                           'grease, purple flower petals, and veggie scraps.',
                                 'touch': 'You touch one of the pans. It is coated in grease and oil.',
                                 'taste': 'You take one of the pans and bring it up to your mouth. Tasting the '
                                          'substance inside it. It coats your tongue with a greasy bitter taste '
                                          'that takes a bit of time to dissipate.',
                                 'smell': 'The pans smell strongly of grease',
                             },
                             False)

    sys.add_feature(F01R02)

    # P06 Ava Scarlett (The Killer)

    P06 = person.Person('P06','Ava Scarlett',
                        'You take a step closer to the woman who introduced herself earlier as Ava Scarlett. '
                        'She is a woman in her early to mid 30s, young but with some wrinkles starting to '
                        'appear. She keeps her hair cut short and dyed a deep '
                        'shade of black with red highlights. Her makeup has been carefully done, with dark '
                        'eyeliner and red lipstick. She is wearing a patterned dark t-shirt with jeans and '
                        'black boots. She only has one earring in. She seems a bit annoyed by your presence '
                        ' as she reads a novel in a small breakfast nook near the window.',
                        'Ava Scarlett sits near the window in a breakfast nook reading a novel.',
                        {
                            'ask': {
                                'P01': "You question Ava about Alice. Ava responds: 'Well I don't know much about her "
                                       "I only just met her when I got here. If you ask me though, I think her and our "
                                       "recently deceased host were 'well acquainted' if you know what I mean'",
                                'P02': "You question Ava about Adam, the victim's son. Ava's eyebrows raise as she says "
                                       "'You didn't hear it from me, but I heard him and his dad fighting before we found "
                                       "the body. I'm not sure if he's the one that killed his dad, but I can tell you "
                                       "that they did not have the best relationship'",
                                'P03': "You question Ava about Sam. She looks annoyed, stating 'I never liked that guy. "
                                       "We arrived together, and he had a bad attitude. Not only that but he just looks "
                                       "like a thug. What a weird guy'",
                                'P04': "You ask Ava about the groundskeeper. Ava responds 'To be honest I don't really "
                                       "know much about him. He seems like a bit of a loner'",
                                'P05': "You question Ava about Heather. Ava states 'She seems pretty cheery. Kind of odd "
                                       "that she's not more upset about the murder though, isn't it?'",
                                'F01R01': "'You question Ava about the victim. She quickly answers, 'I didn't know him "
                                          "very well. I only spoke with him once over the phone when I called to set up "
                                          "this weekend. I'm sorry to say, he seemed like a great guy'",
                                'O01': "You ask Ava about the candlestick. Her eyes widen, and she quickly glances toward "
                                       "the door, 'Isn't that "
                                       "the gaudy candlestick from the foyer? Why'd you pick it up?'",
                                'O05': "You question Ava about the earring. She snatches it from your hand and looks it "
                                       "over. She says 'Where did you find this? The bathroom huh? I must have lost it "
                                       "when I washed my face earlier. If it helps your investigation you're welcome to "
                                       "keep it until we can leave'",
                                'O06': "You show Ava the bloodied washcloth. She recoils 'Gross! Keep that away from me, "
                                       "I can't stand the sight of blood'",
                                'O09': "You ask Ava about the letter. Her face goes blank. She sheepishly looks around and "
                                       "sighs. 'Okay' she says 'You caught me, my motives for coming here weren't exactly "
                                       "one hundred percent genuine. Norman and I used to be lovers when I was in my "
                                       "twenties. It didn't end well...I came here so I could confront him. I swear I'm "
                                       "not the one that killed him though! Before I even got to talk to him he was "
                                       "murdered! The only reason I've been lying was because I didn't want to be pegged "
                                       "as the killer. I'm not a bad person I promise. You have to believe me!'",
                                'O11': "You ask Ava about the will. 'What's that?' She says 'Norman's will? Does it say "
                                       "he's giving everything to Alice? I wonder what could possess him to do something "
                                       "like that instead of giving it to his son?'",
                                'O12': "You question Ava about the FBI badge. 'Oh no way!' She says excitedly 'Someone "
                                       "here is an FBI agent? I wonder who it is. Wait, you don't think I'm an FBI Agent, "
                                       "do you? I wish! That would be a great gig'"
                            },
                            'search': 'You ask Ava if she has any belongings that could help in your investigation, '
                                      'she turns her pockets inside out, showing she has nothing on her. She shrugs '
                                      "and says 'Sorry I can't be more help'",
                            'touch': 'As you walk up to her, hand outstretched, Ava holds her hand up and says '
                                     "'I would prefer if you didn't'",
                            'smell': 'You walk up to Ava and sniff. You smell a slightly floral perfume. As you '
                                     'look up, Ava is staring at you with a concerned look on her face.',
                            'listen': 'Ava is remarkably silent as she reads her book.',
                        })

    sys.add_person(P06)

    # This command saves the base files in the game
    sys.save_base_game_files()
