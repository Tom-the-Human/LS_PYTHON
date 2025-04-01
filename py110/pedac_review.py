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

"""
You are given an integer N. Your job is to figure out how many substrings 
inside of N divide evenly with N.

Let's say that you are given the integer '877692'.

8 does not evenly divide with 877692. 877692/8 = 109711 with 4 remainder.
7 does not evenly divide with 877692. 877692/7 = 125384 with 4 remainder.
7 does not evenly divide with 877692. 877692/7 = 125384 with 4 remainder.
6 evenly divides with 877692. 877692/6 = 146282 with 0 remainder.
9 does not evenly divide with 877692. 877692/9 = 97521 with 3 remainder.
2 evenly divides with 877692. 877692/2 = 438846 with 0 remainder.

We aren't going to stop there though. We need to check ALL of the substrings 
inside of 877692.

87 does not evenly divide with 877692. 877692/87 = 10088 with 36 remainder.
77 does not evenly divide with 877692. 877692/77 = 11398 with 46 remainder.
76 does not evenly divide with 877692. 877692/76 = 11548 with 44 remainder.
69 does not evenly divide with 877692. 877692/69 = 12720 with 12 remainder.
etc.

Rules:
-If an integer is 0, then it does NOT divide evenly into anything.
-Even though N can divide evenly with itself, we do not count it towards the 
end number. 

For Example:

N = 23, the answer will be 0.  
-If there are multiple instances of a number, they all get counted. For example:

N = 11, the answer will be 2 
Input:
A non negative integer.

Output:
The number of times you found an integer that was evenly divisible with N.
-----
P
Input: non-negative integer
Output: integer count v
(count of substrings of the input that the input can be evenly divided by)
Find the number (count) if individual substrings of any length that are divisible
by the input.

E
Substrings of any length count (except the full input)
A substring counts if the result of `input % int(substring) == 0`
0 is not a valid divisor
If multiple instances of the same number, they all get counted, i.e.
    n = 11, output will be 2 since both instance of 1 divide into 11 evenly
Single digit imputs will always return 0

C
Check

H
Coerce int to string
Use a nested for loop to get all possible substrings with length less than input
    and that are not 0
Put the valid substrings (coerced bank to int) in a list
Use another for loop to get modulus for the input and each substring
If modulus is 0, increment counter

D
Strings
List of valid subs
Counter

A
Coerce input int to string
Init a counter
Use a nested for loop to get all possible substrings with length less than input
    and that are not 0
Put the valid substrings (coerced back to int) into a list
Use another for loop to get modulus for the input and each substring

If modulus is 0, increment counter
-   for num in list:
        if input % num == 0:
        counter += 1

Return counter

C
"""
# def get_count(n):
#     string = str(n)
#     counter = 0
#     subs = []

#     for i in range(len(string)):
#         for j in range(i + 1, len(string) + 1):
#             sub = string[i: j]
#             if (len(sub) < len(string)) and int(sub):
#                 subs.append(int(sub))

#     for num in subs:
#         if n % num == 0:
#             counter += 1

#     return counter

# print(get_count(623456222222242))

"""
You have to search all numbers from inclusive 1 to inclusive a given number x, 
that have the given digit d in it.
The value of d will always be 0 - 9.
The value of x will always be greater than 0.

You have to return as an array

the count of these numbers,
their sum
and their product.

For example:
x = 11
d = 1
->
Numbers: 1, 10, 11
Return: [3, 22, 110]

If there are no numbers which include the digit, return [0,0,0].

P
Search all numbers from 1 through `x` (inclusive)
Count all numbers in that range that include single character int `d`
d will always be in 0-9
x will always be positive
Return as a list: the count, the sum of these numbers, the product of same

Input = 2 integers
Output = list of 3 integers

E
Given example of (x=11, d=1), numbers including digit d (1) are 1, 10, and 11
So we'd want a list [1, 10, 11,] then can get the count (list length), the sum,
and the product
We'd return [3 (the count), 22 (the sum), and 110 (the product)]

I also see that a d may be given which is greater than x, which means no numbers
meet the criteria (output of [0, 0, 0])

C
Yes, looks like I understand the expected output

H
Need to coerce inputs to strings
Use a for loop with a range of 1 to x + 1, and check a string of d for membership
in a string representation of each number in that range
If d is found, add that number to a list

Once all numbers in ranged are checked, make a new list of, in order:
Count = length of list
Sum of all numbers found
Product of all numbers found

D
Integers
Strings
List of matching numbers
List of output

A
Need to coerce inputs to strings
string_x
string_d
Initialize a num_list
Use a for loop with a range of 1 to x + 1, and check a string of d for membership
in a string representation of each number in that range
If d is found, add that number to a list
    for num in range(1, x + 1):
        if string_d in str(num):
            num_list.append(num)

Once all numbers in ranged are checked, make a new list of, in order:
Count = length of list
Sum of all numbers found
Product of all numbers found

Output = [len(num_list), sum(num_list), prod(num_list)]

Return output

C
"""
# from math import prod

