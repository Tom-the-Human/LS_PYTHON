"""
1
P
Write a function that takes a string and returns a dictionary containing the 
following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie 
between "0.00" and "100.00", respectively. 
Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.
1 Return a dict containing the percentage of letter cases in a string
2 The percentages mut be strings with a value between "0.00" and "100.00"
3 and must be formatted to 2 decimal places

E
No surprises.

D
String in. Dict out. Probably use the dict as a counter as well.
Or maybe better to use a different counter.

A
- For each char in string
    - if char isupper
        - count + 1 uppercase
    - if char islower
        - count + 1 lowercase
    - else
        - count + 1 neither
- Use math to determine the percentages (how?)
    - count / len(string) seems right
        - in the first example, there're 10 chars and half are lowercase
        - 5 / 10 == .5
        - 1 / 10 == .1
        - 4 / 10 == .4
    - Yes. Ok. Now with those decimals it's easy enough to do
        - decimal * 100 == percent (i.e. .5 * 100 = 50% or "50.00")
- Assign these percents to the dict and return the dict
    
 
C
"""
# def letter_percentages(string):
#     case_dict = {'lowercase': 0, 'uppercase': 0, 'neither': 0}
    
#     for char in string:
#         if char.islower():
#             case_dict['lowercase'] += 1
#         elif char.isupper():
#             case_dict['uppercase'] += 1
#         else:
#             case_dict['neither'] += 1
    
#     case_dict = {
#         'lowercase': f"{((case_dict['lowercase'] / len(string)) * 100):.2f}",
#         'uppercase': f"{((case_dict['uppercase'] / len(string)) * 100):.2f}",
#         'neither': f"{((case_dict['neither'] / len(string)) * 100):.2f}"
#     }

#     return case_dict


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
2
P
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must 
be greater than the length of the longest side, and every side must have a 
length greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as 
arguments and returns one of the following four strings representing the 
triangle's class: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

1 Return a string classifying the type of triangle
2 Valid triangle requires:
    - len(2 shorter sides together) > len(longest side)
    - all len(side) > 0
3 If valid, classify type by above criteria

E
no news

D
Input is 3 individual numbers, output is a string
Might use a list or dict

A

- If any side value is 0, return 'invalid'

- Call the sides a, b, c
- First, find the longest side
    - longest == a
    - if b > longest, longest == b
    - c > longest, longest == c
    - OR is there a math function for this? There is in Java.*
- Use similar logic to get the shortest
- Lastly, whichever side is `not in` (longest, shorted) is mid

- If longest > (shortest + mid) return 'invalid'

- else compare a, b, & c to determine how many sides are the same length
    - how to code this? 
        - if longest == shortest then all 3 must be equal
        -  if longest == mid and mid != shortest
            or shortest == mid and mid != longest then 2
        - if longest != mid and mid != shortest
        - There must be a better way!*

    - if 3, return 'equilateral'
    - if 2, return 'isosoceles'
    - if 1, return 'scalene'
"""
# def triangle(a, b, c):
#     if 0 in [a, b, c]: 
#         return 'invalid'
    
#     longest = max(a, b, c)
#     shortest = min(a, b, c)
#     mid = sum([a, b, c]) - longest - shortest

#     if longest > (shortest + mid):
#         return 'invalid'
    
#     if longest == shortest: # if longest == shortest, all must be equal
#         return 'equilateral'
    
#     if mid in [longest, shortest]:
#         return 'isosceles'
    
#     return 'scalene'

# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

"""
3
P
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
worry about floating point errors. You may also assume that the arguments 
are in degrees.

1 Take 3 int arguments representing degrees
2 Return a string representing the type of triangle or 'invalid' 
    if not a valid triangle, according to the rules stated above
3 No floats

E
No surprises

D
Might use a list for easy/concise evaluation
ints in, strings out

A
- check if all 3 sides add to 180
    - sum([a, b, c])
    - if not, return 'invalid'
