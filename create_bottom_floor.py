import system
import room
import object
import feature
import person

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
                    'The large empty expanse of the grand foyer stretches out in front of you. Impressively clean '
                    'marble floors, dark stained wood panel walls, and a large double-sided curved staircase make '
                    'up the architecture of this massive entrance room. The walls are decorated with several paintings, '
                    'some of which look to be quite expensive. \n'
                    'To the south is the entrance to the house. You know you cannot leave until the murder has been '
                    'solved.\n'
                    'To the west, through an open archway, appears to be the entrance to a gleaming white kitchen.\n'
                    'To the east seems to be a library of sort.\n'
                    'To the north is the upstairs hallway.',
                    'The grand foyer stretches out in front of you. To the west is the kitchen, to the east is the '
                    'library, and going upstairs to the north will take you to the upstairs hallway.')
    # sets the connections for the room
    R01.set_connections({
        'west': 'R02',  # kitchen
        'east': 'R03',  # library
        'north': 'R11'  # hallway
    })
    # sets the objects in the room
    # sets the objects in the roof
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
        'search': "You walk around the room, inspecting every nook and cranny. As far as you can tell, "
                  "the only things in the room are the victim's body, an end table, a rotary phone,  and some gaudy old furniture.",
        'touch': 'You run your hands along the ground, careful to avoid the puddle of blood. It feels cool '
                 'to the touch. Placing your hands upon the wood paneling of the wall reveals it is sturdy dark wood. '
                 'This building was clearly quite expensive to construct.',
        'taste': 'You get on all fours and lean down to touch the marble with your tongue. It tastes similar to some '
                 'kind of floor polish.',
        'smell': 'For the first time since entering the room, you notice the smell of the blood. It smells acrid '
                 'and metallic. You recoil and turn your nose out of surprise.',
        'listen': 'You can hear the creaks and groans of an old house. You sit in silence for a minute before you '
                  'hear someone speaking in the library. You cannot make out what they are saying.',
    })

    sys.add_room(R01)

    # F01R01 the victims body
    F01R01 = feature.Feature('F01R01', "Victim's Body",
                             'You turn the body over for a minute, careful not to touch the blood. '
                             'Examining his face closely, you can tell he is an older man in his 50s '
                             'with graying hair and wrinkles. In life, he may have been quite handsome, '
                             'but the shock of death has left him pale with a purple tinge around his lips. ',
                             "The victim's body lays face down on the floor in the middle of the room. He is wearing "
                             "a green sweater with gray slacks. You can see a little dirt around the collar of his "
                             "sweater. Judging by the large gash on the back of his head, "
                             "he was likely struck by some sort of object. A small pool of blood has surrounded "
                             "him, slowly congealing on the cold floor.",
                             {
                                 'search': 'You pat the body down, searching his pockets for any belongings he may '
                                           'have been carrying. You quickly discover that in his front left pocket is a '
                                           'rusty metal key.',
                                 'touch': "You place your fingers on the victim's neck. He is still slightly warm. "
                                          "You are unable to locate a pulse.",
                                 'taste': "You place two fingers in the pool of blood around the victim. Touching "
                                          "them to your tongue immediately confirms that this is blood. You may want "
                                          "to get tested when you get home.",
                                 'smell': 'Smelling the body reveals the overwhelming scent of a deep musky cologne. Although, '
                                          'you can detect hints of another less powerful smell: one that is more '
                                          'flowery and delicate.',
                                 'listen': "You place your ear to the victim's chest. You can hear no heartbeat.",
                             },
                             False)

    sys.add_feature(F01R01)

    # F02R01 the end table
    F02R01 = feature.Feature('F02R01', "End Table",
                             'Examining the end table closer reveals nothing out of the ordinary at first. You '
                             'open the window, which allows a beam of light to enter the room, to get a closer look. '
                             'The light reveals a thin layer of dust on the table, almost imperceptible. Next to the '
                             'candlestick is a ring of clean table where a similar object appears to have been removed.',
                             'A small end table sits in the corner of the room near the entrance to the kitchen. '
                             'A single candlestick sits on top of it.',
                             {
                                 'touch': 'You run a finger along the top of the end table. You feel a little bit of '
                                          'dust between your fingers.',
                                 'taste': 'You bend down and run your tongue along the table. It tastes as if it has '
                                          'not been cleaned in a little while.',
                                 'smell': 'The table smells dusty. You recoil as you begin to sneeze.',
                             },
                             False)

    sys.add_feature(F02R01)

    # F03R01 the rotary phone

    F03R01 = feature.Feature('F03R01', "Rotary Phone",
                             'You examine the phone closely. It is an older model of phone, maybe from the 50s or 60s. '
                             'It is a shiny black, although its age shows through the dulling of the gloss on its surface.',
                             'A rotary phone sits on a table near the front door of the house.',
                             {
                                 'touch': 'You touch the handle of the earpiece. A layer of dust has settled on it. Clearly '
                                          'the victim has not called anyone in quite a while.',
                                 'taste': 'You raise the earpiece and run your tongue over the end you talk into. You '
                                          'realize that doing this may seem a bit weird to others.',
                                 'smell': 'The phone has no distinct smell.',
                                 'listen': 'You bring the earpiece to your ear and listen for a second. A harsh dial tone '
                                           'rings in your ear as you realize that you may need to input a number into the phone. '
                                           '(Hint: Try the "call" command to call the police and end the game)'
                             },
                             False)

    sys.add_feature(F03R01)

    # O02 the rusty key

    O02 = object.Object('O02', 'rusty key',
                        'The key is quite old. Examining it in your hands reveals that it is made of some sort of metal. '
                        'Nearly the entire key has been coated in rust. It is smaller than a normal door key.',
                        'A rusty key sits on the ground.',
                        {
                            'touch': 'The key is old and rough. The years have been unkind to it as rust has eaten '
                                     'through the top layer of metal.',
                            'taste': 'The key feels rough and tastes metallic on your tongue. The only question '
                                     'running through your mind is, "Am I up to date on my tetanus shot?"',
                            'smell': 'The key lacks any distinct smell.',
                        },
                        True)

    sys.add_obj(O02)

    # R02 The Kitchen

    R02 = room.Room('R02', 'Kitchen',
                    "The bright whiteness of the kitchen almost blinds you. Under different circumstances, this would "
                    "excite you in anticipation for a weekend of great meals. However, due to Norman Bates' "
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
        'search': "You walk around the room, opening cabinet doors and drawers. The cabinets are filled with various "
                  "cooking utensils and dishes. You do not sense anything out of the ordinary.",
        'touch': 'You run your hands along the cold marble counters and the warm metal top of the stove. The room has '
                 'been impeccably cleaned. Aside from a small pile of dishes, there is not a spot of grease to be found.',
        'taste': 'You place your tongue on the marble countertop and lick, confirming that the marble has recently '
                 'been cleaned.',
        'smell': 'The room has recently been used to cook. You can smell hints of garlic and butter wafting from the '
                 'dishes near the sink.',
        'listen': 'You can hear the electric buzz of the appliances and not much else.',
    })

    sys.add_room(R02)

    # F01R02 pantry

    F01R02 = feature.Feature('F01R02', "Pantry",
                             'Opening the door to the pantry and switching on the light, you can see the kitchen is well-'
                             'stocked. Every kind of food imaginable is stored in this pantry: boxes of pasta, bags of '
                             'potatoes, a bin of onions and garlic, and several large sacks of flour. Those who live '
                             'in the house full-time clearly do not go hungry.',
                             'The door to a large open pantry is cracked open. You can see many boxes of food inside.',
                             {
                                 'search': 'You take a minute to comb through every box and bag in the pantry. You do not '
                                           'notice anything out of the ordinary stored in here.',
                                 # NOTE: May need to change this and put an item in search
                                 'touch': 'You touch a few of the boxes in the pantry. It appears to be normal food.',
                                 'taste': 'You open up a box of crackers and take one out. Examining it reveals that '
                                          'it is a normal water cracker. You take a bite and determine that it is a '
                                          'little bland.',
                                 'smell': 'The pantry smells of dried food that has been stored for quite a while.',
                                 'listen': 'You do not hear anything out of the ordinary in the pantry.',
                             },
                             False)

    sys.add_feature(F01R02)

    # F02R02 dishes

    F02R02 = feature.Feature('F02R02', "Dishes",
                             'Examining the pile of dishes closely, you can see that they were recently used to cook a '
                             'full meal. You see several pans that have been used to cook many different things.',
                             'A pile of dirty dishes sits by the sink, recently used.',
                             {
                                 'search': 'You look through the pile of dirty dishes, absentmindedly searching for '
                                           'something. You see several substances stuck on the pans: bits of meat, '
                                           'grease, purple flower petals, and veggie scraps.',
                                 'touch': 'You touch one of the pans. It is coated in grease and oil.',
                                 'taste': 'You take one of the pans and bring it up to your mouth, tasting the '
                                          'substance inside it. It coats your tongue with a greasy, bitter taste '
                                          'that takes a bit of time to dissipate.',
                                 'smell': 'The pans smell strongly of grease.',
                             },
                             False)

    sys.add_feature(F02R02)

    # P06 Ava Scarlett (The Killer)

    P06 = person.Person('P06', 'Ava Scarlett',
                        'You take a step closer to the woman who introduced herself earlier as Ava Scarlett. '
                        'She is in her early to mid 30s, young but with some wrinkles starting to '
                        'appear. She keeps her hair cut short and dyed a deep '
                        'shade of black with red highlights. Her makeup has been carefully done, with charcoal '
                        'eyeliner and red lipstick. She is wearing a patterned dark t-shirt with jeans and '
                        'black boots. She only has one earring in. She seems a bit annoyed by your presence '
                        'as she reads a novel in a small breakfast nook near the window.',
                        'Ava Scarlett sits near the window in a breakfast nook reading a novel.',
                        {
                            'ask': {
                                'P01': "You question Ava about Alice. Ava responds, 'Well, I don't know much about her. "
                                       "I only just met her when I got here. If you ask me, though, I think her and our "
                                       "recently deceased host were 'well acquainted' if you know what I mean.'",
                                'P02': "You question Ava about Adam, the victim's son. Ava's eyebrows raise as she says, "
                                       "'You didn't hear it from me, but I heard him and his dad fighting before we found "
                                       "the body. I'm not sure if he's the one that killed his dad, but I can tell you "
                                       "that they did not have the best relationship.'",
                                'P03': "You question Ava about Sam. She looks annoyed, stating 'I never liked that guy. "
                                       "We arrived together, and he had a bad attitude. Not only that, but he just looks "
                                       "like a thug. What a weird guy.'",
                                'P04': "You ask Ava about the groundskeeper, Al. Ava responds, 'To be honest, I don't "
                                       "really know much about him. He seems like a bit of a loner.'",
                                'P05': "You question Ava about Heather. Ava states, 'She seems pretty cheery. Kind of odd "
                                       "that she's not more upset about the murder though, isn't it?'",
                                'P06': "You ask Ava about herself. 'Me?' she says. 'Well, I work as a software developer "
                                       "at a tech company in the city. It's a lot of screen time, so every once in a while "
                                       "I like to get out of the office and do a retreat like this one.' She pauses. 'This "
                                       "is the first time I've been to this retreat though. I wish it could have been "
                                       "under better circumstances...'",
                                'F01R01': "You question Ava about Norman. She quickly answers, 'I didn't know him "
                                          "very well. I only spoke with him once over the phone when I called to set up "
                                          "this weekend. I'm sorry to say, he seemed like a great guy.'",
                                'O01': "You ask Ava about the candlestick. Her eyes widen, and she quickly glances toward "
                                       "the door. 'Isn't that the gaudy candlestick from the foyer? Why'd you pick it up?'",
                                'O05': "You question Ava about the earring. She snatches it from your hand and looks it "
                                       "over. She says, 'Where did you find this? The bathroom, huh? I must have lost it "
                                       "when I washed my face earlier. If it helps your investigation, you're welcome to "
                                       "keep it until we leave.'",
                                'O06': "You show Ava the bloodied washcloth. She recoils. 'Gross! Keep that away from me. "
                                       "I can't stand the sight of blood'",
                                'O09': "You ask Ava about the letter. Her face goes blank. She sheepishly looks around and "
                                       "sighs. 'Okay,' she says 'You caught me. My motives for coming here weren't exactly "
                                       "one hundred percent genuine. Norman and I used to be lovers when I was in my "
                                       "twenties. It didn't end well... I came here so I could confront him. I swear I'm "
                                       "not the one who killed him though! Before I even got to talk to him, he was "
                                       "murdered! The only reason I've been lying was because I didn't want to be pegged "
                                       "as the killer. I'm not a bad person, I promise. You have to believe me!'",
                                'O11': "You ask Ava about the will. 'What's that?' she says. 'Norman's will? Does it say "
                                       "he's giving everything to Alice? I wonder what could possess him to do something "
                                       "like that instead of giving it to his son?'",
                                'O12': "You question Ava about the FBI badge. 'Oh, no way!' she says excitedly. 'Someone "
                                       "here is an FBI agent? I wonder who it is. Wait, you don't think I'm an FBI Agent, "
                                       "do you? I wish! That would be a great gig.'"
                            },
                            'search': 'You ask Ava if she has any belongings that could help in your investigation. '
                                      'She turns her pockets inside out, showing that she has nothing on her. She shrugs '
                                      "and says, 'Sorry I can't be of more help.'",
                            'touch': 'As you walk up to her, hand outstretched, Ava holds her hand up and says, '
                                     "'I would prefer if you didn't.'",
                            'smell': 'You walk up to Ava and sniff. You smell a slightly floral perfume. As you '
                                     'look up, Ava is staring at you with a concerned look on her face.',
                            'listen': 'Ava is remarkably silent as she reads her book.',
                        })

    sys.add_person(P06)

    # R03 The Library

    R03 = room.Room('R03', 'Library',
                    'You walk into a massive double story room lined with books. Every wall is covered in a book of every '
                    'size and color. In the center of the room is a large red cloth couch with two matching sitting chairs. '
                    'Between them sits a massive oak coffee table.\n'
                    'In a massive set of double doors to the southwest is the entrance to the grand foyer.\n'
                    'Through a door to the northwest you can see the ridiculously oversized table of the dining room.\n'
                    'To the north is a set of french doors that lead outside to the patio.',
                    'You enter the library and marvel at the wall to wall bookcase lined with books. To the southwest is '
                    'the double doors that lead to the grand foyer, to the northwest is a door leading to the dining room, '
                    'and to the north is a set of french doors leading to the patio.')
    # sets the connections for the room
    R03.set_connections({
        'north': 'R06',  # patio
        'southwest': 'R01',  # grand foyer
        'northwest': 'R05',  # dining room
        # secret room is to the east, and will get added by the open command
    })
    R03.set_features(['F01R03',  # bookcase
                      'F02R03',  # book on table
                      'F03R03',  # button
                      'F04R03',  # gun
                      ])
    R03.set_people([
        'P05'  # Heather Poirot, the FBI Agent
    ])
    R03.set_interactions({
        'search': "You walk around the room looking for any objects that look out of the ordinary. You realize you may "
                  "need to get a closer look at the books if you want to find anything.",
        'touch': 'You run your hands along the soft green carpet of the room. It is clearly high quality',
        'taste': 'You get on all fours and lean down to lick the carpet. You realize you probably should not have done '
                 'this as the carpet tastes a bit musty',
        'smell': 'The smell of paper and old books is unmistakable. Someone has used a perfume or air freshener to make '
                 'the room smell a little less musty',
        'listen': 'The room is eerily quiet. Heather coughs, looking to break the uncomfortable silence.',
    })

    sys.add_room(R03)

    # F01R03 bookcase

    F01R03 = feature.Feature('F01R03', "Bookcase",
                             'The bookcase has books of every size and color. You absentmindedly look through the books,'
                             'examining them. You see a set of encyclopedia, a few classic novels, and some books on '
                             'nonfiction topics as well, such as horticulture and cooking.',
                             'Massive wooden bookcases line the eastern wall of the room.',
                             {
                                 'search': 'You run your hands along the bookcases, pulling out a few books and searching '
                                           "along the back and undersides of the shelves. You're almost ready to give up "
                                           "until you pull out one last book, revealing a small red button behind it.",
                                 'touch': 'You run your hands along the books, nothing appears to be out of the ordinary. '
                                          'You then touch a book which seems oddly stiff and out of place, maybe you should '
                                          'look a little closer.',
                                 'smell': 'The bookcase smells of old wood and paper that has been sitting for a long time.',
                                 'listen': 'The bookcase is strangely silent.',
                                 'open': {
                                     'unlocked': 'You grab the bookcase with the little bit of leverage you can find on '
                                                 'the corner '
                                                 'of the wood. As you pull the bookcase easily swings away revealing an entrance to '
                                                 'a secret room behind it.',
                                     'locked': 'You attempt to grab the bookcase to pull on it, but you cannot get a good '
                                               'hold on the wood around it.',
                                     'room_ids': [['east','R04']]
                                 },
                                 'use': {
                                     'F03R03': 'You press the button, you hear a satisfying click as the bookshelf shifts '
                                               'slightly toward you, revealing a small indented handle on the side.',
                                 }
                             },
                             False)

    F01R03.add_condition(False)

    sys.add_feature(F01R03)

    # F02R03 book

    F02R03 = feature.Feature('F02R03', "Book",
                             'The book has a green cover, the title states it is a book on gardening and horticulture. '
                             'You take a closer look and it appears the book has a page ripped out of it in the plant '
                             'biography.',
                             'A book with a green cover is sitting in the center of the room on the coffee table.',
                             {
                                 'touch': 'The book is made of a rough paper, it appears to be some kind of organic '
                                          'recycled material.',
                                 'smell': 'The book smells slightly perfumed, as if it had been around flowers recently.',
                                 'listen': 'The book does not sound like anything',
                                 'use': {
                                     'O10': 'You take the piece of paper and hold it up to the torn page. Although the '
                                            'paper has been damaged by water, you are able to tell this book is where the '
                                            'page came from.'
                                 },
                                 'read': 'The book mostly talks about gardening and horticulture, several pages on the '
                                         'correct times to plant and water flowers, where to plant them, and many other '
                                         "topics that don't really interest you. You do find a torn page with some of the "
                                         "words still on it, you can make chunks of letters that spell out 'wolfs-' and "
                                         "'poi-'",
                             },
                             False)

    sys.add_feature(F02R03)

    # F03R03 button

    F03R03 = feature.Feature('F03R03', "Button",
                             'A small, red button sits on the back of the shelf, all but hidden if the books were'
                             ' in their normal '
                             'spot on the shelf',
                             'A button peers out from where a book used to be on the shelf',
                             {
                                 'touch': 'Touching the button reveals it is able to be pressed (perhaps you could try to '
                                          "'use' the button on the bookcase)",
                             },
                             True)

    sys.add_feature(F03R03)

    F04R03 = feature.Feature('F04R03', 'Gun',
                             'You attempt to take a closer look at the gun Heather is carrying. Unfortunately her coat '
                             'hides everything besides a brief flash of it when she moves around quickly.',
                             '',
                             {

                             },
                             True)

    sys.add_feature(F04R03)

    # P05 Heather Poirot

    P05 = person.Person('P05', 'Heather Poirot',
                        'You take a look at Heather and scan her up and down, trying to get a read on who she is. She is '
                        'middle aged, maybe early 30s. She is tall, with long brown hair pulled back into a ponytail. She '
                        "doesn't appear to be wearing that much makeup, and her outfit is plain as well, just a simple "
                        "long tan coat with jeans and brown boots. She acts a bit nervous, like she doesn't know what "
                        "to be doing as you walk in the room. She looks away as she notices you staring at her.",
                        'A young woman you recognize as Heather Poirot sits in one of the chairs, staring at the window',
                        {
                            'ask': {
                                'F04R03': 'You ask Heather about the gun she is carrying, she seems surprised then responds '
                                          "'I was asked to come to a creepy retreat by my boss and you expected me not to "
                                          "bring a weapon? Clearly I was right to come armed since someone already died. "
                                          "I'm not the one that killed him though, he didn't die of a gunshot'",
                                'P01': "You ask Heather about Alice. She responds 'I don't know much about her, she seemed "
                                       "really broken up by the death though. I wonder how she's doing?'",
                                'P02': "You ask Heather about Adam. She says 'That guy seems like a hothead. I can't "
                                       "believe he is the son of that kind old man.'",
                                'P03': "You ask Heather about Sam. She responds 'I don't really know about that guy. He "
                                       "seems pretty shady. Earlier I saw him snooping around the library and outside "
                                       "before you arrived. I wonder what he was doing'",
                                'P04': "You ask Heather about Al. She states 'The groundskeeper? He seemed nice, but I "
                                       "noticed he was complaining about being underpaid earlier'",
                                'P05': "You ask Heather about herself. She states 'Well I am a single mom and I work as a "
                                       "lawyer. My life is a little...stressful. So my boss sent me on this trip in order "
                                       "to get me away from it all. To be honest I think it's kind of a waste of time, "
                                       "especially since it looks like this is going to be more stressful than working for "
                                       "obvious reasons",
                                'P06': "You ask Heather about Ava. She responds 'She seems off. Too calm in this situation'",
                                'F01R01': "You ask Heather about the victim. 'Mr. Bates seemed really nice. He greeted me "
                                          "at the door and seemed very excited to spend the weekend with everyone. I'm "
                                          "surprised someone would even want to kill him...'",
                                'O01': "You ask Heather about the candlestick. 'Oh man, that thing is ugly. Why are you "
                                       "carrying it around?'",
                                'O05': "You question Heather about the earring. 'Oh? That's not mine, I only brought one "
                                       "pair "
                                       "and they're still in'. You check her earlobes, and can see two pearl earrings in "
                                       "place.",
                                'O06': "You show Heather the bloodied washcloth. She seems surprised. 'Oh!' she exclaims "
                                       "'Could you take that away, I really can't stand the sight of blood'",
                                'O09': "You show Heather the letter. She takes a second to glance over it, blushing "
                                       "slightly. 'This is...a little scandalous' she says",
                                'O10': "You show heather the smudged drawing. 'Huh' she says, 'It looks like it could "
                                       "have been ripped out of one of the books in here'",
                                'O11': "You ask Heather about the will. She says 'Sorry all this lawyer speak is above "
                                       "my head. Not sure how I could help'",
                                'O12': "You show the FBI badge to Heather. Her eyes widen as she pats a pocket in her "
                                       "jacket. 'Shit!' she exclaims 'First big case and I manage to lose my badge' she "
                                       "mutters under her breath. 'Well you caught me. I was sent here to investigate "
                                       "Mr. bates for tax fraud, but before I could even start the investigation he was "
                                       "murdered. I'm sorry for hindering the investigation but some people tend to "
                                       "get... angry when we reveal that we were lying to them so I decided it was for the "
                                       "best. Let me know if there is anything else I can do to help'"
                            },
                            'touch': 'You take a step closer to Heather and touch her arm. She recoils and jumps back, '
                                     "surprised you would touch her. 'Please don't do that!' she says taking a second to "
                                     "calm down and adjust her coat. As she is adjusting you do see something interesting, "
                                     "the hilt of a pistol poking through a shoulder holster under her left arm.",
                            'smell': 'You take a step toward Heather and sniff. She gives you a strange look and takes a '
                                     'step back. She does not appear to be wearing any perfume.',
                            'listen': 'Heather does not appear to be making any noise besides the odd cough to break the '
                                      'silence every once in a while',
                            'search': 'You ask Heather if you can pat her down to check if she has any items that could '
                                      "help the investigation. She stops you and says 'No, if you want to search me you're "
                                      "just going to have to have the police come here and do it themselves, sorry'",
                        })

    sys.add_person(P05)

    # R04 Secret Room

    R04 = room.Room('R04', 'Secret Room',
                    'You see a cold windowless room in front of you. Clearly designated as a secret room by the owner of '
                    'the house. The sides of the room made of rough brick with a wood '
                    'floor. The room is cold and dark, a single lamp stands near the door to the library. You switch it on '
                    'to allow you to get a better look at the room. The room is bare with few decorations and only a single '
                    'side table and chair as furniture.\n'
                    'The entrance back to the library is through the doorway behind you to the west.',
                    'The secret room is cold and dark, the only thing inside is some sparse furniture. The doorway back '
                    'toward the library stands behind you to the west.')

    R04.set_features([
        'F01R04',  # Picture
        'F02R04',  # Fireplace
        'F03R04',  # Safe
    ])

    R04.set_objects([
        'O03',  # Golden Key
        'O11',  # Will
    ])

    R04.set_interactions({
        'search': 'You look over every inch of the room. It does not take long since the room is already remarkably bare. '
                  'You do not notice anything out of the ordinary until you notice the frame to the painting is thicker '
                  'than it seems, perhaps there is more to it than meets the eye.',
        'touch': 'The room is made of rough brick and wood. It is unclear if this was a finished room or added on in an '
                 'expansion. Perhaps the owner of the house had it custom made',
        'smell': 'The room smells dusty, it has clearly been quite some time since it was cleaned.',
        'listen': "You listen in, at first it is silent until you hear someone speak in one of the other rooms. 'The target "
                  "has been eliminated, unsure of the next actions to take' whispers the voice of Heather from the library. "
                  "She appears to be talking to someone else.",
        'taste': 'You touch your fingers to the floor and draw a line in the dust. You bring it to your mouth and almost '
                 'begin to lick it before you decide it is probably not the best idea to go around tasting everything you '
                 'see.',
    })

    R04.set_connections({
        'west': 'R03'
    })

    sys.add_room(R04)

    # F01R04 painting

    F01R04 = feature.Feature('F01R04', 'Painting',
                             'You step up to take a closer look at the painting. It is a wonderful painted portrait of '
                             'what appears to be '
                             'the victim in his youth. You notice that the frame of the painting is thicker than it should '
                             'be, it sticks '
                             'out from the wall a good 2 to 3 inches.',
                             'A painting of a young man in a nice suit sits on the northern wall',
                             {
                                 'search': 'As you touch the painting, you notice it has a small latch on one side and '
                                           'hinges on the '
                                           'other. It appears to be hiding something underneath it.',
                                 'touch': 'You run your hand along the paintings frame. Your fingers touch a latch on the '
                                          'side of the '
                                          'painting. Perhaps you could open the latch.',
                                 'open': {
                                     'unlocked': 'The latch easily comes undone and you swing the painting open on the '
                                                 'hinges, revealing an '
                                                 'electronic safe underneath it.'
                                 },
                                 'smell': 'The painting smells of old paint and wood',
                                 'taste': 'You stick your tongue out and lick the paint. Not only does it taste bad, '
                                          'but you likely just '
                                          'ruined an old, old painting',
                             },
                             False)

    F01R04.add_condition(True)

    sys.add_feature(F01R04)

    # F02R04

    F02R04 = feature.Feature('F02R04', 'Fireplace',
                             'You glance at the cold fireplace. It is made of brick and flagstone, with an iron grate in '
                             'the hearth. '
                             'The hearth is filled with ashes, it clearly has been used many times before without being '
                             'cleaned out',
                             'A cold fireplace sits on the eastern wall, filled with ash.',
                             {
                                 'search': 'You sift through the ashes of the fireplace, searching for something. You '
                                           'almost give up '
                                           'before your dirty fingers grasp something. What appears to be a golden key.',
                                 'touch': 'You press your hand into the ash, it appears to be cold as if it has not been '
                                          'used in a '
                                          'while',
                                 'smell': 'The fireplace smells like burnt wood',
                                 'taste': 'You touch the ash and lick your fingers, you can be absolutely sure that this '
                                          'is ash.',
                                 'listen': 'If the fireplace was active, you would be able to hear the sound of a '
                                           'crackling fire. '
                                           'Currently it is silent',
                             },
                             False)

    sys.add_feature(F02R04)

    # F03R04 The Safe

    F03R04 = feature.Feature('F03R04', 'Safe',
                             'You get a closer look at the safe, it is a simple electronic lock with a normal keypad. '
                             'The safe is made of strong looking steel.',
                             'A safe sits on the wall underneath the painting that has been swung open',
                             {
                                 'use': {
                                     'O04': 'You take the code written on the envelope and type it into the keypad on the '
                                            'safe. It beeps three times and the small red light on the front turns green.'
                                 },
                                 'open': {
                                     'locked': 'You attempt to open the safe. It is sealed shut, you clearly need to find '
                                               'a code in order to unlock it.',
                                     'unlocked': 'You grasp the handle of the safe and swing it open, revealing the contents'
                                                 ' '
                                                 "of the safe underneath it; several thick black rubber bands with '$10,000 "
                                                 "written on them in white writing, and a piece of high quality paper with "
                                                 "'Norman Bates's Will' written on it in thick bold lettering.",
                                     'obj_ids': ['O11'],
                                 },
                             },
                             True)

    F03R04.add_condition(False)

    sys.add_feature(F03R04)

    # O03 The Golden Key

    O03 = object.Object('O03', 'Golden Key',
                        'The key is large and made of high quality material. It is plated in gold with a single red gem '
                        'placed on the hilt of the key.',
                        'A golden key sits undisturbed on the floor',
                        {
                            'touch': 'The key is made of high quality material, it is smooth to the touch',
                            'smell': 'The key does not smell',
                            'taste': 'The key tastes metallic'
                        },
                        True)

    sys.add_obj(O03)

    # O11 The Will

    O11 = object.Object('O11', "Victim's Will",
                        "The Victim's will is complicated and created with very technical vocabulary",
                        "The Victim's will sits, waiting to be read",
                        {
                            'touch': 'The will is made of high quality paper',
                            'smell': 'The will smells of ink, it must have been created or edited relatively recently',
                            'read': 'The will is complicated, with very technical writing. You look it over trying to parse '
                                    'it. it contains the normal information on what to do with the body in the event of '
                                    'his death, as well as some additional information on where he wants individual objects '
                                    'to go. You skip to the bottom of the page and read an interesting line: '
                                    "'I, Norman Bates, hereby remove any inheritance from my son, Adam Bates, and instead "
                                    "relinquish my estate and all my earthly possessions to my dear friend and business "
                                    "partner, Alice Stone, in the event of "
                                    "my death'"
                        },
                        True)

    O11.add_condition(False)

    sys.add_obj(O11)

    # R05 Dining Room

    R05 = room.Room('R05', 'Dining Room',
                    'The incredibly lavish dining room is well lit and beautifully decorated. Huge windows line the '
                    'northern wall, allowing you to peer into the backyard of the house. '
                    'A large table with 8 seats '
                    'made of expensive dark wood sits in the center of the room. A well stocked bar stands at the other '
                    'end of the room, clearly it has been well used as many of the bottles are half full.\n'
                    'A set of large glass doors sit to the west that lead to the kitchen.\n'
                    'An open doorway in the east leads to the library.',
                    'The Dining Room is lavish and beautiful. With a large table and a well stocked bar at one end.'
                    'A set of glass doors to the west leads to the kitchen, while an open doorway to the east leads '
                    'to the library.')

    R05.set_features([
        'F01R05',  # Food
        'F02R05',  # Glasses
    ])

    R05.set_interactions({
        'search': 'You search under the table and behind the bar. You cannot find anything out of the ordinary in this '
                  'room.',
        'touch': 'You run your hand along the beautiful wood of the table and bar. It is smooth and sturdy',
        'smell': 'The room smells of food that has recently been cooked',
        'listen': "You attempt to listen to the room. The room is silent, besides the wind howling on the windows outside",
        'taste': 'You lick the table, it tastes of a bitter varnish.',
    })

    R05.set_connections({
        'west': 'R02',  # the kitchen
        'east': 'R03',  # the library
    })

    sys.add_room(R05)

    # F01R05 The Food

    F01R05 = feature.Feature('F01R05','Plate of Food',
                             'You examine the food more closely, it was made within the last few hours although it '
                             'has long since gone cold. The steak is cooked rare with a flowery pepper cream sauce. '
                             'The mashed potatoes have been well seasoned with garlic and bits of greenish herbs. The '
                             'salad is coated in an oily vinaigrette with a lot of purple flowers used as garnish. '
                             'It appears only a few bites have been taken off the plate.',
                             'A plate of food sits barely touched on the table',
                             {
                                 'touch': 'The food has long since gone cold.',
                                 'taste': 'The food tastes off somehow. The steak is well cooked and the rest of the food '
                                          'is well seasoned, but there is a bitter after taste that holds in the back of '
                                          'your mouth as you try a bite.',
                                 'smell': 'The food smells delicious, you almost want to take a bite to try it for yourself',
                                 'search': 'Combing through the mashed potatoes and salad with a fork does not reveal '
                                           'anything hidden within'
                             },
                             False)

    sys.add_feature(F01R05)

    # F02R05 The Glasses

    F02R05 = feature.Feature('F02R05','Glasses',
                             'You examine the glasses on the bar more closely. Both are half full, one with a red liquid '
                             'and the other with a clear amber colored drink. The glass with the read liquid appears to '
                             'have lipstick around the glass',
                             'A pair of glasses sit on the bar, each half full.',
                             {
                                 'touch': 'The glasses are warm to the touch, they have been sitting out for a while',
                                 'taste': 'You individually bring each of the glasses to your lips, tasting the liquids '
                                          'inside. The red glass contains a bitter red wine, while the amber glass contains '
                                          'a slightly watered down sweet whiskey.',
                                 'smell': 'It quickly becomes very clear to you as you bring the glasses to your nose, that '
                                          'these drinks are alcoholic.',
                             },
                             False)

    sys.add_feature(F02R05)

    # This command saves the base files in the game
    sys.save_base_game_files()
