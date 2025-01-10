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
# def get_char_count(string):
#     char_count = {}

#     while string:
#         char = string[0]
#         if not char.isalnum():
#             string = string.replace(char, '')
#             continue

#         counter = string.count(char)

#         if counter not in char_count.keys():
#             char_count[counter] = [char.lower()]
#         elif counter in char_count.keys():
#             char_count[counter].append(char.lower())
#             char_count[counter].sort()
#         string = string.replace(char, '')

#     return {key: char_count[key] for key in
#             sorted(char_count.keys(), reverse=True)}


# print(get_char_count("Mississippi")) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
# print(get_char_count("Hello. Hello? HELLO!!")) # should return {6: ['l'], 3: ['e', 'h', 'o']}
# print(get_char_count("aaa...bb...c!")) # should return {3: ['a'], 2: ['b'], 1: ['c']}
# print(get_char_count("aaabbbccc")) # should return {3: ['a', 'b', 'c']}
# print(get_char_count("abc123")) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

"""
P
1
Write a function that takes a list of words as input and returns a list of
integers. Each integer represents the count of letters in the word that occupy
their positions in the alphabet.

1 take a list of words arg
2 return a list of ints
3 each int represents the count of letters in the word that occupy their
    positions in the alphabet

E
Literally if "a" is at index 0 in the word, that counts, "b" at idx 2, etc

D
List of strings input
List of ints output
String to hold alphabet

A
- init alphabet string
- init counter = 0
- init matches = []

- check each word against the alphabet and count element @ index matches
    for word in words:
        for idx, char in word:
            if char.casefold() == alphabet[idx]:
                counter += 1
        matches.append(counter)
        counter = 0

- after checking each word, append the counter to matches

- reset the counter before checking the next word

- return matches

C
"""

# def solve(words):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     counter = 0
#     matches = []

#     for word in words:
#         for idx, char in enumerate(word):
#             if char.casefold() == alphabet[idx]:
#                 counter += 1
#         matches.append(counter)
#         counter = 0

#     return matches

# print(solve(["abode","ABc","xyzD"])) # should return [4, 3, 1]
# print(solve(["abide","ABc","xyz"])) # should return [4, 3, 0]

"""
P
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the 
opportunity to go for a short walk. The city provides its citizens with a Walk 
Generating App on their phones -- every time you press the button it sends you a 
list of one-letter strings representing directions to walk 
(e.g., ['n', 's', 'w', 'e']). You always walk only a single block in a direction,
and you know it takes you one minute to traverse one city block. 
Create a function that will return `True` if the walk the app gives you will 
take you exactly ten minutes (you don't want to be early or late!) and will, of 
course, return you to your starting point. Return `False` otherwise.

Note: You will always receive a valid list containing a random assortment of 
direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty 
list (that's not a walk, that's standing still!).

1 take a list of single char strings representing 4 cardinal directions
2 return a boolean representing whether the walk takes exactly 10 mins
3 True ONLY IF ends up back at starting point *** this is the hard part

- long description seems to just be asking for length of list, but examples
    seem to show otherwise

E
examples show rule 3

D
List of strings input
Boolean output
Possibly a 2nd list or dict
- if 'e' for every 'w' and 'n' for every 's', and len(list) == 10, True

A
check if len(list) == 10:
    if not, return False

init dict {char: list.count(char) for char in list}

if dict.get('n') == dict.get[s] and dict.get[e] == dict.get[w]:
    return True

return False

C
"""
# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
    
#     directions = {dir: walk.count(dir) for dir in walk}
    
#     if directions.get('n') == directions.get('s') and\
#         directions.get('w') == directions.get('e'):
#         return True
    
#     return False

# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # should return True
# print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # should return False
# print(is_valid_walk(['w'])) # should return False
# print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # should return False


"""
P
Write a function, persistence, that takes in a positive parameter
`num` and returns its multiplicative persistence, which is the number
of times you must multiply the digits in `num` until you reach a single digit.

1 take a positive int arg `num`
2 return the number of times you must multiple the digits in `num` until you
    reach a single digit (???) (examples clarify)

E
Makes sense now - 39 == 3 * 9 == 27 == 2 * 7 == 14 == 1 * 4 == 4,
so we need to do 3 multiplications to get to a single digit number

D
Int input
Int output
Will use a list, probably also string coercion (could do with math, though)

A
break the argument into single digits
    coerce to string
    coerce to list
    coere to int

multiply the digits together
    persistence = 0
    product = 1
    while True:
        for digit in list:
            product *= digit
            persistence += 1
        if len(str(product)) == 1:
            return persistence

return persistence when len(str(product)) is 1

"""
# def persistence(num):
#     num = [int(n) for n in list(str(num))]
#     if len(num) == 1:
#         return 0

#     persistence = 0
#     while True:
#         product = 1
#         for digit in num:
#             product *= digit

#         persistence += 1
#         num = [int(n) for n in list(str(product))]

#         if len(str(product)) == 1:
#             return persistence

# print(persistence(39)) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# # and 4 has only one digit
# print(persistence(999)) # should return 4, because 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, and finally 1*2=2
# print(persistence(4)) # should return 0, because 4 is already a one-digit number
# print(persistence(25)) # should return 2, because 2*5=10, and 1*0=0