- check if any side is <= `0`
    - all([a, b, c])    *this condition works for the examples, but
        would not work for negative ints ...
    - if not, return 'invalid'
    * both steps abov can be done on 1 line with `or`
- if any side is 90, return 'right'
- if any sides greater than 90, return 'obtuse'
- else return 'acute'

My solution passes all tests, but would not work if a negative number was
passed in as an argument. I updated my code based on LS solution:
Instead of `not all([a, b, c])` use `not all(angle > 0 for angle in angles)`
"""
# def triangle(a, b, c):
#     angles = [a, b, c]
#     if sum(angles) != 180 or \
#         not all(angle > 0 for angle in angles):
#         return 'invalid'

#     for angle in angles:
#         if angle == 90:
#             return 'right'
#         if angle > 90:
#             return 'obtuse'
    
#     return 'acute'

# print(triangle(60, 70, 50) == "acute")      # True
# print(triangle(30, 90, 60) == "right")      # True
# print(triangle(120, 50, 10) == "obtuse")    # True
# print(triangle(0, 90, 90) == "invalid")     # True
# print(triangle(50, 50, 50) == "invalid")    # True


"""
4
P
Some people believe that Fridays that fall on the 13th day of the month are 
unlucky days. Write a function that takes a year as an argument and returns 
the number of Friday the 13ths in that year. You may assume that the year is 
greater than 1752, which is when the United Kingdom adopted the modern 
Gregorian Calendar. You may also assume that the same calendar will remain in 
use for the foreseeable future.

1 Take a year greater than 1752
2 Return the number of Friday the 13ths

E
Looks straightforward

D
None really
int in, int out
Use a counter

A
- import datetime
- init `f13s`
- find the syntax to retrieve the year input from datetime
    - do that and assign it to `year`
    - Friday is day `4` of any given week
    - datetime includes the weekday() method to get the day of the week for a 
        date (Monday is 0, Sunday is 6)
        
- for `year`, increment `f13s` for each Friday the 13th
    - I'll have to look this up as I have no idea how
    - Fingers crossed the docs are clear
    - Try it, but if not clear, ask AI how to use it
    - There is only 1 '13th' per month, so determining if it is a Friday (`4`)
        - for month in year:   # maybe it's like this
            - find what day the 13th is, and
            - if Friday, append to `f13s` list
    - I don't know how to perfectly get there, but I have info to get started

- return `len(f13s)`

- Ok, I'm going to look at the solution. I could probably figure it out
eventually, but so much of this is just figuring out how to use `datetime`.
I did figure out the algorithm, I just need to be shown how to implement it.

