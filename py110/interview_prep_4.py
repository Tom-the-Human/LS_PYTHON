'''
A featured number (something unique to this exercise) is an odd number that is 
a multiple of 7, with all of its digits occurring exactly once each. 
For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not 
(it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there is 
no next featured number.

NOTE: The largest possible featured number is 9876543201.

1 featured number is odd, multiple of 7, no repeat digits, 
    and not more than 9876543201
2 take an int arg
3 return the next featured number greater than the arg
4 or return error if no next featured number

E

D
Int input
Int output


A
MAX = 9876543201
if arg => MAX:
    return error

    test = 7
while True:
    if test < arg:
        test += 14
        continue
    if len(str(test)) != len(set(str(test))):
        test += 14
        continue
    return test
    
'''
# def next_featured(arg):
#     MAX = 9876543201
#     if arg >= MAX:
#         return error

#     test = 7
#     while True:
#         if test < arg + 1:
#             test += 14
#             continue
#         if len(str(test)) != len(set(str(test))):
#             test += 14
#             continue
#         return test
    
    

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that "
#          "fulfills those requirements.")
# print(next_featured(9876543201) == error)       # True

'''
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, 
and every angle must be greater than 0. If either of these conditions is not 
satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and 
returns one of the following four strings representing the triangle's 
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to 
worry about floating point errors. You may also assume that the arguments are 
in degrees.

P
1 take 3 int args
2 return string representing triangle class
3 determine type and validity of triangle as described above

E

D
3 ints input
string output

A
-determine if valid and return "invalid" if not
angles = (a, b, c)
valid = (sum(angle) == 180)
if not valid or not all(angles):
    return "invalid"

-determine and return type
if 90 in angles:
    return "right"

for angle in angles:
    if angle > 90:
        return "obtuse"

return "acute"
'''
# def triangle(a, b, c):
#     angles = (a, b, c)
#     valid = (sum(angles) == 180 and all(angle > 0 for angle in angles))

#     if not valid:
#         return "invalid"

#     if 90 in angles:
#         return "right"
    
#     if any(angle > 90 for angle in angles):
#         return "obtuse"

#     return "acute"

# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True
# print(triangle(180, -180, 180) == "invalid")

'''
Write a function that takes a string and returns a dictionary containing 
the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values l
ie between "0.00" and "100.00", respectively. Each value should be rounded 
to two decimal points.

You may assume that the string will always contain at least one character.

P
1 take a string arg
2 return a dict with 3 properties as above
3 all percentages must be returned as strings with a numberic value between
    0.00 and 100.00, rounded to 2 decimal places

E
all non-alphas are "neither",

D
String input
Dictionary output
Maybe another structure for counts

A
- init result = {}

- get len(string) # total chars
    total = len(string)

- count lowercase letters, div total by lower and store result in dict
    lower = 0
    upper = 0
    neither = 0

    for char in string:
        if char.islower():
            lower += 1
        if char.isupper():
            upper += 1
        if not char.isalpha():
            neither += 1
            
    result["lowercase"] = f'{total / lower}.2f' 

- count uppercase letters, div total by upper and store result in dict

- count nonalphas, div total by neither and store result in dict

return dict

FAILED: because a) most importantly, I got the math backwards and I couldn't 
immediately see what was wrong. Percentage is not (total / part) but the other
way around * 100. And b), I forogt how to format numbers in string output. It
is done INSIDE the curly braces, by first placing a colon (:) followed by a
decimal point (.), then the number of decimal places desired (2 in this case),
and lastly the letter 'f' specifying fixed-point notation (f).
f'{number:.2f}'
'''
# def letter_percentages(string):
#     result = {}
#     total = len(string)
#     lower = 0
#     upper = 0
#     neither = 0

#     for char in string:
#         if char.islower():
#             lower += 1
#         if char.isupper():
#             upper += 1
#         if not char.isalpha():
#             neither += 1
 
#         result['lowercase'] = f'{(lower / total) * 100:.2f}'

#         result['uppercase'] = f'{(upper / total) * 100:.2f}'

#         result['neither'] = f'{(neither / total) * 100:.2f}'

#     print(result)
#     return result


# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

"""
A prime number is a positive number that is evenly divisible only by itself 
and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 
is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that 
the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns true 
if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your 
task is to programmatically determine whether a number is prime without 
relying on functions that already do that for you.

1 take an int arg
2 return a boolean representing primeness
3 no add-ons

E

D
Int input
Boolean output
range(2, math.sqrt(arg))

A
- import math

determine if arg num divisible by anything other than 1 or itself,
    only need to go up to sqrt(num) for this

    for divisor in range(2, math.sqrt(num)):
        if (num / divisor) % 1 == 0:
        return False

    return True


"""
# import math

# def is_prime(num):
#     if num == 1:
#         return False
    
#     for divisor in range(2, int(math.sqrt(num)) + 1):
#         if (num / divisor) % 1 == 0:
#             return False
        
#     return True

# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

'''
Create a function that takes a string argument and returns a copy of the 
string with every second character in every third word converted to 
uppercase. Other characters should remain the same.

1 take a string arg
2 return a copy of the string with every 2nd char in every 3rd word uppercased
3 no changes to other chars

E

D
String input
String ouput
MAYBE nested list, but maybe try to directly manipulate the string this time

A
split to individiual words
words = string.split()

for every 3RD word, change specified chars

for word in words[2::3]:
    for idx in range(1, len(word), 2):
        word[idx] = word[idx].upper()

return ' '.join(words)

'''
# def to_weird_case(string):
#     words = [list(word) for word in string.split()]
#     result = []

#     for i, word in enumerate(words):
#         if i in range(2, len(words), 3):
#             for idx in range(1, len(word), 2):
#                 word[idx] = word[idx].upper()
#         word = ''.join(word)
#         result.append(word)

#     return ' '.join(result)

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)

'''
Create a function that takes a string argument and returns the character that 
occurs most often in the string. If there are multiple characters with the same 
greatest frequency, return the one that appears first in the string. 
When counting characters, consider uppercase and lowercase versions to be the 
same.

P
1 take a string arg
2 return the char occuring most frequently in the string
3 if multiple most frequent chars, return the char with lowest index
4 counts are case-insenstive

E

D
String input
String output
Dict for char counts

A
counts =  {char.lower(): char.count() for char in string.casefold()}

return the char with highest count
return counts[max(counts.values)]

FAILED to remember syntax for the last part, so had to look up where I'd 
asked LSBot before. Use the max function, of course, but we need to use
`key=counts.get` to use the values to determine max. Look how I tried to 
overcomplicate it again.
'''
# def most_common_char(string):
#     counts =  {char: string.casefold().count(char) for char in string.casefold()}

#     return max(counts, key=counts.get)

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')

'''
Create a function that takes a list of integers as an argument and returns 
the number of identical pairs of integers in that list. For instance, the 
number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 
2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. 
For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2.
The first list contains two complete pairs while the second has an extra 2 that 
isn't part of the other two pairs.

P
1 take a list of ints arg
2 return int num of identical pairs in list
3 if list has < 2 numbers, return 0
4 count each complete pair, including additional pairs of same int

E

D
List input
Int output
Dictionary for counting {num: numbers.count(num) for num in numbers}

A
create counts dict
    counts = {num: numbers.count(num) for num in numbers}

init result = 0
get the total number of pairs
    for count in counts:
        result += counts[count] // 2
    
    return result

'''
# def pairs(numbers):
#     counts = {num: numbers.count(num) for num in numbers}
#     result = 0

#     for count in counts:
#         result += counts[count] // 2
    
#     return result

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
