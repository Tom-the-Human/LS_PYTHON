# 1
# P
# Compute and display the total age of the family's male members. 
# Try working out the answer two ways: first with an 
# ordinary loop, then with a comprehension.
# The result should be 444.
# Explicitly
# Sum the ages of the male family members:
#    first with a loop, then with a comprehension.
# Implicitly
# 1 It is necessary to select only male family members.

# E
# The input is a dict of nested dicts as follows:
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# From this we can see that Herman, Grandpa, and Eddie indeed have
# a total age of 444. I see no other new information.

# D
# Dicts of course. Maybe a list to collect extracted ages.

# A
# 0 Initialize a total age variable to 0
# 1 Create a for loop that iterates through the outer dict
# 2 For each person, check 'gender'
# 3 If 'gender' is 'male', add 'age' to total age
# 4 Print total age
# 5 Steps 1-4 on single line in a comprehension
# 6 Print outcome of comprehension

# C
total_age = 0
for munster in munsters.values():
    if munster['gender'] == 'male':
        total_age += munster['age']
print(total_age)

age_total = sum(munsters[person]['age'] for person in munsters 
                if munsters[person]['gender'] == 'male')
print((age_total))

# 2
# P
# Given the following data structure, return a new list with 
# the same structure, but with the values in each sublist ordered 
# in ascending order. Use a comprehension if you can. 
# (Try using a for loop first.)
# Explicitly
# 1 Return NEW list with sorted sublists
# 2 Use a for loop first
# 3 then use a comprehension
# 4 Values in the sublists must be in ascending order
# Implicitly
# 1 Will require sorted() so as not to destroy input list
# 2 Objects in the main list should be in the original order
# Questions
# Is it ok to mutate the sublists if the copied list is different?
# Or should the sublists be copied to avoid destruction as well?

# E
# Expected output:
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
# Original list is in the code below. It is still unclear if
# mutating the original substring is ok, so I won't.

# D
# Nested lists

# A
# 0 import copy
# 1 Define a function that takes a list as argument
# 2 Use deepcopy to copy the entire nested data structure
# 3 for sublist in copy_lst, sort sublist
# 4 return copy_list
# 5 do 1-4 with a single comprehension

# C
import copy

# def sublist_sort(in_list):
#     copy_list = copy.deepcopy(in_list)
#     for sublist in copy_list:
#         sublist.sort()
    
#     return copy_list

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# print(sublist_sort(lst))
# print(lst)

# new_list = [sorted(sublist) for sublist in lst]
# print(new_list)
# print(lst)


# 3
# P
# Given the following data structure, return a new list with the 
# same structure, but with the values in each sublist ordered in 
# ascending order as strings (that is, the numbers should be 
# treated as strings). Use a comprehension if you can. 
# (Try using a for loop first.)
# This is very similar to the last problem, with the added rule
# that the output must be sorted as strings. 
# implicitly, this will require the ints to be coerced to strings
# and then coerced back again to match the expected output.

# E
# Expected output:
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

# D
# Same as before

# A
# 1 copy code from previous exercise
# 2 insert a nested for loop before sorting to target the ints
# 3 in the nested loop, coerce ints to strs
# 4 use another nested loop to coerce them back after sorting
# 5 [sorted(sublist) for str(sublist) in lst] ??

# C
def sublist_sort(in_list):
    copy_list = copy.deepcopy(in_list)
    for sublist in copy_list:
        for object in sublist:  # This approach isn't working right,
            str(object)         # but it's not worth figuring out why
        sublist.sort()          # at this moment. Maybe later.
    
    for object in copy_list[1]:
        int(object)
    
    return copy_list

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
print(sublist_sort(lst))
print(lst)

new_list = [sorted(sublist, key=str) for sublist in lst]
print(new_list)
print(lst)


# 4
# P
# Given the following data structure, write some code 
# that defines a dictionary where the key is the first 
# item in each sublist, and the value is the second.
# Explictly
# 1 The input is a list of two object sublists (example below).
# 2 Convert the sublists to key value pairs
# Implicitly
# 1 the objects are of a variety of types, so the
#       code should be type agnostic
# 2 all the objects to be used as keys are strings
#       so are valid key types

