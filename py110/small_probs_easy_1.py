# 1
# P
# Write a program that solicits six (6) numbers from the user and prints 
# a message that describes whether the sixth number appears among the first five.
# Take 6 individual number inputs.
# Print a message determined by final number membership in first 5 numbers.
# It looks as if all inputs will be ints. I will assume that for the exercise.
# I will also asusme that the input and output messages don't have 
# to be formatted exactly as shown. Coding the input messages would take extra time.

# E
# Example 1
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17
#
# 17 is in 25,15,20,17,23.
#
#
# Example 2
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

# D
# Input values will need to be collected. A list will work.
# The final input will be a separate object that can be
# checked for membership in the collection.

# A
# 1. Initialize an empty list.
# 2. Use a for loop to collect 5 ints and save them to the list.
# 3. Initialize a variable as the final input.
# 4. Check the variable for membership in the list.

# C

# def membership(list_of_ints, integer):
#     int_string = ",".join(list_of_ints)
#     if integer in list_of_ints:
#         return f"{integer} is in {int_string}"
    
#     return f"{integer} is not in {int_string}"

# int_list = []
# for i in range(1, 6):
#     int_list.append(input("Enter an integer: "))

# last_int = input("Enter the last integer: ")

# print(membership(int_list, last_int))


# 2
# P
# Write a function that returns True if the string passed as an argument 
# is a palindrome,False otherwise. A palindrome reads the same forwards and backwards. 
# For this problem, the case matters and all characters matter.
# Explicit Rules:
# 1 all characters matter
# 2 case matters
# 3 must be exactly the same forwards and backwards
# Implicit Rules:
# 1 in a string with odd number of characters, middle character won't matter
# 2 numbers and special characters are checked the same as letters
#
# Example tests will be included below. Not seeing any new info in the tests.
#
# D
# Strings will be used, most likely with slicing. I don't think any other data
# structures will be used (if indeed a string can be considered a data structure).
#
# A
# 1 take string as parameter
# 2 check if string length is even or odd - len(str)%2
# 3 check if the first character and last character are equal
# 4a if even, repeat step 3 for the second and second to last, etc, until all are checked
# 4b if odd, do the same as 4a but ignore the middle character
# 5 return True if all equal, False if not

# C

# def is_palindrome(input):
#     return input == input[::-1]

# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)


# 3
# P
# Write another function that returns True if the string passed as an argument is a palindrome, 
# or False otherwise. This time, however, your function should be case-insensitive, and should 
# ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the 
# is_palindrome function you wrote in the previous exercise.
# Explicit Rules
# 1 only alphanumeric characters matter
# 2 case is to be ignored
# 3 given 1 and 2, must be the same forwards as backwards
# Implicit Rules
# 1 in a string with odd number of characters, middle character won't matter

# E
# Examples included below funtion. No new information.

# D
# String input, a new string for the "cleaned" input. Again, are strings data structures?

# A
# 1 take string as parameter
# 2 clean the string
#   - initialize new empty string
#   - copy only alphanumeric chars to new string
#   - convert new string to lower case
# 3 check if new string is palindrome w/ slicing [::-1]
# 4 return True if yes, False if no

# C

# def is_real_palindrome(input):
#     clean_string = ""
#     for char in input:
#         if char.isalnum():
#             clean_string += char.casefold()

#     return clean_string == clean_string[::-1]

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True


# 4
# P
# Write a function that takes a list of numbers and returns a list with the same number 
# of elements, but with each element's value being the running total from the original list.
# Explicitly:
# 1 take a list of numbers as input (example cases seem to require ints)
# 2 return a list with numbers being the running total of elements in the input list
# Implicitly:
# 1 numbers here means ints

# E
# Test cases below. Looks like only ints are used, empty lists are fine, as are single element lists.

# D
# Lists in and out. Doesn't look like any others are needed.

# A
# 1 take a list as a parameter
# 2 initialize a new empty list
# 3 for int in parameter list, sum all elements up to and including that int
# 4 append result to new list
# 5 return new list

# C

# def running_total(input_list):
#     running_total = []
#     for i, _ in enumerate(input_list):
#         running_total.append(sum(input_list[:i+1]))

#     return running_total

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True


