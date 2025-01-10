'''
1***
P
Create a function that takes a list of numbers as an argument. For each 
number, determine how many numbers in the list are smaller than it, and 
place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs 
multiple times in the list, it should only be counted once.

Try to use a comprehension.

1 take a list of numbers arg
2 for each num, determine how many others in the list are smaller than it
3 place each count in a new list
4 return the new list
5 when a number appears multiple times in the list, it should only be counted
    once i.e. [7, 7, 7, 8] == [0, 0, 0, 1]

E

D
List input
List output
Might use a set

A
- counts = [sum(1 for num in set(numbers) < num)] err... maybe do
    comprehension after determining basic structure

    - counter = 0
- counts = []
- for num1 in numbers:
    for num2 in set(numbers):
        if num1 > num2:
        counter += 1
    counts.append(counter)
    counter = 0

return counts    

SOLVED: got it done with loops in about 11ish minutes, 
figured out comprehension by 16 mins
'''
# def smaller_numbers_than_current(numbers):
#    # counter = 0
#     counts = [sum(1 for num2 in set(numbers) if num1 > num2)
#               for num1 in numbers]

#     # for num1 in numbers:
#     #     for num2 in set(numbers):
#     #         if num1 > num2:
#     #             counter += 1
#     #     counts.append(counter)
#     #     counter = 0

#     return counts  


# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)


'''
3***
P
Create a function that takes a string argument and returns a copy of the 
string with every second character in every third word converted to uppercase.
Other characters should remain the same.

1 take a str arg
2 reutrn a copy of the arg, with every 2nd char in every 3rd word uppercase
3 no changes to other chars

E

D
String in
String out
Possibly lists. Probably.

A
- split the string into a list of words

- split every 3rd word, starting with index 2, into a nested list

- for these nested lists, uppercase every 2nd char beginning at index 1
    - make sure to reassign the actual list element, not just the char,
        updating the char will not update the list

- rejoin the nested lists of chars

- rejoin the list of words and return it

SOLVED: 11.5 minutes - concise, little or no problems, 
could be a bit more readable, but happy with it
'''

# def to_weird_case(string):
#     words = string.split()

#     for idx in range(2, len(words), 3):
#         words[idx] = list(words[idx])
#         for j in range(1, len(words[idx]), 2):
#             words[idx][j] = words[idx][j].upper()
#         words[idx] = ''.join(words[idx])

#     return ' '.join(words)


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
4***
P
Create a function that takes a list of integers as an argument and returns a 
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

1 take a list of ints arg
2 return a tuple of the 2 numbers that are closest in value
3 if multiple pairs with same value difference, return pair that occurs first

E

D
List input
Tuple output
Probably want a list of tuples to compare, or maybe JUST a single tuple 
that is updated if the difference between the 2 elements is smaller than
the current difference

A
least_diff = ()
diff = max(numbers)

- check the difference between each num in numbers
    for num1 in numbers:
        for num2 in numbers:
            diff = abs(num1 - num2)
            if (diff != 0) and (diff < abs(least_diff[0] - least_diff[1])):
                least_diff = (num1, num2)

- return least_diff

SOLVED: about 11 mins, new approach, felt good!
'''

# def closest_numbers(numbers):
#     least_diff = (max(numbers), min(numbers))

#     for num1 in numbers:
#         for num2 in numbers:
#             diff = abs(num1 - num2)
#             if (diff != 0) and (diff < abs(least_diff[0] - least_diff[1])):
#                 least_diff = (num1, num2)

#     return least_diff


# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

'''
7***
P
Create a function that takes a list of integers as an argument and returns 
the number of identical pairs of integers in that list. For instance, the 
number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 
2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. 
For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should 
return 2. The first list contains two complete pairs while the second has an 
extra 2 that isn't part of the other two pairs.

1 take a list of ints arg
2 reutrn the number of identical pairs in list
3 if less than 2 nums in list, return 0
4 count all COMPLETE pairs of the same num

E

D
List input
Int output
Dictionary of value: count(value)

A
counts = {num: numbers.count(num) for num in numbers}

counter = 0

