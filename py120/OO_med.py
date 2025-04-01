"""
1
circular buffer 
description too long 
see https://launchschool.com/exercises/699c68e4?track=python

P
1 initialize the buffer with None for empty positions
2 when a value is added or `put` to the buffer, it replaces a `None`, not 
    appended to the end
3 when `get`, essentially "pop" oldest non-None value
4 if buffer full, overwrite oldest value
5 if buffer empty, return None


"""
# # Tried twice to write this on my own and havent been able to. 
# # Tricky to model mentally.
# # Below is LS solution.

# class CircularBuffer:
#     def __init__(self, size):
#         self.buffer = [None] * size
#         self.next = 0
#         self.oldest = 0

#     def put(self, obj):
#         next_item = (self.next + 1) % len(self.buffer)

#         if self.buffer[self.next] is not None:
#             self.oldest = next_item

#         self.buffer[self.next] = obj
#         self.next = next_item

#     def get(self):
#         value = self.buffer[self.oldest]
#         self.buffer[self.oldest] = None
#         if value is not None:
#             self.oldest += 1
#             self.oldest %= len(self.buffer)

#         return value



# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True

# buffer.put(1)
# buffer.put(2)
# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True

"""
2 & 3
Number guessing game
Create an object-oriented number guessing class for numbers in the 
range 1 to 100, with a limit of 7 guesses per game. 
The game should play like this:
Problem description is mostly given as example terminal output
P
1 game should involve the range of 1 to 100, unclear from example if inclusive
2 limit of 7 guesses per game
- 0 is out of bounds
- must say whether too high or too low after each incorrect guess
- game is started with game.play()

E
refer to https://launchschool.com/exercises/f4e85bbd?track=python

D
range(1, 100) or maybe (1, 101)
lots of string output

A
- init game instance with no parameters
    - include valid range as instance variable
    - maybe include optional parameter to change range
    - init random secret number in range
    - init guesses, include another optional parameter

- need a call and response structure, with these mechanics
0   - game.play() is called to start the game
1   - if guesses equal 0, print "You have no more guesses. You lost!"
    - user is prompted with number of guesses remaining
        and the valid range
2    - guess is evaluated
        - if guess out of range
            - print "Invalid guess. Enter a number between {min(range)} and max(range):"
            - do not decrement guesses
        - if guess is greater than secret number
            - output "Your guess is too low."
            - decrement guesses
            - go to 1
        - if guess is greater than secret number
            - output "Your guess is too high."
            - decrement guesses
            - go to 1
        - if guess is equal to secret number
            - print "That's the number! \n"
            - print "You won!"
            - game ends and game.play() must be called again to restart

methods:
init(range=range(1, 100), guesses=7)
play    # starts game
prompt
eval_guess
too_high
too_low
you_win

"""
# import math
# import random

# class GuessingGame:
#     def __init__(self, low, high):
#         self.low = low
#         self.high = high
#         self.valid = range(low, high + 1)
#         self.guesses = int(math.log2(high - low + 1)) + 1
#         self.secret_num = random.randrange(low, high + 1)

#     def prompt(self):
#         if self.guesses == 0:
#             print("You have no more guesses. You lost!")
#             return
        
#         print(f"You have {self.guesses} guesses remaining.")
#         return input(f"Enter a number between {self.low} and {self.high}: ")
    
#     def eval_guess(self, guess):
#         if guess == None:
#             return
        
#         guess = int(guess)

#         if guess not in self.valid:
#             guess = input(f"Invalid guess. Enter a number between {self.low} and {self.high}: ")
#             self.eval_guess(guess)
#         elif guess > self.secret_num:
#             print("Your guess is too high.\n")
#             self.guesses -= 1
#             guess = self.prompt()
#             self.eval_guess(guess)
#         elif guess < self.secret_num:
#             print("Your guess is too low.\n")
#             self.guesses -= 1
#             guess = self.prompt()
#             self.eval_guess(guess)
#         elif guess == self.secret_num:
#             print("That's the number!\n")
#             print("You won!")
#             return
    
#     def play(self):
#         self.__init__(self.low, self.high)
#         guess = self.prompt()
#         self.eval_guess(guess)

# game = GuessingGame(501, 1500)
# game.play()
# game.play()