# E
# Expected output:
# # Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }

# D
# Primarily lists and dicts. Not seeing a need for others.

# A
# Can this be a comprehension? Seems probable.
# 1 {key: value for sublist in lst} ???

# C
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

my_dict = {sublist[0]:sublist[1] for sublist in lst}
print(my_dict)

# 5
# P
# Given the following data structure, sort the list so that 
# the sub-lists are ordered based on the sum of the odd numbers 
# that they contain. You shouldn't mutate the original list.
# Try to use a comprehension in your solution.
# Explicitly
# 1 Do not mutate the original list.
# 2 Sum only the odd numbers.
# 3 Sort so that the sublists are ordered by sum of odds.
# Implicitly
# 1 The sublists should be in ascending order,
#   judging by expected output.

# E
# Expected output:
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

# D
# Nested lists

# A
# Unsure if it's possible to do the entire thing in a comprehension
#   or if a comprehension is only part of the solution.
# 1 for sublist in list, sum odd nums
# 2 sort list based on sum values (ascending)

def odd_sum(sublist):
    odds = [num for num in sublist if num % 2 == 1]

    return sum(odds)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

new_list = sorted(lst, key=odd_sum)
print(new_list)

# 6
# P
# Given the following data structure, return a new list 
# identical in structure to the original, but with each 
# number incremented by 1. Do not modify the original 
# data structure. Use a comprehension.
# Explicitly
# 1 Increment each number by 1 without modifying the original data
# 2 Return a new list structured like the original
# 3 Use a comprehension
# Implicitly
# 1 The numbers are all dict values, so we'll use dict.values()

# E
# Expected result:
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# D
# List of dicts

# A
# 1 dict for dict in list
# 2 key=add_1
# 3 def add_1(dict), for each key, add 1 to value

# C
# def add_1(in_dict):
#     return {key: value + 1 for key, value in in_dict.items()}
        

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# new_list = [add_1(d) for d in lst]
# can be done instead with a single comprehension!
new_list = [{key: value + 1 for key, value in d.items()} for d in lst]
print(new_list, lst, sep='\n')


# 7
# P
# Given the following data structure return a new list identical 
# in structure to the original, but containing only the numbers 
# that are multiples of 3. Try to use a comprehension for this. 
# However, we recommend first trying it without comprehensions.
# Explicitly
# 1 Return a new list with identical structure to the first
# 2 it must contain only the multiples of 3
# 3 First, try without comprehensions, then with them.
# Implicitly
# 1 Disregard non-multiples of 3, maybe with num % 3 == 0
# 2 Numbers are ints in sublists, so nested loops may be used

# E
# Expected result:
# [[], [3, 12], [9], [15, 18]]

# D
# Listses

# A
# 1 def function that takes sublist as argument
# 2 for sublist, return new sublist with only multiples of 3
# 3 condense to comprehension

# C
# def triples_only(sublist):
#     new_sub = []
#     for num in sublist:
#         if num % 3 == 0:
#             new_sub.append(num)
    
#     return new_sub

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# new_list = []
# for sub in lst:
#     new_list.append(triples_only(sub))
# ^ w/o comprehensions
#new_list = [triples_only(sublist) for sublist in lst]
# ^ sort of a hybrid approach
new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
# ^ single comprehension
print(new_list)


# 8
# P
# Given the following data structure, write some code to return 
# a list that contains the colors of the fruits and the sizes 
# of the vegetables. The sizes should be uppercase, and the 
# colors should be capitalized.
# Explicitly
# 1 Return a list that contains the colors of the fruits
#   and sizes of the vegetables
# 2 Sizes must be uppercase
# 3 Colors must be capitalized (first letter uppercase)
# Implicitly
# 1 input is nested dicts, so dict view object will help
# 2 colors are in lists as dict values in nested dicts,
#   but according to the output the color strings don't
#   need to be extracted from their lists

