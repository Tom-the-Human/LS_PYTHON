'''
To prep for PY119 interview retake. Do at least a couple problems each week. 
Spaced repetition is key. If LS problems become too familiar, use CodeWars.
Main thing is to practice strong PEDAC EVERY TIME, and identify any other
areas for improvement.
'''

"""
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

P
1 take a list of 10 single digit ints arg 
    - (no tests attempt to pass more than 1 digit per value)
    - (no tests attempt to pass a list of length other than 10)
2 return a STRING of those numbers in the form a phone #
3 make sure formatting is exact

E
one test included,

D
List input
Formatted string output

A
- even though probably not necessary, check that list length is 10
    - could also check that only single digits are list values
        (`11` or `336` would be illegal)
- group digits into phone number sections by index
    - i.e. nums[0: 3] is the area code
    - we can go ahead and use join to create the string we want for our output
        - area = ''.join(nums[0: 3]
        - prefix = nums[3: 6]
        - suffix = nums[6:]
- format the output as shown
        - f"({area}) {prefix}-{suffix}"

CodeWars 6 kyo       
1-26-25 Solved 15 mins
"""
# def create_phone_number(nums):
#     if len(nums) != 10:
#         return "Invalid input"
    
#     area = ''.join(str(num) for num in nums[0: 3])
#     prefix = ''.join(str(num) for num in nums[3: 6])
#     suffix = ''.join(str(num) for num in nums[6:])

#     return f"({area}) {prefix}-{suffix}"

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890"

"""
Write a function that takes one or more arrays and returns a new array of 
unique values in the order of the original provided arrays.

In other words, all values present from all arrays should be included in 
their original order, but with no duplicates in the final array.

The unique numbers should be sorted by their original order, but the final 
array should not be sorted in numerical order.

Check the assertion tests for examples.
    # Note, without installing codewars_test and solution libraries, 
        I can't actually copy/paste the tests right from Codewars, 
        but can approximate them with print statements based on my 
        understanding of the rules.

P
1 take 1 or more list args (tests show up to 3, so will do up to 3) (list(s) in)
2 return a new list of UNIQUE values in the order originally provided (list out)
3 All values in the args must be included in output, in the order they
    first appeared, no sorting should take place otherwise

E
room for up to 3 lists, some may be blank
outputs are as expected from problem rules

D
multiple list inputs
list output

E
- use list extend to combine all lists
    - call extend on first arg, pass 2nd and 3rd lists to extend method

- init an output list []

- for loop to iterate through all values in input list
    - if value not in output list, append it to output list

- return output
"""
# def unite_unique(list1, *args):
#     for arg in args:
#         list1.extend(arg)
    
#     output = []
#     for val in list1:
#         if val not in output:
#             output.append(val)

#     return output

# print(unite_unique([1, 2], [3, 4]) == [1, 2, 3, 4])
# print(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]) == [1, 3, 2, 5, 4])
# print(unite_unique([4, 3, 2, 2]) == [4, 3, 2])
# print(unite_unique([4, "a", 2], []) == [4, "a", 2])
# print(unite_unique([], [4, "a", 2]) == [4, "a", 2])
# print(unite_unique([], [4, "a", 2], []) == [4, "a", 2])
# print(unite_unique([]) == [])
# print(unite_unique([],[]) == [])
# print(unite_unique([],[1, 2]) == [1, 2])
# print(unite_unique([],[1, 2, 1, 2],[2, 1, 1, 2, 1]) == [1, 2])

"""
Move the first letter of each word to the end of it, then add "ay" 
to the end of the word. Leave punctuation marks untouched.

P
1 take a string arg of words
2 move the first letter of each word to the end of it
3 append "ay"to the end of the word
4 ignore punctuation (leave it untouched)
5 return the new string

E
2 tests included below
only test with punctuation has it separated from the words, so still
a little unclear how a word should be handled if it has punctuation
atteched to it. I assume 'orldway!' would be correct

D
string in
string out
will need to use split, so operating on a list of strings will be necessary
probably even need to split individual letters, so sublist of chars

A
- split to list of words
- for word in list, move thefirst character to the end and add "ay"
    - assign first char to a variable (first = word[0])
    - new_word = word[1:] + first + "ay"
    - word = new word
    !!!this solution will not word for words with attached punctuation!!!

- join and return word list

1/27/25 - passed both tests in about 20 mins, but haven't gotten to test
    it against theother tests on Codewars yet. Will check later and may update

"""
# def pig_it(text):
#     words = text.split()
#     pig_words = []

#     for word in words:
#         if word.isalpha():    
#             first = word[0]
#             new_word = word[1:] + first + "ay"
#             pig_words.append(new_word)
#         else:
#             pig_words.append(word)

#     return ' '.join(pig_words)


# print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
# print(pig_it('Hello world !'))     # elloHay orldway !

