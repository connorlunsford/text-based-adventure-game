import system
import room
import interactable
import object
import feature
import person
import converter

if __name__ == "__main__":
       
       # Instantiate the system
       sys = system.System()

       # HALLWAY (R11)
       R11 = room.Room("R11", "Hallway",
                     "You find yourself in a wide, dimly lit hallway surrounded by large oak panel walls. "
                     "A small amount of daylight streams in through a curtained window on the opposite end of the hallway, "
                     "exposing floating dust in the air and providing a sliver of light by which you make out some of "
                     "the features within the hallway. There are four doors, two on each side of the hallway: "
                     "a northwest door, a southwest door, a northeast door, and a southwest door. "
                     "To the south, a grand staircase leads to the bottom floor",
                     "You find yourself in a dimly lit hallway. There are four doors, two on each side of the hallway: "
                     "a northwest door, a southwest door, a northeast door, and a southwest door. "
                     "A grand staircase leads back to the bottom floor."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R11.set_connections({"northeast": "R15", # study
                            "southeast": "R12", # bathroom
                            "northwest": "R14", # master bedroom
                            "northeast": "R13", # second bedroom
                            "south": "R01"      # grand foyer
                            })

       R11.set_features(["F01R11", # console table
                         "F02R11"  # rug
                         ])
       
       # Set the interactions
       R11.set_interactions({
              "search": "You search the entirety of the hallway but find nothing of else of interest. The only two "
              "things in this hallway are the rug and console table.",
              "touch": "The oak panel walls are cool to the touch except where the sunlight hits them.",
              "taste": "What does it mean to taste a room? No, really... what is it that you had in mind?",
              "smell": "Like many parts of this house, the hallway has a faint 'old' smell to it.",
              "listen": "The soft sound of a woman crying comes from behind the southeast door."
              })

       sys.add_room(R11)

       # Console Table (F01R11)
       F01R11 = feature.Feature("F01R11", "Console Table",
                                   "A picture of the retreat owner and a younger man with glasses and messy brown hair "
                                   "sits on the top of the table. The younger man appears to be in his mid-to-late thirties. "
                                   "The retreat owner's arm is wrapped around the man's shoulder in a loving embrace, but "
                                   "the expression on the younger man's face is hard to read. You observe nothing else of "
                                   "note on the table.",
                                   "A wooden console table with a few items on it resides between the two doors to the east.",
                                   {
                                   "search": "There is nothing else here.",
                                   "touch": "You run your fingertips across the top of the console table. Dust. "
                                   "Lots of dust.",
                                   "taste": "Taste the table? Really?",
                                   "smell": "The table smells faintly of wood varnish.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F01R11)

       # Rug (F02R11)
       F02R11 = feature.Feature("F02R11", "White Rug",
                                   "For a white rug in a commonly used space, this rug seems oddly clean. That is, until "
                                   "you notice a small red stain on the corner of the rug nearest to the southwest door.",
                                   "A white, strangely pristine rug lies in the center of the floor.",
                                   {
                                   "search": "There is nothing else here.",
                                   "touch": "Soft. Very soft.",
                                   "taste": "Against what should be your better judgment, you taste the rug that lies "
                                   "in the center of the floor of a commonly used hallway. It tastes like nothing, "
                                   "although a small thread does get stuck on your tongue. Did we mention that this "
                                   "hallway was commonly used?",
                                   "smell": "You smell nothing",
                                   "listen": "You hear nothing. It's a rug."
                                   },
                                   False)

       sys.add_feature(F02R11)

       # BATHROOM (R12)
       R12 = room.Room("R12", "Bathroom",
                     "You enter a bathroom with marble floors and granite countertops. The bathroom is large... "
                     "almost too large. And bright... almost too bright. It reminds you of a museum gallery.  You feel "
                     "strangely small within it. Behind you, a door leads back to the hallway. You notice a faint smell...",
                     "You enter a large bathroom with marble floors and granite countertops. Behind you, a door leads "
                     "back to the hallway."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R12.set_connections({"east": "R11" # hallway
                            })

       R12.set_features(["F01R12", # sink
                         "F02R12"  # trashcan
                         ])

       R12.set_objects(["O05"  # earring
                         ])
       
       # Set the interactions
       R12.set_interactions({
              "search": "A brief search initially yields nothing, although you may want to check the trashcan if you have "
              "not already.",
              "touch": "The marble floors and granite countertops are cold.",
              "taste": "Sigh... so be it. You taste the sink handles and the toilet seat. Neither offers any valuable "
              "information beyond perhaps a sobering insight into your own judgment.",
              "smell": "The faint smell of cleaning chemicals lingers in the air. The smell is very familiar. Bleach?",
              "listen": "The room is so quiet that you can hear the occasional drop of water leaking from the faucet."
              })

       sys.add_room(R12)

       # Sink (F01R12)
       F01R12 = feature.Feature("F01R12", "Sink",
                                   "The sink is made of granite and features a silver faucet  The bowl of the sink is "
                                   "enormous. You can tell by the shine on the faucet that it has been recently cleaned. "
                                   "A pile of clean, white washcloths sit neatly folded next to the sink.",
                                   "A fancy sink with a silver faucet is built into one of the granite countertops.",
                                   {
                                   "search": "There is nothing else here.",
                                   "touch": "The sink feels smooth.",
                                   "taste": "The bowl of the sink tastes like cleaning chemicals. Tasting it definitely "
                                   "seems safe...",
                                   "smell": "The smell of cleaning chemicals lingers in the air. You're almost certain "
                                   "that the smell is bleach.",
                                   "listen": "You hear the occasional drop of water leaking from the sink faucet."
                                   },
                                   False)

       sys.add_feature(F01R12)

       # Trashcan (F02R12)
       F02R12 = feature.Feature("F02R12", "Trashcan",
                                   "The trashcan is made of stainless steel and is one of those trashcans that has a step "
                                   "used for opening it. As you begin to look away, the glint of a small shiny object on the "
                                   "floor catches your eye.",
                                   "A small, metal trashcan sits in the in the corner of the room.",
                                   {
                                   "search": "You step on the trashcan's step, and the lid silently opens. The inside of "
                                   "the trash can is completely empty.",
                                   "touch": "The stainless steel exterior feels slightly cold.",
                                   "taste": "Please try to use your better judgment. This is a trashcan.",
                                   "smell": "The smell of the trashcan is unremarkable.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R12)

       # Earring (O05)
       O05 = object.Object("O05", "Silver Earring",
                            "The women's earring is made of silver and shaped like a small crescent moon.",
                            "A small shiny object lies on the floor. It looks like a women's earring.",
                            {
                                   "touch": "The earring feels strong and well-made.",
                                   "taste": "It tastes like metal. We would like to take this opportunity to note that "
                                   "tasting a stranger's earring is not really sanitary.",
                                   "smell": "You smell nothing.",
                                   "listen": "As you listen to the earring, you begin to hear a faint hum and the sound of "
                                   "drums in the distance. Just kidding. It's an earring. You hear nothing."
                            },
                            True)

       sys.add_obj(O05)

       # SECOND BEDROOM (R13)
       R13 = room.Room("R13", "Second Bedroom",
                     "You enter a medium-sized bedroom pleasantly decorated with flower wallpaper. Bright, morning "
                     "light pours in through a set of large windows on the opposite side of the room. An assortment of "
                     "vases filled with flower arrangements are scattered around the room. Behind you, a door leads"
                     "back to the hallway.",
                     "You enter a sunlight-lit bedroom pleasantly decorated with flower wallpaper. Behind you, a door "
                     "leads back to the hallway."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R13.set_connections({"west": "R11" # hallway
                            })

       R13.set_features(["F01R13", # bed
                         "F02R13"  # vanity
                         ])

       R13.set_objects(["O06" # washcloth
                        ])

       R13.set_people(["P01" # Alice Stone
                       ])
       
       # Set the interactions
       R13.set_interactions({
              "search": "You search the room but find nothing of note. Perhaps you should examine either the bed or "
              "the vanity in more depth.",
              "touch": "Perhaps specify which part of the room you'd like to touch?",
              "taste": "Really? You want to 'taste' the bedroom?",
              "smell": "The soft scent of flowers fills the room.",
              "listen": "Alice sobs quietly in the corner of the room."
              })

       sys.add_room(R13)

       # Bed (F01R13)
       F01R13 = feature.Feature("F01R13", "Bed",
                                   "The queen-sized bed has been neatly made. Its thick white comforter looks like it "
                                   "would sink right in if you were to lie down on top of it. You find yourself "
                                   "suddenly yearning for a nap. You suddenly notice a white washcloth sticking out from "
                                   "underneath the corner of the bed.",
                                   "A queen-sized bed with a thick white comforter sits in the center of the room.",
                                   {
                                   "search": "The bed is empty.", # CHECK - Add washcloth?
                                   "touch": "The comforter slowly sinks in a very satisfying manner when you press your "
                                   "hand into it. You make a mental note to get yourself one of these when you return "
                                   "home.",
                                   "taste": "The bed tastes like... nothing.",
                                   "smell": "The bed and its comforter smell clean.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F01R13)

       # Vanity (F02R13)
       F02R13 = feature.Feature("F02R13", "Vanity",
                                   "The walnut vanity features a large mirror and intricate woodwork along its edges "
                                   "and base. You wonder if it might be an antique. A framed photograph of Norman "
                                   "and Alice sits right at the center of the top of the vanity. They both look very "
                                   "happy. Beside the photograph, a jewelry box filled with all kinds of jewelry--"
                                   "from earrings, to necklances, to bracelets--is open. You notice that all of the "
                                   "jewelry is gold.",
                                   "A walnut vanity sits on one side of the room, near where Alice is standing.",
                                   {
                                   "search": "You search the vanity but find nothing beyond what can easily be seen "
                                   "on top of the vanity desk.",
                                   "touch": "The wood surface is slightly rough.",
                                   "taste": "You lick the top of the vanity, learning nothing of value. Alice stops "
                                   "her crying for just long enough to give you a strange look.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R13)

       # Washcloth (O06)
       O06 = object.Object("O06", "Washcloth",
                            "The white washcloth looks like it might belong to a bathroom set. It's stained with the "
                            "unmistakable color of blood.",
                            "The corner of a white washcloth sticks out from beneath the bed. It has a red stain on it.",
                            {
                                   "touch": "The washcloth is soft except for where the blood has started to dry.",
                                   "taste": "You lick the washcloth and notice the metallic taste of blood.",
                                   "smell": "The washcloth has a strange, unfamiliar metallic scent. Is that blood?",
                                   "listen": "You hear nothing."
                            },
                            True)

       sys.add_obj(O06)

       # Alice Stone (P13)
       P13 = person.Person("P13", "Alice Stone",
                            "Alice Stone turns her head to meet your gaze as you look at her. The bright sunlight from "
                            "the window clearly illuminates her face, revealing her swollen eyes and red, blotchy skin "
                            "from crying. She dabs the corner of her eyes with a tissue before turning back to the "
                            "window.",
                            "Alice Stone stands in the corner of the room, gazing out the window and quietly sobbing.",
                            {
                                   "ask": {
                                   "P02": "Alice sighs softly before answering. 'Norman and Adam's relationship was... "
                                          "complicated, to say the least. They had your typical father and son "
                                          "disagreements about who should inherit the house and Norman's business. "
                                          "Norman wanted Adam to stay here and take over the business, but Adam wanted  "
                                          "to forge a new path on his own. Norman loved Adam dearly, though, and I "
                                          "believe Adam loved his father too.",
                                   "P03": "Alice waves her hand dismissively. 'He's a little shady looking, if you ask "
                                          "me, but, quite frankly, I haven't had much time to get to know the most "
                                          "recent retreat participants after what happened.'",
                                   "P04": "Alice's face lights up slightly. 'He can be quite the miserable old "
                                          "character, but I like him. He's been a loyal employee of Norman's for over "
                                          "twenty years.'",
                                   "P05": "Alice shrugs her shoulders dismissively. 'She seems like any other retreat "
                                          "participant to me.'",
                                   "P06": "", # Check - Did Alice know Ava?
                                   "F01R01": "At the very mention of Norman, Alice begins to heavily sob again. She "
                                          "waves you away, indicating that she wants to be left alone.",
                                   "O01": "Alice looks at the candlestick with a vague disinterest. 'That looks like it "
                                          "belongs in the foyer downstairs,' she mumbles. She pauses and then eyes you "
                                          "suspiciously. 'Please don't tell me you're using this as an opportunity to "
                                          "steal items from a dead man.'",
                                   "O05": "Alice takes the earring, quickly examines it, then hands it back to you. "
                                          "'There's no way that's mine,' she says. 'I'm allergic to silver.'",
                                   "O06": "Alice recoils when you show her the blood-stained washcloth. 'Is that... "
                                          "his blood?' she asks, her voice barely a whisper. When you tell her that it "
                                          "was found in her room, she squints her eyes. 'Do you...? Do you think... "
                                          "that I did it?' When you don't answer, she responds angrily. 'Norman meant"
                                          "'the world to me. I won't be subjected to such accusations.' She looks away,"
                                          "indicating that the conversation is over.",
                                   "O09": "", # Check - Did Alice know about Ava?
                                   "O11": "" # Check - Does Alice know she is in the will?
                                   },
                                   "search": "Alice is wearing only a plain t-shirt and jeans. You ask her if she has "
                                   "anything of importance on her. She shakes her head.",
                                   "touch": "Alice watches you warily as you approach then says, 'Please don't touch me.' "
                                   "You respect her wishes.",
                                   "smell": "You walk closer towards Alice, but, just as you are about to smell her, "
                                   "she turns and gives you a look of disgust, clearly communicating that you need to "
                                   "back away.",
                                   "listen": "Alice sobs quietly."
                            })

       sys.add_person(P13)

       # MASTER BEDROOM (R14)
       R14 = room.Room("R14", "Master Bedroom",
                     "You enter a large, dark bedroom with velvet curtains that are partially closed. In the dim light, "
                     "you can see that the floors, walls, and furniture are made from the same dark wood with a "
                     "reddish hue to it. The room has a very old feel to it, like it was designed in the 17th century. "
                     "A wooden door leads back to the hallway.",
                     "You enter large, dim bedroom that looks like it was designed in the 17th century. A wooden door "
                     "leads back to the hallway."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R14.set_connections({"west": "R11" # hallway
                            })

       R14.set_features(["F01R14", # bed                # CHECK: add fireplace, tapestry/painting if time
                         "F02R14"  # nightstand
                         ])

       R14.set_objects(["O12" # love letter
                        ])
       
       # Set the interactions
       R14.set_interactions({
              "search": "You search the room but find nothing of note. Perhaps you should examine either the bed or "
              "the nightstand in more depth.",
              "touch": "Perhaps specify which part of the room you'd like to touch?",
              "taste": "Why is it that you want to taste everything?",
              "smell": "The room has a musky smell to it.",
              "listen": "The room is silent."
              })

       sys.add_room(R14)

       # Bed (F01R14) # CHECK - Give different name?
       F01R14 = feature.Feature("F01R14", "Bed",
                                   "You pull aside the canopy curtain to look at the bed. The covers and sheets are "
                                   "unmade. Norman must have not had the chance to make it before he was killed. "
                                   "Either that, or he was messy, which doesn't seem very likely based upon the rest "
                                   "of the house. Judging from its size, the bed must be at least a California King.",
                                   "A large canopy bed resides in the center of the room.",
                                   {
                                   "search": "You look through the unmade bed but find nothing.",
                                   "touch": "The bed sheets are surprisingly soft. You wonder what their thread count "
                                   "is and make a mental note to look into it when you get back home.",
                                   "taste": "You rather intrusively taste the bed and glean no useful information "
                                   "from it.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F01R14)

       # Nightstand (F02R14)
       F02R14 = feature.Feature("F02R14", "Nightstand",
                                   "The small nightstand is made of the same dark, red wood as the rest of the  "
                                   "furniture in the room, leading you to believe that they must all be part of the "
                                   "same set, likely passed down through several generations. Its legs and borders are "
                                   "feature intricately carved designs of leaves and vines. The nightstand has a "
                                   "drawer, which as far as you can tell, has no lock.",
                                   "A small nightstand made of the same dark, red wood as the rest of the furniture "
                                   "sits right next to the bed.",
                                   {
                                   "search": "You search nightstand. You find nothing interesting among the assortment "
                                   "of items lying on top of it, but opening the drawer reveals a letter inside.", # CHECK
                                   "touch": "The dark red wood is smooth and clearly polished.",
                                   "taste": "The nightstand tastes like wood polish. It is also tastes like dust.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing." # open?
                                   },
                                   False)

       sys.add_feature(F02R14)

       # Letter (O12)
       O12 = object.Object("O12", "Letter",
                            "The letter is neatly folded and looks otherwise unremarkable at first glance. Maybe you "
                            "should read it.",
                            "A neatly folded letter sits in the nightstand drawer.", # CHECK
                            {
                                   "touch": "It feels like paper.",
                                   "taste": "You lick the letter and taste, well, nothing aside from maybe a little "
                                   "ink.",
                                   "smell": "The letter has the familiar scent of paper.",
                                   "listen": "You hear nothing.",
                                   "read": "You open the letter and read the following: "
                                   "DATE\n"
                                   "Dear Norman,\n I know it's been a long time since we last spoke but last night, "  # CHECK
                                   "as I was walking around the lake near my house, I couldn't stop thinking about "
                                   "our trip to Lake Tahoe and how wonderful it was. What was it, 10 years ago? That "
                                   "one of the happiest times of my life.\n I know you think that our break up was "
                                   "for the best, and I know that our relationship could be unhealthy at times, but "
                                   "I really do think that we were meant to be together. I mean, after all, there must "
                                   "be a reason why you haven't dated anyone else after all these years.\n Anyway, "
                                   "I know that, like always, you likely won't respond to this, but I'll be in your "
                                   "area in a couple weeks for work, and I was thinking that maybe I could stop by.\n"
                                   "Love, A.S."
                            },
                            True)

       sys.add_obj(O12)

       # STUDY (R15)
       R15 = room.Room("R15", "Study",
                     "You enter a very welcoming study. Behind you, a door leads back to the hallway.",
                     "You enter a very welcoming study. Behind you, a door leads back to the hallway."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R15.set_connections({"east": "R11" # hallway
                            })

       R15.set_features(["F01R15", # desk
                         "F02R15"  # bar cart
                         ])

       R15.set_objects(["O04"  # safe code paper
                        ])

       R15.set_people(["P02" # Adam Bates
                       ])
       
       # Set the interactions
       R15.set_interactions({
              "search": "You search the study but don't see anything interesting. Have you checked the desk already?",
              "touch": "You run your hand across some of the items in the room but don't notice anything important.",
              "taste": "You cannot taste a room.",
              "smell": "The smell of cigar smoke permeates the air.",
              "listen": "Adam sighs sadly."
              })

       sys.add_room(R15)

       # Desk (F01R15)
       F01R15 = feature.Feature("F01R15", "Desk",
                                   "The large desk sits in front of the window. Several books, a few papers, and "
                                   "an ash tray are on top it. It seems like Norman liked to smoke cigars as there's "
                                   "a wooden box of what you assume must be expensive cigars near the ash tray. ",
                                   "In front of the window, there's a large desk with several books and papers on top "
                                   "of it.",
                                   {
                                   "search": "You rummage through the papers and books on top of the desk. There's a "
                                   "book on Greek history and an electric bill, but nothing else stands out to you."
                                   "You notice that the ashtray hasn't yet been emptied. You attempt to open the desk "
                                   "drawer, but it's locked.",
                                   "touch": "The wood that the desk is made of feels rough.",
                                   "taste": "You taste nothing.",
                                   "smell": "You smell cigar smoke.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F01R15)

       # Bar Cart (F02R15)
       F02R15 = feature.Feature("F02R15", "Bar Cart",
                                   "The antique bar cart looks like it is made of brass and may be several centuries "
                                   "old. Several bottles and decanters of liquor, a few of which are only partially "
                                   "full, along with some crystal tumblers are on the top shelf. One of the whiskey "
                                   "decanters has its stopper removed. There's a dirty tumbler beside it.",
                                   "An antique bar cart is beside the desk.",
                                   {
                                   "search": "You search the bar cart but don't find anything aside from a few "
                                   "expensive-looking bottles of liquor and crystal tumblers",
                                   "touch": "The bar cart feels slightly cool.",
                                   "taste": "You open a bottle of whiskey and take a sip. It burns as it goes down "
                                   "your throat.",
                                   "smell": "You open a bottle of whiskey and sniff it. It smells sharp and burns "
                                   "the inside of your nose.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R15)

       # Safe Code Paper (O04)
       O04 = object.Object("O04", "Safe Code Paper",
                            "The small piece of paper is dirty and looks like it has been previously crumpled. Four "
                            "letters are written across it in thick ink: 0142",
                            "A small piece of paper sits beneath the other items in the drawer.",
                            {
                                   "touch": "The paper is rough where it has been previously folded.",
                                   "taste": "You taste the dirtied paper. It tastes like paper.",
                                   "smell": "The paper has a slight smell of cigar smoke.",
                                   "listen": "You hear nothing.",
                                   "read": "In thick ink, the paper reads: 0142"
                            },
                            True)

       sys.add_obj(O04)

       # Adam Bates (P02)
       P02 = person.Person("P02", "Adam Bates",
                            "Adam Bates raises his eyebrows and adjusts his glasses when he senses you looking at him. "
                            "He appears to be in his late thirties or early forties. His brown hair is messy, and his "
                            "eyes look sad. 'Can I help you?' he asks.",
                            "Adam Bates is bent over the top of the desk, going through the papers on the desk. He "
                            "quickly straightens up and moves to a nearby bookcase, picking up a book, when you enter. "
                            "He begins flipping through the book absentmindedly.",
                            {
                                   "ask": {
                                   "P02": "",
                                   "P03": "",
                                   "P04": "",
                                   "P05": "",
                                   "P06": "",
                                   "F01R01": "",
                                   "O01": "",
                                   "O05": "",
                                   "O06": "",
                                   "O09": "",
                                   "O11": ""
                                   },
                                   "search": "",
                                   "touch": "You place your hand on Adam's shoulder. He looks up, pats it awkwardly, "
                                   "and then returns to reading.",
                                   "smell": "You near Adam and attempt to smell him. He smells slightly of alcohol.",
                                   "listen": "Adam sighs sadly and turns the page of the book that he's reading."
                            })

       sys.add_person(P02)

       # Save top floor base game files
       sys.save_base_game_files()