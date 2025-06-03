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
will need to use break, so operating on a list of strings will be necessary
probably even need to break individual letters, so sublist of chars

A
- break to list of words
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
#     words = text.break()
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


# ----------------------------------------------------------------------------


# 5/5/2025 Taking another run at the interview soon,
# so let's redo all probs for practice. Remember to also consult
# your notes to recall methods and other tools
"""

Write a program that solicits six (6) numbers from the user 
and prints a message that describes whether the sixth 
number appears among the first five.

P
Input: user input to create list of nums
Output: String based on boolean (in/not in)
Explicit rules:
1 get 6 nums from user
2 return string saying whether 6th num is in first 5
Implicit:
1 can nums be ints and/or floats? Examples only show ints

E
Examples are clear.
Teat first 5 nums as collection, check 6th for membership

H
Use `input()` to get nums and append each of first 5 to list
Use `in` to determine whether 6th input is in the list
Return formatted string based on membership

D
int (or float?) input
string output
list for nums

A
Use `input()` to get nums and append each of first 5 to list
    with for loop
    can a list comprehension do this? probably not

Use `in` to determine whether 6th input is in the list
    set membership to "is ..." if True
    "isn't ..." if False
Return formatted string based on membership
f"{num6} {membership} in {num_list} # may need to play w formatting

"""
# def get_nums(quant):
#     num_list = []
#     for _ in range(quant):
#         num_list.append(input("Enter a number: "))
    
#     return num_list

# nums = ', '.join(get_nums(5))
# last = input("Enter the last number: ")
# membership = "is" if last in nums else "isn't"

# print(f"{last} {membership} in {nums}.")
# # I slightly modified the input messages to allow for dryer code
# # original prob specifes "... 1st ...", "... 2nd ...", etc

"""
2
Write a function that returns True if the string passed as an argument is a 
palindrome, False otherwise. A palindrome reads the same forwards and backwards. 
For this problem, the case matters and all characters matter.

P
Input: string
Output: bool
Explicit:
1 return True if string is a palindrome
2 case and all characters count
Implicit:
?

E
"madam" is True, but "Madam" is False
as is  "madam i'm adam' (whitespace and apostraphe asymmetric)

C
check

H
use slice notation to create a reverse of the string
check if the input and its reverse are equal

D
string input
string of reversed input
bool output

A
use slice notation to create a reverse of the string
string[-1:0:-1] is that right? might need to fiddle with this

check if the input and its reverse are equal
use ==

"""
# def is_palindrome(string):
#     backwards = string[::-1]
#     return string == backwards


# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

"""
3
Write another function that returns True if the string passed as an argument 
is a palindrome, or False otherwise. This time, however, your function should 
be case-insensitive, and should ignore all non-alphanumeric characters. 
If you wish, you may simplify things by calling the is_palindrome function 
you wrote in the previous exercise.

P
Input: string
Output: bool
Explicit:
1 return True if string is a palindrome
2 case doesn't count
3 non-aplhanums don't count (letters and numbers only)
Implicit:
?

E
this time "Madam" is True, as is "Madam I'm Adam"

C
check

H
clean the string of any non-alphanum chars
use slice notation to create a reverse of the string
check if the casefolded input and its casefolded reverse are equal


D
string input
bool output
probably a list of chars during cleaning

A
clean the string of any non-alphanum chars
    use a list comprehension combined with join?

call is_palindrome on cleaned string
    use slice notation to create a reverse of the string
    modified to check if casefolded input and casefolded reverse are equal



"""
# def is_palindrome(string):
#     return string == string[::-1]

# def is_real_palindrome(string):
#     cleaned = ''.join([char.casefold() for char in string if char.isalnum()])

#     return is_palindrome(cleaned)

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

"""
4
Write a function that takes a list of numbers and returns a list with the 
same number of elements, but with each element's value being the running 
total from the original list.

P
Input: list of numes (looks like all ints)
Output: list of nums (running total of input)
Explicit:
1 same number of elements in input and output lists
2 output elements should be total of input list elements to same index (see E)
Implicit:
?

E
[2, 5, 13] == [2, 7, 20] (2 == 2)(2 + 5 == 7)(7 + 13 == 20)
[1, 25, 3, 100] == [1, 26, 29, 129]

C
check

H
init new list for totals
iterate through input list, adding up each element from 0 to current index
    add that sum to new list
return new list

D
imput list
output list
none else needed

A
init new list for totals
iterate through input list, adding up each element from 0 to current index
    add that sum to new list
    sum(input_list[0: idx + 1])
return new list

C
"""
# def running_total(input_list):
#     return [sum(input_list[0: idx + 1]) for idx in range(len(input_list))]
            
# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

