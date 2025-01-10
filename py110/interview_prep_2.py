"""
1***
P
Create a function that takes a list of numbers as an argument. For each 
number, determine how many numbers in the list are smaller than it, and 
place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs 
multiple times in the list, it should only be counted once.

1 take a list of ints arg
2 for each number, count how many numbers in the list are smaller
3 only count unique values
4 return a list of the counts

E
clarifies rule 3
if all nums are same, counts will be 0

D
List input
List output (can be done with comprehension?)
Set

A
- for each number, count how many unique smaller numbers in list


- append count to counts list
    counts = []

    - w/ comprehension?
    - [numbers.count(num) for num in numbers ] nope

    - for num1 in numbers:
        - counts = 0
        - for num2 in set(numbers):
            - if num2 < num1:
                count += 1
            counts.append(count)
        

- return counts list

SOLVED: 15 mins, only had a couple small problems, including appending to the
list at the wrong level of nesting. Nested loops are confusing, so let's try
a comprehension again, got 5 minutes remaining to put it into one.

Didn't figure out comprehension on my own, copied from LSBot. But the takeaway is
that [sum(1 for element if condition) for element in collection] is a good
way to count in a comprehension. sum(1) is the key.

SOLVE AGAIN, BUT MUST USE COMPREHENSION!
"""
# def smaller_numbers_than_current(numbers):
#     counts = []

#     # for num1 in numbers:
#     #     count = 0
#     #     for num2 in set(numbers):
#     #         if num2 < num1:
#     #             count += 1
#     #     counts.append(count)

#     counts = [sum(1 for num2 in set(numbers) if num2 < num1)
#                 for num1 in numbers]
#     print(counts)
#     return counts

# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

"""
3***
P
Create a function that takes a string argument and returns a copy of the 
string with every second character in every third word converted to uppercase.
 Other characters should remain the same.

1 take a string arg
2 return a copy of the string, with every 2nd char in every 3rd word uppercase
3 make no other changes to the string

E

D
String input
String output
List of words (split)
Sublists of individual chars in words?

A
- split string into list of words
    - words = string.split()

- split words into lists of chars
    - words = [[char for char in word] for word in words]

- itentify can capitalize odd index chars in index/3 words
    - for idx, word in enumerate(words):
        if idx % 3 == 0:
            for j, char in enumerate(word):
                if j % 2 == 1:
                    char = char.uppercase()
        word = ''.join(word)

- rejoin chars, words, and then return
return ' '.join(words)

FAILED: Pretty much total failure. Still not actually mutating the list.
Changing the string elements in the sublist is not resulting in the strings
in the main list being changed. This is really bugging me.
Partially fixed this - don't reassign the `char`, reassign the list
element directly, i.e. `word[2][1]`. **For some reason this worked on part of
this exercise, but caused a TypeError part way through the first test. 
Why part way through and not right away? 

Further, the deepely nested fors and ifs have to go. Pretty confusing way to
do things and too often ends up being my default.**
"""
# def to_weird_case(string):
#     words = string.split()
#     words = [[char for char in word] for word in words]
    

#     for i, word in enumerate(words):
#         if i % 3 == 0: # NO, WRONG
#             for j, char in enumerate(word):
#                 if j % 2 == 1:
#                     words[i][j] = char.upper()
#                 print(word)
#         words = [''.join(word) for word in words]

#     print(words)

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

"""
4***
P
Create a function that takes a list of integers as an argument and returns a 
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

1 take list of ints arg
2 return a tuple of 2 nums that are closest together in walue
3 if multiple pairs equally close, return pair with lowest indices

E

D
List input
Tuple output
Possibly list of tuples, or dict of tuples

A
- get all possible 2 element tuples , dict where key is difference between
    the tuple elements, and value is tuple pair
    pairs = {difference: (num1, num2), ...}
        - comprehension?
        {difference: (num1, num2) for abs(num1 - num2) in list}

- return the value with the min(difference)
    - return min(pairs)  # probably wrong syntax

FAILED: Barking up the wrong tree. Comprehensions cannot check whether a value
already exists before updating the dict, because that's not how comprehensions
work. The entire comprehension expression is calculated together, not via
iteration as with a for loop. So this problem needs to be solved with for loops.
Further, I failed again to reember how to return the value of a dict key: value
pair, based on an evaluation of the key. I.e. return the value with the lowest 
key, as I am trying to do here. *syntax is dict[min(dict)]*
"""

# def closest_numbers(numbers):
#     pairs = {abs(num1 - num2): (num1, num2) for num2 in numbers
#              for num1 in numbers if num1 != num2}


#     print(pairs[min(pairs)])

#     return min(pairs)

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