"""
4, 
Update this class so you can use it to determine the lowest ranking and 
highest ranking cards in a list of Card objects: (see below)

For this exercise, numeric cards are low cards, ordered from 2 through 10. 
Jacks are higher than 10s, Queens are higher than Jacks, Kings are higher 
than Queens, and Aces are higher than Kings. The suit plays no part in the 
relative ranking of cards.

If you have two or more cards of the same rank in your list, your min and max 
methods should return one of the matching cards; it doesn't matter which one.

Besides any methods needed to determine the lowest and highest cards, create 
a __str__ method that returns a string representation of the card, e.g., 
"Jack of Diamonds", "4 of Clubs", etc.

5
Using the Card class from the previous exercise, create a Deck class that 
contains all of the standard 52 playing cards. Use the following code to 
start your work:

The Deck class should provide a draw method to deal one card. The Deck should 
be shuffled when it is initialized. If no more cards remain when draw is 
called, the method should generate a new set of 52 shuffled cards, 
then deal one card from the new cards.

Note that the last line should almost always print "True"; if you shuffle the 
deck 1000 times a second, you will be very, very, very old before you see two 
consecutive shuffles produce the same results. If you get a "False" result, 
you almost certainly have something wrong.

6
In the previous two exercises, you developed a Card class and a Deck class. 
You are now going to use those classes to create and evaluate poker hands. 
Create a class, PokerHand, that takes 5 cards from a Deck of Cards and 
evaluates those cards as a poker hand.
"""
# from random import shuffle

# class Card:
#     VALUES = {
#         "Jack": 11,
#         "Queen": 12,
#         "King": 13,
#         "Ace": 14,
#     }

#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"
    
#     @property
#     def value(self):
#         return Card.VALUES.get(self.rank, self.rank)

#     def __lt__(self, other):
#         return self.value < other.value

#     def __gt__(self, other):
#         return self.value > other.value
    
#     def __eq__(self, other):
#         return self.rank == other.rank and self.suit == other.suit
    

# class Deck:
#     RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
#     SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

#     def __init__(self):
#         self.cards = [Card(rank, suit) for rank in Deck.RANKS
#                       for suit in Deck.SUITS]

#         shuffle(self.cards)

#     def draw(self):
#         if not self.cards:
#             self.__init__()

#         return self.cards.pop()    

# # Include Card and Deck classes from the last two exercises.

# class PokerHand:
#     def __init__(self, deck):
#         self.hand = [deck.draw() for _ in range(5)]

#     def print(self):
#        for card in self.hand:
#            print(card)

#     def evaluate(self):
#         if self._is_royal_flush():
#             return "Royal flush"
#         elif self._is_straight_flush():
#             return "Straight flush"
#         elif self._is_four_of_a_kind():
#             return "Four of a kind"
#         elif self._is_full_house():
#             return "Full house"
#         elif self._is_flush():
#             return "Flush"
#         elif self._is_straight():
#             return "Straight"
#         elif self._is_three_of_a_kind():
#             return "Three of a kind"
#         elif self._is_two_pair():
#             return "Two pair"
#         elif self._is_pair():
#             return "Pair"
#         else:
#           return "High card"

#     def _is_royal_flush(self):
#         # is flush and ranks 10 - Ace
#         return self._is_straight_flush() and \
#             (min(card.value for card in self.hand) == 10)

#     def _is_straight_flush(self):
#         # sorted hand ranks are 100% sequential and is flush
#         return self._is_flush() and self._is_straight()

#     def _is_four_of_a_kind(self):
#         # 4x same rank
#         return self._is_n_of_a_kind(4, 1)

#     def _is_full_house(self):
#         # contains a pair and 3-of-a-kind
#         return self._is_three_of_a_kind() and self._is_pair()

#     def _is_flush(self):
#         return all(card.suit == self.hand[0].suit for card in self.hand)

#     def _is_straight(self):
#         # sorted hand ranks are 100% sequential
#         values = sorted([card.value for card in self.hand])
#         sequence = list(range(values[0], values[0] + 5))

#         return values == sequence

#     def _is_three_of_a_kind(self):
#         # 3x same rank
#         return self._is_n_of_a_kind(3, 1)

#     def _is_two_pair(self):
#         # a pair of 1 rank + a pair of another rank
#         return self._is_n_of_a_kind(2, 2)

#     def _is_pair(self):
#         # 2x same rank
#         return self._is_n_of_a_kind(2, 1)

#     def _is_n_of_a_kind(self, n, m):
#         rank_counts = {}
#         for card in self.hand:
#             rank_counts[card.rank] = (rank_counts.get(card.rank, 0) + 1)
            
#         matches = [1 for count in rank_counts.values()
#                    if count == n]

#         return len(matches) == m

# hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()

# # Adding TestDeck class for testing purposes

# class TestDeck(Deck):
#     def __init__(self, cards):
#         self.cards = cards

# # All of these tests should return True

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Ace", "Hearts"),
#             Card("Queen", "Hearts"),
#             Card("King", "Hearts"),
#             Card("Jack", "Hearts"),
#             Card(10, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Royal flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Clubs"),
#             Card("Queen", "Clubs"),
#             Card(10, "Clubs"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Four of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Full house")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Diamonds"),
#             Card(10, "Clubs"),
#             Card(7, "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Queen", "Clubs"),
#             Card("King", "Diamonds"),
#             Card(10, "Clubs"),
#             Card("Ace", "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(6, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Three of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(9, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(8, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Two pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card("King", "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "High card")

