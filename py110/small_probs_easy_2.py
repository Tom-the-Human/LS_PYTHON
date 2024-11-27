# 1
# P
# Write a function that takes a floating point number representing an angle
#  between 0 and 360 degrees and returns a string representing that angle in
#  degrees, minutes, and seconds. You should use a degree symbol (°) to
#  represent degrees, a single quote (') to represent minutes, and a double
#  quote (") to represent seconds. There are 60 minutes in a degree, and 60
#  seconds in a minute.
# 1 Accept float between 0 and 360 as argument
# 2 Convert to degrees, minutes, seconds
# 3 Return converted value as a string
# Implicitly
# 1 Numbers outside of 0 - 360 are not allowed
# 2 Must escape either ' or "
# 3 Looks like whole part of number is degrees (i.e. before decimal)
# 4 But it's very unclear how, for example, 76.73 becomes 76*43'48"
#                                       (read degrees, not multiplication)

# E
# Tests in code. No new info, but part of me is wondering why these tests
# return true given floating point imprecision. May need to include
# `math.close`?

# D
# Unsure any are needed, but maybe lists. I still don't understand how this
# conversion is supposed to work. 

# A
# Well, I guess it's a conversion from base 10 to base 60 
# (like coverting time to a decimal for payroll).
# 1 Take a float
# 2 degrees = everything before the decimal
# 3 divide part after decimal by 60 (wrong direction!, multiply instead)
# 4 first 2 numbers after decimal = minutes
# 5 multiply what's left by 60?

# C
DEGREE = "\u00B0"

def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string

def dms(angle_float):
    if angle_float < 0 and angle_float > -360:
        angle_float = angle_float + 360
    elif angle_float >  360 or angle_float < -360:
        angle_float = abs(angle_float) - 360
    
    degrees = int(angle_float)
    minutes = int((angle_float - degrees) * 60)
    seconds = int((angle_float - degrees - (minutes / 60)) * (60 * 60))

    return (f"{degrees}{DEGREE}"
            f"{pad_zeroes(minutes)}'"
            f'{pad_zeroes(seconds)}"')

# All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
# print(dms(254.6) == "254°35'59\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# further exploration tests
# print(dms(-1))   # 359°00'00"
# print(dms(400))  # 40°00'00"
# print(dms(-40))  # 320°00'00"
# print(dms(-420)) # 300°00'00"


# 2
# P
# Write a function that takes two lists as arguments and returns a set that
#  contains the union of the values from the two lists. You may assume that
#  both arguments will always be lists.
# 1 take 2 lists
# 2 join as set
# 3 return set

# E
# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# D
# Lists and a set

# A
# 1 take lists
# 2 join the lists
# 3 convert to set
# 4 return set

# C
def union(list1, list2):
    return set(list1 + list2)

# print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
# print(union([1, 3, 5], [3, 6, 9]))


# 3
# P
# Write a function that takes a list as an argument and returns a list that
#  contains two elements, both of which are lists. Put the first half of the
#  original list elements in the first element of the return value and put the
#  second half in the second element. If the original list contains an odd
#  number of elements, place the middle element in the first half list.
# 1 take a list of arguments
# 2 return a list of 2 lists
# 3 first half of elements in original list go in 1st list
# 4 rest go in 2nd list
# 5 if odd number of elements, middle element goes in 1st list

# E
# tests in code, looks like all tests have int elements, but will try to
# make the code element agnositic

# D
# lists and more lists

# A
# 1 take a list argument
# 2 get list length
# 3 split the list at half the length (number of elements),
#   or just over half if even (i.e. if length 9, include 5 in first half)
# 4 assign first half of elements to a new list
# 5 assign second half of elements to a new list
# 6 create another list and assign both new lists to that one, as 2 elements

# C
import math

def halvsies(input_list):
    elements = len(input_list)
    half1 = input_list[0: math.ceil(elements / 2)]
    half2 = input_list[math.ceil(elements / 2):]

    return([half1, half2])

# All of these examples should print True
# print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
# print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
# print(halvsies([5]) == [[5], []])
# print(halvsies([]) == [[], []])

# 4
# P
# Given an unordered list and the information that exactly one value in the
#  list occurs twice (every other value occurs exactly once), determine
#  which value occurs twice. Write a function that finds and
#  returns the duplicate value.
# 1 list always has 1 duplicate
# 2 take a list
# 3 find the duplicate
# 4 return the duplicate

# E
# tests in code

# D
# lists

# A
# 1 take a list argument
# 2 init new empty list
# 3 iterate through the input list
# 4 for element, check if element already in new list
# 5 if not, add element to new list
# 6 if so, return element

# C
def find_dup(input_list):
    checked = []
    for element in input_list:
        if element not in checked:
            checked.append(element)
        else:
            return element

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


# 5
# P
# Write a function that combines two lists passed as arguments and returns a
#  new list that contains all elements from both list arguments, with each
#  element taken in alternation.
# You may assume that both input lists are non-empty, and 
# that they have the same number of elements.
# 1 take 2 list arguments
# 2 zip the 2 lists together (alternating elements) (is there zip function?)
# 3 return new combined list

# E
# example/test in code, show string and int elements

# D
# lists

# A
# 1 take 2 list arguments
# 2 create new empty list
# 3 yes, there is a zip function, so use it liks so: zip(list1, list2)
# 4 return zipped list

# C
def interleave(list1, list2):
    return [item for pair in zip(list1, list2) for item in pair]


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# expected = [1, "a", 2, "b", 3, "c"]
# print(interleave(list1, list2) == expected)      # True


