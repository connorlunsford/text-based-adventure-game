import json

# load prepositions - read each line/word from the file and create a game_dictionary list
with open("./resources/prepositions.txt", "r") as contents:
    game_dictionary = list(contents.read().split())
contents.close()

# load game_verbs from json file
with open("./resources/game_verbs.json", "r") as contents:
    game_verbs = json.load(contents)
contents.close()

# iterate through each word within each alias for the game
# verbs and append it to the game_dictionary list
for i in range(len(game_verbs)): 
  for j in range(len(game_verbs[i])):
      for obj_set in game_verbs[i]:
          key_list = list(game_verbs[i].keys())
          value_list = list(game_verbs[i].values())
          for value in value_list:
            for word in value: 
              game_dictionary.append(word)

# load game_items from json file
with open("./resources/game_items.json", "r") as contents:
    game_items = json.load(contents)
contents.close()

# iterate through each word within each alias for the game
# items and append it to the game_dictionary list
for i in range(len(game_items)): 
  for j in range(len(game_items[i])):
      for obj_set in game_items[i]:
          key_list = list(game_items[i].keys())
          value_list = list(game_items[i].values())
          for value in value_list:
            for w in value:
              phrase = w.split()
              for word in phrase: 
                game_dictionary.append(word)

# remove duplicate words
game_dictionary = list(set(game_dictionary))

# sort for ease of human readability
game_dictionary.sort()

# write to txt file to be loaded by game system
filename = 'resources/game_dictionary.txt'
json.dump(game_dictionary, open(filename, 'w'))