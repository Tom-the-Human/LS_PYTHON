"""
Write a program that, given a word, computes the Scrabble score for that word.

Letter Values

You'll need the following tile scores:

Letter	Value
A, E, I, O, U, L, N, R, S, T	1
D, G	2
B, C, M, P	3
F, H, V, W, Y	4
K	5
J, X	8
Q, Z	10

How to Score

Sum the values of all the tiles used in each word. 
For instance, lets consider the word CABBAGE which has the 
following letters and point values:
3 points for C
1 point for each A (there are two)
3 points for B (there are two)
2 points for G
1 point for E

Thus, to compute the final total (14 points), we count:
3 + 2*1 + 2*3 + 2 + 1
=> 3 + 2 + 6 + 3
=> 5 + 9
=> 14

P
Input: Scrabble object with a string stored as state
Output: int
Explicit:
1 each chatacter in the string must be scored appropriately
2 empty words, `None`, and whitespace score 0
3 nonsense and single chars ok
4 case insensitive
5 requires a `Scrabble` class, a `score()` instance method, 
    and a `calculate_score(string)` class method
Implicit:
?

E
Examples provide most of the rules above.
Other than that, we just need to score inidividual chars and sum the points

C
check

H
create class constant SCORES dictionary
    keys = string of chars having a comon value
    values = score values for chars in each string
    so that using the dict is something like
    for char in Scrabble obj:
        for key, value in dict:
            if char in key:
                score += value

Scrabble class with constructor and 2 addtl required methods
    constructor stores a string to state
    score instance method takes only self returns string score
    calculate_score class method takes a string and returns string score

Make sure to cover cases of chars that arent in the dict
Also make sure case doesn't matter (casefold())

D
dict for score table
string inputs
int outputs

A
create class constant SCORES dictionary
    keys = string of chars having a common value
    values = score values for chars in each string

    so that using the dict is something like
        score = 0
        for char in self.word:
            for key, value in dict:
                if char in key:
                    score += value

Scrabble class with constructor and 2 addtl required methods
    constructor stores a string to state
    score instance method takes only self returns string score
        see potential nested loop above ... can possibly be better or more concise
        maybe a comprehension 
        sum(list(value for key, value in dict[char] for char in string)) ???

    calculate_score class method takes a string and returns string score
        similar to other method but takes a string insteaf of self

Make sure to cover cases of chars that arent in the dict
Also make sure case doesn't matter (casefold())

C
"""
class Scrabble:
    SCORES = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10,
    }

    def __init__(self, word):
        if word.__class__ is str:
            self.word = word.strip()
        else:
            # if input isn't a string, use empty string
            self.word = ""

    def score(self):
        # if empty, return 0
        if not self.word:
            return 0
        
        score = 0
        for char in self.word:
            for key, value in self.SCORES.items():
                if char.casefold() in key.casefold():
                    score += value
        
        return score

    @classmethod
    def calculate_score(cls, string):
        return Scrabble(string).score()


# test1 = Scrabble("morning")
# print(test1.score())
# test2 = Scrabble(None)
# print(test2.score())
# # test3
# print(Scrabble.calculate_score("morning"))