"""
5 & 6
Write a function that takes a string consisting of zero or more space-separated 
words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

P
Input: string of words (or empty string)
Output: dict of word counts by size
Explicit:
1 Words are separated on space
2 word size is dict key, count is value
Implicitly:
1 any char other than space counts as part of a word (punctuation, etc)

E
All examples are clear, any char contributes to word count

C

H
use break with the default arg to get words
use a dict comprehension to create a dict of lengths as keys and counts as values

D
string input
list from break
dict output

A
words = break string

use a dict comprehension to create a dict of lengths as keys and counts as values
might not actually be able to do this in one go ...
make list of lengths first, then generate dict from that
word_dict = length, lengths.count(length) for length in lengths
something like that

C
"""
# def cleaned(word):
#     return ''.join(ch for ch in word if ch.isalnum())

# def word_sizes(string):
#     lengths = [len(cleaned(word)) for word in string.break()]
#     return {length: lengths.count(length) for length in lengths}

# # All of these examples should print True

# # string = 'Four score and seven.'
# # print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# # string = 'Hey diddle diddle, the cat and the fiddle!'
# # print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# # string = 'Humpty Dumpty sat on a wall'
# # print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# # string = "What's up doc?"
# # print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# # print(word_sizes('') == {})

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

"""
Easy 2: 1
Write a function that takes a floating point number representing an angle 
between 0 and 360 degrees and returns a string representing that angle in 
degrees, minutes, and seconds. You should use a degree symbol (°) to 
represent degrees, a single quote (') to represent minutes, and a double 
quote (") to represent seconds. There are 60 minutes in a degree, and 60 
seconds in a minute.

P
Input: float
Output: string
Explicit:
1 take a number representing an angle (0 to 360) and convert to string representation
2 include degrees, minutes, seconds with proper notation
Implicit:
1 requires converting between percentage and degrees/minutes/seconds (see examples)

E
dms(93.034773) == "93°02'05\""
what's going on here?
60/100 or 100/60?
"""
# print(93.034773 / 100) # .93034773
# print(93.034773 / 60) # 1.55057955
# print(93.034773 % 1) # get rid of degrees first, so left with approx ...
# print(0.034773 * 60) # 2.08638, ok, so there's our 2 minutes?
# print(2.08638 / 1) # get rid of minutes
# print(0.08638 * 60) # 5.1828, looks like we have our seconds!
"""
Let's do one more example
dms(76.73) == "76°43'48\""
"""
# print(76.73 % 1) # .73 (approx)
# print(0.73 * 60) # 43.8, ok, looks like the pattern is working here as well
# print(0.8 * 60) # 48.0, yep, success
"""

C
check

H
assign degrees to variable

get minutes and assign to variable

get seconds and assign to variable

use f string to construct and return output

D
could put each part of output in a list instead individual vars, 
    but not sure that's useful
float input
string output

A
assign degrees to variable
    1 int coercion or floor division to remove nums after decimal

get minutes and assign to variable
    1 (input % 1) * 60 # save this result to calculate seconds
    2 repeat process for degree assignment (prob floror div)

get seconds and assign to variable
    1 ((result from minutes pt 1) % 1) * 60
    2 repeat floor div

use f string to construct and return output
"""

# def dms(number):
#     DEGREE = "\u00B0"

#     degrees = int(number // 1)
#     minutes = int(((number % 1) * 60) // 1)
#     seconds = int(((((number % 1) * 60) % 1) * 60) // 1)

#     return f"{degrees}{DEGREE}{minutes:02d}'{seconds:02d}\""

    


# # All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

"""
Write a function that takes two lists as arguments and returns a set that 
contains the union of the values from the two lists. You may assume that 
both arguments will always be lists.

P
Input: 2 lists
Output: a set
Explicit: 
1 return the union of the 2 lists as a set
2 ?

E
1 example given, union is clearly both lists added together except
set coercion removes duplicate entries

C
check

H
combine the lists via extend or +
return a set of the combined lists

D

A

C
"""
# def union(list1, list2):
#     return set(list1 + list2)

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

"""
5
Given an unordered list and the information that exactly one value in the list 
occurs twice (every other value occurs exactly once), determine which value 
occurs twice. Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate value.

P
Input: list
Output: list element (int)
Explicit:
1 List has a single duplicate value
2 return the duplicate
Implicit: ?

E
List can presumably be any length of 2 or greater, if it'll always have a duplicate
Need an efficient way to count occurences of each element

C
check

H
a dictionary comprehension of element: count(element) could be used
return the key that has a value > 1

D
list input
dict for counts

A
a dictionary comprehension of element: count(element) could be used
return the key that has a value > 1

C
"""
# def find_dup(numlist):
#     counts = {num: numlist.count(num) for num in numlist}

#     for num , count in counts.items():
#         if count > 1:
#             return num

