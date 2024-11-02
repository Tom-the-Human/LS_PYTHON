# Given a list of strings, return a new list where the strings are sorted 
# based on the highest number of adjacent consonants a string contains. 
# If two strings contain the same highest number of adjacent consonants, 
# they should retain their original order in relation to each other. 
# Consonants are considered adjacent if they are next to each other in 
# the same word or if there is a space between two consonants in adjacent words.

# (P)roblem
# Input: list of strings
# Output: new list of strings sorted by number of adjacent consonants

# Explicit Rules
# 1. Output list is sorted based on highest number of adjacent consonants
# 2. If 2 strings have same count, retain original relative order
# 3. Adjacent means either next to each other in the same word or
#    in adjacent words (i.e. 'good dog' has adjacent 'd' characters)
#    In other words, consonants may be separated by a space and still be counted.
# 4. Output list should be a NEW list, so no mutation

# Implicit Rules
# 1. Spaces may be completely ignored during the counting process.
#    This means split or replace may be a good option here.

# Clarifying Questions
# Sort in ascending or descending count order?
# Is 'y' being considered a consonant or a vowel for this exercise?
# Should all substrings of consecutive consonants be counted or just consonant pairs?
# I.e. does 'three' have a value of 3 ('t', 'h', 'r') or 2 ('th', 'hr') or
#    even just 1 ('thr') for counting purposes? 
# Or are strings valued based on the longest consecutive string of consonants? 
# I.e. is 'three' (3 in a row) of higher value than
#    'friction' (2 instances of 2 in a row) -> (yes, see Data Structures below)

# (E)xamples and Tests
# Copied below the function.
# The test cases clarify some a little, but don't answer my questions. 
# They don't provide much insight about how the consecutive consonants are counted,
# since they are all low count and none of them have multiple sets of
# consecutive consonants, as in 'friction'. 

# (D)ata Structures
# Input and output must both be lists. It may also be worth using lists or tuples in
# the counting process, but perhaps not.
# The discussion point regarding potential use of a dictionary has inadvertently
# clarified my question about counting value. The string 'rstafgdjecc' is
# given a value of 4, which seems to indicate that what counts is the longest
# substring of consecutive consonants and nothing else. 

# (A)lgorithm
# Take a list of strings as a parameter
# Define a list to check each character for membership (vowels or consonants)
# Initialize a count variable to 0
# In a nested for loop, compare the character at each index of each string 
#   against the membership list. The outer loop will iterate through the input list,
#   and the inner loop will iterate through the string at each list index.
# To count only consecutive integers, the logic will need to be something like
#   "If last_char is in membership list and current_char is in membership list" ...
#   and I think we'll want to run string.replace(' ', '') in the outer loop for
#   this to work. But we'll want to use the original string in the output list,
#   so assigning the clean string to a variable may be required. 
#   last_char can be set at end of inner loop.
# For each word, we'll need to track the count, and words will have to be inserted
#   in output list at the proper relative position, so comparing counts is required.
# Thinking about this, it's becoming apparent that a dictionary would be very helpful.
# Each word from the list can be added to a dictionary in the order it is indexed in
#   the list. The word will be the key, and the count will be the value.
# Once all words in the list are evaluated, the dictionary keys will be put into
#   a new output list in the order of their value, highest to lowest. 
# Since dicts are ordered in modern Python, order should be maintained by default.
# Only we'll do a sort to find the highest value in the dict and add that key
#   to the list at index 0, or if none are highest, add the first key that ties for
#   highest value (how to find that?). Each time we do this, the item must be
#   removed from the dict. This requires another for loop. Maybe a helper function.
# The return value should be a list of reordered strings.

# (C)ode

def dict_to_sorted_list(word_dict):
    return_list = list(word_dict.keys())

    for i in range(len(return_list)):
        for j in range(i + 1, len(return_list)):
            if word_dict[return_list[i]] < word_dict[return_list[j]]:
                return_list[i], return_list[j] = return_list[j], return_list[i]
            elif word_dict[return_list[i]] == word_dict[return_list[j]]:
                if my_list.index(return_list[i]) > my_list.index(return_list[j]):
                    return_list[i], return_list[j] = return_list[j], return_list[i]

    return return_list

def sort_by_consonant_count(input_list):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    word_dict = {}
    last_char_is_cons = False

    for string in input_list:
        word_dict[string] = 0
        spaceless = string.replace(' ', '')
        for char in spaceless:
            if char not in vowel_list and last_char_is_cons:
                word_dict[string] += 1

            last_char_is_cons = char not in vowel_list
        last_char_is_cons = False

    return dict_to_sorted_list(word_dict)



my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

# This is not a good solution.
# I didn't understand the logic well enough before starting.
# By the time I realized this I was far enough in I didn't want to start over,
# So I asked an AI chatbot to help me fix my dict_to_sorted_list() function.
# It works but is difficult to read and understand. 
# `if` nested in `elif` nested in `for` nested in `for` ...