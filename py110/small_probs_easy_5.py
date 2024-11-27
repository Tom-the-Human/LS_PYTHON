"""
1
P
Given a dictionary where both keys and values are unique, invert this 
dictionary so that its keys become values and its values become keys.

E
Test shows all string keys and values.

D
Dict, maybe dict view obj??? Or lists. Some way to swap the strings.

A
Oh, I bet this is an easy comprehension. 
"""

# def invert_dict(dictionary):
#     return {dictionary[food]: food for food in dictionary}

# print(invert_dict({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#       }) == {
#           'fruit': 'apple',
#           'vegetable': 'broccoli',
#           'fish': 'salmon',
#       })  # True

"""
2
P
Given a dictionary and a list of keys, produce a new dictionary that only
 contains the key/value pairs for the specified keys.
1 return a dict of only the specified pairs

E
No new info

D
Lists,dicts

A
Can likely be a comprehension
{item: dict[item] for item in dict if item in keys}
"""

# def keep_keys(input_dict, keys):
#     return {item: input_dict[item] for item in input_dict if item in keys}

# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }

# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True

"""
3
P
Write a function that takes a list of strings and returns a list of the same 
string values, but with all vowels (a, e, i, o, u) removed.
1 remove all vowels from the strings in the input list
2 return list of modified strings

E
No surprises.

D
Lists

A
Will need a loop to remove vowels, and also a list of vowels
1 init vowel list
2 for string in list, for char in string
    if char.casefold() in vowels, remove char
"""

# def remove_vowels(original):
#     vowels = 'aeiouAEIOU'
    
#     return [''.join(char for char in string if char not in vowels)
#             for string in original]

# # All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True

# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True

# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True

"""
4
P
Write a function that takes a string as an argument and returns a list that
 contains every word from the string, with each word followed by a space and
   the word's length. If the argument is an empty string or if no argument is
     passed, the function should return an empty list.

You may assume that every pair of words in the string will
 be separated by a single space.
1 return a list of strings
2 the list should have each individual word of the input followed by a number
3 the number should represent the number of letters in the word (length)

E
From the 3rd example, it looks like punctuation should be treated the same
as other characters, i.e. counted and not removed

D
Output list. Might possibly need another list or something to hold the lengths

A
- use split to get a list of words
- use a loop and len() on the list to get a list of lengths
    - coerce to string
- zip the words and lengths together
"""
# def word_lengths(input=''):
#     words = input.split()
#     lengths = [str(len(word)) for word in words]

#     return [' '.join(pair) for pair in zip(words, lengths)]


# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

"""
5
P
Given two lists of integers of the same length, return a new list where each 
element is the product of the corresponding elements from the two lists.
1 return a list
2 multiply the integers at the same indices in 2 different lists

E
Test case looks pretty basic.

D
Lists, nothing else needed

A
Zip the lists together and multiply the elements of each pair 
Can be done in comprehension
1 zip lists
2 pair[0] * pair[1] for pair

Had some trouble with an extra pair of paranthesis,
which made the generator not work right.
"""

# def multiply_items(list_a, list_b):
#     return [(pair[0] * pair[1]) for pair in zip(list_a, list_b)]

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

"""
6
P
Write a function that takes a list of numbers and returns the sum of the sums 
of each leading subsequence in that list. Examine the examples to see what we 
mean. You may assume that the list always contains at least one number.
1

E
Examples clarify the problem. Basically, each number will be added a number of
times inversely related to its position in the list. The int at the last index
only gets included once, the second to last twice, third to last 3 times, etc.

So basically, we'll loop through, at each iteration adding every element up to
the current one. 

D
List input

A
- init total = 0
- for index in list, sum a list of elements from 0 to current index and
- add that sum to total
- return total
"""

# def sum_of_sums(input_list):
#     total = 0
#     for i in range(len(input_list)):
#         total += sum([num for num in input_list[:i + 1]])

#     return total

# print(sum_of_sums([3, 5, 2]) == 21)               # True
# # (3) + (3 + 5) + (3 + 5 + 2) --> 21

# print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# print(sum_of_sums([4]) == 4)                      # True