# print(find_dup([1, 5, 3, 1]) == 1) # True
# print(find_dup([
#                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
#               ]) == 73)       # True

"""
Easy 3: 5
Write a function that takes a positive integer as an argument and returns 
that number with its digits reversed.

P
Input: int
Output: int (reversed digits)
Explicit:
1 reverse the digits in the number (easy enough)

E
no news here

C

H
coerce to string
use slice to reverse
coerce back to int
probably doable in 1 line

D
string

A

"""
# def reverse_number(num):
#     return int(str(num)[::-1])

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

"""
Easy4: 6
Write a function that takes a string argument and returns a list of substrings
of that string. Each substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.

P
Input: string
Output: list of strings
Explicit:
1 return a list of only the substrings starting at index 0
2 sort the list from shortest to longest (should be by default depending on
    how list is constructed)

E
easy

C

H
might try a comprehension, but is easy with for loop
might be a one-liner

D
string input
list output

A
"""
# def leading_substrings(string):
#     return [string[0: idx + 1] for idx in range(len(string))]


# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

"""
7
Write a function that returns a list of all substrings of a string. 
Order the returned list by where in the string the substring begins. 
This means that all substrings that start at index position 0 should come 
first, then all substrings that start at index position 1, and so on. Since 
multiple substrings will occur at each position, return the substrings at a 
given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the 
previous exercise:

P
Input: string
Ouput: list of strings
Explicit:
1 create list of all substrings, ordered by substring starting index
2 then from shortest to longest at each starting index
3 should use function created in alst exercise
Implicit:
?

E
"abcde" results in 15 subs

C

H
nested for loop, or may be able to do in nested comprehension
    (would be valuable to have in memory)
need 2 indices

D

A

"""
# def leading_substrings(string):
#     return [string[0: idx + 1] for idx in range(len(string))]

# def substrings(string):
#     all_subs = []
#     for idx in range(len(string)):
#         all_subs += leading_substrings(string[idx:])

#     return all_subs

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True

"""
8
Write a function that returns a list of all palindromic substrings of a string. 
That is, each substring must consist of a sequence of characters that reads the 
same forward and backward. The substrings in the returned list should be sorted 
by their order of appearance in the input string. Duplicate substrings should 
be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay 
attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' 
are not. In addition, assume that single characters are not palindromes.

P
Input: string
Output: list of strings
Explicit:
1 return a list of all palindrominc substrings, sorted by appearance in the string
2 include all duplicates
3 case sensitive, all characters count, no single character subs
4 use function from previous exercise
Implicit:
?

E
examples confirm understanding
"substrings" can include full string if it is a palindrome

C

H
use slice to define a reversed sub
    i.e. string[i: j] == string[j: i: -1]
    may need to mess with that a bit
using the substrings function isn't especially intuitive to me, since I'll want
    to test individual subs for palindrome-ness and this function returns a list
    but let's use it anyway
    can concat to a new list


D
string input
list output
yet another list

A
use slice to define a reversed sub
    i.e. string[i: j] == string[j: i: -1]
    may need to mess with that a bit
    no need if using helper function

using the substrings function isn't especially intuitive to me, since I'll want
    to test individual subs for palindrome-ness and this function returns a list
    but let's use it anyway
    can concat to a new list

probably make an is_palindrome helper
    can scroll up to copy or write from scratch



"""
# def is_palindrome(string):
#     return string == string[::-1] and len(string) > 1

# def leading_substrings(string):
#     return [string[0: idx + 1] for idx in range(len(string))]

# def substrings(string):
#     all_subs = []
#     for idx in range(len(string)):
#         all_subs += leading_substrings(string[idx:])

#     return all_subs

# def palindromes(string):
#     # subs = substrings(string)
#     # pal_subs = []

#     # for sub in subs:
#     #     if is_palindrome(sub):
#     #         pal_subs.append(sub)

#     # return pal_subs

#     return [sub for sub in substrings(string) if is_palindrome(sub)]
    

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

"""
Write a function that takes a string and returns a dictionary containing 
the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values 
lie between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

P
Input: string
Output: dict
Explicit:
1 return dict of respective percentages of uppcase, lowercase, and chars that
    are neither
2 format output as strings rounded to the 2nd decimal place (syntax!!!)
3 percentages are always between "0.00" and "100.00"
4 no empty strings will be given
Implicit:
?

E
Seen this and solved it before
Divide total chars by each category of char? Or the other way round?

(chars_of_type / total_chars(or len(string))) * 100

C
I get what needs to be done

H
get the total length of the string
get the count of each type of character
init a dict with keys for each type
for each type, divide the number of chars by the length of the string and
    multiply that result by 100 to get a percentage
store each percentage in the dict as an appropriately formatted f-string
return dict

D
string input
dict output

A
get the total length of the string
get the count of each type of character
    FUCK! Can't believe how badly I'm doing.
init a dict with keys for each type

for each type, divide the number of chars by the length of the string and
    multiply that result by 100 to get a percentage
    (chars_of_type / total_chars(or len(string))) * 100

store each percentage in the dict as an appropriately formatted f-string
    I should probably know how to do this by now
    sill have to play with it some, so let's code!

return dict

C
"""
# def letter_percentages(string):
#     total = len(string)
#     output = {
#         'lowercase': 0,
#         'uppercase': 0,
#         'neither': 0,
#         }
    