# def numbers_with_digit_inside(x, d):
#     found_nums = []

#     for num in range(1, x + 1):
#         if str(d) in str(num):
#             found_nums.append(num)

#     output = [len(found_nums), sum(found_nums), prod(found_nums) if found_nums else 0]
#     print(f"Found: {found_nums}")

#     return output

# print(numbers_with_digit_inside(11, 1))
# print(numbers_with_digit_inside(5, 6))
# print(numbers_with_digit_inside(44, 4))
# print(numbers_with_digit_inside(20, 0))

"""
Given an array of numbers (in string format), you must return a string. 
The numbers correspond to the letters of the alphabet in reverse order: 
a=26, z=1 etc. 

You should also account for '!', '?' and ' ' that are represented 
by '27', '28' and '29' respectively.

All inputs will be valid.

P

E

C

H

D

A

C
"""
# def switcher(num_strings):
#     pass

"""
In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

"""
# def square_digits(num):
#     pass

"""
Write a function that takes in a string of one or more words, 
and returns the same string, but with all words that have five or more 
letters reversed. Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
"""
# def spin_words(sentence):
#     pass

"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

P
Input: string
Output: new string
Explicit: param is a string of ONLY ALPHAS upper and lowercase
Implicit: For each letter
Capitalize letter
Follow it with lowercases of the same letter equal to the index of the letter
Hyphens in between letter groups, but not before or after 

E
First example:
'abcd'
'a' is at index 0 -> 'A'
'b' index 1 -> 'Bb'

Doesn't matter if letter is upper or lower in input, all treated same

C
check

H
Initialize an empty string
For each letter in the input
-   Add that letter in uppercase to the new string
-   Add a number of that letter in lowercase equal to the index of the original letter
-   Add a hyphen '-'
Strip '-' from the end
Return new string

D
String input and output
Reference indices
For loop

A
Initialize an empty string
For each index and letter in the enumerated input
-   Add that letter in uppercase to the new string
-   Add a number of that letter in lowercase equal to the index of the original letter
-   Add a hyphen '-'
Strip '-' from the end
Return new string

C
"""
# def accum(string):
#     output = ''

#     for idx, char in enumerate(string):
#         output += char.upper() + (char.lower() * idx) + '-'

#     return output.strip('-')

# Agent 47, you have a new task! Among citizens of the city X are hidden 2 dangerous criminal twins. Your task is to identify them and eliminate!

# Given an array of integers, your task is to find two same numbers and return one of them, for example in array [2, 3, 6, 34, 7, 8, 2] answer is 2.

# If there are no twins in the city - return None or the equivalent in the language that you are using.

"""
P
Input: list of integers
Ouput integer that is duplicated in the list
Explicit: 
-   If an int is duplicated in the list return it
-   If no duplicates, return None
-   What if more than 2????
-   What if more than one set of twins????
Implicit: 

E
examples are straightforward

C
check
2 questions unanswered

H
Make a new empty list
For each number in input list
-   Check to see if it is in the new list
-   If not:
-       append it to the list
-   If so:
        Return it

D
List input
Intermediary list to collect ints that have been seen
Integers

A
Make a new empty list
For each number in input list
-   Check to see if it is in the new list
if number in new_list:
    return number

new_list.append(number)

-   If not:
-       append it to the list
-   If so:
        Return it

C
"""

# def elimination(lst):
#     new_lst = []

#     for num in lst:
#         if num in new_lst: #if lst.count(num) == 2
#             return num

#         new_lst.append(num)

tup1: tuple = (1, 2, 3,)
list1: list = (1, 2, 3,)
list1 += (4,)
print(list1)
print(list1.__class__)
tup1 += list1
print(tup1)