# 6
# P
# Write a function that takes a list of positive integers as input, multiplies
#  all of the integers together, divides the result by the number of entries
#  in the list, and returns the result as a string with the value rounded to
#  three decimal places.
# 1 take a list of positive integers
# 2 multiply all the ints together
# 3 divide the product by the number of ints (length of the list)
# 4 return the result as a string with the value rounded to
#  three decimal places
# Implicitly
# 1 String coercion is necessary
# 2 Rounding may be necessary - probably can do with a formatted string?

# E
# In code. No surprises really, just all low numbers. One example is 4 "1"s.
# That returns "0.250", which is of course 1/4.

# D
# Just the list

# A
# 1 Take a list of ints.
# 2 Init product variable to 1
# 3 for int in list, product *= int
# 4 result = product / len(list)
# 5 format result as string w 3 decimals
#   - f-string? look up syntax
# 6 return result

# C
def multiplicative_average(input_list):
    product = 1
    for num in input_list:
        product *= num
    
    result = product / len(input_list)

    return f"{result:.3f}"

# All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")


# 7
# P
# Write a function that takes two list arguments, each containing a list of
#  numbers, and returns a new list that contains the product of each pair of
#  numbers from the arguments that have the same index. You may assume that
#  the arguments contain the same number of elements.
# 1 take 2 lists of numbers as arguments
# 2 multiply the numbers at the same index in each list,
#  i.e. list1[0] * list2[0], etc
# 3 return a new list of the products i.e. list3[0] for the above

# E
# In code. Only 1 test and no new info.

# D
# so much list

# A
# 1 take 2 lists
# 1.5 init new list
# 2 for each num in list1, multiply it by the num at the same index in list 2
# 3 for each multiplication, store the result in new list 
#   - this can all be accomplished with an enumerated for loop
#   - list3.append(list1[i] * list2[i])
# 4 return new list

# C
def multiply_list(list1, list2):
    list3 = []
    for i, _ in enumerate(list1):
        list3.append(list1[i] * list2[i])

    return list3


# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True


# 8
# P
# Write a function that takes one argument, a positive integer,
#  and returns a list of the digits in the number.
# 1 take an int argument
# 2 return a list of the digits in the number

# E
# Tests show that all digits should be included even if they are duplicates.
# For example, 444 = [4, 4, 4]
# Also, the digits remain in the same order they had in the input int
# I.e. 12345 = [1, 2, 3, 4, 5]

# D
# some more lists

# A
# 1 take int argument
# 2 init an empty list
# 3 split int into individual digits
#   - at least a couple ways to do this
#   - one way would be to coerce to string then use for loop with indexing to
#        extract chars to list, and coerce those back to ints
#   - another is to use modulo 10 and take the modulus
#        until it doesn't divide anymore
# 4 assign ints to new list in order they first appeared, so if using modulo
#       insert the digits at index 0 instead of appending
# 5 retunr list

# C
def digit_list(number):
    num_list = []
    # while number:
    #     digit = number % 10
    #     num_list.insert(0, digit)
    #     number = int(number // 10)

    numstr = str(number)
    for digit in numstr:
        num_list.append(int(digit))

    return num_list

# print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
# print(digit_list(7) == [7])                       # True
# print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
# print(digit_list(444) == [4, 4, 4])               # True


# 9
# P
# Write a function that counts the number of occurrences of each element in a
#  given list. Once counted, print each element alongside the number of
#  occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
# 1 take a list argument
# 2 for each unique element print a count of the number of occurences
# 3 words are case sensitive

# E
# Only one test, shows a list of all strings as input. Output is
#   strings formatted like "car => 4". Might be tricky to work out how to
#   get this ouput, but perhaps I can imbed a comprehension in an f-string?
# No, I just need to PRINT it, not return it. But yes, f-strings of course.
# Or might just need a helper function.
# Nah bro, this is what dicts are for.

# D
# Lists! Again! OH! And a dictionary!

# A
# 1 take a list argument
# 2 init an empty dict
# 3 for each element in the list, add the element as a dict key and increment
#   int value as the count. i.e. {'car': 1}, {'truck': 1}, {'car': 2}, etc
#   - might need to break this down further. not sure if can be done at once
# 4 once complete, format & print as shown, with 4 print lines

# C
# def count_occurrences(vehicles):
#     vehicle_count = {}

#     for vehicle in vehicles:
#         vehicle_count[vehicle.lower()] = vehicle_count.get(vehicle.lower(), 0) + 1

#     for vehicle in vehicle_count:
#         print(f"{vehicle} => {vehicle_count[vehicle]}")

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck', 'suv']
# # added 'suv' to test case insensitivity

# count_occurrences(vehicles)


# 10
# P
# Write a function that takes one argument, a list of integers, and returns
#  the average of all the integers in the list, rounded down to the integer
#  component of the average. The list will never be empty, and the numbers
#  will always be positive integers.
# 1 take a list of ints
# 2 return the average of all the integers in the list,
#    rounded down to the integer component of the average (???)

# E
# Tests in code. List contains 1 or more positive ints.

# D
# # Lists. 

# A
# I'm unsure what "integer component of the average" means exactly.
# But I will take a whack at it.
# 1 take list of ints argument
# 2 assign the sum of the ints to a variable
# 3 divide the sum by the number of ints
# 4 round down the result to nearest int
def average(int_list):
    return sum(int_list) // len(int_list)


# print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
# print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
# print(average([7]) == 7)                          # True