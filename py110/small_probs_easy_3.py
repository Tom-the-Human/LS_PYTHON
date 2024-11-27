"""
1
P - The time of day can be represented as the number of minutes before or 
after midnight. If the number of minutes is positive, the time is after 
midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns 
the time of day in 24-hour format (hh:mm). 
Your function should work with any integer input.
You may not use Python's datetime module.
1 No `datetime`
2 Take a number of minutes (ints) as argument
3 Return time in 24 hour format (string like "18:31")
4 Negative numbers sort backwards from midnight (-60 should return 23:00)

E - Tests in code, minutes can be any int, must return string representing
clock time in 24 hr format

D - I'm unsure - perhaps a dict could come in handy for the time conversion,
or maybe something else, or none.

A -
1 - Take an int argument
2 - init MIN_PER_HR const to 60
3 - init init HR_PER_DAY const to 24
4 - use int % MIN_PER_HR to get time_minutes from parameter int
5 - and int // MIN_PER_HR % HRS_PER_DAY to get time_hours from perameter int
6 - use f-string like f"{time_hours}:{time_minutes}" include formatting for
    zero and single digit numbers i.e. "01:00" or "00:02"
7 - return string
"""
# MIN_PER_HR = 60
# HRS_PER_DAY = 24
# def time_of_day(minutes):
#     time_minutes = minutes % MIN_PER_HR
#     time_hours = (minutes // MIN_PER_HR) % HRS_PER_DAY

#     output = f"{time_hours:02d}:{time_minutes:02d}"
#     return output

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True
#####
"""
2
P - As seen in the previous exercise, the time of day can be represented as
 the number of minutes before or after midnight. If the number of minutes is
   positive, the time is after midnight. If the number of minutes is negative,
     the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return
 the number of minutes before and after midnight, respectively. Both functions
   should return a value in the range 0 through 1439.

You may not use Python's datetime module.
1 - take time in 24hr format
2 - return number of minutes before midnight AND
3 - write a second function that returns the number of minutes after midnight
3 - No `datetime`
4 - return value should be an int between 0 and 1439 (inclusive)

E - Tests in code, show all inputs as strings in the manner of the last
exercise's output. i.e. "00:00". Both "00:00" and "24:00" should return 0.

D - None, except the same constants I defined before if those can be sorted.
Also, are strings data structures?

A -
0 - define constants (hours, minutes per day)
1 - take a string argument in 24hr format
2 - extract time_hours from string w int coercion
3 - do same with time_minutes
4 - use minutes = minutes + (time_hours * MIN_PER_HOUR)
5 - if before_midnight use -minutes
6 - return minutes

C -
"""
# MIN_PER_HR = 60
# MIN_PER_DAY = 1440

# def after_midnight(time):
#     time_hours = int(time[0:2])
#     time_minutes = int(time[3:])

#     minutes = time_minutes + (time_hours * MIN_PER_HR)

#     while minutes >= MIN_PER_DAY:
#         minutes -= MIN_PER_DAY

#     return minutes

# def before_midnight(time):
#     minutes = after_midnight(time)

#     minutes = MIN_PER_DAY - minutes
#     if minutes == MIN_PER_DAY:
#         minutes = 0

#     return abs(minutes)

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

"""
3
P
Write a function that takes a string, doubles every character in the string,
 then returns the result as a new string.
1 take a string argument
2 double each character in the string (double how?)
3 return new string
Implicitly
1 from examples, print 2-in-a-row of each character, regardless of type

E
Tests in code show i.e. 'Hello' == "HHeelllloo". Empty string remains empty.

D
Might want an intermediate list or dict. Could fairly easily loop through
the string adding each char to a list twice, then join to make new string.

A
1 take string argument
2 in comprehension, add each char twice to a list, in order
3 join list to make new string
4 return string

c
"""
# def repeater(input):
#     char_list = [char * 2 for char in input]
#     output = ''.join(char_list)
#     return output

# print(repeater('Hello') == "HHeelllloo")              # True
# print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
# print(repeater('') == "")                             # True

"""
4
P
Write a function that takes a string, doubles every consonant in the string,
 and returns the result as a new string. The function should not double vowels
   ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

E
Tests below, very similar problem to last one, just need to check membership
before addign to new string.

D
Membership list for vowels and list comprehension.

A
1 take string argument
2 create vowel list
3 if aplha and not vowel, in comprehension, add each char twice to a list
    - if not alpha or not vowel, add once
4 join list to make new string
5 return string
"""
# def double_consonants(input):
#     vowels = ['a','e','i','o','u']
#     char_list = [char * 2 if char.isalpha() and char.casefold() not in vowels
#                   else char for char in input]
#     output = ''.join(char_list)
#     return output

# # All of these examples should print True
# print(double_consonants('String') == "SSttrrinngg")
# print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
# print(double_consonants('July 4th') == "JJullyy 4tthh")
# print(double_consonants('') == "")