#     for char in string:
#         if char.islower():
#             output['lowercase'] += 1
#         elif char.isupper():
#             output['uppercase'] += 1
#         else:
#             output['neither'] += 1

#     for key, count in output.items():
#         output[key] = f'{count / total * 100:.2f}'

#     return output


# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must 
be greater than the length of the longest side, and every side must have a 
length greater than 0. If either of these conditions is not satisfied, the 
triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as 
arguments and returns one of the following four strings representing the 
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

P
Input: 3 ints
Output: string
Explicit rules:
1 rules regarding triangle above
2 Return triangle's classification or 'invalid'
Implicit rules:
?

E
Examples show each type including both types of invalid triangle

C
check

H
if any side is 0, return invalid
determine maximum length side
if (all sides minus max side) is less than max side, return invalid
then just compare to see how many sides are the same and return
    string based on that

D
list or tup of sides probably
string output

A
if any side is 0, return invalid

determine maximum length side
if (all sides minus max side) is less than max side, return invalid
    (a, b, c) - max(a, b, c) < max(a, b, c)

then just compare to see how many sides are the same and return
    string based on that
    if a == b == c
    if a in (b, c) or b in (a, c)
    else

C
"""
# def triangle(a, b, c):
#     sides = (a, b, c)

#     if 0 in sides or sum(sides) - max(sides) < max(sides):
#         classification = 'invalid'
#     elif a == b == c:
#         classification = 'equilateral'
#     elif a in (b, c) or b in (a, c):
#         classification = 'isosceles'
#     else:
#         classification = 'scalene'
    
#     return classification
    


# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

"""
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, 
and every angle must be greater than 0. If either of these conditions is not 
satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and 
returns one of the following four strings representing the triangle's 
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to 
worry about floating point errors. You may also assume that the arguments are 
in degrees.

P
Input: 3 ints (angles this time, not sides)
Output: string
Explicit rules:
1 all rules regarding triangles (above)
2 all inputs will be ints representing degrees
Implicit rules:
?

E
all types including both kinds of invalid trianges in examples

C
check

H
if any angle is 0 or the angles don't sum to 180, return 'invalid'
if any angle == 90, return 'right'
if all angles < 90, return 'acute'
else, return 'obtuse'

D
tuple for angles
stringoutput

A
if any angle is 0 or the angles don't sum to 180, return 'invalid'
if any angle == 90, return 'right'
if all angles < 90, return 'acute'
else, return 'obtuse'

C
"""
# def triangle(a, b, c):
#     angles = (a, b, c)

#     if 0 in angles or sum(angles) != 180:
#         tri_type = 'invalid'
#     elif 90 in angles:
#         tri_type = 'right'
#     elif any(a > 90 for a in angles):
#         tri_type = 'obtuse'
#     else:
#         tri_type = 'acute'

#     return tri_type
    

# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True

"""
Some people believe that Fridays that fall on the 13th day of the month are 
unlucky days. Write a function that takes a year as an argument and returns 
the number of Friday the 13ths in that year. You may assume that the year is 
greater than 1752, which is when the United Kingdom adopted the modern 
Gregorian Calendar. You may also assume that the same calendar will remain in 
use for the foreseeable future.

P
Input: int representing year
Output: int representing numbr of Friday 13ths
Explicit:
1 year is greater than 1752 (start of modern calendar year)
2 ?
Implicit:
?

E
Examples are clear but show no edge cases like invalid input
    or years with no Friday 13ths
Fairly obvious we'll need to use datetime, and I don't know the 
    syntax to work with that, maybe in Hint 1

C
yep, I understand the problem

H
import datetime
calculate (or retrieve?) how many 13ths of the month land on a Friday 
    within a given year
return that number

D
int input
how to process with datetime? do I need a list of weekdays or what?
int output

A
import datetime
calculate (or retrieve?) how many 13ths of the month land on a Friday 
    within a given year
    - without knowing the syntax, this is impossible, however
        - for each month of the specified year, if the 13th is on a Friday
            - either increment a counter or add the date to a list
            - return the counter or the length of the list
                - counter is probably simpler

return that number