"""
7
P
Write a function that takes one argument, a positive integer, 
and returns the sum of its digits.

E
Examples clarify but don't provide any new info

D
Will need to extract digits to a list. Probably no need for any others

A
There's a couple of ways to go about this. I can get the digits with math or
with coercion. Let's go with coercion on this one.
- [int(char) for char in str(number)] should work to get list of digits
- return sum(list)
"""

# def sum_digits(number):
#     return sum([int(char) for char in str(number)])

# print(sum_digits(23) == 5)              # True
# print(sum_digits(496) == 19)            # True
# print(sum_digits(123456789) == 45)      # True

"""
8
P
Write a function that takes a string as an argument and returns that string 
with a staggered capitalization scheme. Every other character, starting from 
the first, should be capitalized and should be followed by a lowercase or 
non-alphabetic character. Non-alphabetic characters should not be changed, 
but should be counted as characters for determining when to switch between 
upper and lower case. (Ok, this looks a little trickier)
1 First char is caps, second is lower, third caps, etc
2 Ignore non-alphas but still count them for determining case of following chr
    - that actually makes this easier
    - if an index is `i % 2 == 0` and alpha it is caps
    - elif alpha is lower
    - else continue

E
No new info

D
Might be necessary to use a list

A
Since strings are immutable, I'm thinking I need to collect the chars I need
in a list and then join the list. So:
- for each char in the string, determine what char to add to the list,
- add it,
- then join the list
might be able to do most of this with a comprehension.
"""

# def staggered_case(string):
#     output = []
#     for i, char in enumerate(string):
#         if i % 2 == 0:
#             output.append(char.upper())
#         else:
#             output.append(char.lower())
    
#     return ''.join(output)

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

"""
9
P
Modify the function from the previous exercise so it ignores non-alphabetic 
characters when determining whether it should uppercase or lowercase each 
letter. The non-alphabetic characters should still be included in the return 
value; they just don't count when toggling the desired case.
1 Don't change case for non-alpha characters
    - this seems to add a lot of complexity, since we can't just use a basic
        index check to determine case
    - but since I'm calling my previous function, maybe it's not that complex

E
No news here

D
Not sure if any additional structures needed. Possibly another list.

A
Ok ... could create some kind of toggle indicator, like if isalpha and isupper
next char is lower, if isalpha and islower then next char is upper.
`isalpha` will be critical here. 
last_alpha?
Seems like I need to actually modify the function, not add a helper. After all,
`i % 2 == 0` is no longer a good determinant, unless I first remove all the 
non-alphas from the string, and I want to keep those IN the string.
But if I do that, is that even the same function anymore? 
"""

# def staggered_case(string):
#     output = []
#     last_alpha = ''

#     for i, char in enumerate(string):
#         if last_alpha.islower() or not last_alpha:
#            char = char.upper()
#         else:
#             char = char.lower()

#         output.append(char)
#         if char.isalpha():
#             last_alpha = char
    
#     return ''.join(output)

# string = 'I Love Launch School!'
# result = "I lOvE lAuNcH sChOoL!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_cApS"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True

"""
10
P
Given a sequence of integers, filter out instances where the same value occurs
 successively, retaining only the initial occurrence. 
 Return the refined sequence.
1 Specifically states return only the INITIAL occurence of a value where the
    same value occurs successively
2 Implicitly, the output values must be in order in the list. Though it looks
    like returning any instance of each value will be fine. I don't think
    Python can tell the difference between one `1` and another `1`, so long
    as the indices are correct and we aren't actually checking ID.

E
See rule 2 above

D
List in, list out. Should probably return a new list instead of mutating the
    one passed in.

A
- init an empty list
- for num in input list, if num not in output list, add num
- else continue
This is an easy comprehension!
Ok, so no, it looks like it isn't. Apparently checking for membership in
    output only happens once during the comprehension instead of at every
    iteration, like it would in a regular for loop? Need to explore this more.
Yeah, seems like that's the case. 
Probably exactly what this problem is meant to teach.
"""

def unique_sequence(original):
    output = []
#    output = [num for num in original if num != ]
    for num in original:
        if num not in output:
            output.append(num)

    return output

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True