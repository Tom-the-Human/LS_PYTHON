"""
Write a function that takes a string as input and counts the occurrences of 
each lowercase letter in the string. Return the counts in a dictionary where 
the letters are keys and their counts are values.

1 count all lowercase letters
2 each lowercase letter will have a dict key with the count as its value
3 ignore non-lowercase chars (implicit)
4 says "return the counts" but the example output shows the entire 
    dictionary being returned, so I'll follow the example

E
see rule 4

D
String in, dict out

A
- init letter_count dict
- use a for loop to iterate over the string
    - if char.islower() and char not in letter_count:
        - letter_count[char] = 1
    - elif char.islower():
        - letter_count[char] += 1
- return letter_count
"""
# def letter_count(string):
#     count = {}
#     for char in string:
#         if char.islower() and char not in count:
#             count[char] = 1
#         elif char.islower():
#             count[char] += 1
    
#     return count

# print(letter_count('Launch School')) 
# #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 1, ‘o’: 2, ‘u’: 1 }
"""
Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists 
entirely of vowels (a, e, i, o, u).

1 take a string arg
2 return an int of the length of the longest sub of only vowels
* I bet this is more easily said than done.

E
No surprises. Vowels may occur in any order, of course.

D
A string, list, or set of vowels will be needed.
String input. Int output.

A
- init vowels
- init count = 0 to track current consecutive vowel count
- init hi_count = 0 to track the longest vowel chain so far
- for char in string:
    if char in vowels:
        count += 1
    else:
        count = 0
    if count > hi_count:
    hi_count = count
- return hi_count
"""
# def solve(string):
#     vowels = 'aeuio'
#     count = 0
#     hi_count = 0

#     for char in string:
#         if char in vowels:
#             count += 1
#         else:
#             count = 0

#         if count > hi_count:
#             hi_count = count
    
#     return hi_count

# print(solve("roadwarriors")) # should return 2
# print(solve("suoidea")) # should return 3

"""
Write a function that, given a string of text, returns a list of the top-3 most
occurring words, in descending order of the number of occurrences.

Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more 
apostrophes (').
- Matches should be case-insensitive.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or 
top-1 words should be returned, or an empty list if a text contains no words.

1 take a string, return a list of strings
2 most common word first, others following in descending order,
    up to 3 per the assumptions above

E
The examples kind of suck, honestly. Why are 3 or 4 out of 5 weird edge cases?
Nonetheless, looks like only substrings containing letters should be counted
as "words" - that since " ' " and " ''' " are both expected to return empty
lists.

D
String in, List out, Intermediary list to store substrings.

A
- small helper function to determine word validity `is_word` or something
    - take a list of strings
    - return new list of only valid words
    - 
- split input string into subs and assign to sub list
- pass sub list to `is_word` to determine validity
- create dict for word count 
    - {word: 0 for word in list}
        - try to get the comprehension to count, but if not, do in for loop
- if word list < 3 elements
    - return key with highest value in dict
- else
    - return [key w highest value, second highest, third highest]
    - may be useful to build list before returning
    
"""
# def validate_words(list_of_strings):
#     valid = "'abcdefghijklmnopqrstuvwxyz"
#     words = []
    
#     for string in list_of_strings:
#         toggle = True
#         for char in string:
#             if char.casefold() not in valid:
#                 toggle = False
#         if string.strip("'") == "":
#             toggle = False
#         if toggle:
#             words.append(string)
    
#     return words

# def top_3_words(text_input):
#     list_of_strings = text_input.split()
#     valid_words = validate_words(list_of_strings)
#     word_count = {word: valid_words.count(word) for word in valid_words}

#     if not word_count:
#         return []
    
#     top_most = max(word_count, key=word_count.get)
#     word_count.pop(max(word_count, key=word_count.get))

#     if len(valid_words) < 3:
#         return [top_most]

#     second_most = max(word_count, key=word_count.get)
#     word_count.pop(max(word_count, key=word_count.get))

#     third_most = max(word_count, key=word_count.get)
#     word_count.pop(max(word_count, key=word_count.get))
#     # The above code is bad, repeating instructions. It works but would be
#     # better refactored to dry it up a bit.

#     return [top_most, second_most, third_most]

# print(top_3_words(" , e .. ")) # ["e"]
# print(top_3_words(" ... ")) # []
# print(top_3_words(" ' ")) # []
# print(top_3_words(" ''' ")) # []
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.""")) # should return ["a", "of", "on"]

"""
A panagram is a sentence that contains every single letter of the alphabet at
least once. Given a string, detect whether or not it is a panagram.
Return True if it is, False if not. Ignore numbers and punctuation.

1 Return True if the string includes every letter in the alphabet
2 Return False if not
3 Non-alpha chars are inconsequential

E:
No news, should get a True and then a False

D
String input, boolean output. Could use a collection to contain the alphabet
String, or maybe list. Would a tuple work?

A
- init collection of alphabet

- for each char in alphabet:
    - if char not in string:
        - return False

- return True
"""
# def panagram(string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     panagram = True

#     for letter in alphabet:
#         if letter not in string.casefold():
#             panagram = False

#     return panagram

# print(panagram("The quick brown fox jumps over the lazy dog."))
# print(panagram("This is not a pangram."))

"""
Write a function that takes a string as an argument and groups the
number of times each character appears in the string as a dictionary
sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore
spaces, special characters, and count uppercase letters as lowercase ones.

1 take string arg
2 create a dict to sort chars in the string by how man times they appear
    - key is count, value is list of chars appearing that many times
3 the dict keys (ints) should be sorted highest to lowest
4 the dict values (lists) should be sorted alphabetically
    - from examples, beginning of alphabet first
5 ignore non-alphanumerics, count all chars as lower

E
Last example includes numbers, and shows them listed ahead of letters

D
String input
Dict output with nested lists
Possibly would use another list as well

A
- init counter = 0
- init empty dict
# - for char.lower() in string:
#     - count = string.count(char)
#         - if count is not already a dict key:
#             - add count: [char.lower()] to dict
#         - if count is already a key in the dict:
#             - dict[count].append(char)
#             - dict[count].sort()
- while string:
    - char = string[0]
    - count = string.count(char)
    - if count is not already a dict key:
        - add count: [char.lower()] to dict
    - if count is already a key in the dict:
        - dict[count].append(char)
        - dict[count].sort()
    - string.replace(char, '') to remove char from string

- sort dict by key before returning       
"""
def get_char_count(string):
    char_count = {}

    while string:
        char = string[0]
        if not char.isalnum():
            string = string.replace(char, '')
            continue

        counter = string.count(char)

        if counter not in char_count.keys():
            char_count[counter] = [char.lower()]
        elif counter in char_count.keys():
            char_count[counter].append(char.lower())
            char_count[counter].sort()
        string = string.replace(char, '')

    return {key: char_count[key] for key in
            sorted(char_count.keys(), reverse=True)}


print(get_char_count("Mississippi")) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!")) # should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!")) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc")) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123")) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}