for count in counts.values():
    counter += (count // 2)

return counter

SOLVED: 5 mins. That dict makes this so much easier. REMEMBER!
Note that the conditional `return 0` at the top isn't necessary, but does
prevent the rest of the code from running in the event the output will just
be 0 anyway
'''

# def pairs(numbers):
#     if len(numbers) < 2:
#         return 0
    
#     counts = {num: numbers.count(num) for num in numbers}

#     counter = 0

#     for count in counts.values():
#         counter += (count // 2)

#     return counter

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

'''
10***
P
Create a function that takes a string of digits as an argument and returns 
the number of even-numbered substrings that can be formed. For example, in 
the case of '1432', the even-numbered substrings are '14', '1432', '4', 
'432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as 
a separate substring.

1 take a string of digits arg
2 return the number of even-valued substrings that can be made
3 if a substring occurs more than once, count EACH occurence

E
any sub whose int value is even

D
string input
int output
list of substrings (comprehension?)

A
make a list of substrings for which int(substring) % 2 == 0 is true
    even_subs = [string[i: j + 1] if string[i: j + 1] % 2 == 0
                for i in range(len(string)) for j in range(len(string))]

reutrn len(even_subs)

SOLVED: 11.5 mins, fussed with indices a little, and forgot to coerce my 
substrings to ints before checking evenness, but got it sorted fairly quickly
'''
# def even_substrings(string):
#     even_subs = [string[i: j + 1] for i in range(len(string)) 
#                  for j in range(len(string))
#                 if len(string[i: j + 1]) != 0
#                 and int(string[i: j + 1]) % 2 == 0]
#     # even_subs = []

#     # for i in range(len(string)):
#     #     for j in range(len(string)):
#     #         if len(string[i: j + 1]) != 0 and string[i: j + 1] % 2 == 0:
#     #             even_subs
    
#     return len(even_subs)


# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)

'''
15***
P
Create a function that takes a string argument that consists entirely of 
numeric digits and computes the greatest product of four consecutive digits 
in the string. The argument will always have more than 4 digits.

1 take a string arg of digits
2 compute greatest product of 4 consecutive digits
3 string will always have more than 4 digits

E

D
String input
Int output
List of 4 digit substrings

A
collect all 4 digit substrings
four = [list(string[i: i + 4]) if len(string[i: i + 4]) == 4
        for i in range(len(string))]

get highest product of substring
    greatest = 0
    for sub in four:
        product = sub[0] * sub[1] * sub[2] * sub[3]
        if product > greatest:
        greatest = product
    
    return greatest

SOLVED: a little over 10 mins, would still like to find a better way than hard
coding `product = int(sub[0]) * int(sub[1]) * int(sub[2]) * int(sub[3])`.
Feels like there should be a simple-enough way to multiply all items in a list
of any length. There is, see below!
'''

# def greatest_product(string):
#     four = [list(string[i: i + 4]) for i in range(len(string))
#             if len(string[i: i + 4]) == 4]
#     greatest = 0
#     product = 1
    
#     for sub in four:
#         for char in sub:
#             product *= int(char)
#         if product > greatest:
#             greatest = product
#         product = 1
        
#     return greatest
    

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

'''
17
P
Create a function that takes a list of integers as an argument. The function 
should determine the minimum integer value that can be appended to the list 
so the sum of all the elements equal the closest prime number that is greater 
than the current sum of the numbers. For example, the numbers in [1, 2, 3] 
sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to 
the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

To check primeness: if dividing a number by anything between 2 and the
number's own square root (inclusive) results in an integer, it is not prime. 
math.sqrt() can help here. Or if the number is < 2, it's not prime.

1 take a list of ints arg
2 determine the min int value that can be added to the list so the sum of the
    list is equal to the closest prime that is greater than the current sum
    of the list
3 

E

D
List input
Int output
Range to test primeness

A
sum the list and save value

starting with sum + 1, check primeness
    - if divisible by any num between 2 and sqrt(sum), NOT prime
        - incremement to sum + 2 (etc) and try again, until prime
    - if not evenly divisible by 2 - sqrt(sum), is prime

once prime is found, get the difference between sum(list) and prime

return difference

FAILED: Got almost there by about 15-16 minutes, but had a bug I couldn't find.
Turned out to be just that I was using `int(math.sqrt(check + 1))` for the top
end of my range, when I should have used `int(math.sqrt(check)) + 1`. This was
resulting in 2/5 tests failing. 
Lesson here is that what I wanted was to check range(2, sqrt(check)) INCLUSIVE
or sqrt(check) + 1 - by placing that `+ 1` inside the parenths, I was adding it
to `check` before the math.sqrt() function did its thing, which means 
(a) I was checking the wrong set of numbers, and
(b) I was incorrectly setting the upper bound of my range
'''
import math

def is_prime(check):
    divisors = range(2, int(math.sqrt(check)) + 1)

    for div in divisors:
        if (check / div) % 1 == 0:
            return False
    
    return True

def nearest_prime_sum(numbers):
    total = sum(numbers)
    n = 1
    
    while not is_prime(total + n):
        n += 1       

    print(n)
    return n


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)