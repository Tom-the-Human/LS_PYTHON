"""
4
P
Create a function that takes a list of integers as an argument and returns a 
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

1 take list of ints arg
2 return a tuple of 2 nums closest together in value
3 if multiple pairs tie, return first pair

E
nums can be in any order in list. Isee in case 3 that 12 and 7 are returned,
even though 17 comes next to 7, so "closest" means numerically only,
regardless of difference in index

D
List in, tuple out
Can't think right now because my mom talking to my baby son @.O
Poo
Maybe an intermediary structure, like list of tups
Dict. I think that's the way.

A
- compare every pair of numbers in the list to find the pair
    with the smallest difference between the 2
    
    - actually, a dict could be really helpful here
        - key is difference, value is tuple
        - if key already in dict, pass
        - return value of lowest key in dict

    - init pairs dict = {}

    - for num1 in list:
        - for num2 in list:
        - pairs += (max(num1, num2) - min(num1, num2)): (num1, num2)
                * not sure if += works w dict, may need different syntax
    - return min(pairs) *again may need different syntax
                

    Another case of right logic, bad syntax. failed to solve on time,
    hacked away on it a little longer besides and have failed to find the
    syntax to return the tuple value for the lowest key in the in the dict.
    Get this syntax down!!! Also consider alternative solutions that may
    be easier to code on the spot.
"""


def closest_numbers(numbers):
    pairs = {}

    for num1 in numbers:
        for num2 in numbers:
            if max(num1, num2) - min(num1, num2) in pairs.keys()\
            or max(num1, num2) - min(num1, num2) == 0:  # avoids tups where num2 is num1
                pass
            else:
                pairs[max(num1, num2) - min(num1, num2)] = (num1, num2)
    print(pairs)
    print(value for key, value in min(pairs[key]))

    # return lowest in pairs

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))