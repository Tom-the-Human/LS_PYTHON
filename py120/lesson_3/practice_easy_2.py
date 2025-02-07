# class Game:
#     count = 0
#     def play(self):
#         return f'Start the {self.game_name} game!'

# class Bingo(Game):
#     def __init__(self, game_name, player_name):
#         self.game_name = game_name
#         self.player_name = player_name
#         Game.count += 1

# class Scrabble(Game):
#     def __init__(self, game_name, player_name1, player_name2):
#         self.game_name = game_name
#         self.player_name1 = player_name1
#         self.player_name2 = player_name2
#         Game.count += 1
        
# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'
# #####

"""
Q3: Benefits of OOP in Python

Ability to change and track state of multiple objects of the 
    same class/type

Ability to create custom classes/types and objects

Ability to define custom operations for custom classes & objects

Multiple inheritance and Mixins to aid creating class heirarchy

Managing complexity

"""

# class Cat:
#     def __init__(self, type):
#         self.type = type

#     def __str__(self):
#         return f"I am a {self.type}."

# print(Cat('hairball'))
# #####

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model(tv))