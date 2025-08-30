# Remove all duplicate letters from a string, keeping only the first occurrence.
# The input is restricted to contain no numerals and only words containing the 
# English alphabet letters.

# You may not use a set.
'''
P
1 takee a string arg
2 remove all duplicate letters from arg, keeping only the first occurence
3 will only be english chars and whitespace

E
I see the rules apply to the whitespace as well, not just letters
Also, case insensitive!

D
String input
String output
Maybe a string or list of encountered letters to check against

A
- init encountered = list or str?
- check each letter in the string
    - if not in encountered
        - append to both encountered and to output str
    - if in encountered
        - pass

    - return output string
'''

# def remove_duplicates(string):
#     output = ''

#     for char in string:
#         if char.casefold() not in output.casefold():
#             output += char

#     return output

# # Tests
# print(remove_duplicates("Launch School") == "Launch So")
# print(remove_duplicates("CodeWars can't Load Today") == "CodeWars n'tLy")
# print(remove_duplicates("success") == "suce")

'''
write a function that removes every other element from a list

P
1 take a list arg
2 remove every other function from a list

E
none provided, but I'll provide a list to test the function
no additional rules, just constructing this problem from a given possible
interview question

D
List input
None output
might use a copy of the list to avoid issues of mutating while iterating

A
list_copy = list.copy()

for idx in range(len(list_copy)):
    if idx % 2 == 1:
    list.pop(idx)


'''

# def every_other(lst):
#     lst = [x for i, x in enumerate(lst) if i % 2 == 1]
    
#     return lst



# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(lst)
# lst = every_other(lst)
# print(lst)

'''
reverse a list without using the built-in list.reverse method
or list.sort method or sorted function

1 none of the named functions/methods
2 take a list arg
3 reverse the elements in the list

E
I wrote 2 simple tests, 1 with even number of elements and one with odd number

D
List input
None output
dont think I need other structures

A
swap the positions of the first and last element,
repeat for second and next to last, and so on
    get list length
    for range of list length//2
        swap
        list[0], list[-0]
        list[1], list[-1]
        This is wrong. needs list[0], list[-1], etc

Had an off-by-1 error, and had a little trouble fixing it because I was trying
to add to a negative number, which meant I needed to employ the abs() function.
`-abs(idx + 1)`or I guess `-idx - 1` might have also done the job ... yes,
either option works. As for readability, I think the version with abs() is
better, though it might be slightly less efficient (function call instead of
just operating directly on the integers).
'''
# def switch(eroo):
#   # WARNING! Mutates AND returns input!
#     for idx in range(len(eroo) // 2):
#         eroo[idx], eroo[-idx - 1] = eroo[-abs(idx + 1)], eroo[idx]

#     # return eroo

# hitter = [1, 2, 3, 11, 22, 33,]
# print(hitter)
# print(switch(hitter))
# print(hitter)
# # hitter = switch(hitter)
# print(hitter)

# blade = [1, 11, 111, 1111, 11111]
# print(blade)
# print(switch(blade))
# # blade = switch(blade)
# # switch(blade)
# print(blade)

# my_set = {1, 2, 3, 4, 5, 6, 7, 8,}
# print(my_set)
# my_set.remove(1)
# print(my_set)
# other_set = {5, 6, 7, 8, 9, 0,}
# print(my_set | other_set)
# print(my_set.intersection(other_set))
# print(other_set.difference(my_set))

