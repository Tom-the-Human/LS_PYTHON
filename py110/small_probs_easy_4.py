"""
1
P
Write a function that takes a list of integers between 0 and 19 and returns a 
list of those integers sorted based on the English word for each number:
(list of number words in code)
1 return the list sorted based on the English words for the numbers
    (basically an alphabetical sort)

E
Only 1 example, no new info

D
Lists, and maybe an intermediate dict to map the digits and words together.
Can't think of how I would solve this without a dict, actually.

A
1 init list of words
2 use a comprehension to make a dict of digits and words
3 another comprehension to make a list of dict values sorted by their keys
4 return sorted list
"""

words = ['zero',
        'one', 
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# def alphabetic_number_sort(input_list):
#     return sorted(input_list, key=lambda x: words[x])

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

"""
2
P
Given two lists, convert them to sets and return a new set
 which is the union of both sets.
1 return the union of 2 sets as a new set
2 input will be lists that must be converted to sets

E
Test is pretty straightforward. This is an easy one.

D
Lists and sets

A
1 takes 2 list args
2 can this be a comprehension? I think so

"""

# def merge_sets(list1, list2):
#     return set(x for x in list1 + list2)

# list1 = [3, 5, 7, 9]
# list2 = [5, 7, 11, 13]
# print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# # Prints True

"""
3
P
Transform 2 lists into frozen sets and find their common elements.
1 It says "transform" them, which I take to mean mutate
    - Is it mutation if we do `list1 = frozenset({list1})`?
    - Seems like that's just pointing the variable to a new object
    - But maybe I'm focusing on the wrong thing
2 Find (and return) their common elements
Implicitly
1 Test shows that the output should be a frozenset

E
Test shows output as frozenset

D
Lists and frozensets

A
1 list = frozenset(list) for both lists
2 use intersection to return a new frozenset of common elements
"""

# def intersection(list1, list2):
#     list1 = frozenset({x for x in list1})
#     list2 = frozenset({x for x in list2})

#     return list1.intersection(list2)

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 8]
# expected_result = frozenset({8})
# print(intersection(list1, list2) == expected_result) # True

"""
4
P
Given a dictionary, return its keys sorted by the values
 associated with each key.
1 sort the dict by value
2 return the keys sorted thus

E
Test shows single character string keys and int values, returned as a list

D
Dict in, list out

A
might be doable with a lamba
1 it's kind of 1 step
"""

# def order_by_value(my_dict):
#     return sorted([letter for letter in my_dict], key=lambda x: my_dict[x])

# my_dict = {'p': 8, 'q': 2, 'r': 6}
# keys = ['q', 'r', 'p']
# print(order_by_value(my_dict) == keys)  # True

"""
5
P
From two list arguments, determine the elements that are unique to the first 
list. The return value should be a set.
1 return a set of only the items unique to the first list

E
Example/test shows all list elements are ints

D
Lists,
sets

A
1 Take 2 list args
2 Coerce first list to set
3 Use set.difference()
"""

# def unique_from_first(list1, list2):
#     return set(list1).difference(list2)

# list1 = [3, 6, 9, 12]
# list2 = [6, 12, 15, 18]
# print(unique_from_first(list1, list2) == {9, 3})

"""
6
P
Write a function that takes a string argument and returns a list of substrings
 of that string. Each substring should begin with the first letter of the
   word, and the list should be ordered from shortest to longest.
1 return a list of substrings
2 all substrings must start with the first letter of the string
3 the list should be ordered from shorted to longest substring

E
Tests show very short strings, no unexecpected output.

D
Lists

A
Loop and slicing? That would do it, though I suspect there's a better way.
Not sure if can do in comprehension.
1 take str arg
2 init empty list
3 for letter in string, capture substring from index 0 to index of letter
4 add each substring to list
5 return list
"""

# def leading_substrings(string):
#     output = []
#     for i, _ in enumerate(string):
#         output.append(string[:i + 1])
    
#     return [string[:i + 1] for i in range(len(string))]

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