"""
Three candidates take part in a TV show.

In order to decide who will take part in the final game and probably become 
rich, they have to roll the Wheel of Fortune!

The Wheel of Fortune is divided into 20 sections, each with a number from 
5 to 100 (only mulitples of 5).

Each candidate can roll the wheel once or twice and sum up the score of each
 roll. The winner one that is closest to 100 
 (while still being lower or equal to 100). 
 In case of a tie, the candidate that rolled the wheel first wins.

You receive the information about each candidate as an array of objects: 
each object should have a name and a scores array with the candidate roll values.

Your solution should return the name of the winner or false if there is 
no winner (all scored more than 100).

***Problem
1 - Wheel consists of intervals of 5 from 5 to 100, i.e. [5, 10, 15, ...]
for a total of 20 possible outcomes
2 - Each player can roll(spin) once or twice
3 - The player's score is the total of thier rolls
4 - The highest score that does not go over 100 wins (score == 100 is fine)
5 - In case of tie, player that went first wins
6 - Take candidate(player) info as a dict with {'name': str, 'score': [int, int]}
7 - return name of winner, or False if no winner (all scores exceed 100)

***Confirm


***Hypothesis
must check each score total in order
return False instead of None for no winner is unusual, 
but seems to be the requirement


***Example

***Data
input list of dictionaries
each dict has a 'name' key and a 'score' key
the value of 'score' is a list

probably store 'name' with highest 'score' as var (unless score total > 100)
return value of name for high scoring player
else return False

***Algorithm
- init var winner = {'name': False, 'score':[0]}
- iterate through list of dicts
- for each player(dict), total the values in 'score'
- if player score is higher than score of `winner` AND
    score is 100 or less, then `winner = player`
- return name of winner

SOLVED: I had a solution that worked for this single test case in about 22 mins,
    but it took me about 30 minutes total to make it pass all the Codewars tests.
    I missed an important detail that there must be 3 candidates(players). The
    other tests, such as checking that each dict has both a 'name' and a 'scores'
    key, were not made totally explicit, though I probably should have been able
    to infer them. 
"""
# def winner(player_list):
#     winner = {'name': False, 'scores': [0]}

#     for player in player_list:
#         total_score = 0
#         for score in player['scores']:
#             total_score += score
#         if sum(winner['scores']) < total_score <= 100:
#             winner = player

#     return winner['name']

# c1 = {"name": "Bob", "scores": [10, 65]}
# c2 = {"name": "Bill", "scores": [90, 5]}
# c3 = {"name": "Charlie", "scores": [40, 55]}
# print(winner([c1, c2, c3])) #Returns "Bill"

"""
You are going to be given a string. Your job is to return that string in a 
certain order that I will explain below:

Let's say you start with this: "012345"

The first thing you do is reverse it:"543210"
Then you will take the string from the 1st position and reverse it again:"501234"
Then you will take the string from the 2nd position and reverse it again:"504321"
Then you will take the string from the 3rd position and reverse it again:"504123"

Continue this pattern until you have done every single position, and then you 
will return the string you have created. 
For this particular number, you would return:"504132"

Input:
A string of length 1 - 1000

Output:
A correctly reordered string.

***Problem
- take a string input and return a new string with the chars rearranged as described
- i.e. reverse string, lock 0, reverse rest, lock 1, reverse rest, lock 2, until
    end of string is reached

- should work for strings of lengths 1 - 1000
    - does that mena it should NOT work for strings longer than 1000?

***Confirm
012345
543210
501234
504321
504123
504132

***Hypothesis
will need to use counter and while loop
while counter less than string length - 1
use slicing to reverse string starting at index equal to counter
get char at index equal to counter
add that char to new string
return new string

***Example

***Data
string input
strng output
counter
while loop

***Algorithm
- init counter
- while counter < string length:
    - slice a reverse of the string starting from the index == counter
    - get the char at index 0 of the slice
    - add that char to new string
- return new string

FAILED first attempt. Seems like such an easy one honestly, but I had problems
with transforming the string while iterating through indices. Spent almost 30 
minutes with no joy. My algorithm isn't far off, but I was losing characters.
With only a few minutes left, I decided to try something pretty different, based
on nothing but an idea, and that didn't work at all. Got quickly into hack n slash.

Just thought of a posible solution using list coercion and pop. Something like
`while string_list: 
    output += string_list.pop()
    output += string_list.pop(0)`

And yeah, that works perfectly. Well, I don't know how to rate my success on this.
Would've definitely been bad if my first attempt was during an interview.
But after stepping away for a few moments I just sat down and saw this perfectly
neat and viable solution. I had the idea and then confirmed it would work by pointing
and reasoning through the expected transformation for the 3rd test (a word is easier
for me to visually reason with). Only caveat is this solution never actually 
reverses the string, just pops the chars from each end in the expected order.
"""
# def reverse_fun(string):
#     output = ''
#     string_list = list(string)

#     while string_list:
#         output += string_list.pop()

#         if string_list: # may be empty if odd number of elements
#             output += string_list.pop(0)

#     return output

# print(reverse_fun('012345') == '504132')
# print(reverse_fun('0123456789') == '9081726354')
# print(reverse_fun('Hello') == 'oHlel')