"""
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
2 return number of identical pairs in the list
3 if less than 2 values, return 0
4 count each complete pair of the same int 

E

D
List input
Int output (pair count)
Dictionary {int: count,}

A
- collect counts of each value in the list
    - counts = {num: lst.count(num) for num in lst}

- init total_pairs = 0
    - for count in counts.values():
        total_pairs += count // 2

- return total_pairs

SOLVED: Done in about 9 mins, but that's after struggling yesterday and having
another student suggest a dictionary to keep my counts. This was WAY better than
the mess I made yesterday with a bunch of nested loops and conditionals.
Wouldn't hurt me to do it one more time, but I think it's optional if I can
remember some key takeaways.
Problem type: match and count
For this kind of problem, count method is indispensible. 
Using a dict to track {object: count} is an ideal way to keep track and avoid 
counting the same object twice, without the need to mutate the original data.
"""
# def pairs(lst):
    # counts = {num: lst.count(num) for num in lst}
    # total_pairs = 0

    # for count in counts.values():
    #     total_pairs += count // 2

    # return total_pairs

    

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

"""
9
P
Create a function that takes two string arguments and returns the number of 
times that the second string occurs in the first string. Note that 
overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

1 TAKE 2 STRING ARGS
2 return number of times 2nd arg appears in first arg
3 do NOT count overlapping strings
4 2nd arg is never empty

E
1 if 1st arg empty, return 0
2 all tests are 100% lowercase letters

D
Strings input x2
Int output
Maybe a list to hold instances of the string, but could be done with just
a counter, I think

A
- init counter = 0
- init found = True

- while found:
    found = False

- determine if the 2nd string can be found in first string
    - str2 in str1

- if so, increment counter and remove instance of 2nd string from 1st string
    - found = True
    - then go back to step 2 to determine if another instance is found

- if not, return counter

SOLVED: about 12.5 minutes. Worked out really well! Couple missteps. There is no
string.remove() method, I wanted string.replace(). I also initially forgot to
reassign `str1` to the result of `str1.replace(str2, '', 1)`. 
Overall, great job!
"""
# def count_substrings(str1, str2):
#     counter = 0
#     found = True

#     while found:
#         found = False
#         if str2 in str1:
#             found = True
#             counter += 1
#             str1 = str1.replace(str2, '', 1)

#     return counter


# print(count_substrings('babab', 'bab') == 1)
# print(count_substrings('babab', 'ba') == 2)
# print(count_substrings('babab', 'b') == 3)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('babab', 'x') == 0)
# print(count_substrings('', 'x') == 0)
# print(count_substrings('bbbaabbbbaab', 'baab') == 2)
# print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
# print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

"""
10***
P
Create a function that takes a string of digits as an argument and returns 
the number of even-numbered substrings that can be formed. For example, in 
the case of '1432', the even-numbered substrings are '14', '1432', '4', 
'432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as 
a separate substring.

1 take a string of digits arg
2 return the number of even-numbered substrings
3 if a substring occurs more than once, count each occurence

E

D
String input
Int output
List for substrings

A
- try to do with comprehension
- append each possible substring to a list, if int(substring) % 2 == 0
    - string[i + 1: j] for string[i + 1: j] in string if string[slice]
        is even - hmm ... going to need to use standard nested for loop
        to start, but can convert to comprehension pretty easily I think

- return len(list)

SOLVED: 19 mins - I spent MUCH TOO LONG messing with indices for the slice.
    That was just silly and is unnacceptable for the interview. I just watched
    Shelby do this yesterday in like 12 mins and without half the missteps. 
    I didnt even have time to put it in a comprehension due to failing to
    understand what indices to use.
    I had the range in my 2nd loop wrong (make sure to start at `i` for this
    kind of problem). And I kept hacking around for different permutations
    of digits[i: j] spending probably 5+ minutes just fooling with that. 
Problem type: Compare and count
"""
# def even_substrings(digits):
#     subs = [digits[i: j + 1] for i in range(len(digits))
#             for j in range(i, len(digits))
#             if int(digits[i: j + 1]) % 2 == 0]

#     # for i in range(len(digits)):
#     #     for j in range(i, len(digits)):
#     #         if int(digits[i: j + 1]) % 2 == 0:
#     #             subs.append(digits[i: j + 1])

    
#     return len(subs)

# print(even_substrings('1432') == 6)
# print(even_substrings('3145926') == 16)
# print(even_substrings('2718281') == 16)
# print(even_substrings('13579') == 0)
# print(even_substrings('143232') == 12)


