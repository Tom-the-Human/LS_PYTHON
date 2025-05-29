"""
Write a program that takes a word and a list of possible anagrams and selects 
the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists", 
"google", "inlets", and "banana", the program should return a list 
containing "inlets". Please read the test suite for the exact rules of anagrams.

P
Input: Anagram object (string), and a list of strings
Output: list of strings from the input list that contain 
    the same chars as the Anagram object
Explicit:
1 anagrams are case INsensitive (i.e. 'Carthorse' IS anagram of 'Orchestra')
2 list is variable length and there may be any number of matches
3 same word does not count (i.e. 'corn' is not an anagram of 'corn')
4 return empty list if no match
5 subsets do not count (i.e. 'dog', 'goody' not anagrams of 'good')
Implicit:
1 can input list be blank? return empty list?
2 wtf is a checksum? I'm guessing this to do with with UTF-8/ASCII numeric values
    if so, words with differing chars but same checksum don't count
    looks like that is correct

E
Rules mainly derived from examples ... looking for further info ...
I am confused by this test:

    def test_does_not_confuse_different_duplicates(self):
        detector = Anagram("galea")
        self.assertEqual([], detector.match(["eagle"]))

What does "different duplicates" mean in this context? What is being demonstrated?
    I can see that the words are not anagrams, though they have all but one letter
    in common. The assertion is an empty list, as I'd expect. Is there anything
    more to it?

C
mostly clear. may need to revisit if tests fail

H
create `Anagram` class
    instantiation assigns input string to object state (self.word or similar)
include `match` instance method
    takes 'self' and list of strings
    detects strings from the list that are anagrams of self.word and
    returns a list of the matched anagrams

D
input string
input list of strings
output list

A
create `Anagram` class
    instantiation assigns input string to object state (self.word or similar)

include `match` instance method
    takes 'self' and list of strings
    detects strings from the list that are anagrams of self.word
        could use string sort and equality to detect anagrams
            i.e. anagrams = word ofr word in list if 
                sorted(self.word.casefold()) == sorted(word.casefold())
                and word != self.word
        use casefold to ignore case

    returns a list of the matched anagrams

C
"""
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = [
            word for word in word_list 
            if sorted(word.casefold()) == sorted(self.word.casefold())
            and word.casefold() != self.word.casefold()
        ]

        return anagrams
