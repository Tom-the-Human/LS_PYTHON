# 1
# P
# Sort the following list of numbers first in ascending numeric 
# order, then in descending numeric order. Do not mutate the list.
# Explicitly
# 1 Sort a list of numbers into ascending order.
# 2 Sort the same list into descending order.
# 3 Do not mutate the list.
# Implicitly
# 1 sorted() will be used
# 2 judging by the list and examples, all numbers will be positive or negative ints

# E
# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# D
# Lists will be used. Others are probably not needed.

# A
# 1 initialize a new list and assign it to sorted(lst)
# 2 initialize another list assigned to sorted(lst, reverse=True)
# 3 Profit!

# C
lst = [10, 9, -6, 11, 7, -16, 50, 8]
ascending = sorted(lst)
descending = sorted(lst, reverse=True)
print(ascending)
print(descending)


# 2
# P
# Repeat the previous exercise but, 
# this time, perform the sort by mutating the original list.
# Explicitly
# 1 same as before BUT
# 2 MUST mutate the list
# Implicitly
# 1 use list.sort instead of sorted()

# E
# Inputs and outputs are same as before.

# D
# Lists!

# A
# 1 call .sort on list
# 2 Does .sort method take reverse keyword? let's find out
# It does indeed!

# C
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


# 3
# P
# Repeat problem 2 but, this time, sort the list as string values. 
# Both the list passed to the sorting function and the returned 
# list should contain numbers, not strings.
# Explicitly
# 1 Convert each element to a string before sorting
# 2 Convert the sorted elements back to ints
# Implicitly
# 1 Use str() function
# 2 Probably needs a custom function for sorting key
# 3 Maybe not, potentially use a for loop w/ something like int(str())

# E
# Same input list, but output should be:
# [-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
# [9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort

# D
# Lists! Idk if strings count.

# A
# 1 sort list with key=str
# 2 print list
# 3 sort list w key=str, reverse=True
# 4 print list

# C
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst.sort(key=str)
print(lst)
lst.sort(key=str, reverse=True)
print(lst)


# 4
# P
# How would you sort the following list of dictionaries based on the
# year of publication of each book, from the earliest to the most recent?
# Explicitly
# 1 Sort the list by publication date
# 2 Earliest publication first
# Implicitly
# 1 The list needs to be sorted by the value of the 'published' key in each dict
# 2 The dates are in string format, so may require use of int() for proper sort

# E
# Input list is below in the code, expected output is:
# Pretty printed for clarity
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]
# No new information, but expected output does confirm that coercion 
#   to int for sorting will be needed.

# D
# Lists and dictionaries of course. 
# Very likely a dictionary view object as well, or maybe tuples.

# A
# 1 define a custom sorting function
# 2 function takes a dictionary argument and returns
#    the value of 'published' as an int
# 3 use sorted(books, key=function)

# C

def year_published(book):
    return int(book['published'])

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

print(sorted(books, key=year_published))