"""
11
P
Create a function that takes a nonempty string as an argument and returns a 
tuple consisting of a string and an integer. If we call the string argument
 s, the string component of the returned tuple t, and the integer component 
 of the tuple k, then s, t, and k must be related to each other such that s 
 == t * k. The values of t and k should be the shortest possible substring 
 and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase 
alphabetic letters.

1 take a nonempty string arg
2 return tuple consisting of a string and an integer
3 string == (t * k) must be true, where t is a substring and k is an int
4 t must be the shortest possible substring and k must be the largest possible
    int that will satisfy rule 3
5 string arg is 100% lowercase alphas

E

D
String input
Tuple output of str, int
List of all possible substrings

A
- collect all possible substrings
    - any valid sub will start at index 0

- find the shortest possible substring that can be multiplied to make the string
    - sort the list by length (shortest first) to ensure checking subs in order
        of length, (ensures shortest possible should be checked before a possible
        longer substring that could be used)
    - try multiplying the sub by ints ranging from len(string) to 1, largest to
        smallest, to find right combo sooner

- return (substring, multiplier)

SOLVED: just under 15 mins. Yep. Felt pretty good. No significant missteps,
just a couple of off-by-1 errors that were easily resolved.
"""
# def repeated_substring(string):
#     subs = sorted([string[:i + 1] for i in range(len(string))])
    
#     for sub in subs:
#         for num in range(len(string), 0, -1):
#             if string == sub * num:
#                 return (sub, num)

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))

"""
15***
P
Create a function that takes a string argument that consists entirely of 
numeric digits and computes the greatest product of four consecutive digits 
in the string. The argument will always have more than 4 digits.

1 take string arg of numeric digits
2 compute greatest product of 4 consecutive digits
3 string will always have more than 4 digits
4 return product

E

D
String input
Int output
List, probably nested

A
- collect relevant substrings (4 chars exactly)
    - coerce substrings to lists, which should split them to individual nums
    - subs = [list(string[i; i + 4]) for i in string]

- compute product of each substring list
    - sub[0] * sub[1] * ... is there a better way to do this?
    - replace the sub with the product

- return max(subs)

SOLVED: actually failed once, got tangled up mostly in syntax shit. Took a
break and then attempted again. Done in 10 mins, though the prob and solution
were fresh in mind. ***Would be good to do again.***
"""

# def greatest_product(string):
#     subs = [list(string[i: i + 4]) for i in range(len(string))
#             if len(list(string[i: i + 4])) == 4]

#     for i, sub in enumerate(subs):
#         subs[i] = int(sub[0]) * int(sub[1]) * int(sub[2]) * int(sub[3])
        
#     return max(subs)

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6


"""
16
P
Create a function that returns the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in 
the input string. You may assume that the input string contains only 
alphanumeric characters.

1 return the count of distinct case-insensitive letters and digits that
    occur more than once in the input string
2 take a string arg of only alphanumerics

E
doesnt matter how many times the char repeats

D
String input
Int output
Dict to store char: count

A
- init counter = 0
counts = {char: string.count(char) for char in string.casefold()}
- count number of occurences of each char in string.casefold()
    - is there string.count()? if not, coerce to list
    - for char in string.casefold():

- count the number values in counts dict that are greater than 1
    - for count in counts.values():
    counter = sum(1 for (count > 1) in counts.values())

SOLVED: under 13 mins. Got a little tangled up with the counts not accurately
recording my casefolded chars, which I resolved by calling casefold on the string
before creating the dictionary. Overall, good performance.
Problem type: match and count
"""
# def distinct_multiples(string):
#     string = string.casefold()

#     counts = {char: string.count(char) for char in string}

#     return sum((count > 1) for count in counts.values())

# print(distinct_multiples('xyz') == 0)               # (none)
# print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
# print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
# print(distinct_multiples('unununium') == 2)         # u, n
# print(distinct_multiples('multiplicity') == 3)      # l, t, i
# print(distinct_multiples('7657') == 1)              # 7
# print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
# print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

"""
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

***I'm going to do this pasting in the is_prime function that I wrote for one
of the small exercises. While this would not be acceptable for the interview,
I honestly doubt I will be given a problem that requires me to have memorized
a mathematical formula, which is what trips me up on this the most.***

1 take a list of ints arg
2 find the minimum int value that can be added to the list to equal the next
    prime number that is greater than the current sum of the list
3 return that value (difference between prime and sum(list))

E

D
List input
Int output
Range to test primeness

A
- total = sum(list)

- check (total + n) for primeness (start at total + 1)
    - if prime, return n
    - can do with while loop and is_prime function

SOLVED: see note above*** 7.5 mins using my prewritten is_prime function,
worked on first run. Probably not a good test, but again, I don't expect to
have to solve for primeness in the interview. Might try once more without the
function, but with the formula available, which is a more likely scenario
"""
import math

def is_prime(num):
    if num <= 1:
        return False
    
    divisors = [integer for integer in range(2, int(math.sqrt(num)) + 1)]

    for d in divisors:
        if (num / d) % 1 == 0:
            return False
    
    return True

def nearest_prime_sum(numbers):
    total = sum(numbers)
    n = 0
    prime = False

    while not prime:
        n += 1
        prime = is_prime(total + n)
            
    
    return n

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)