# E
# Expected result:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
# More than one color can be given for a fruit

# D
# Dicts and lists

# A
# How can I make the best use of comprehensions for this?
# 1 identify keys and indices of relevant information
#   i.e. dict1['grape']['type'] and dict1['grape']['colors']
# 2 initialize a new empty list
# 3 apply the correct string method to the appropriate string
#   i.e. dict1['grape']['colors'][0].capitalize()
#   or dict1['carrot']['size'].upper()
# 4 append resulting string to new list
# 5 return new list
# subdict['colors'][i].capitalize() for i in 'colors' 
#                   if subdict['type'] == 'fruit'
# subdict['size'].upper() for subdict['size'] in dict1 
#                   if subdict['type'] == 'vegetable'

# C
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

result = [[color.capitalize() for color in item['colors']] 
          if item['type'] == 'fruit' 
          else item['size'].upper() 
          for item in dict1.values()]
# AI assisted
print(result)


# 9
# P
# Given the following data structure, write some code 
# to return a list that contains only the dictionaries 
# where all the numbers are even.
# Explicitly
# 1 Return a list
# 2 The list should only contain the dicts 
#   where all numbers are even
# Implicitly
# 1 Check the values to select only even numbers

# E
# Expected output:
# [{e: [8], f: [6, 10]}]
# Values are lists of ints.

# D
# Lists, dicts, lists

# A
# 1 define a function that checks the values of the dicts,
#   it should begin by initializing a new list
# 2 for each value (sublist), check the values of ints
# 3 if all ints in all sublists are even, 
#   add the dict to the new list
# 4 return new list
# 5 refactor to use comprehensions?

# C
def only_evens(input_dict):
    for sublist in input_dict.values():
        if not all(value % 2 == 0 for value in sublist):
            return False
        
    return True


lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new_list = [d for d in lst if only_evens(d)]
print(new_list)

# 10
# P
# Write a function that takes no arguments and 
# returns a string that contains a UUID.
# 1 An UUID consists of 32 characters broken up into an 
#   8-4-4-4-12 pattern
# 2 The characters are all hexadecimal (0-9 + a-f)
# 3 return a string

# E
# Example - 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

# D
# Unsure if any needed, maybe lists

# A
# 1 import random
# 2 create const string of valid hex chars
# 3 in function, create a string of 8 random chars from const
# 4 repeat for 3 strings of length 4, and 1 of length 12
# 5 join all strings with '-'
# 6 return resulting string

import random
HEX = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']

def uuid_maker():
    str1 = ''.join([random.choice(HEX) for _ in range(8)])
    str2 = ''.join([random.choice(HEX) for _ in range(4)])
    str3 = ''.join([random.choice(HEX) for _ in range(4)])
    str4 = ''.join([random.choice(HEX) for _ in range(4)])
    str5 = ''.join([random.choice(HEX) for _ in range(12)])
    str_list = [str1, str2, str3, str4, str5]
    return '-'.join(str_list)

print(uuid_maker())


# 11
# P
# The following dictionary has list values that contain strings. 
# Write some code to create a list of every vowel (a, e, i, o, u) 
# that appears in the contained strings, then print it.
# Extra Challenge: Once your nested loop code works, try 
# to refactor the code so it uses a single list comprehension.
# Explicitly
# Create a list of every vowel that appears in the listed strings
# Working with nested lists as dict values
# Print the new list
# Implicitly
# ?

# E
# Expected output:
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
# No surprises here.

# D
# Dict of lists. Make a new list.

# A
# 0 init new empty list
# 1 create membership variable for vowels
# 2 for each string in each list in the dict,
#   check each chr for membership
# 3 if member, add to new list
# 4 print list

# C
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []
vowel_string = 'aeiouAEIOU'

for lst in dict1.values():
    for string in lst:
        for chr in string:
            if chr in vowel_string:
                list_of_vowels.append(chr)

chars = [chr for lst in dict1.values()
         for string in lst
         for chr in string if chr in vowel_string]

print(list_of_vowels)
print(chars)