C
"""
# import datetime as dt

# def friday_the_13ths(year):
#     thirteenths = [dt.date(year, month, 13) for month in range(1, 13)]

#     count = 0
#     for day in thirteenths:
#         if day.weekday() == 4:
#             count += 1

#     return count

# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

"""
A featured number (something unique to this exercise) is an odd number that 
is a multiple of 7, with all of its digits occurring exactly once each. For 
example, 49 is a featured number, but 98 is not (it is not odd), 97 is not 
(it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there is 
no next featured number.

NOTE: The largest possible featured number is 9876543201.

P
Input: int
Ouput: int (next greater "featured" number)
Explicit:
1 featured numbers must be: 
    odd, 
    multiple of 7, 
    free of repeated digits, 
    <= 9876543201
2 return the next featured number greater than the input
3 if no greater featured number, return specified error message
Implicit:
1 if given number IS a featured number, find the NEXT GREATER featured number
    (in no event should we return the same number)

E 
examples are strightforward
I can see that any featured number will be a nultiple of 7 and another odd number
and a string representation of that number will be the easiest option to check
    for duplicate digits

C
check

H
init error message
if input >= 9876543201, return error

create a helper to determine if a number contains repeating digits
    convert to string and use a dict with str.count
    if any value in the dict is > 1, return True
    else False
    False is the correct condition for a featured number

use a while loop to find the next multiple of 7 and an odd number 
    greater than the input
    i.e. while featured < given and not repeat_digits(featured)

when number discovered, return it

D
int input
string coercion of input
dict to store digit counts
int output

A
init error message
if input >= 9876543201, return error

create a helper to determine if a number contains repeating digits
    convert to string and use a dict with str.count
    digit_counts, str(number).count(digit)
    if any value in the dict is > 1, return True
    else False
    False is the correct condition for a featured number

use a while loop to find the next multiple of 7 and an odd number
    greater than the input
    i.e. while featured < given and not repeat_digits(featured)

when number discovered, return it

C
"""
# def next_featured(number):
#     if number >= 9876543201:
#         return ("There is no possible number that "
#          "fulfills those requirements.")
    
#     def has_repeat_digits(num):
#         # True if repeated digits
#         num_str = str(num)
#         return len(num_str) != len(set(num_str))
    
#     def not_odd_mult_of_7(num):
#         return num % 7 != 0 or num % 2 != 1
    
#     featured = number + 1
#     while not_odd_mult_of_7(featured):
#         featured += 1

#     while has_repeat_digits(featured):
#         featured += 14

#     return featured

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that "
#          "fulfills those requirements.")
# print(next_featured(9876543201) == error)       # True

"""
Write a function that computes the difference between the square of the sum 
of the first count positive integers and the sum of the squares of the first 
count positive integers.

P
Input: int
Output: int
Explicit:
1 see the problem, single sentence instruction
Implicit:
1 sum all the numbers up to and including the input
2 square that sum
3 sum the squares of all the numbers up to and including the input
4 subtract the latter from the former

E
first example is already worked and illustrates well

C
check

H
get sum of counts and square it - call this squared_sum
get sum of squared counts - call this summed_squares
return the difference between the two

D
int input
probably some lists
int output

A
get sum of counts and square it - call this squared_sum
sum[range(1, number + 1)]**2

get sum of squared counts - call this summed_squares
sum([num**2 for num in range(1, number + 1)])

return the difference between the two

C
"""
# def sum_square_difference(number):
#     squared_sum = sum([num for num in range(1, number + 1)])**2
#     summed_squares = sum([num**2 for num in range(1, number + 1)])
#     return abs(squared_sum - summed_squares)

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

"""
Bubble Sort is one of the simplest sorting algorithms available. 
It is not an efficient algorithm, so developers rarely use it in real code. 
However, it is an excellent exercise for student developers. 
In this exercise, you will write a function that sorts a list using the 
bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. 
On each pass, the two values of each pair of consecutive elements are 
compared. If the first value is greater than the second, the two elements 
are swapped. This process is repeated until a complete pass is made without 
performing any swaps. At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without 
making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the 
algorithm, as well as a minor optimization technique -- see the 
Bubble Sort Wikipedia page.

Write a function that takes a list as an argument and sorts that list using 
the bubble sort algorithm described above. The sorting should be done 
"in-place" -- that is, the function should mutate the list. 
You may assume that the list contains at least two elements.

P
Input: list
Output: list
Explicit:
1 compare each consectutive pair of values in the list and 
    swap them if they aren't sorted
2 ?
3 profit (stop sorting if no changes made on an entire pass through the list)
Implicit:
?

E
Examples just show unsorted lists and expected sorted versions, 
so not much help really.
But let's examine the 2nd example:
lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True
first we compare 6 and 2, which need to be swapped, so now:
[2, 6, 7, 1, 4]
then compare 6 and 7, so:
[2, 6, 7, 1, 4]
then compare 7 and 1, so:
[2, 6, 1, 7, 4]
then compare 7 and 4:
[2, 6, 1, 4, 7]
That completes the first pass.
Then start again:
2 < 6, so go to next pair
6 > 1, so swap:
[2, 1, 6, 4, 7]
then 6 > 4, so swap:
[2, 1, 4, 6, 7]
6 < 7, so no change. That completes the second pass.
On the third pass, we only need to swap 2 and 1:
[1, 2, 4, 6, 7]
That's the third pass completed. Then there will be a final fourth pass.
No changes will be made on the fourth pass, which indicates we're done.

C
check

H
set a swap counter
use a for loop inside a while loop
set swaps to 0 at the start of the while loop
while swaps, for item in list, compare to next item
if item is greater than next, swap and add to counter
should naturally exit once complete

D
list input
list output
I don't think any others are needed

A
not included in instructions, but copy the list to avoid
    unnecessarily mutating the original
    OOPS! actually, the original list MUST be mutated for this exercise
set a swap counter
use a for loop inside a while loop
set swaps to 0 at the start of the while loop
while swaps, for item in list, compare to next item
if item is greater than next, swap and add to counter
should naturally exit once complete

C
"""
# def bubble_sort(lst):
#     swaps = True
#     while swaps:
#         swaps = False
#         for idx in range(len(lst) - 1):
#             if lst[idx] > lst[idx + 1]:
#                 # swap
#                 lst[idx], lst[idx + 1] = \
#                     lst[idx + 1], lst[idx]
#                 # reset flag
#                 swaps = True


# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True


"""
Write a function that takes two sorted lists as arguments and returns a new 
list that contains all the elements from both input lists in ascending sorted 
order. You may assume that the lists contain either all integer values or all 
string values.

You may not provide any solution that requires you to sort the result list. 
You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

P
Input: 2 lists
Output: 1 sorted list
Explicit:
1 return a NEW sorted list that contains all elements from both inputs
2 both list will contain the same element type (no TypeError/ValueError)
3 DON'T mutate the inputs
4 Here's where it gets interesting! The output list must be constructed
    "one element at a time" in sorted order, not sorted after initialization
5 MISSED THIS! both inputs are already sorted
Implicit:
1 identical values can appear in one or both input lists
2 input can include an empty list

E
Hmm, not sure how to construct element by element in order - tempted to revert
to using bubble sort. But actually, maybe I could use min() and lst.pop() if
I first compile the inputs to an intermediary list. That would be a good step
since the inputs aren't to be mutated anyway.
Let's work through an example>
merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9]
So, if first we do something like list1.extend(list2) we get
[1, 5, 9, 2, 6, 8]
Which could then be sorted via bubble sort, but I don't think that's in the
spirit of the exercise. More likely, I should do something like
while len(result_list) < len(both_lists):
    result_list.append(min(both_lists))
    both_lists.remove(min(both_lists))