Looks pretty intuitive, actually. See below.
I think this is even an improvement on LS's solution, since I moved their
for loop filter into the list comprehension, so the 13ths that are not Fridays
aren't added in the first place.
"""
# import datetime

# def friday_the_13ths(year):
#     f13s = [datetime.date(year, month, 13)
#             for month in range(1, 13)
#             if (datetime.date(year, month, 13)).weekday() == 4]
    
#     return len(f13s)



# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

"""
5
P
A featured number (something unique to this exercise) is an odd number that 
is a multiple of 7, with all of its digits occurring exactly once each. For 
example, 49 is a featured number, but 98 is not (it is not odd), 97 is not 
(it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there is 
no next featured number.

NOTE: The largest possible featured number is 9876543201.

1 Return the NEXT featured number greater than the input
2 Input and output are ints
3 Return an error message if the number is greater than 9876543201
4 Featured number == odd, multiple of 7, no repeat digits

E
A specific error message is prescribed.

D
String coercion may be needed to determine digit repetition

A
- take an int arg
- if arg > 9876543201 return error
- init `featured = 7` (smallest possible featured number)
- while featured < arg OR featured % 2 == 0
    - `featured += 7`
- if str(featured) contains any repeat chars (how?)
    `featured += 7`, then run other checks again,
    so this probably should go in the while loop
    - for char in list(str(featured)): (nest in while loop)
        if list.count(char) > 1
        continue (move to next iteration, regardless of other criteria)
- return featured
"""
# def next_featured(num):
#     if num >= 9876543201:
#         return ("There is no possible number that "
#                 "fulfills those requirements.")
    
#     featured = num + 1
#     while featured % 7 != 0:
#          featured += 1

#     while (featured % 2 == 0 \
#         or len(set(str(featured))) != len(str(featured))) \
#         or featured <= num:
#             if featured % 2 == 1:
#                  featured += 14
#             else:
#                  featured += 7
    
#     return featured

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

"""
6
P
Write a function that computes the difference between the square of the sum 
of the first count positive integers and the sum of the squares of the first 
count positive integers.
1 square the sum of the "first count" positive integers (unclear what that is)
2 sum the squares of the first count positive integers (???)
3 return the difference between these

E
First example comments are helpful. Where `count` (I guess?) is `3`, the
return value is `22`, as seen here:
22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
        sum squared minus sum of squares
So it becomes clear that we are actually adding up all the values from 
1 to `count` inclusive, squared either before or after summation.

D
Maybe a list, set, or just a range.
Range will be used regardless, but would use list or set to save the
values to a variable. 
I/O is all ints.

A
- sum a range of 0 to `count + 1` (or 1 to count + 1 if we're being pedantic/
    or desperate to save clock cycles)
    square it and assign to variable
- for a range up to `count + 1` square each number in the range
    - will need to save these to a collection
    - sum the collection
- subtract the second result form the first one
- return that final value
"""
# def sum_square_difference(count):
#     sum_sq = sum(range(count + 1))**2

#     sq_sum = sum([num**2 for num in range(count + 1)])

#     return sum_sq - sq_sum

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

"""
7
P
Bubble Sort is one of the simplest sorting algorithms available. It is not an 
efficient algorithm, so developers rarely use it in real code. However, it is 
an excellent exercise for student developers. In this exercise, you will 
write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On 
each pass, the two values of each pair of consecutive elements are compared. 
If the first value is greater than the second, the two elements are swapped. 
This process is repeated until a complete pass is made without performing any 
swaps. At that point, the list is completely sorted.

1 Write a function that sorts a list by comparing 2 elements at a time
    over multiple consecutive passes, swapping the elements if the
    2nd element is less than the 1st element
2 If a complete pass is made without any swaps, end the process

E
There is a table shown in the problem deconstruction, which shows that more
than one swap may be made udring a single pass through the list. 
To me, looks like loop comparing `i` to `i + 1`

D
List in
We're just mutating the input list, so no other structure or return value

A
- for i in range(len(list) - 1):         # `- 1` to avoid IndexError
    - if list[i] > list[i + 1]:
        - list[i], list[i + 1] = list[i + 1], list[i]         # swap
- # I suspect the loop above is incomplete, needing to be nested or adjusted
    in some way to ensure the loop keeps going until the list is fully sorted.
    - That is correct. How can I ensure it keeps running until all sorting is
        done, but not longer?

- Well, I almost got the but couldn't get it finish sorting all the way.
    For some reason, the list of strings was really far off, but the longer
    list of ints was close except for 2 and 1 being reversed. Maybe just due
    to number of elements/iterations?
    - My solution is really close to LS's and I'm not yet sure why my solution
        doesn't work and theirs does. I approaching every step in an almost 
        identical manner. I guess that "almost" is my problem ...
    Key differences:
    - I define swapped inside the for loop, not just inside the while loop
        - BINGO! This was the only issue. Moving `swapped = 0` to before
            the for loop solved the problem
        - I see now that resetting swapped inside the for loop meant that
            the loop would never run enough times, since `swapped` would
            always be 0 if the final 2 elements weren't swapped, when what
            is needed is swapped to be 0 ONLY IF no swaps were made during
            the entire pass through the list
"""
# def bubble_sort(list_in):
#     swapped = 1
#     while swapped:
#         swapped = 0
#         for i in range(len(list_in) - 1):
#             if list_in[i] > list_in[i + 1]:
#                 list_in[i], list_in[i + 1] = list_in[i + 1], list_in[i]
#                 swapped = 1

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True