import system
import room
import object
import feature
import person

if __name__ == "__main__":
       
       # Instantiate the system
       sys = system.System()

       # HALLWAY (R11)
       R11 = room.Room("R11", "Hallway",
                     "You find yourself in a wide, dimly lit hallway surrounded by large oak panel walls. "
                     "A small amount of daylight streams in through a curtained window on the opposite end of the hallway, "
                     "exposing floating dust in the air and providing a sliver of light by which you make out some of "
                     "the features within the hallway. "
                     "Four rooms connect to the hallway: a bathroom to the northwest, a study to the northeast, "
                     "a master bedroom to the southeast, and a second bedroom to the southwest. "
                     "Going south will lead you back to the grand foyer downstairs.",
                     "You find yourself in a dimly lit hallway. "
                     "Four rooms connect to the hallway: a bathroom to the northwest, a study to the northeast, "
                     "a master bedroom to the southeast, and a second bedroom to the southwest. "
                     "Going south will lead you back to the grand foyer downstairs."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R11.set_connections({"northeast": "R15", # study
                            "northwest": "R12", # bathroom
                            "southwest": "R13", # second bedroom
                            "south": "R01"      # grand foyer
                            })

       R11.set_features(["F01R11", # grandfather clock
                         "F02R11",  # rug
                         "F03R11",  # master bedroom door
                         ])
       
       # Set the interactions
       R11.set_interactions({
              "search": "You search the entirety of the hallway but find nothing else of interest. The only two "
                        "things in the hallway are the rug and grandfather clock.",
              "touch": "The oak panel walls are cool to the touch except where the sunlight hits them.",
              "taste": "What does it mean to taste a room? No, really... what is it that you had in mind?",
              "smell": "Like many parts of this house, the hallway has a faint 'old' smell to it.",
              "listen": "The soft sound of a woman crying comes from the second bedroom."
              })

       sys.add_room(R11)

       # Grandfather Clock (F01R11)
       F01R11 = feature.Feature("F01R11", "Grandfather Clock",
                                   "The grandfather clock features impressive, highly detailed woodwork and appears "
                                   "very aged. You can see its large, golden pendulum swaying behind the glass door. "
                                   "Roman numerals and large serpentine clock hands mark the time.",
                                   "A grandfather clock resides on the eastern side of the hallway. You hear the "
                                   "familiar tick tock, tick tock of the pendulum swinging.",
                                   {
                                   "search": "There is nothing here.",
                                   "touch": "You run your fingertips across the surface of the grandfather clock. Dust. "
                                            "Lots of dust.",
                                   "taste": "Taste the clock? Really?",
                                   "smell": "The grandfather clock smells faintly of wood varnish.",
                                   "listen": "You hear the tick tock, tick tock of the pendulum swinging."
                                   },
                                   False)

       sys.add_feature(F01R11)

       # Rug (F02R11)
       F02R11 = feature.Feature("F02R11", "White Rug",
                                   "For a white rug in a commonly used space, this rug seems oddly clean. That is, until "
                                   "you notice a small red stain on the corner of the rug nearest to the bathroom.",
                                   "A white, strangely pristine rug lies in the center of the floor.",
                                   {
                                   "search": "There is nothing else here besides the red stain on the corner nearest "
                                            "to the bathroom.",
                                   "touch": "Soft. Very soft.",
                                   "taste": "Against what should be your better judgment, you taste the rug that lies "
                                            "in the center of the floor of the commonly used hallway. It tastes like nothing, "
                                            "although a small thread does get stuck on your tongue. Did we mention that this "
                                            "hallway was commonly used?",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing. It's a rug."
                                   },
                                   False)

       sys.add_feature(F02R11)

       # Locked Master Bedroom Door (F03R11)
       F03R11 = feature.Feature("F03R11", "Master Bedroom Door",
                                "The large door to the master bedroom stands imposingly. There is a massive golden lock on "
                                "the door. You could try to open it to see if it is locked.",
                                "The door to the master bedroom has a massive golden lock just above the handle.",
                                {
                                    "touch": "The door is made of wood.",
                                    "taste": "You lick the door. It tastes of wood and varnish.",
                                    "smell": "You smell nothing.",
                                    "listen": "You hear nothing. Nobody appears to be in the room.",
                                    "use": {
                                        "O03": "You insert the large golden key into the lock. It turns easily with a "
                                               "satisfying click. The master bedroom door appears to be unlocked now. "
                                               "Open the master bedroom door so that you can enter the room."
                                    },
                                    "open": {
                                        "locked": "The door appears to be locked from the other side with a heavy "
                                                "bolt. (Hint: If you've found the key to this room, try 'use [key] on [door to room]' "
                                                "in order to unlock it)",
                                        "unlocked": "The door easily swings open, revealing the master bedroom.",
                                        "room_ids": [["southeast", "R14"]]
                                    },
                                },
                                False)

       F03R11.add_condition(False)

       sys.add_feature(F03R11)

       # BATHROOM (R12)
       R12 = room.Room("R12", "Bathroom",
                     "You enter a bathroom with marble floors and granite countertops. The bathroom is large... "
                     "almost too large. And bright... almost too bright. It reminds you of a museum gallery. You feel "
                     "strangely small within it. You notice a faint smell that you may want to further investigate. "
                     "To your east is the hallway from which you entered.",
                     "You enter a large bathroom with marble floors and granite countertops. "
                     "To your east is the hallway from which you entered."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R12.set_connections({"east": "R11" # hallway
                            })

       R12.set_features(["F01R12", # sink
                         "F02R12"  # trash can
                         ])

       R12.set_objects(["O05"  # earring
                         ])
       
       # Set the interactions
       R12.set_interactions({
              "search": "A brief search initially yields nothing, although you may want to take a closer look at "
                        "the trash can, if you haven't already.",
              "touch": "The marble floors and granite countertops are cold.",
              "taste": "Sigh... so be it. You taste the sink handles and the toilet seat. Neither offers any valuable "
                        "information beyond perhaps a sobering insight into your own judgment.",
              "smell": "The faint smell of cleaning chemicals lingers in the air. The smell is very familiar. Bleach?",
              "listen": "The room is so quiet that you can hear the occasional drop of water leaking from the faucet."
              })

       sys.add_room(R12)

       # Sink (F01R12)
       F01R12 = feature.Feature("F01R12", "Sink",
                                   "The sink is made of granite and features a silver faucet. The bowl of the sink is "
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
                                   "listen": "You hear the occasional drop of water leaking from the faucet."
                                   },
                                   False)

       sys.add_feature(F01R12)

       # Trash can (F02R12)
       F02R12 = feature.Feature("F02R12", "Trash can",
                                   "The trash can is made of stainless steel and is one of those trash cans that has a small "
                                   "step used for opening it. As you begin to look away, the glint of a small shiny object "
                                   "on the floor catches your eye.",
                                   "A small, metal trash can sits in the corner of the room.",
                                   {
                                   "search": "You step on the trash can's step, and the lid silently opens. The inside of "
                                            "the trash can is completely empty.",
                                   "touch": "The stainless steel exterior feels slightly cool.",
                                   "taste": "Please try to use your better judgment. This is a trash can.",
                                   "smell": "The smell of the trash can is unremarkable.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R12)

       # Earring (O05)
       O05 = object.Object("O05", "silver earring",
                            "The woman's earring is made of silver and shaped like a small crescent moon.",
                            "A small shiny object lies on the floor. It looks like a woman's earring.",
                            {
                                   "touch": "The earring feels strong and well-made.",
                                   "taste": "It tastes like metal. We would like to take this opportunity to note that "
                                            "tasting a stranger's earring is not very sanitary.",
                                   "smell": "You smell nothing.",
                                   "listen": "As you listen to the earring, you begin to hear a faint hum and the sound of "
                                            "drums in the distance. Just kidding. It's an earring. You hear nothing."
                            },
                            True)

       sys.add_obj(O05)

       # SECOND BEDROOM (R13)
       R13 = room.Room("R13", "Second Bedroom",
                     "You enter a small bedroom pleasantly decorated with flower wallpaper. Bright, morning "
                     "light pours in through a set of large windows on the opposite side of the room. An assortment of "
                     "vases filled with flower arrangements are scattered around the room. "
                     "To your east is the hallway from which you entered.",
                     "You enter a sunlit bedroom pleasantly decorated with flower wallpaper. "
                     "To your east is the hallway from which you entered."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R13.set_connections({"east": "R11" # hallway
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
              "touch": "Perhaps try touching one of the features that you observe within the room.",
              "taste": "Really? You want to 'taste' the bedroom?",
              "smell": "The soft scent of flowers fills the room.",
              "listen": "Alice sobs quietly in the corner of the room."
              })

       sys.add_room(R13)

       # Bed (F01R13)
       F01R13 = feature.Feature("F01R13", "Bed",
                                   "The queen-sized bed has been neatly made. Its thick white comforter looks like it "
                                   "would sink right in if you were to lie down on top of it. You find yourself "
                                   "suddenly yearning for a nap. You wonder if perhaps you should search the bed...",
                                   "A queen-sized bed with a thick white comforter sits in the center of the room.",
                                   {
                                   "search": "You search the bed and notice a white washcloth.",
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
                                   "and Alice sits in the center of the top of the vanity. They both look very "
                                   "happy. Beside the photograph, a jewelry box sits open. It's filled with all kinds of jewelry - "
                                   "from earrings, to necklaces, to bracelets. You notice that all of the "
                                   "jewelry is gold.",
                                   "A walnut vanity sits on one side of the room, near where Alice is standing.",
                                   {
                                   "search": "You search the vanity but find nothing beyond what can easily be seen "
                                            "on top of it. You do notice, however, that all of the jewelry in the jewelry "
                                            "box is gold.",
                                   "touch": "The wood surface is slightly rough.",
                                   "taste": "You lick the top of the vanity, learning nothing of value. Alice stops "
                                            "her crying for just long enough to give you a strange look.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R13)

       # Washcloth (O06)
       O06 = object.Object("O06", "washcloth",
                            "The white washcloth looks like it might belong to a bathroom set. It's stained with the "
                            "unmistakable color of blood.",
                            "A white washcloth lies on the ground. It has a red stain on it.",
                            {
                                   "touch": "The washcloth is soft except for where the blood has started to dry.",
                                   "taste": "You lick the washcloth and notice the metallic taste of blood.",
                                   "smell": "The washcloth has a strange, unfamiliar metallic scent. Is that blood?",
                                   "listen": "You hear nothing."
                            },
                            True)

       sys.add_obj(O06)

       # Alice Stone (P01)
       P01 = person.Person("P01", "Alice Stone",
                            "Alice Stone turns her head to meet your gaze as you look at her. The bright sunlight from "
                            "the window clearly illuminates her face, revealing her swollen eyes and red, blotchy skin "
                            "from crying. She dabs the corner of her eyes with a tissue before turning back to the "
                            "window.",
                            "Alice Stone stands in the corner of the room, gazing out the window and quietly sobbing.",
                            {
                                   "ask": {
                                   "P02": "You ask Alice about Adam. "
                                          "Alice sighs softly before answering. 'Norman and Adam's relationship was... "
                                          "complicated, to say the least. They had your typical disagreements "
                                          "about who should inherit the house and Norman's business. "
                                          "Norman wanted Adam to stay here and take over the business, but Adam wanted "
                                          "to forge a new path on his own. Norman loved Adam dearly though, and I "
                                          "believe that deep down Adam loved his father too.",
                                   "P03": "You ask Alice about Sam. "
                                          "Alice waves her hand dismissively. 'He's a little shady, if you ask "
                                          "me, but, quite frankly, I haven't had much time to get to know the retreat "
                                          "participants after what happened.'",
                                   "P04": "You ask Alice about Al. "
                                          "Alice's face lights up slightly. 'He can be quite the miserable old "
                                          "character, but I like Al. He's been a loyal employee of Norman's for over "
                                          "twenty years.'",
                                   "P05": "You ask Alice about Heather. "
                                          "Alice shrugs her shoulders dismissively. 'She seems like any other retreat "
                                          "participant to me.'",
                                   "P06": "You ask Alice about Ava. "
                                          "'Ava Scarlett is her name, right?' Alice asks. 'The woman straight up "
                                          "glared at me like I had killed her dog when she arrived here. Gave me a really "
                                          "bad vibe.'",
                                   "F01R01": "You ask Alice about Norman. " 
                                          "At the very mention of him, Alice begins to sob heavily. She "
                                          "waves you away, indicating that she wants to be left alone.",
                                   "O01": "You show the candlestick to Alice. "
                                          "Alice looks at the candlestick with a vague disinterest. 'That looks like it "
                                          "belongs in the foyer downstairs,' she mumbles. She pauses and then eyes you "
                                          "suspiciously. 'Please don't tell me you're using this as an opportunity to "
                                          "steal items from a dead man.'",
                                   "O04": "You ask Alice about the envelope with the code written on it. "
                                          "'I vaguely recall Norman mentioning something about a safe,' she tells "
                                          "you. 'I believe it was on the bottom floor, although I can't be entirely "
                                          "certain. He didn't share its exact location with me.'",
                                   "O05": "You ask Alice about the earring. "
                                          "Alice examines the earring, but avoids touching it. "
                                          "'There's no way that's mine,' she says. 'I'm allergic to silver.'",
                                   "O06": "You ask Alice about the washcloth. "
                                          "Alice recoils when you show her the blood stains. 'Is that... "
                                          "his blood?' she asks, her voice barely a whisper. When you tell her that it "
                                          "was found in her room, she squints her eyes. 'Do you...? Do you think... "
                                          "that I did it?' When you don't answer, she responds angrily. 'Norman meant "
                                          "the world to me. I won't be subjected to such accusations.' She looks away, "
                                          "indicating that the conversation is over.",
                                   "O09": "You ask Alice about the letter. "
                                          "'Norman had mentioned that one of his exes was still trying to get back "
                                          "together with him,' Alice tells you after reading the letter. 'Although he "
                                          "never mentioned that she was this serious. This woman sounds obsessed.' "
                                          "She thinks for a moment. 'What was the name of that one retreat "
                                          "participant downstairs? Ava, right? If I recall correctly, he "
                                          "dated a woman who went by that name many years ago, although it could just "
                                          "be a coincidence.'",
                                   "O11": "You ask Alice about the will. "
                                          "Alice's lips purse when you mention that she will inherit everything. You "
                                          "find her expression hard to read. 'Does Adam know?' she asks with a little "
                                          "fear in her voice. 'I knew that Norman had changed it,' she states after "
                                          "you press her on the matter, 'but it was entirely Norman's decision. I even "
                                          "urged him not to change it, knowing that it would ruin the relationship "
                                          "between him and Adam, but Norman was stubborn.'",
                                   "O12": "You show the FBI badge to Alice. "
                                          "Alice's face turns white when you show her the FBI badge. 'Where did you "
                                          "find that?' she asks, clearly agitated. You attempt to question her "
                                          "further, but she refuses to provide you with any additional information."
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

       sys.add_person(P01)

       # MASTER BEDROOM (R14)
       R14 = room.Room("R14", "Master Bedroom",
                     "You enter a large, dark bedroom with velvet curtains that are partially closed. In the dim light, "
                     "you can see that the floors, walls, and furniture are made from the same dark reddish wood. "
                     "The room has a very old feel to it, like it was designed in the 17th century. A large canopy bed "
                     "resides in the center of the room. "
                     "To your west is the hallway from which you came.",
                     "You enter a large, dim bedroom that looks like it was designed in the 17th century. "
                     "To your west is the hallway from which you came."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R14.set_connections({"west": "R11" # hallway
                            })

       R14.set_features(["F01R14", # bear head wall mount
                         "F02R14"  # nightstand
                         ])

       R14.set_objects(["O09" # love letter
                        ])
       
       # Set the interactions
       R14.set_interactions({
              "search": "You search the room but find nothing of note. You may want to search the nightstand if you "
                        "have not already.",
              "touch": "Perhaps try touching one of the features that you observe within the room.",
              "taste": "Why is it that you want to taste everything?",
              "smell": "The room has a musky smell to it.",
              "listen": "The room is silent."
              })

       sys.add_room(R14)

       # Bear Head Wall Mount (F01R14)
       F01R14 = feature.Feature("F01R14", "Bear Head Wall Mount",
                                   "You stride over to the large bear head that is mounted on the wall and stand under "
                                   "it, gazing up at its intimidating face. Its expression is frozen in a ferocious snarl, "
                                   "its large teeth bared, and black eyes as impenetrable as a moonless night. You "
                                   "consider yourself to be the rational and analytical type, but, for some unknown "
                                   "reason, you find yourself growing scared the longer you look at it.",
                                   "A large bear head is mounted on one of the walls.",
                                   {
                                   "search": "Looking around the mounted bear head reveals nothing.",
                                   "touch": "You reach up and touch the bear's fur. It feels rough.",
                                   "taste": "The bear head is mounted too high on the wall for you to taste it.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F01R14)

       # Nightstand (F02R14)
       F02R14 = feature.Feature("F02R14", "Nightstand",
                                   "The small nightstand is made of the same dark, red wood as the rest of the "
                                   "furniture in the room, leading you to believe that they must all be part of the "
                                   "same set, likely passed down through several generations. Its legs and borders "
                                   "feature intricately carved designs of leaves and vines. There is a pile of papers "
                                   "on top of the nightstand.",
                                   "A small nightstand made of the same dark, red wood as the rest of the furniture "
                                   "sits right next to the bed.",
                                   {
                                   "search": "You search the nightstand. You find nothing interesting among the assortment "
                                            "of items lying on top of it, but, as you comb through a pile of papers, a neatly "
                                            "folded letter sticks out to you.",
                                   "touch": "The dark red wood is smooth and clearly polished.",
                                   "taste": "The nightstand tastes like wood polish. It also tastes like dust.",
                                   "smell": "You smell nothing.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R14)

       # Letter (O09)
       O09 = object.Object("O09", "letter",
                            "The letter is neatly folded and looks otherwise unremarkable at first glance. Maybe you "
                            "should read it.",
                            "There is a neatly folded letter that looks otherwise unremarkable at first glance.",
                            {
                                   "touch": "It feels like paper.",
                                   "taste": "You lick the letter and taste... well, nothing aside from maybe a little "
                                            "ink.",
                                   "smell": "The letter has the familiar scent of paper.",
                                   "listen": "You hear nothing.",
                                   "read": "You open the letter and read the following: "
                                   "\n"
                                   "Dear Norman,\nI know it's been a long time since we last spoke but last night, "
                                   "as I was walking around the lake near my house, I couldn't stop thinking about "
                                   "our trip to Lake Tahoe and how wonderful it was. What was it, 10 years ago? That was "
                                   "one of the happiest times of my life.\nI know you think that our break up was "
                                   "for the best, and I know that our relationship could be unhealthy at times, but "
                                   "I really do think that we were meant to be together. I mean, after all, there must "
                                   "be a reason why you haven't dated anyone else after all these years.\nAnyway, "
                                   "I know that, like always, you likely won't respond to this, but I'll be in your "
                                   "area in a couple weeks for work and I was thinking that maybe I could stop by.\n"
                                   "Love,\n     A."
                            },
                            True)

       sys.add_obj(O09)

       # STUDY (R15)
       R15 = room.Room("R15", "Study",
                     "You enter a very welcoming study with walls lined with paintings, maps, and other oddities. "
                     "Several leather chairs are positioned in various parts of the room, presumably to accomodate "
                     "visitors. A large paned window provides a view to the outside. "
                     "To your west is the hallway from which you entered.",
                     "You enter a very welcoming study with walls lined with paintings, maps, and other oddities. "
                     "To your west is the hallway from which you entered."
                     )
       
       # Set the connections, features, objects, and persons (if applicable)
       R15.set_connections({"west": "R11" # hallway
                            })

       R15.set_features(["F01R15", # desk
                         "F02R15"  # bar cart
                         ])

       R15.set_objects(["O04"  # safe code envelope
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
                                   "a wooden box of what you assume must be expensive cigars near the ash tray. "
                                   "A photograph of Norman and Adam sits on one side of the desk. Norman's arm "
                                   "is wrapped over Adam's shoulder in a loving embrace, but the expression on Adam's "
                                   "face is hard to read. You observe nothing else of note on the desk. You notice a "
                                   "desk drawer that can be opened, although it appears to require a key.",
                                   "In front of the window, there's a large desk with several books and a few papers "
                                   "on top of it.",
                                   {
                                   "search": "You rummage through the papers and books on top of the desk. There's a "
                                            "book on Greek history and an electric bill, but nothing else stands out to you. "
                                            "You notice that the ashtray hasn't been emptied. You also notice a desk drawer "
                                            "that can be opened, although it appears to require a key.",
                                   "touch": "The wood that the desk is made of feels rough.",
                                   "taste": "You taste nothing.",
                                   "smell": "You smell cigar smoke.",
                                   "listen": "You hear nothing.",
                                   "open": {
                                       "unlocked": "You open the drawer and rummage through it. At the bottom of the "
                                   "drawer, you notice an envelope.",
                                       "locked": "You attempt to open the desk drawer. It is locked. "
                                       "(Hint: If you've found the key to this object, try 'use [key] on [object]' "
                                       "in order to unlock it)",
                                       "obj_ids": ["O04"]
                                   },
                                   "use": {
                                       "O02": "You take the small rusty key out of your pocket and insert it into the lock "
                                              "on the drawer. It fits perfectly. The drawer appears to be unlocked now.",
                                   },
                                   },
                                   False)

       F01R15.add_condition(False)

       sys.add_feature(F01R15)

       # Bar Cart (F02R15)
       F02R15 = feature.Feature("F02R15", "Bar Cart",
                                   "The antique bar cart looks like it is made of brass and may be several centuries "
                                   "old. Several bottles and decanters of liquor, a few of which are only partially "
                                   "full, and some crystal tumblers, are on the top shelf. One of the whiskey "
                                   "decanters has its stopper removed. There's a dirty tumbler beside it.",
                                   "An antique bar cart is beside the desk.",
                                   {
                                   "search": "You search the bar cart but don't find anything aside from a few "
                                            "expensive-looking bottles of liquor and crystal tumblers.",
                                   "touch": "The bar cart feels slightly cool.",
                                   "taste": "You open a bottle of whiskey and take a sip. It burns as it goes down "
                                            "your throat.",
                                   "smell": "You open a bottle of whiskey and sniff it. It smells sharp and burns "
                                            "the inside of your nose.",
                                   "listen": "You hear nothing."
                                   },
                                   False)

       sys.add_feature(F02R15)

       # Safe Code Envelope (O04)
       O04 = object.Object("O04", "envelope",
                            "The envelope is dirty and looks like it was crumpled at one point. Four "
                            "numbers are written across it in thick ink. Perhaps you should read it?",
                            "A dirtied envelope with something written on it catches your attention.",
                            {
                                   "touch": "The envelope is rough where it had been previously folded.",
                                   "taste": "You taste the dirtied envelope. It tastes like paper.",
                                   "smell": "The envelope has the slight smell of cigar smoke.",
                                   "listen": "You hear nothing.",
                                   "read": "In thick ink, the envelope reads: 0123."
                            },
                            True)

       O04.add_condition(False)

       sys.add_obj(O04)

       # Adam Bates (P02)
       P02 = person.Person("P02", "Adam Bates",
                            "Adam Bates raises his eyebrows and adjusts his glasses when he senses you looking at him. "
                            "He appears to be in his late 30s or early 40s. His brown hair is messy, and his "
                            "eyes look sad. 'Can I help you?' he asks.",
                            "Adam Bates is bent over the top of the desk, going through the papers on the desk. He "
                            "quickly straightens up and moves to a nearby bookcase, picking up a book, when you enter. "
                            "He begins flipping through the book absentmindedly.",
                            {
                                   "ask": {
                                   "P01": "You ask Adam about Alice. "
                                          "'Alice and my father have been dating for a few years,' Adam says. 'She "
                                          "started out as just his assistant, but then I guess they grew closer. I have mixed "
                                          "feelings about her. On the one hand, she's been good for my father in many ways. "
                                          "On the other hand, I feel that they grew too close too quickly and, when there's "
                                          "money involved, you can never be completely sure of a person's intentions, "
                                          "you know?'",                                       
                                   "P03": "You ask Adam about Sam. "
                                          "'Sam Smith is his name, right?' Adam says.'To be honest, he's a little "
                                          "suspicious, and I noticed that he mentioned nothing about occupation when "
                                          "we spoke. That being said, I don't know much about him.'",
                                   "P04": "You ask Adam about Al. "
                                          "'Truth be told, my father probably didn't treat him as well as he should have,' "
                                          "Adam tells you. 'But Al was always loyal, maybe even too loyal...'",
                                   "P05": "You ask Adam about Heather. "
                                          "'Ah, Heather Poirot,' Adam says. 'I didn't get much of an opportunity to "
                                          "speak with her, but I got the sense that she came here with a purpose. As far "
                                          "as what that purpose may be, your guess is as good as mine...'",
                                   "P06": "You ask Adam about Ava. "
                                          "'She looks very familiar to me,' Adam says, 'but, for the life of me, I "
                                          "can't entirely place her. I think my father may have known her years ago...'",
                                   "F01R01": "You ask Adam about Norman. " 
                                          "Adam grimaces when he hears you say his father's name. 'He wasn't the "
                                          "best father,' Adam admits. 'He wasn't exactly there for me when I was younger, "
                                          "and we didn't get along. For years, I wished the old man would just pass away "
                                          "so I could live my life without forever being weighed down by his presence in "
                                          "my life.' Adam pauses, as if deliberating over something. After a few "
                                          "moments, he continues. 'To be honest, we got into an argument this morning. The last "
                                          "words I said to him were... well, let's just say that they weren't that kind.' "
                                          "Adam's expression changes to one of sorrow and regret. He clears this throat and "
                                          "turns away.",
                                   "O01": "You ask Adam about the candlestick. "
                                          "'That candlestick is part of a set that my father inherited,' Adam says. "
                                          "'I'm not sure how long it's been in our family.'",
                                   "O04": "You ask Adam about the envelope with the numbers written on it. "
                                          "'Looks like a safe combination,' Adam says. 'I don't recall my father "
                                          "having a safe anywhere, although I wouldn't be surprised if he kept one "
                                          "hidden from me.' He narrows his eyes and repeats the numbers under his "
                                          "breath as if commiting them to memory.",
                                   "O05": "You ask Adam about the earring. "
                                          "Adam looks at the earring with clear disinterest. 'I don't recognize it,' "
                                          "he says.",
                                   "O06": "You ask Adam about the washcloth. "
                                          "Adam winces ever so slightly when you show him the blood-stained washcloth. "
                                          "'So that's his blood, eh?' he asks, although it's more of a statement. When you "
                                          "give him a suspicious look, he raises his hands defensively. 'Hey, I had nothing "
                                          "to do with it. You mentioned that you found it in Alice's room though?' He rubs his "
                                          "chin thoughtfully. 'I wonder if...' He shakes his head. 'Nah...'",
                                   "O09": "You show the letter to Adam. "
                                          "Adam takes the letter and quickly looks over it. 'My father has dated a lot "
                                          "of women over the years,' he says, 'but I don't recall him mentioning anyone other "
                                          "than Alice recently. From the looks of it, it sounds like this woman was obsessed.' "
                                          "He pauses for a moment to think. 'You don't think that woman downstairs was the "
                                          "the one who sent this, do you?' He shakes his head. 'Nah, probably not. Although "
                                          "I swear she looks familiar...'",
                                   "O10": "You show the torn page to Adam. "
                                          "Adam's cheeks turn red when he looks at the page. You notice him "
                                          "clenching his fists so tightly that his knuckles turn white. 'Alright,' he "
                                          "says. 'I had a hunch that my father might be changing his will sometime "
                                          "soon, what with him and Alice being so close and all. That didn't sit right "
                                          "with me. After all, the estate has been in our family for many generations. "
                                          "I saw that plant in a book and thought I remembered seeing it in the garden.' "
                                          "Adam pauses, and takes a deep breath. 'So I poisoned his food. The man "
                                          "had it coming. He was an utterly worthless father and a terrible human "
                                          "being. But, at the last minute, we got into an argument, and I confessed "
                                          "what I had done to him. He stormed off, and that was the last time I saw "
                                          "him alive. He didn't eat the food though, so that's not what killed him.'",
                                   "O11": "You ask Adam about the will. "
                                          "Adam's interest is clearly piqued when you mention the will. 'What's that?' "
                                          "he asks. 'You found it?' When you tell him that Alice stands to inherit everything, "
                                          "he slams his fist down on the desk. 'That weasel,' he says. 'Leave it to him to "
                                          "do something as backstabbing as disinheriting his own son. And here I was feeling "
                                          "sorry that he had died. I should have killed him when...' Realizing that he may "
                                          "have said too much, Adam suddenly stops speaking.",
                                   "O12": "You show the FBI badge to Adam. "
                                          "He seems slightly startled at the sight. 'That's "
                                          "concerning,' he states, lowering his voice. 'To be completely honest with you, "
                                          "I suspect that my father, well, may have gotten into some trouble with the IRS if "
                                          "you catch my drift. Although I was never one-hundred percent sure. He wouldn't "
                                          "talk about it when I brought it up. Either way, it looks like something caught up "
                                          "to him. My guess is that one of the retreat participants is here undercover.' He "
                                          "eyes you suspiciously. 'You wouldn't happen to be an undercover FBI agent, "
                                          "would you?'",
                                   "F01R15": "You ask Adam about the desk. "
                                          "'My father kept a lot of important papers in there,' he says. 'Let me know if "
                                          "you find anything of interest.'",
                                   "F02R15": "You ask Adam about the bar cart. " 
                                          "Adam shrugs. 'My father liked to drink,' he simply says."
                                   },
                                   "search": "Adam doesn't seem like the type of person that would let you search him.",
                                   "touch": "You place your hand on Adam's shoulder. He looks up, pats it awkwardly, "
                                            "and then returns to reading.",
                                   "smell": "You near Adam and smell him. He smells slightly of alcohol.",
                                   "listen": "Adam sighs sadly and turns the page of the book that he's reading."
                            })

       sys.add_person(P02)

       # Save top floor base game files
       sys.save_base_game_files()