So on first loop:
result_list == [1]
both_lists == [5, 9, 2, 6, 8]
Next loop:
result_list == [1, 2]
both_lists == [5, 9, 6, 8]
but, oops, need a different while condition since I'm changing 
    the length of both_lists! Maybe (len(list1) + len(list2) - yeah, should do

^^^ ABOVE IS NO GO - O(n**2) time complexity and apparently doesn't fully
    meet the requirements

instead, maybe just bubble sort the first elements of each input list
    could be tricky with unequal length inputs, especially empty lists

C
check

H
concat the lists
on the concatenated list, perform the while loop
    while len(result_list) < len(list1 + list2):
        result_list.append(min(both_lists))
        both_lists.remove(min(both_lists))
return the result list

D
2 lists input
intermediary list (concat of inputs)
result/output list

A
concat the lists
on the concatenated list, perform the while loop
    while len(result_list) < len(list1 + list2):
        result_list.append(min(both_lists))
        both_lists.remove(min(both_lists))
return the result list

C
"""
# def merge(list1, list2):
    # # both_lists = list1 + list2
    # # result_list = []
    
    # # while len(result_list) < len(list1 + list2):
    # #     result_list.append(min(both_lists))
    # #     both_lists.remove(min(both_lists))

    # # return result_list
    # copy1 = list1[:]
    # copy2 = list2[:]
    # result = []

    # while copy1 and copy2:
    #     if copy1[0] <= copy2[0]:
    #         result.append(copy1.pop(0))
    #     else:
    #         result.append(copy2.pop(0))

    # return result + copy1 + copy2

# All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

"""
Merge Sort
A merge sort is a recursive sorting algorithm that works by breaking down a 
list's elements into nested sub-lists, then combining those nested sub-lists 
back together in sorted order. It is best explained with an example. 
Given the list [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of 
sorting it with merge sort. We'll start off by breaking the list down into 
nested sub-lists:

Copy Code
[9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# repeat until each sub-list contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

In the first step, we partition the list into a list of two sub-lists, 
so that each sub-list contains approximately half of the entries. 
In the next step, we partition each sub-list in the same way. 
This process repeats until each of the innermost lists contains 
exactly one element.

We now work our way back to a flat list by merging each pair of nested 
sub-lists in the proper ascending order:

Copy Code
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
[[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
[[2, 6, 7, 9], [0, 1, 5, 8]] -->
[0, 1, 2, 5, 6, 7, 8, 9]

For example, on the 2nd line, we merge [2, 9] with [6, 7], 
which becomes [2, 6, 7, 9].

Write a function that takes a list argument and returns a new list 
that contains the values from the input list in sorted order. 
The function should sort the list using the merge sort algorithm as 
described above. You may assume that every element of the list will have 
the same data type: either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.

P
Input: list
Output: sorted list
Explicit:
1 break the list into nested sublists
2 repeat until each element is in its own sublist, nested as deeply as 
    necessary to break each element to its own list
3 reconstruct the list in sorted order, one step at a time (see example)
Implict:
?

E
The example above makes sense but is hard to read. I'll work another example
step by step.
merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
[6, 2, 7, 1, 4] -> this being of odd length, I'm not sure where it will break.
Since 5 // 2 == 2, I'll assume it breaks after the 2nd element.
[[6, 2], [7, 1, 4]]
[[[6], [2]], [[7], [1, 4]]]
Again, because of the odd length, most elements are successfully separated,
    but another break is necessary for the last 2 elements.
[[[6], [2]], [[7], [[1], [4]]]]
Ok, now we're ready to reconstruct it starting at the deepest level,
    with all rejoined elements sorted.
[[[6], [2]], [[7], [1, 4]]] -> rejoin [1, 4] which is already in order
[[2, 6], [1, 4, 7]] -> 7 rejoined to 1, 4 and sorted, [2, 6] sorted
[1, 2, 4, 6, 7] -> final rejoin, all sorted

Hmm ... not especially enlightening. All I see for sure is I'll call merge()
when rejoining the nested lists

Might also need a helper that breaks a list in 2 if it has more than
1 element. Not sure what part of that to make recursive.

C
I understand what's expected. Still not 100% on how to acheive it.

H
function merge_sort(list):
 if list is small enough (len <= 1):  # base case
   return list
 else:
   split list into left_half and right_half until base case
   sorted_left = merge_sort(left_half)  # recursive call
   sorted_right = merge_sort(right_half)  # recursive call
   return merge(sorted_left, sorted_right)  # using your merge function

D
we heard you like lists, so we put some lists in your lists

A
function merge_sort(list):
 if list is small enough (len <= 1):  # base case
   return list
 else:
   split list into left_half and right_half until base case
   sorted_left = merge_sort(left_half)  # recursive call
   sorted_right = merge_sort(right_half)  # recursive call
   return merge(sorted_left, sorted_right)  # using your merge function

C
"""
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst

#     sorted_left = merge_sort(lst[:len(lst) // 2])
#     sorted_right = merge_sort(lst[len(lst) // 2:])
    
#     return merge(sorted_left, sorted_right)


# # All of these examples should print True
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

# original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']
# print(merge_sort(original) == expected)

# original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
#             43, 5, 25, 35, 18, 46]
# expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
#             35, 37, 43, 46, 51, 54]
# print(merge_sort(original) == expected)

"""
It is quite common to find yourself in a situation where you need to perform 
a search on some data to find something you're looking for. Imagine that you 
need to search through an old-fashioned phone book. Back in the day, phone 
books were printed every year by phone companies. The phone books contained 
an alphabetical list (by last name) of every customer, together with their 
phone number. A straightforward way to search the phone book would be to go 
through the phone book one name at a time, checking whether the current name 
is the one you're trying to find.

This may be a simple and easy way to search, but it's not very efficient. 
In the worst case scenario, it could mean having to search through every 
single name in the book, and some phone books could be over 1000 pages. 
A linear search such as this can take quite a long time.

A binary search is a much more efficient alternative. This algorithm lets you 
cut the search area in half on each iteration by discarding the half that you 
know your search term doesn't exist in. The binary search algorithm is able 
to do this by relying on the data being sorted. Going back to the phone book 
example, let's say that we're searching the following phone_book data for the 
search item 'Smith':

# Phone book data
phone_book = [
    'Embry',
    'Hanson',
    'Hawkins',
    'John',
    'Lee',
    'Seeli',
    'Smith',
    'Zimmer',
]

With a linear search, we would have to sequentially go through each of the 
names until we found the search item, 'Smith'. In a binary search, however, 
the following sequence happens:

Retrieve the middle value from the data (assume truncation to integer) --> 'John'.
If the middle value is equal to 'Smith', stop the search.
If the middle value is less than 'Smith':
Discard the lower half, including the middle value --> 
    `['Embry', 'Hanson', 'Hawkins', 'John'].
Repeat the process from the top, using the upper half as the starting data --> 
    ['Lee', 'Seeli', 'Smith', 'Zimmer'].
If the middle value is greater than 'Smith', do the same as the previous step, 
but with opposite halves.
Using the process described above, the search successfully ends on the third 
iteration when the middle value is 'Smith'. For an 8-element list like this, 
we need, at most, 3 iterations. For an 8000-element list, we need, at most, 
just 13 iterations. For 8,000,000 elements, we need just 23 iterations. This 
is incredibly efficient.

Implement a binary_search function that takes a list and a search item as 
arguments, and returns the index of the search item if found, or -1 otherwise. 
You may assume that the list argument will always be sorted.

P
Input: list, "search item" (string or int in examples (probably any type))
Output: int reprenting index of target "search item", or -1 if not found
Explicit:
1 target an index halfway through the list and see if its element is higher 
    or lower in value than the search item
2 if it's lower, repeat with the 2nd half of the list
3 if higher, repeat with 1st half
4 repeat until target index holds search item
5 return index of search item
6 assume input is non-empty and already sorted
Implicit:
?

E
binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
looks like I'll want a similar operation to what was used in `merge_sort`
    probably also recursive, or maybe just a while loop
    base case being ele_at_target_index == search_item
So:
len([1, 5, 7, 11, 23, 65, 89, 102]) == 8
set target to len(list) // 2 (-> 4)
list[4] == 11 -> too low
since too low, check upper/rightmost portion of list
    or can think of as ADD to target index 1/2 of difference between
        len(list) and target_index
        yeah, I like this better than actually altering the list
so target_idx += (len(list) - target_idx) // 2 
    > 4 += (8 - 4) // 2 (-> 2) == 6
    (use -= if element at target_idx is too high)
list[6] == 65 -> too low
so repeat target_idx += (len(list) - target_idx) // 2
    > 6 += (8 - 6) // 2 (-> 1) == 7
list[7] == 89 -> MATCH!
return target_idx == 7
Oh. Off by 1 error that whole time. Use (len(list) - 1) in place of len(list)
    to correct.

C
check

H
1 target an index halfway through the list and see if its element is higher 
    or lower in value than the search item
2 if it's lower, repeat with the 2nd half of the list
3 if higher, repeat with 1st half
4 repeat until target index holds search item
5 return index of search item

D
list input
int output

A
init max_idx = len(list) - 1
init target_idx = max_idx // 2
1 target an index halfway through the list and see if its element is higher 
    or lower in value than the search item
2 if it's lower, repeat with the 2nd half of the list
3 if higher, repeat with 1st half
    - this isn't working as expected
        i.e. (8 - 2) // 2 == 3, when I need 1 to make it work
4 repeat until target index holds search item
5 return index of search item

C
"""
# def binary_search(lst, search_item):
#     max_idx = len(lst) - 1
#     min_idx = 0

#     while min_idx <= max_idx:
#         target_idx = min_idx + (max_idx - min_idx) // 2

#         if lst[target_idx] == search_item:
#             return target_idx
#         elif lst[target_idx] < search_item:
#             min_idx = target_idx + 1
#         elif lst[target_idx] > search_item:
#             max_idx = target_idx - 1


#     return -1

# # All of these examples should print True
# businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
#               'Donuts R Us', 'Eat a Lot', 'Good Food',
#               'Pasta Place', 'Pizzeria', 'Tiki Lounge',
#               'Zooper']
# print(binary_search(businesses, 'Pizzeria') == 7)
# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
#          'Tyler']
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)

"""
A Rational Number is any number that can be represented as the result of the 
division between two integers, e.g., 1/3, 3/2, 22/7, etc. The number to the 
left is called the numerator, and the number to the right is called the denominator.

A Unit Fraction is a rational number where the numerator is 1.

An Egyptian Fraction is the sum of a series of distinct unit fractions 
(no two are the same), such as:

1   1    1    1
- + - + -- + --
2   3   13   15

Every positive rational number can be written as an Egyptian fraction. 
For example:

    1   1   1   1
2 = - + - + - + -
    1   2   3   6

Write two functions: one that takes a Rational number as an argument, and 
returns a list of the denominators that are part of an Egyptian Fraction 
representation of the number, and another that takes a list of numbers in the 
same format, and calculates the resulting Rational number. You will need to 
use the Fraction class provided by the fractions module.
"""
from fractions import Fraction

def egyptian():
    pass

def unegyption():
    pass


# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))