# 5 and 6
# P
# Write a function that takes a string consisting of zero or more space-separated words and 
# returns a dictionary that shows the number of words of different sizes.
# Words consist of any sequence of non-space characters.
# For 6, non-alpha characters do not count.
# Explicitly
# 1 take a string of any size
# 2 return a dictionary with the number of words of each different size
# 3 "words" are any sequence of non-space characters in 5, not in 6
# Implicitly
# 1 the keys should be the word sizes, since we will only count each size once
# 2 the values will be the count for each size
# 3 all whitespace must be removed, so .split() may not be enough cleaning
# 4 punctuation, etc. are part of the words, i.e. 'doc?' is a 4 character word
# 4.5 in 6, 'doc?' is a 3 character word

# E
# Tests are below. No new inpormation except that I'm seeing none of the tests involve sequences
# of multiple whitespace characters, so .split() should be sufficient to prep for counting.
# In 6, it'll be better to make a new string with the non-alpha characters removed before splitting.

# D
# String in, dict of strings out. Might also use a list or dict view object in the counting.

# A
# 1 take a string as a parameter
# 1.5 remove characters other than letters and spaces
# 2 use .split() to create a collection of substrings (words), assign to list
# 3 initialiaze empty dict
# 4 for substring in list, get length of substring
# 5a if length is not a dict key, add it with the value 1
# 5b if length is a dict key, add 1 to the value
# 6 return dict

# C

# def word_sizes(input_string):
#     cleaned_string = ''.join([c for c in input_string 
#                               if c.isalpha() or c.isspace()])
#     word_list = cleaned_string.split()
#     lengths = {}

#     for word in word_list:
#         if len(word) not in lengths:
#             lengths[len(word)] = 1
#         else:
#             lengths[len(word)] += 1
    
#     return lengths

# # All of these examples should print True

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

# string = 'Humpty Dumpty sat on a wall'
# print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

# print(word_sizes('') == {})

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})


# 7
# P
# Given a string of words separated by spaces, write a 
# function that swaps the first and last letters of every word.
# You may assume that every word contains at least one letter, 
# and that the string will always contain at least one word. 
# You may also assume that each string contains nothing but 
# words and spaces, and that there are no leading, trailing, 
# or repeated spaces.
# Explicitly
# 1 Use a function to swap first and last letters of every word
# 2 Words are separated by spaces and contain at least 1 letter
# 3 There will always be at least 1 word
# 4 All strings contain words and space, no leading, trailing,
#   or repeated spaces
# Implicitly
# 1 There are no special characters

# E
# Example test cases in code below. No new info.

# D
# Probably a list of split words.

# A
# 1 define a function that takes a string as parameter
# 2 split the string into a list of individual words
# 3 for each word in list, swap the first and last letters
# 4 join the transformed words, separated by spaces
# 5 return the new string

# C
# def swap(input_string):
#     words = input_string.split()
#     for i, word in enumerate(words):
#         swapped = word[-1:] + word[1:-1] + word[:1] \
#             if len(word) > 1 else word
#         words[i] = swapped

#     return ' '.join(words)

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# 8
# P
# Write a function that takes a string of digits and returns 
# the appropriate number as an integer. You may not use any 
# of the standard conversion functions available in Python, 
# such as int. Your function should calculate the result by 
# using the characters in the string.
# For now, do not worry about leading + or - signs, nor 
# should you worry about invalid characters; 
# assume all characters are numeric.
# Explicitly
# 1 Convert a string of digits into an int
# 2 Do not use int() or other built-in conversion functions
# 3 Calculate the result by using the characters in the string
# Implicitly
# 1 it may be necessary to use ASCII codes
# 2 and/or maybe use a loop to replace each character

# E
# Example tests in code below. No new info.

# D
# List or dict, very likely. Could make a dict with
# letters as keys and ints as values.

# A
# 1 Define a function that takes a string of digits
# 2 Init dictionary of KVPs such as '1': 1 for each digit
# 3 Init variable with 0
# 4 For chr in string, find the dict key that matches chr
# 5 Multiple int variable by 10 and add value for key
#   So if the input is "45": 0 * 10 + 4 == 4, 4 * 10 + 5 == 45

# C
# def string_to_integer(string_of_digits):
#     int_pairs = {'1': 1, '2': 2, '3': 3, 
#                  '4': 4, '5': 5, '6': 6, 
#                  '7': 7, '8': 8, '9': 9, '0': 0}
#     output = 0