########
# class LoggerMixin:
#     # provides logging functionality
#     def log(self):
#         print(self)

# class SerializableMixin:
#     # provides methods that convert objects to and from dicts
#     def to_dict(self):
#         return self.__dict__.copy()

#     @classmethod
#     def from_dict(cls, data):
#         instance = cls.__new__(cls)
#         for key, value in data.items():
#             setattr(instance, key, value)
#         return instance

# class DhammapadaQuote(LoggerMixin, SerializableMixin):
#     # creates instances of quotes with attributes for text and verse_num
#     def __init__(self, text, verse_num):
#         self.text = text
#         self.verse_num = verse_num

#     def __str__(self):
#         return f"{self.text}\n- Dhammapada verse {self.verse_num}"

#     def __repr__(self):
#         return f"DhammapadaQuote{self.text, self.verse_num}"

# class SongLyric(LoggerMixin, SerializableMixin):
#     # creates instances of quotes with attributes for lyric, song, band, and author
#     def __init__(self, lyric, song, artist, author):
#         self.lyric = lyric
#         self.song = song
#         self.artist = artist
#         self.author = author

#     def __str__(self):
#         return f"{self.lyric}\n{self.artist} - {self.song}\nwritten by {self.author}"

#     def __repr__(self):
#         return f"SongLyric{self.lyric, self.song, self.artist, self.author}"


# dhamma33 = DhammapadaQuote(
#     "The restless, agitated mind,\n     Hard to protect, hard to control,\nThe sage makes straight\n     As a fletcher the shaft of an arrow.",
#     33,
# )

# puscifer_algorithm = SongLyric(
#     "We bend the knee\nWe serve the will\nWe venerate and genuflect to\nOur God\nThe algorithm",
#     "The Algorithm",
#     "Puscifer",
#     "Maynard James Keenan",
# )

# # Demonstrate logging functionality
# print("Logging Dhammapada quote:")
# dhamma33.log()
# print("\nLogging song lyric:")
# puscifer_algorithm.log()

# # Demonstrate serialization
# print("\nSerializing to dictionaries:")
# dhamma_dict = dhamma33.to_dict()
# print(dhamma_dict)
# puscifer_dict = puscifer_algorithm.to_dict()
# print(puscifer_dict)

# # Demonstrate deserialization
# print("\nDeserializing from dictionaries:")
# new_dhamma = DhammapadaQuote.from_dict(dhamma_dict)
# new_puscifer = SongLyric.from_dict(puscifer_dict)

# print("\nLogging recreated objects:")
# new_dhamma.log()
# print()
# new_puscifer.log()

#####

# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     def __repr__(self):
#         return f"Book{self.title, self.author, self.isbn}"

# class Library:
#     def __init__(self):
#         self.books = dict()  # ISBN -> (Book object, status)

#     def add_book(self, title, author, isbn):
#         # Create a Book object as a collaborator
#         book = Book(title, author, isbn)
#         # Store the book with its status using ISBN as the key
#         self.books[isbn] = (book, "available")
#         return f"{book} added"

#     def remove_book(self, isbn):
#         if isbn in self.books:
#             book, _ = self.books[isbn]
#             del self.books[isbn]
#             return f"{book} removed"
#         return "Book not found"

#     def search(self, term):
#         # Search for books by title or author
#         results = []
#         for isbn, (book, status) in self.books.items():
#             if term.casefold() in book.title.casefold() \
#             or term.casefold() in book.author.casefold():
#                 results.append((book, status))
#         return results

#     def check_out_book(self, isbn):
#         if isbn in self.books:
#             book, status = self.books[isbn]
#             if status == "available":
#                 self.books[isbn] = (book, "checked out")
#                 return f"{book} is now checked out"
#             else:
#                 return f"{book} is already checked out"
#         return "Book not found"

#     def return_book(self, isbn):
#         if isbn in self.books:
#             book, status = self.books[isbn]
#             if status == "checked out":
#                 self.books[isbn] = (book, "available")
#                 return f"{book} has been returned"
#             else:
#                 return f"{book} was not checked out"
#         return "Book not found"

# lib = Library()
# lib.add_book("Dhammapada, The", "Gil Fronsdal", 9781645472438)
# lib.add_book("Limitless", "Jim Kwik", 9781401958237)

# print(lib.books)

# print(lib.search("Kwik"))
# print(lib.check_out_book(9781401958237))
# print(lib.return_book(9781401958237))