"""
P
Find the highest scoring word in a string.
Each letter scores points based on its position in the alphabet: 
a = 1, b = 2, c = 3, ... z = 26.
Return the highest scoring word. If two words score the same, 
return the word that appears earliest in the string.

1 take string arg
2 find highest scoring word in string, based on position in alphabet
3 return highest scoring word
4 if 2 words score same, return one appearing first in string

E

D
String input
String output
List of words, prob nested list of chars

A
init alphabet

split the string into words
init dict of words {word: 0 for word in words}
split the words into chars

for word in words:
    score = 0
    for char in word:
        score += 1 + alphabet.find(char)
    dict[word] = score

score the chars to get score for word
update dict with score for word

return dict[max(dict)]


C

*** Got a working solution, but took over 20 minutes and had to consult notes
multiple times as well as ask LSBot how to return the key associated with the 
highest value. Poor performance. ***
"""

# def high(string):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     words = string.split()
#     word_dict = {word: 0 for word in words}
#     words = [list(word) for word in words]

#     for word in words:
#         score = 0
#         for char in word:
#             score += 1 + alphabet.find(char)
#         word_dict[''.join(word)] = score

#     return max(word_dict, key=word_dict.get)

# print(high('man i need a taxi up to ubud') == 'taxi')
# print(high('what time are we climbing up the volcano') == 'volcano')
# print(high('take me to semynak') == 'semynak')
# print(high('aaa b') == 'aaa')


"""
P
# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out. It's a dark night and no
# one can see each other. But you were flying nearby and you can see in the
# dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children,
# i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.

1 take string arg
2 rearrange the letters so that a given capital letter is followed by all the 
    lowercase instances of the same letter, for all letters
3 return the updated string

E
it appears the capital letters must first be sorted alphabetically

D
String input
String output
Might use a list of individual letters for easier sorting

A
chars = list(string)

chars.sort() will get us most of the way there

for idx, char1 in enumerate(chars):
    if char1.isupper():
        for char2 in chars:
            if char2.islower() and char2 == char1.lower():
                chars.intert()
                
FAILED: made a spaghetti plate and then turned to ChatGPT for help.
That's where the neat solution with the lambda came from.
From this, I learned that `sorted()` coerces its iterable argument to a list,
and that the `key=` keyword, along with `lambda` is ideal for custom sorting.
Actually, I already knew than 2nd part, I guess I just learned a little about
identifying appropriate times to use it.
"""

# def find_children(dance_floor):
#     # return ''.join(sorted(dance_floor, 
#     #           key=lambda char: (char.casefold(), char.islower())))
#     print(dance_floor)
#     print(sorted(dance_floor, 
#               key=lambda char: (char.casefold(), char.islower())))

# print(find_children("abBA") == "AaBb")
# print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
# print(find_children("CbcBcbaA") == "AaBbbCcc")
# print(find_children("xXfuUuuF") == "FfUuuuXx")
# print(find_children("") == "")

"""
Sort the list so that shorter words come first. Use a lambda.
"""
# words = ["apple", "cat", "banana", "dog", "elephant"]

# words = sorted(words, key=lambda word: len(word))

# print(words)

"""
Sort the list by their absolute values (e.g., treat -10 as 10).
"""
# numbers = [-10, 15, -20, 5, 0, -5]
# numbers = sorted(numbers, key=lambda num: abs(num))
# print(numbers)

'''
Find the sublist with the largest last number.
'''
# nested = [[1, 5, 3], [10, 4, 2], [6, 8, 7]]
# highest_last = max(nested, key=lambda sub: sub[-1])
# # nested.sort(key=lambda sub: sub[-1], reverse=True)

# print(highest_last)

'''
Goal: Sort the students by:

1-Grade (higher grades come first).
2-If grades are the same, sort by age (younger students come first).
3-If grades and ages are the same, sort by name alphabetically.

'''
# students = [
#     ("Alice", 90, 20),
#     ("Bob", 85, 20),
#     ("Charlie", 90, 19),
#     ("Diana", 85, 20),
#     ("Eve", 90, 22),
# ]

# students.sort(key=lambda student: (student[1], -student[2], student[0]), reverse=True)
# print(students)

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

1 take a string arg
2 PRINT a list of top 3 most occuring words, in order from most to least occuring
3 if less than 3 words, return whatever words exist (2, 1, or 0) in desc ord

E
examples show that if just 1 "word", empty list is returned. Also, it's
unclear form these examples if "..." or "," is being taken as a word. Anyway,
it seems that my rule 3 is wrong. Or the 3rd and 4th examples are wrong. Seems
just as likely.

D
String input
List output

A
-split string into words
    words = string.split()

-if word has no alphas, discard it
    for word in words:
        for char in word:
            alphas = char.isalpha()
            if alphas:
                break
        if not alphas:
            words.remove(word)

-sort list of words by count
    words = sorted(words, key=count)

-print list of top used words
    try:
        print(words[0:3])
    except:
        print(words)

FAILED: did well on everything, except I failed to realize that my code would 
most likely just return multiples of the most-occurring word(s). This problem 
is actually ideal for a dictionary. Dictionaries are often the right tool for 
for counting problems.

"""

# def top_3_words(string):
#     word_list = string.split()
#     words = {word: word_list.count(word) for word in word_list}

#     for word in word_list:
#         for char in word:
#             alphas = char.isalpha()
#             if alphas:
#                 break
#         if not alphas:
#             words.pop(word)

    
#     word_list = sorted(words, key=words.get, reverse=True)

#     try:
#         print(word_list[0:3])
#     except:
#         print(word_list)

# top_3_words(" , e .. ") # ["e"]
# top_3_words(" ... ") # []
# top_3_words(" ' ") # []
# top_3_words(" ''' ") # []
# top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.""") # should return ["a", "of", "on"]