#     for char in string_of_digits:
#         output = (output * 10) + int_pairs[char]

#     return output

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True


# 9
# P
# Write a function that takes a string of digits and returns 
# the appropriate number as an integer. The string may have 
# a leading + or - sign; if the first character is a +, your 
# function should return a positive number; if it is a -, 
# your function should return a negative number. If there is 
# no sign, return a positive number.
# Like the previous exercise, no built-in conversions.
# Using the function from the previous exercise is fine.
# Explicitly:
# 1 Same as before BUT
# 2 the input may be signed
# 3 return the correctly signed integer as output
# Implicitly
# 1 '+' can be ignored, since the output will be 
#   positive by default

# Examples in code, no surprises.

# Dicts, same as before

# A
# 1 copy string_to_integer function
# 2 if first char is '+', remove '+' then proceed as before
# 3 if first char is '-', make int output negative

# C
# def string_to_integer(string_of_digits, negative):
    # int_pairs = {'1': 1, '2': 2, '3': 3, 
    #              '4': 4, '5': 5, '6': 6, 
    #              '7': 7, '8': 8, '9': 9, '0': 0}
#     output = 0

#     for char in string_of_digits:
#         output = (output * 10) + int_pairs[char]

#     if negative:
#         output = -output

#     return output

# def string_to_signed_integer(signed_string_of_digits):
#     if signed_string_of_digits[0] == '+':
#         signed_string_of_digits = signed_string_of_digits.lstrip('+')
#         negative = False
#     elif signed_string_of_digits[0] == '-':
#         signed_string_of_digits = signed_string_of_digits.lstrip('-')
#         negative = True
#     else:
#         negative = False

#     return string_to_integer(signed_string_of_digits, negative)
    

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

# 10
# P
# In the previous two exercises, you developed functions that 
# convert simple numeric strings to signed integers. In this 
# exercise and the next, you're going to reverse those functions.
# Write a function that converts a non-negative integer value 
# (e.g., 0, 1, 2, 3, and so on) to the string representation 
# of that integer.
# You may not use any of the standard conversion functions 
# available in Python, such as str. Your function should do 
# this the old-fashioned way and construct the string by 
# analyzing and manipulating the number.
# Explicitly
# 1 convert integers to strings
# 2 don't use str(), etc.

# E
# Tests in code below. Ints will have at least 1 character
# and can have 10 or maybe more.

# D
# Possibly a dict will still be helpful. Could even use the same
# one as before and change my code.

# A
# 1 define a function that takes an integer argument
# 2 init a dict of int: str pairs (or vice-verse)
# 3 init an empty string
# 4 use division and/or modulo to retreive each digit
#   from the int
# 5 for each digit, add the corrosponding dict value to string

# def integer_to_string(integer):
#     int_pairs = {1: '1', 2: '2', 3: '3', 
#              4: '4', 5: '5', 6: '6', 
#              7: '7', 8: '8', 9: '9', 0: '0'}
#     output = ''

#     while integer > 0:
#         integer, remainder = divmod(integer, 10)
#         output = int_pairs[remainder] + output

#     return output or "0"
    

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True


# 10
# P
# In the previous exercise, you developed a function that 
# converts non-negative numbers to strings. In this exercise, 
# you're going to extend that function by adding the ability 
# to represent negative numbers as well.
# Write a function that takes an integer and converts 
# it to a string representation.
# Explicitly
# 1 Same as 2 probs ago, extend last function to include negs
# Implicitly
# 1 From the test cases, looks like I SHOULD add a '+'
#   to positive numbers
# 2 looks like 0 should remain unsigned

# Example tests in code

# D
# Dict from before

# A
# Same function as before
# But add a helper function with match case and a 3-way flag
#   that can be set to '+','-', or ''

# C

def integer_to_string(integer, sign):
    int_pairs = {1: '1', 2: '2', 3: '3', 
             4: '4', 5: '5', 6: '6', 
             7: '7', 8: '8', 9: '9', 0: '0'}
    output = ''

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        output = int_pairs[remainder] + output
    
    output = sign + output

    return output or "0"

def signed_integer_to_string(number):
    if number > 0:
        sign = '+'
    elif number < 0:
        sign = '-'
    else:
        sign = ''

    return integer_to_string(abs(number), sign)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True