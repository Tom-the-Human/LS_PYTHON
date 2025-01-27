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
"""
def pig_it(text):
    pass

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !