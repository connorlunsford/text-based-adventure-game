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

    # creates the patio
    R06 = room.Room("R06", "Patio",
                    "The patio and pool deck look fit for a party. Lounge chairs are lined up along "
                    "the south edge of the pool. A small dining area is on the southeast corner of the patio, "
                    "complete with a massive umbrella to provide shade from the sun. Let's not forget about the pool. "
                    "It sparkles and shimmers and looks so inviting. Maybe when all of this is over "
                    "you can go for a nice swim. \n"
                    "To the west are french doors that appear to go into the living room. The doors are locked. "
                    "To the north is a pool house. It doesn't look like it's currently being used. "
                    "These doors are also locked. \n"
                    "To the east is the garden. It looks rather beatiful from here. There seem to be "
                    "some outbuildings on the far edges of the garden, but you can't quite tell from here what they are. "
                    "There are some muddy footprints coming out of the garden, maybe they deserve a closer look. \n"
                    "To the south are french doors that will take you back into the house via the library.",
                    "You are on the patio with a dazzling pool and ample seating for lounging or dining. "
                    "To the west is the locked door into the living room, the library is to the south, "
                    "to the east is the garden, and to the north is the pool house."
                    )
    
    # Set the connections
    R06.set_connections({"south": "R03", # library
                        "east": "R07", # garden
                        })

    # Set the features
    R06.set_features(["F01R06" # muddy footprints
                    ])

    # set the people in the room
    R06.set_people(['P03',  # Sam Smith (shady retreat participant)
                    ])                    
    
    # Set the interactions
    R06.set_interactions({
            "search": "The pool is well maintained and the patio is quite clean. There's nothing of note here, "
            "aside from those muddy footprints...",
            "touch": "The pool water is quite chilly. Maybe you'll rethink that swim later. ",
            "taste": "You taste the pool water. Salty. Interesting choice.",
            "smell": "Aah...fresh air. There's a faint smell of something floral being carried by the breeze. "
            "Probably something in the garden.",
            "listen": "You hear the relaxing sounds of the breeze rustling the trees and the birds singing away. "
            "Too bad this situation is anything but relaxing. Wait, what's that? It sounds like a faint mumbling "
            "in the distance. It's coming from the direction of the footprints."
            })

    sys.add_room(R06)

    # Muddy Footprints (F01R06)
    F01R06 = feature.Feature("F01R06", "Muddy Footprints",
                                "You follow the muddy footprints. The prints are close together so it doesn't appear "
                                "this person was in any hurry. You reach the end of the footprints and find one of the other guests. "
                                "You think his name is Sam. He's acting shady, as usual. "
                                "You wonder what he's doing lurking around out here. ",
                                "The muddy footprints lead to Sam, another retreat guest. He's acting a bit shady and is "
                                "avoiding eye contact.",
                                {
                                "search": "There is nothing else to see here.",
                                "touch": "The mud are still wet. ",
                                "taste": "Tastes like what you've always assumed mud tastes like. ",
                                "smell": "Smells...like mud.",
                                "listen": "What do you really expect to hear from footprints?"
                                },
                                False)

    sys.add_feature(F01R06)

    # gloves (F02R06)
    F02R06 = feature.Feature("F02R06", "Gloves",
                                "You follow the muddy footprints. The prints are close together so it doesn't appear "
                                "this person was in any hurry. The footprints lead directly to Sam. "
                                "He's acting shady, as usual. You wonder what he's doing lurking around out here. ",
                                "The muddy footprints lead to Sam, another retreat guest. He's acting a bit shady and is "
                                "avoiding eye contact.",
                                {
                                "search": "There is nothing else to see here.",
                                "touch": "The mud are still wet. ",
                                "taste": "Tastes like what you've always assumed mud tastes like. ",
                                "smell": "Smells...like mud.",
                                "listen": "What do you really expect to hear from footprints?"
                                },
                                False)

    sys.add_feature(F02R06)

    # P03 Sam Smith (shady retreat participant)

    P03 = person.Person('P03', 'Sam Smith',
                        'You see Sam Smith. He\'s open about his past. Says he used to get into trouble a lot. '
                        'Mostly just burglaries he said. He says he\'s changed his ways but you\'re not sure you '
                        'believe him. "Sam Smith" certainly sounds like a made up name. He\s probably early 30s '
                        'good looking in a rugged, bad boy kind of way. You can see how he might be able to '
                        'manipulate people into trusting him. It looks like something sticking out of his pocket. '
                        '"What is that?" you try to figure out. Gloves perhaps? Well, he is acting kind of guilty. Of what though '
                        'you\'re not quite sure. He\'s been acting like that since you got here. '
                        'You might want to keep an eye on him.',
                        'Sam Smith is acting shifty, as usual.',
                        {
                            'ask': {
                                'P01': "You question Sam about Alice. He responds: 'Is that the broad, I mean lady, that lives here? "
                                       "She seems nice enough, pretty broken up about what happened. Not sure what else "
                                       "I can say about her.' ",
                                'P02': "You question Sam about Adam, the victim's son. 'Seems pretty jealous of his old "
                                       "man's money if you ask me. Can't say I blame him though. I heard his dad keeps "
                                       "all his money in the house, right under the kid's nose and he can't even touch it. "
                                       "Doesn't trust banks or something like that, the old kook.' ",
                                'P03': "You question Sam about himself. He seems exasperated, 'Man, why's everyone always "
                                       "suspecting me? I told you guys I've gone straight. Nothing to hide.' ",
                                'P04': "You ask Sam about the groundskeeper. Sam responds 'That old guy? He sure does love "
                                       "his plants. He saw me in the garden and threatened me if I picked any of his "
                                       "precious flowers. What's the big deal if I pick a few? He's got plenty.'",
                                'P05': "You question Sam about Heather. He gets a far off look 'She's kind of mysterious, isn't "
                                       "she. She doesn't talk much but you can tell the wheels are always turning. A tall "
                                       "drink of water for sure, just my type.' ",
                                'P06': "You ask Sam about Ava. 'Something about her doesn't sit well with me. Too full of "
                                       "herself. And it's strange, she says it's the first time she's been here but she "
                                       "seems awfully familiar with the place. I thought I saw her poking around in the "
                                       "pantry earlier. Like she lives here or something...' ",
                                'F01R01': "You question Sam about the victim. 'I never met him before. I've heard stories "
                                          "in town though. They say he's a bit eccentric, doesn't trust the government or banks, "
                                          "keeps all his money stashed around the house like hidden treasures. I thought "
                                          "it would be fun to check the place out myself.' He stammers a bit, 'I mean, "
                                          "not that I'd look for the money or take it or anything, I just wanted to see what "
                                          "the guy was like in person.'",
                                'F01R06': "You ask Sam about the muddy footprints. What was he doing in the garden anyway? "
                                          "He acts guilty. 'I was just enjoying the garden, honest.' He fidgets a little more "
                                          "and you wait, it seems like there's more he wants to say but he stays silent. ",
                                'F02R06': "You ask Sam about the gloves in his pocket. 'The what? Oh, these. I ... uh ... "
                                          "ok fine, took them from the shed. I wanted to surprise Heather with some roses "
                                          "from the garden. I didn't want to get cut up by those pesky thorns.' ",
                                'F01R10': "You ask Sam about the broken pots in the greenhouse. 'Yeah, that was me. I was "
                                          "just looking through the flowers and accidentally dropped one of the pots. It "
                                          "fell on a few other pots and broke them to. I panicked and ran. I didn't want"
                                          "to face the wrath of the gardener. His plants are like his babies.'",
                                'O01': "You ask Sam about the candlestick. 'Candlestick? What candlestick? I don't know "
                                        "anything about a candlestick.'",
                                'O06': "You ask Sam about the bloodied washcloth. 'I've never seen that before. Where'd"
                                       "you find it?' Clearly, he's not going to tell you anything useful.",
                                'O08 ': "You ask Sam about the garden shears found in the greenhouse. 'I got them from the "
                                        "shed. I was going to use them to cut some flowers, but dropped them when I "
                                        "was startled and just left them there.'",                                       
                                'O12': "You question Sam about the FBI badge. 'Huh. I knew the owner was strange. I bet "
                                       "he's being investigated for something crazy!' "
                            },
                            'search': "You ask Sam if he's found anything interesting. 'Nope, I've just got these "
                                      "gloves here in my pocket.'",
                            'touch': "Sam smacks your hand away. 'What are you doing? Don't touch me! Geez, what's wrong "
                                     "with you?'",
                            'smell': "You try to be subtle as you lean towards Sam and sniff. A mix of sweat and strong "
                                     "cologne. 'Note to self: don't get too close to him again' you think to yourself.",
                            'listen': "You hope Sam will start talking just to fill the awkward silence but he just"
                                        "looks at you expectantly."
                        })

    sys.add_person(P03)

    # Garden (R07)
    R07 = room.Room("R07", "Garden",
                    "As you enter the garden you have to stop to take it all in. 'Wow' you think, 'this garden is "
                    "amazing!' A maze of flowers and plants lies before you, all immaculately manicured and cared for.  "
                    "It seems every color of the rainbow is represented through beautiful flowers. A particularly beautiful "
                    "purple flower in the far corner catches your eye. As you start to head that way to get a better look "
                    "you spot something shiny down another path. 'Well that seems out of place' you think to yourself.\n"
                    "To the north you see a large greenhouse. In the northeast corner is the gardener's tool shed. The gateway "
                    "to the west will return you to the patio.\n"
                    "There's so much to see you don't know which way to go first. ",
                    "You enter an immaculately manicured garden. Beautiful purple flowers and something shiny catch your eye. "
                    "To the north is a greenhouse and a shed is to the northeast. Going west will return you to the patio. "
                    )
    
    # Set the connections, features, objects, and persons (if applicable)
    R07.set_connections({"west": "R06", # patio
                        "north": "R10", # greenhouse
                        "northeast": "R09", # gardener's shed
                        })

    R07.set_features(["F01R07" # wolfsbane/purple flowers
                        ])

    R07.set_objects(["O10",  # drawing/page from book about wolfsbane
                    "O13",  # FBI badge
                    ])
    
    # Set the interactions
    R07.set_interactions({
            "search": "You wander around the garden slowly, taking it all in. You see what appears to be a crumpled "
                "paper on one path, perhaps a page torn from a book? Oh wait, what's that? The sun glimmers "
                "off a shiny object down another path. 'Well that seems out of place' you think.",
            "touch": "You delicately touch some of the flowers as you pass. Ouch! A thorn. ",
            "taste": "So many options! Do you really think eating random plants and flowers will help you?",
            "smell": "Ah, such a wonderful fragrance from all of the flowers. But wait, is that a trace of a woman's "
                "perfume you smell? Someone else has been here recently.",
            "listen": "The sound of a light breeze blowng through the trees that surround the garden is so relaxing. "
                "You could spend hours in here, it's so peaceful. That is, if you didn't have a murder to solve."
            })

    sys.add_room(R07)

    # wolfsbane/purple flowers (F01R07)
    F01R07 = feature.Feature("F01R07", "Wolfsbane",
                                "The leaves are dark green with sharp, almost tooth-like points around the perimenter. "
                                "The shape of the deep purple flowers remind you of a medieval helmet, domed across "
                                "the top longer in the back.",
                                "The plant has dark green leaves and deep purple, helmet-like flowers. ",
                                {
                                "search": "There is nothing else here. This plant seems to be separate from the rest. ",
                                "touch": "You reach out to touch the beautiful flowers but something makes you hesitate. ",
                                "taste": "Tasting such a random mysterious plant seems risky. You change your mind. "
                                "Better safe than sorry.",
                                "smell": "Hmm, for such a lovely flower you'd expect a lovely scent, but nope, nothing. ",
                                "listen": "Listen to a plant? Really? People talk to plants but it doesn't usually work "
                                "the other way around."
                                },
                                False)

    sys.add_feature(F01R07)

    # drawing/page from book about wolfsbane (O10)
    O10 = object.Object("O10", "drawing of Wolfsbane",
                        "The paper has gotten wet from the irrigation system so you can't quite make out what was "
                        "on the page. It looks like it may have been a picture with some text. There are faint "
                        "purple and green colors and you can make out part of a word, 'Wolfs'-something. Definitely "
                        "looks like a page torn out of a book or notebook, you decide.",
                        "A page torn from a book which had a picture of something green and purple and the incomplete "
                        "word 'Wolfs-'.",
                        {
                                "touch": "It is still damp as the flowers were recently watered.",
                                "taste": "Tastes like...damp paper. No surprise there.",
                                "smell": "Smells like...damp paper. No surprise there.",
                                "listen": "Are you really expecting to hear something from a piece of paper? Mmm-kay..."
                        },
                        True)

    sys.add_obj(O10)

    # FBI badge (O13)
    O13 = object.Object("O13", "FBI badge",
                        "The gold shiny object is partially buried in the dirt, like someone may have stepped on it. "
                        "You wipe the dirt away and see 'F...B...I'. It's an FBI badge! Where did that come from?! ",
                        "A shiny object is partially buried in the dirt. It's an FBI badge'.",
                        {
                                "touch": "It's hard metal. Probably the real thing.",
                                "taste": "It tastes like metal...and dirt.",
                                "smell": "Dirt. Definitely smells like dirt. But wait...is that a trace of a woman's "
                                "perfume too?",
                                "listen": "I don't think the badge is going to tell you anything. You're on your own."
                        },
                        True)

    sys.add_obj(O13)    

    # Garage (R08)
    R08 = room.Room("R08", "Garage",
                    "You enter a large garage. This thing is huge! There's only one car though, "
                    "a vintage VW van that looks like it's kept immaculate. In the back corner there is a large "
                    "storage closet. A workbench along the far wall looks very orderly with tools. To the east is "
                    "the door back into the kitchen. To the north is the back door. It opens onto a paved path that "
                    "will take you around the back of the house to the patio. To the south are the main garage doors. "
                    "There's a fancy looking keypad though, and no button in sight. It appears you need a code to "
                    "open the doors from inside. ",
                    "You enter a large well-kept garage with a vintage VW and a large storage closet. To the east is "
                    "the kitchen and to the north is a path that leads to the patio."
                    )
    
    # Set the connections, features, objects, and persons (if applicable)
    R08.set_connections({"east": "R02", # kitchen
                        "north": "R06" # patio
                        })

    R08.set_features(["F01R08", # storage closet
                    "F02R08"  # VW van
                        ])

    R08.set_objects(["O01" # candlestick (murder weapon)
                    ])
    
    # Set the interactions
    R08.set_interactions({
            "search": "You search the garage but everything seems quite orderly. Perhaps you should check the storage closet. ",
            "touch": "Touch what, exactly?",
            "taste": "It doesn't seem quite safe to taste things in the garage.",
            "smell": "Hmm, that's odd. There's a slight smell of exhaust. You didn't think anyone had come or gone recently.",
            "listen": "Just the hum of the overhead lights."
            })

    sys.add_room(R08)

    # storage closet (F01R08)
    F01R08 = feature.Feature("F01R08", "storage closet",
                                "Ah, so this is where they hide all the junk. It's the complete opposite of the orderly "
                                "garage. Shelves full of old and musty smelling boxes. Piles of random things covering "
                                "the floor. Complete disarray. 'How can they even find anything in here' you wonder. ",
                                "A closet full of what appears to be old, forgotten junk...all but that shiny candlestick...",
                                {
                                "search": " Seems like your first impression was right, just a bunch of junk. But just "
                                "as you're about to close the door you notice a nice, shiny candlestick tucked between "
                                "some of the boxes on the shelf. 'Well that seems out of place' you muse.",
                                "touch": "Dust covers almost every surface.",
                                "taste": "Tastes like dust and...old stuff.",
                                "smell": "It's smells like your grandmother's musty old attic.",
                                "listen": "You hear nothing."
                                },
                                False)

    sys.add_feature(F01R08)

    # VW van (F02R08)
    F02R08 = feature.Feature("F02R08", "VW van",
                                "The VW van is every hippie's dream. You've always wanted one of these. You wonder "
                                "what will happen to this old antique now that the owner's dead. The son probably "
                                "wouldn't appreciate it, you think sadly. It seems to be well taken care of and loved. ",
                                "The VW van looks in good condition.",
                                {
                                "search": "The doors are locked but you peer through the windows. Either it's been "
                                "restored lately or it's been very well taken care of. Nothing seems to be out of "
                                "place inside. There seems to be a slight oil leak, there's a stain underneath on "
                                "the garage floor",
                                "touch": "The hood is slightly warm. Someone must have driven it recently.",
                                "taste": "I'm not sure why, but you lick the van. There's a metallic tang like you might "
                                "expect, but nothing else.",
                                "smell": "Just a slight smell of exhaust.",
                                "listen": "I'm sure the van has plenty of stories to tell, if it could talk. Too bad it's "
                                "just a van."
                                },
                                False)

    sys.add_feature(F02R08)

    # Candlestick (O01)
    O01 = object.Object("O01", "Candlestick",
                        "The shiny candlestick definitely looks out of place here, as if it's just been cleaned or "
                        "polished. It doesn't match the rest of the old and dusty items in the closet.",
                        "The shiny candlestick looks out of place in the dirty old closet.",
                        {
                                "touch": "It's clean, not dusty at all like everything else.",
                                "taste": "You lick the candlestick and think you taste bleach.",
                                "smell": "The candlestick smells faintly of bleach, or some other cleaning substance.",
                                "listen": "The candlestick doesn't make noise, silly, it's a candlestick."
                        },
                        True)

    sys.add_obj(O01)

    # Gardener’s shed (R09)
    R09 = room.Room("R09", "Gardener’s shed",
                    "You enter the shed. It seems quite orderly for a tool shed. The walls are made up of pegboard "
                    "and have labeled spots for various tools of all sorts. You've never seen such an organized shed.",
                    "The shed is well organized with a wide array of tools."
                    )
    
    # Set the connections, features, objects, and persons (if applicable)
    R09.set_connections({"west": "R07" # garden
                        # TODO: add secret back staircase to master bedroom, if it gets implemented
                        })

    R09.set_features(["F01R09" # missing tool
                        ])

    R09.set_objects(["O07" # receipt
                    ])

    R09.set_people([
        'P04'  # Gardener
    ])                    
    
    # Set the interactions
    R09.set_interactions({
            "search": "You search the shed. It seems a tool is missing from its spot on the pegboard wall "
            "and a drawer is slightly open. Nothing else seems out of place.",
            "touch": "What exactly would you like to touch?",
            "taste": "Considering there are fertilizers and such in here, I would advise against tasting anything.",
            "smell": "The room smells of soil, mulch, and oil. Seems pretty typical for a garden shed.",
            "listen": "The room is silent save for the nervous mumblings of the gardener."
            })

    sys.add_room(R09)

    # missing tool (F01R09) 
    F01R09 = feature.Feature("F01R09", "Missing Tool",
                                "The empty spot on the pegboard is labeled 'large garden shears'. Based on the "
                                "size of the empty space, you imagine they're pretty large and probably heavy. They could "
                                "probably do some bodily harm.",
                                "A large set of gardening shears are missing from the shed.",
                                {
                                "search": "A scan of the wall confirms that nothing else is out of place.",
                                "touch": "You touch the empty spot. Maybe you can sense what happened to the missing tool. "
                                "Just kidding, you're not psychic.",
                                "taste": "They're missing, remember? Nothing here to taste.",
                                "smell": "They're missing, remember? Nothing here to smell.",
                                "listen": "They're not here, but even if they were, they're not talking."
                                },
                                True)

    sys.add_feature(F01R09)

    # receipt (O07)
    O07 = object.Object("O07", "Receipt",
                        "The receipt seems fresh, the print is still nice and dark, not really any wrinkles to indicate "
                        "age or wear.",
                        "A receipt appears to be from a recent purchase.", 
                        {
                                "touch": "It feels like paper.",
                                "taste": "A bit salty, Al must be sweating.",
                                "smell": "If you try really hard, you think you smell fresh ink.",
                                "listen": "You hear nothing.",
                                "read": "You look at the receipt and read the date, time, and store address. It's from today, "
                                "all right. You're somewhat familiar with the area and know there's no way Al would have been "
                                "able to make this purchase then then get back to the house in time to kill the victim before "
                                "you arrived."
                        },
                        True)

    sys.add_obj(O07)

    # P04 Al Weatherby
    P04 = person.Person('P04', 'Al Weatherby',
                        "Al is acting rather nervous. Pacing and muttering to himself. You try to get a good read on him "
                        "without appearing to stare. He's probably in his 60s, tanned and weathered looking. Makes sense "
                        "since he's worked here for so long and spent so much time outside caring for the garden. You know "
                        "he takes great pride in his work and loves what he does. His hands are dirty, dirt caked under his "
                        "nails. You'd expect as much, there doesn't appear to be any blood though.",
                        "The gardener, Al, is acting nervous muttering about he 'doesn't know what he's going to do now'.",
                        {
                            'ask': {
                                'P01': "You ask Al about Alice. 'Poor kid. She was always nice enough to me, treated me with "
                                "kindness. She's pretty broken up about losing Norman. Hopefully she'll keep me on if "
                                "she inherits this place. I know that's selfish to think about myself at a time like this "
                                "but I've been here so long, I don't know what else I'd do. Not like he ever payed me enough "
                                "to be able to retire and take it easy.'",
                                'P02': "You ask Al about Adam. 'That kid and his dad never got along, all they did was argue "
                                "about money. Adam wanted it and Norman didn't want to give him handouts. If he inherits this "
                                "place I'm a goner for sure. He'd fire me just out of spite for his dad. I hate to even think "
                                "about what will happen to my beautiful gardens.'",
                                'P03': "You mention Sam and Al starts to get agitated. 'He's trouble if you ask me. I caught him " "snooping around the garden earlier, looking guilty as ever. I don't know what he was doing but "
                                "I told him if he messes with any of my plants he'll have me to deal with. I thought I saw him "
                                "around my greenhouse earlier too. There's just no reason for him to go in there.'",
                                'P04': "You ask Al about himself. 'What do you want to know? Seems like I've worked here my whole "
                                "life. I love this garden, spend more time here than I do at my own home. The stingy old man "
                                "doesn't pay me enough to have a garden like this of my own, so I put my heart and soul into "
                                "the one here.'",
                                'P05': "You ask Al about Heather. 'Can't say I really know anything about her. I just met her "
                                "briefly after she arrived, showed her around the garden a little.'",
                                'P06': "You question Al about Ava. 'You know, there's something familiar about her but I can't "
                                "quite put my finger on it. I don't really interact with the retreat participants too much "
                                "unless they want a guided tour of the gardens. I love to talk about my plants.'",
                                'F01R01': "You ask Al about Norman and he seems to get frustrated. 'All the work I do for him, "
                                "keeping his gardens in immaculate shape and he never showed any appreciation. I wouldn't "
                                "still be here if I didn't love what I do so much.'",
                                'F02R08': "You ask Al about the van being used recently. 'Oh yeah, I ran out to the gardening "
                                "center to get some supplies earlier. The boss let me use his van. See, here's my receipt.' Al "
                                "holds the receipt out towards you then goes slightly pale, 'What if I was the last person to "
                                "see him alive when I got the keys from him? Oh man, what if I had just stuck around instead, "
                                "maybe he'd still be alive.'",
                                'F01R09': "You ask Al about the empty space on the wall, where there appears to be a large tool " "missing. 'I just came in here and found it like that. My large gardening shears are missing. "
                                "They're my good heavy-duty ones too. Knock someone over the head with those and...oh God, I "
                                "didn't mean it like that, bad choice of words.' He seems truly embarrassed by his choice of "
                                "words. 'There are some gloves missing too, not sure what somebody is getting up to with those.'",
                                'O01': "You ask Al about the candlestick. 'I don't spend much time in the house. I know there "
                                "used to be a candlestick like that in the foyer. It's been a while since I've seen it, so I'm "
                                "not sure if it's the same one, but it sure was ugly like that one you got there.'",
                                'O04': "You ask Al about the envelope with the code. 'Hmm, well that's not the garage door code, "
                                "I can tell you that much. Knowing Norman, there's probably a safe or two hidden somewhere in the "
                                "house.'",
                                'O05': "You ask Al about the earring. 'Don't know nothin' about that. I never was one for jewelry. "
                                "I don't understand guys wearing earrings, myself.'",
                                'O06': "You ask Al about the washcloth. 'Where'd you find that? It must be from the house, that's "
                                "too fancy for one of my rags.'",
                                'O08': "You ask Al about the gardening shears. 'They went missing from my shed, you can see the "
                                "spot there on the wall. I like to keep a tight ship here, everything in it's place. You can even "
                                "see where I've labled the spot.' Al points to the empty space on the wall. 'Where'd you find "
                                "them?'",
                                'O10': "You ask Al about the smudged drawing. 'Hmm, \"wolfs..\"' he starts to read. 'That looks "
                                "like it used to be a drawing of Wolfsbane. I've got one of those over in the corner of the garden."
                                "Kind of a little pet project I have going on, got interested in it after reading about it in some "
                                "folklore stories I like to read.'",
                                'O11': "You ask Al about the victim's will. 'Pfft, I'm sure I'm not in it. All the hard work I "
                                "put into this garden and Norman never seemed to appreciate it. I'd be surprised if he left me so "
                                "much as a single tool.'",
                                'O12': "You ask Al about the FBI badge. 'You say you found that in my garden? Well it wasn't there "
                                "yesterday, I can tell you that for sure. Never seen it before. '"
                            },
                            'touch': "You reach out and pat Al on the shoulder in a consoling way and he just looks at you funny. "
                            "Ew, he's rather sweaty.",
                            'smell': "You smell an interesting mix of oil from the tools and sweat from Al, not the most pleasant "
                            "combination.",
                            'listen': "You catch mutterings of 'What now?' and 'Where are they?'",
                            'search': "You ask Al if he has anything that will help with the investigation. 'Just this receipt "
                            "that shows I was out shopping when it happened.'",
                        })

    sys.add_person(P04)

    # Greenhouse (R10)
    R10 = room.Room("R10", "Greenhouse",
                    "You enter a lovely greenhouse, it's quite warm in here. The tables are full of "
                    "all sorts of plants and flowers, every color of the rainbow seems to be represented. "
                    "This must be where Al starts his new plants.",
                    "You enter a greenhouse with all sorts of plants and flowers on display."
                    )
    
    # Set the connections, features, objects, and persons (if applicable)
    R10.set_connections({"south": "R07" # garden
                        })

    R10.set_features(["F01R10", # broken flower pots
                        "F02R10" # bags of potting soil
                        ])

    R10.set_objects(["O08"  # gardening shears from shed
                    ])
    
    # Set the interactions
    R10.set_interactions({
            "search": "You walk through the greenhouse. There's an section of flowers pots that are knocked over "
            "and broken. That strikes you as very odd, not something that the gardener would do. There's a pile "
            "of bags of potting soil in the corner that also looks disturbed. The gardener seems to be the orderly "
            "sort so this also seems uncharacteristic.",
            "touch": "There are so many plants in here. What specifically do you want to touch? ",
            "taste": "There are so many plants in here. What specifically do you want to taste?",
            "smell": "It's quite fragrant. There's so many flowers you can pick out just one sent. The smell of"
            "potting soil is also quite prevalent.",
            "listen": "You hear nothing."
            })

    sys.add_room(R10)

    # broken flower pots (F01R10)
    F01R10 = feature.Feature("F01R10", "broken flower pots",
                                "There are numerous broken flower pots. You can't tell if it was intentional or an "
                                "accident. 'What a shame' you think, hopefully the gardener can still save the plants. "
                                "It seems it's just this one section with blue and purple flowers that has been disturbed. ",
                                "The section of blue and purple flowers has many broken and knocked over flower pots.",
                                {
                                "search": "You look through the broken pots. There's nothing but a mess of potting soil "
                                "and damaged plants.",
                                "touch": "The soil is still damp, it hasn't had time to dry out.",
                                "taste": "Tastes like dirt.",
                                "smell": "Potting soil and...maybe a hint of cologne.",
                                "listen": "You hear nothing."
                                },
                                True)

    sys.add_feature(F01R10)

    # bags of potting soil (F02R10)
    F02R10 = feature.Feature("F02R10", "bags of potting soil",
                                "The bags look like they were once stacked neatly but some have been pulled out of the "
                                "middle of the stack and messed up the pile. ",
                                "Some bags have been pulled out of the middle of the pile.",
                                {
                                "search": "You take a closer look at where the bags have been removed and see a pair "
                                "of gardening shears stuck down in the middle of the pile.",
                                "touch": "The bags just feel like bags of potting soil.",
                                "taste": "Tastes like dirt.",
                                "smell": "Smells like potting soil.",
                                "listen": "You hear nothing."
                                },
                                True)

    sys.add_feature(F02R10)


    # gardening shears (O08)
    O08 = object.Object("O08", "gardening shears",
                        "The gardening shears are large and look like they might be quite heavy. They could certainly "
                        "be used as a weapon in the wrong hands. There's a dark stain, you can't quite tell if it's blood "
                        "or rust.",
                        "Large gardening shears with a dark stain, perhaps blood or rust.",
                        {
                                "touch": "The shears are heavy, just as you suspected.",
                                "taste": "There's a metallic taste. Is that due to the metal or maybe blood? Are you "
                                "second-thinking your decision to taste them now?",
                                "smell": "Smells like metal and dirt.",
                                "listen": "The shears have nothing to say at the moment."
                        },
                        True)

    sys.add_obj(O08)

    # Save outside base game files
    sys.save_base_game_files()