"""
7
P
Write a function that returns a list of all substrings of a string. Order the 
returned list by where in the string the substring begins. This means that all
 substrings that start at index position 0 should come first, then all
   substrings that start at index position 1, and so on. Since multiple
     substrings will occur at each position, return the substrings at a given
       index from shortest to longest.

You may (and should) use the leading_substrings function
 you wrote in the previous exercise:
1 Return a list of ALL substrings of a string
2 list should be ordered by index of substring start and then by length
    - all subs starting at string[0], then all at string[1], string[2], etc
    - shortest first, longest last
3 build on previous function

E
Test shows a pretty basic example with no surprises.

D
List

A
Modifying function from last problem - I see that the previous function covers
the first step. So now we just need to get the subs that begin at indices 1+
- could do with a nested for loop for sure, but I suspect there's a way to
    cram it into a comprehension
1 nest 2nd for loop with 'j' or other index counter
2 for i, append all subs by slicing from [i: j + 1]
"""

# def substrings(string):
#     output = []
#     for i, _ in enumerate(string):
#         for j, _ in enumerate(string):
#             output.append(string[i: j + 1])

#     count = output.count('')
#     while count:
#         output.remove('')
#         count -= 1
    
#     return output
#     [string[i:j + 1] for i,j in range(len(string))]

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
P
The instructions did say to build on the previous function again, and I did.
But my original function wasn't great, and instead of building NEW functions
that use my old function by CALLING it, I now have a functional but definitely
BAD piece of code. 
"""

# def palindromes(string):
#     output = []
#     if string == string[::-1]:
#         output.append(string)

#     for i, _ in enumerate(string):
#         for j, _ in enumerate(string):
#              output.append(string[i: j + 1]
#                            if string[i: j + 1] == string[j: i - 1: -1]
#                            and len(string[i: j + 1]) > 1
#                            else '')
    
#     while '' in output:
#         output.remove('')

#     return output

# # print(palindromes('abcd') == [])                  # True
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
9
P
Write a function that takes two arguments, an inventory item ID and a list of 
transactions, and returns a list containing only the transactions for the 
specified inventory item.
1 Return a list of the transactions for the specified item
Implicitly
1 Transactions are dicts, so return a list of transactions
2 Looks like we're basically testing membership, i.e. 101 in dict

E
Examples show returning a list of each of the transactions (dicts) with the
specific id number.

D
Lists, dicts

A
Probably easy in comprehension
1 transaction for transaction in transactions
2 if transaction["id"] == id
"""

def transactions_for(id, transactions):
    return [action for action in transactions
            if action["id"] == id]

# transactions = [
#     {"id": 101, "movement": 'in',  "quantity":  5},
#     {"id": 105, "movement": 'in',  "quantity": 10},
#     {"id": 102, "movement": 'out', "quantity": 17},
#     {"id": 101, "movement": 'in',  "quantity": 12},
#     {"id": 103, "movement": 'out', "quantity": 20},
#     {"id": 102, "movement": 'out', "quantity": 15},
#     {"id": 105, "movement": 'in',  "quantity": 25},
#     {"id": 101, "movement": 'out', "quantity": 18},
#     {"id": 102, "movement": 'in',  "quantity": 22},
#     {"id": 103, "movement": 'out', "quantity": 15},
# ]

# print(transactions_for(101, transactions) ==
#       [
#           {"id": 101, "movement": "in",  "quantity":  5},
#           {"id": 101, "movement": "in",  "quantity": 12},
#           {"id": 101, "movement": "out", "quantity": 18},
#       ]) # True

"""
10
P
Building on the previous exercise, write a function that returns True or False
 based on whether or not an inventory item (an ID number) is available. As 
 before, the function takes two arguments: an item ID and a list of 
 transactions. The function should return True only if the sum of the quantity
 values of the item's transactions is greater than zero. Notice that there is 
 a movement property in each transaction object. A movement value of 'out' 
 will decrease the item's quantity.

You may (and should) use the transactions_for function from the
 previous exercise.
1 Return a boolean representing an item's availability
2 Item is only available if it the sum is greater than zero
3 "out" means minus, so presumably "in" means plus

E
Example looks pretty straightforward. No new info

D
Still taking a list of dicts, might also want an intermediate list to store
quantity values.

A
1 Run transactions list through `transactions_for` to get only relevant data
2 init available = 0
3 To available, add the quantity for the filtered data - list[dict]["quantity"]
    - if list[data]["movement"] == 'out', add negative "quantity"
4 if available > 0 return True, else False
"""

def is_item_available(id, transactions):
    filtered_actions = transactions_for(id, transactions)
    available = 0

    for action in filtered_actions:
        if action["movement"] == 'in':
            available += action["quantity"]
        else:
            available -= action["quantity"]
    print(available)
    return available > 0



transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True