"""
5
P
Write a function that takes a positive integer as an argument and returns
 that number with its digits reversed.

E
Tests show mostly what I expected, except the case that 12000 = 21
So it appears that trailing zeros, which become leading zeros when reversed,
should be removed from output.
From the test cases it *appears* that zeros should be ignored altogether,
but I'll assume the should only be ignored when they would end up in the
leading position. That should be easy to do using a string coercion

D
List or string depending on method used to reverse the digits

A
0 Take int argument
1 init empty string
2 coerce to string
3 iterate through string in reverse
    - for digit in reversed(string), add digit to empty string
4 clean any leading zeros (turned out to not be necessary,
    as it appears ints are automatically returned without leading zeros)
5 coerce to int
6 return

C
"""
# def reverse_number(number):
#     return int(''.join([digit for digit in reversed(str(number))]))

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True
    
"""
6
P
Write a function that takes an integer argument and returns a list containing
 all integers between 1 and the argument (inclusive), in ascending order.
1 Return a list that contains all the ints between 1 and the argument (inclusive)
2 The list must be in ascending order

E
Examples show exactly the expected output. No new info.

D
Lists

A
1 Take an int
2 Use a comprehension to populate a list of the defined range
  - 1 to arg+1

C
"""
# def sequence(number):
#     return [num for num in range(1, number + 1)]

# print(sequence(5) == [1, 2, 3, 4, 5])   # True
# print(sequence(3) == [1, 2, 3])         # True
# print(sequence(1) == [1])               # True

"""
7
P
Write a function that takes a string argument consisting of a first name,
 a space, and a last name. The function should return a new string consisting
   of the last name, a comma, a space, and the first name.
1 Return a new string, reformatted as described

E
Only 1 example, no new info

D
Strings, and probably a list of strings to hold the first and last name subs

A
1 Use split to make a list of the first and last names
2 Join last name + ', ' + first name
"""

# def swap_name(full_name):
#     first, last = full_name.split()
#     return f"{last}, {first}"

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

"""
8
P
Create a function that takes two integers as arguments. The first argument is 
a count, and the second is the starting number of a sequence that your 
function will create. The function should return a list containing the same 
number of elements as the count argument. The value of each element should be 
a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 
0. The starting number can be any integer. If the count is 0, the function 
should return an empty list.

1 Take a count and a starting number as ints
2 Return a list of the same number of elements as count
3 Each element should be a multiple of the starting number
4 Count will always be >= 0
5 0 count returns empty list

E
Examples show that the element at index 0 in the return list is 1x the
 starting number, 2x at index 1, 3x at index 2, etc

D
Output list, none ther needed

A
Try to do in a comprehension
1 [num for num in range(count) lambda num * (index + 1)]
^ Wrong, but a start. See solution below

"""

# def sequence(count, start):
#     return [(start * (idx + 1)) for idx in range(count)]

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

"""
9
P
Write a function that takes a list as an argument and reverses its elements, 
in place. That is, mutate the list passed into the function. The returned 
object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).
1 Write a function that reverses a list by mutating it.
2 No slice or list.reverse()
3 It doesn't say we can't use reversed(), but I imagine were not meant to

E
No new info

D
lists

A
Can do in a comprehension - start with for loop
1 get length
2 for item in list
Man, why can't I wrap my head around what needs to happen here???
3 ok, so for half the length of the list, we want to swap the element
  with an element from the other end of the list
  0 with -1,
  1 with -2,
  2 with -3, etc.
4 once all elements swapped, return list

Checking out LS and other student answers, no one did this with a
comprehension. Not possible? Or just too confusing for that to be useful?
"""

# def reverse_list(lst):
#     for i, _ in enumerate(lst):
#         if i < (len(lst) / 2):
#             lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
    
#     return lst

# list1 = [1, 2, 3, 4]
# result = reverse_list(list1)
# print(result == [4, 3, 2, 1])               # True
# print(list1 is result)                      # True

# list2 = ["a", "b", "c", "d", "e"]
# result2 = reverse_list(list2)
# print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
# print(list2 is result2)                     # True

# list3 = ["abc"]
# result3 = reverse_list(list3)
# print(result3 == ['abc'])                   # True
# print(list3 is result3)                     # True

# list4 = []
# result4 = reverse_list(list4)
# print(result4 == [])                        # True
# print(list4 is result4)                     # True

"""
10
P
Write a function that takes a string as an argument and returns True if all 
parentheses in the string are properly balanced, False otherwise. 
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
1 Check that each parenthesis in the string is closed
2 Return True or False depending on 1

E
Examples show that ')' followed by '(' does NOT count as closed pair so should
reutrn False. So they do need to be in order. All closing parenths must
come after their respective opening parenth.

D
Strings, but might be good to use a list to collect the parenths. Then
could compare list elements in order to determine True or False.

A
1 for char in string, if '(' or ')', add to new list
2 for '(' in list, find next ')' and pop both
  - for ')' do nothing
  - thus, if ')' before '(', that pair should not be removed
3 if list ends up empty, return True
4 else False

NOPE, THIS SOLUTION DOES NOT WORK. TRY AGAIN.

A
1 initialize a parenth count
2 for '(' add 1, for ')' minus 1
3 if count is ever negative, return False
4 if at end of loop, count is not 0, return False
5 else True
"""


def  is_balanced(string):
    count = 0

    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        if count < 0:
            return False
    
    if count != 0:
        return False
    
    return True
        

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True