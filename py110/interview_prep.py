# Solve these in 20 min or less!
"""
1
Create a function that takes a list of numbers as an argument. For each 
number, determine how many numbers in the list are smaller than it, and 
place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs 
multiple times in the list, it should only be counted once.

1 take a list arg
2 for each number, determine how many numbers in the list are less than it
3 place the result of each count in a new list and return that list
4 only count unique number values, ie only multiple instances of a number
    should not be counted multiple times

E
Tests show result numbers in order. Ie. 3 numbers smaller than 8, 0 numbers
smaller than 1, 1 number smaller than 2, 2 numbers smaller than 3. Count is
performed FOR each duplicate, but duplicates are not counted when determining
the count for a given number.

D
List in, list out. Doesnt seem any more are needed.

A
- init result_list = []
- nested for loop would do this well
    - for num in numbers:
        - current_num = num
        - for num2 in set(numbers):
            - count = 0
            - if num2 < current_num:
                count += 1
        - result_list.append(count)
    -return result_list
            

"""
# def smaller_numbers_than_current(numbers):
#     result_list = []

#     for num in numbers:
#         current_num = num
#         count = 0
#         for num2 in set(numbers):
#             if num2 < current_num:
#                 count += 1
#         result_list.append(count)

#     return result_list

# print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
# print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
# print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
# print(smaller_numbers_than_current([1]) == [0])

# my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
# result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
# print(smaller_numbers_than_current(my_list) == result)

"""
2
P
Create a function that takes a list of integers as an argument. The function 
should return the minimum sum of 5 consecutive numbers in the list. If the 
list contains fewer than 5 elements, the function should return None.

1 take a list of ints
2 return the minimum sum of any 5 CONSECUTIVE numbers in the list
3 if less than 5, return None (explicitly?)

E
No surprises, ints may be negative

D
List in, int out. Maybe an intermediary list, but probably not

A

- if len(list) >= 5:
    - init sub_sums = []

    - for num in list:
        - try:
            sub_sums += list[num: num + 5]
        - except:
            break

    - min_sub = min(sum(sub_sums(sub)) for sub in sub_sums)
    - return min_sub

"""
# def minimum_sum(numbers):
#     if len(numbers) >= 5:
#         sub_sums = []

#         for i, _ in enumerate(numbers):
#             try:
#                 if len(numbers[i: i + 5]) == 5:
#                     sub_sums += [numbers[i: i + 5]]
#             except IndexError:
#                 break

#         min_sum = min(sum(sub) for sub in sub_sums)
#         return min_sum

# print(minimum_sum([1, 2, 3, 4]) is None)
# print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
# print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
# print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
# print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

"""
3
Create a function that takes a string argument and returns a copy of the 
string with every second character in every third word converted to uppercase.
 Other characters should remain the same.

 1 return a COPY of the string arg
 2 Every 2nd char of every 3rd word should be UPPERCASE
 3 Other chars should not change

E
No surprises

D
String input
String output (copy)
May use a list to hold words or even nested list w chars

A
1 split string to word_list
2 identify and capitalize the selected letters
- for i in range(2: len(word_list): 3):
    - for j, char in word_list[i]:
        - if j % 2 != 0:
            - char = char.upper() # this might not work, so alternatively
            - 
            
3 return ' '.join(word_list)

***
FAILED: spent 22 MINS without success, so stopped and deconstructed 
with ChatGPT.
Logic was sound but my problem was not correctly capitalizing the targeted
letters - I had at first failed to properly split each word into a list of
strings, which seems to be necessary for this type of problem. Also
reassigning the `char` object directly did not seem to work, where as 
referencing the list element `words[i]` DID work.***

Alternative for loop offered by ChatGPT packs most of the logic into a
list comprehension:
    for i in range(2, len(words), 3):  # Select every third word
        words[i] = ''.join(
            char.upper() if j % 2 != 0 else char
            for j, char in enumerate(words[i])
        )
***
        
"""

# def to_weird_case(string):
#     words = string.split()

#     for i in range(2, len(words), 3):
#         chars = list(words[i])
#         for j in range(1, len(chars), 2):
#             chars[j] = chars[j].upper()
#         words[i] = ''.join(chars)
        
#     print(words)
#     return ' '.join(words)

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# # print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)

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

    DICT.GET() is the way!!! `get` retrieves the value associated with a
    given key, so `pairs.get(min(pairs))` gets the value of the minimum
    key in pairs.
"""

# def closest_numbers(numbers):
#     pairs = {}

#     for num1 in numbers:
#         for num2 in numbers:
#             diff = max(num1, num2) - min(num1, num2)
#             if diff in pairs.keys() or diff == 0:
#                 pass
#             else:
#                 pairs[diff] = (num1, num2)
    
#     return pairs.get(min(pairs))

#     # return lowest in pairs

# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))


"""
5
P
Create a function that takes a string argument and returns the character that 
occurs most often in the string. If there are multiple characters with the 
same greatest frequency, return the one that appears first in the string. 
When counting characters, consider uppercase and lowercase versions to be the 
same.

1 take a string arg
2 return the most frequently occuring char in the string, disregarding case
3 if 2 chars are even, return the one at the lowest index

E
nothing of note

D
String input
String output
Might use another dict for count. Hopefully can remember syntax this time.

A
- init empty count dict
    - can probably make this a comprehension
    - key = count of char.casefold() in string, value = char
        - if key already exists, it's from a char at a lower index
            - though that might only work with regular for loop

- if not comprehension, then for loop to populate dict
    - for char.casefold() in string:
        - if string.count(char) not in count:
            - count[string.count(char)] = char.casefold()
            
- return count.get(max(count))

SOLVED: 13 mins
"""
# def most_common_char(string):
#     count = {}
#     for char in string.casefold():
#         if string.count(char) not in count:
#             count[string.casefold().count(char)] = char

#     return count.get(max(count))

# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')

"""
6
P
Create a function that takes a string argument and returns a dict object in 
which the keys represent the lowercase letters in the string, and the values 
represent how often the corresponding letter occurs in the string.

1 take a string arg
2 return a dict object (keys are lowercase letters, value is times it occurs)

Implicitly, only lowercase letters are to be counted

E
examples show only lowercase letters being counted, no uppercase or special

D
string in
dict out
no others needed

A
- probably doable with a comprehension
- lowercase dict = {char: count for char, string.count(char)
                    if char.islower()}

SOLVED: 7.5 minutes, struggled a little on syntax
"""
# def count_letters(string):
#     return {char: string.count(char) for char in string
#             if char.islower()}


# expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
# print(count_letters('woebegone') == expected)

# expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
#             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
# print(count_letters('lowercase/uppercase') == expected)

# expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
# print(count_letters('W. E. B. Du Bois') == expected)

# print(count_letters('x') == {'x': 1})
# print(count_letters('') == {})
# print(count_letters('!!!') == {})

"""
7
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
2 return number of identical pairs in list
3 return 0 if the list has less than 2 ints - len(list) < 2
4 additional pairs of the same int should also be counted (but not if unpaired)

E
no news

D
list input
int output

A
- init num_count = 0
- init pair_count = 0
- init last_count = 0
- done = False
- while not done:
    - for each num in list:
        - current = num
        - if num == current:
            - num_count += 1
        - pair_count += num_count // 2 (counting pairs, not singles)    
        - num_count = 0
    - remove all elements equaling num from list
- repeat

- I'm making this so much harder than it needs to be.
Use the count method. 5 mins left. Try the algorithm again.

- counted = []
- for num in list:
    - if num not in counted:
        - num_count = list.count(num)
        - pair_count += num_count // 2
        - counted.append(num)

- return pair_count

SOLVED: 19.25 mins - interrupted once and looked at list methods from notes
Spent a long time trying to write code that the count method already does, 
but did manage to pull it together even starting the algorithm over again.
This code could be shortened by removing `num_count` and just assigning
`pair_count += numbers.count(num) // 2` ...
"""
# def pairs(numbers):
#     pair_count = 0
#     counted = []

#     for num in numbers:
#         if num not in counted:
#             num_count = numbers.count(num)
#             pair_count += num_count // 2
#             counted.append(num)

#     return pair_count


# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

"""
8
P
Create a function that takes a non-empty string as an argument. The string 
consists entirely of lowercase alphabetic characters. The function should 
return the length of the longest vowel substring. The vowels of interest 
are "a", "e", "i", "o", and "u".

1 take a non-empty string of lowercase letters
2 return an int of the length of the longest vowel substring
3 aeuio

E
Contiguous vowels

D
String in
Int out
I dont think this needs any intermediary DS, just a counter

A
- init vowels = 'aeuio'
- init counter = 0
- init max_vowels = 0

- for char in string:
    - if char in vowels:
        - counter += 1
    - else:
        - counter = 0
    - if counter > max_vowels:
        - max_vowels = counter
    
- return max_vowels

SOLVED: about 9 mins. No trouble, worked first run.
"""
# def longest_vowel_substring(string):
#     vowels = 'aeiou'
#     counter = 0
#     max_vowels = 0

#     for char in string:
#         if char in vowels:
#             counter += 1
#         else:
#             counter = 0
        
#         if counter > max_vowels:
#             max_vowels = counter
    
#     return max_vowels

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

"""
9
P
Create a function that takes two string arguments and returns the number of 
times that the second string occurs in the first string. Note that 
overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

1 take 2 string args
2 return int of times 2nd arg occurs in 1st arg
3 overlapping occurances don't count
4 arg 2 is never empty

E
all makes sense

D
2x string input
int output
probably just altered copies of arg 1

A
- count each instance of string 2 within string 1
    - count = 0

    - while True:
        - try:
            - string1.replace(string2, '', 1) # only 1 replace per loop!
        - except:
            - break
        - count += 1

- return count

FAILED: Solved after about 24 minutes and consulting notes on the 
string.replace method. Note that replace does not throw an error if the "old"
sub isn't found, so my original algorithm resulted in an infinite loop.
Do it faster and without needing notes.

What type of problem is this? 
Count y in x, return count
Search and count.
"""
# def count_substrings(string1, string2):
#     count = 0

#     while string2 in string1:
#         string1 = string1.replace(string2, '', 1)
#         count += 1

#     return count


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
10
P
Create a function that takes a string of digits as an argument and returns 
the number of even-numbered substrings that can be formed. For example, in 
the case of '1432', the even-numbered substrings are '14', '1432', '4', 
'432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as 
a separate substring.

1 take a string of digits arg
2 return an int of number of even_numbered subs that can be formed
    *Strings that represent an int evenly divisible by 2
3 a substring occuring more than once should be counted each time it appears
    * i.e. '3232' has 2 subs of '32' that should both be counted

E
a string with no even digits will return 0

D
string in
int out
list of strings will be useful, can probably make w comprehension
    and maybe a lambda or small function

A
- create a list of all possible substrings
    - use a comprehension (can I figure out how to only add the even subs?)
    - fuck me, syntax, can't do it :(
    - INSTEAD use a nested for loop
        - for i in string:
            - for j in string:
                append slice

    * this may be a good helper *
- init a counter (if odd subs in list)
    - for string in list:
        - if int(string) % 2 == 0:
            - counter +=1

- return counter (or len(list) if comprehension can filter)

SOLVED: took full 20 mins, failed to remember how to use a comprehension
    to get all substrings, let alone how to filter. Need to redo.
"""
# def is_even(sub):
#     if int(sub) % 2 == 0:
#         return True
    
#     return False

# def even_substrings(string):
#     subs = []
#     count = 0

#     for i, _ in enumerate(string):
#         for j, _ in enumerate(string):
#             if string[i:j + 1] != '':
#                 subs.append(string[i:j + 1])

#     for sub in subs:
#         if is_even(sub):
#             count += 1

#     return count


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

1 Take a non-empty string arg. string arg is 100% lowercase letters
2 Return a tuple of a string and int
3 string = s, tuple = t, int = k, so that s = t * k
*   Problem description is wrong, `t` can't be the tuple, has to be the string
    element of the tuple. NOPE, you just read it wrong. Lost time commenting
    on something that wasn't true. Look again.
4 t should be the shortest possible sub, k largest possible int, to satisfy
    s = t * k

E
no surprises

D
string input
tuple output of (substring, integer)
Probabably a list of subs

A
- make string into list of all possible subs
    subs = []
    for i, _ in enumerate(string):
        for j, _ in enumerate string:
            if string[1: j + 1]:
                subs.append(string[i: j + 1])
    

- check list to find the shortest sub that repeats to build the string arg
    subs.sort(key=len)

- alternatively, check the number of times the sub repeats and find the sub
    with the highest repeat count to make the string
        count = len(string)
        for sub in subs:
            while count:
                if sub * count == string:
                    return tuple(sub, count)
                count -= 1

- return a tuple of (sub, count)

FAILED: Spent 20 mins, got very close, but something is wrong in my way of
of checking to see if t * k == s. Nope, I was wrong! My problem was that I was
never resetting my count, so only the first sub would ever be checked. I also
had a typo in my first nested loop where I was checking the value of the wrong
slice (used `1` instead of `i`, good reason to use `idx` honestly).
"""

# def repeated_substring(string):
#     subs = []
#     for i, _ in enumerate(string):
#         for j, _ in enumerate(string):
#             if string[i: j + 1] and string[i: j + 1] not in subs:
#                 subs.append(string[i: j + 1])

#     subs.sort(key=len) # check shortest first

#     count = len(string) # highest possible count is length of string
#     for sub in subs:
#         while count:
#             if sub * count == string:
#                 print(sub, count)
#                 return (sub, count)
#             count -= 1
#         count = len(string)

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))


"""
12
P
Create a function that takes a string as an argument and returns True if the
 string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least 
once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a 
pangram since it uses every letter at least once. 
Note that case is irrelevant.

1 take a string arg
2 return True if pangram, False if not
3 Case is irrelevant

E

D
String in
Boolean out
String to store alphabet

A
- init alphabet string
- check if every letter in alphabet is in string arg
    - for char in alphabet:
        - if char not in string:
            return False

    - return True

- if yes, return True
    - else return False

SOLVED: 6 mins
"""
# def is_pangram(string):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     for char in alphabet:
#         if char not in string.casefold():
#             return False
    
#     return True

# print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
# print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
# print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
# print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

# my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
# print(is_pangram(my_str) == True)

"""
13
P
Create a function that takes two strings as arguments and returns True if 
some portion of the characters in the first string can be rearranged to match 
the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic 
characters. Neither string will be empty.

1 take 2 string args
2 return True if some of the characters in the 1st string can be rearranged
    to match the 2nd string
3 else return False
4 both strings are non-empty and contain only lowercase alphas

E

D
String input x2
Boolean output
List of individual chars of 2nd string

A
- coerce 2nd string to list

- compare list to string 1
    - for char in char_list:
        - if char not in strin1:
            False

- return True

SOLVED: 9 mins, couple missteps, but overall easy
Problem type: Comparrison
"""

# def unscramble(string1, string2):
#     char_list = list(string2)
    
#     for char in char_list:
#         if char not in string1:
#             return False
    
#     return True


# print(unscramble('ansucchlohlo', 'launchschool') == True)
# print(unscramble('phyarunstole', 'pythonrules') == True)
# print(unscramble('phyarunstola', 'pythonrules') == False)
# print(unscramble('boldface', 'coal') == True)


"""
14
P
Create a function that takes a single integer argument and returns the sum of 
all the multiples of 7 or 11 that are less than the argument. If a number is 
a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, 
and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

1 take an int arg
2 return sum of all multiple of 7 or 11 that are less than arg
3 if number is multiple of both 7 and 11, count ONCE
4 if arg is negative, return 0

E

D
Integer input
Return integer sum(list(multiples))
Intermediary list to hold multiples of 7 & 11 < than argument

A
- init multiples list
- identify and capture multiples of 7 & 11 < than argument
    - identify
        - for num in range(argument, 7, -1)
            - if num % 11 == 0:
                multiples.append(num)
            - if num % 7 == 0 and num not in multiples:
                multiples.append(num)

- return sum(multiples)  

SOLVED: 14 mins
"""

# def seven_eleven(number):
#     if number <= 0:
#         return 0
        
#     multiples = []

#     for num in range(number - 1, 6, -1):
#         if num % 11 == 0:
#             multiples.append(num)
#         elif num % 7 == 0:
#             multiples.append(num)
#     print(multiples)
#     return sum(multiples)

# print(seven_eleven(10) == 7)
# print(seven_eleven(11) == 7)
# print(seven_eleven(12) == 18)
# print(seven_eleven(25) == 75)
# print(seven_eleven(100) == 1153)
# print(seven_eleven(0) == 0)
# print(seven_eleven(-100) == 0)


"""
15
P
Create a function that takes a string argument that consists entirely of 
numeric digits and computes the greatest product of four consecutive digits 
in the string. The argument will always have more than 4 digits.

1 take a string arg of digits
2 compute the greatest product of 4 consecutive digits in the string
3 string always has more than 4 digits

1 return the greatest product

E

D
String input
Int output
Nested list - [['2','3','4','5'], ['3','4','5','6']] check prod 
    of each inner list
Could actually replace the sublist with it's product and then
    find the max()

A
- num_list = [list(sub) for sub in string if len(sub) == 4]
***if comprehension doesn't work***
- num_list = []
    for i, _ in enumerate(string):
        for j, _ in enumerate(string):
            if len(string[i: j + 1]) == 4:
                num_list.append(list(string[i: j + 1]))

- get product of each sublist in list
    for sublist in num_list:
        sublist = int(sublist[0]) * int(sublist[1]) * int(sublist[2]) * int(sublist[3])

- find highest product

- return highest product
    return max(num_list)

Problem type: Comparrison
SOLVED: 17.5 mins, took a couple missteps, but got there without a lot of trouble
Some janky code, but working. Couple more bits of insight gained:
My nested `for` loop is needlessly complicated. All I needed was to iterate
through the length of the string, not through the elements themselves, so:
    for idx in range(len(string)):
Further, since I only want substrings of length 4, I could simply say:
        num_list.append(string[idx: idx + 4])
This can actually be simplified even further with a comprehension, as I originally
hoped but couldn't figure out how to code:
    num_list = [list(string[i:i+4]) for i in range(len(string) - 3)]*
*Note that the `- 3` ensures that we stop collecting substrings when none that
are 4 chars long remain.
"""
# def greatest_product(string):
    
    # num_list = []
    # for i, _ in enumerate(string):
    #     for j, _ in enumerate(string):
    #         if len(string[i: j + 1]) == 4:
    #             num_list.append(list(string[i: j + 1]))

    # for i, sublist in enumerate(num_list):
    #     num_list[i] = int(sublist[0]) * int(sublist[1]) * \
    #         int(sublist[2]) * int(sublist[3])
    
    # return max(num_list)

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

"""
16
Create a function that returns the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in 
the input string. You may assume that the input string contains only 
alphanumeric characters.

1 take string arg
2 count distinct case_insensitive characters and digits that repeat in the string
3 return count

1 don't count any character that only appears once

E
doesnt matter how many times the char repeats, just whether it repeats

D
String input
Int output
List for chars if char.count > 1

A
- repeaters = 0
- for char in string.casefold():
    repeaters += int(char.count() > 1)

return repeaters

SOLVED: 14.75 mins, should have been done MUCH sooner. Tripping over syntax
and trying to use append with sets, which apparently isn't a thing.
See the mre efficient solution using 2 comprehensions.
"""
# def distinct_multiples(string):
#     # repeaters = 0
#     # checked = []
#     # for char in string.casefold():
#     #     if string.count(char) > 1 and char not in checked:
#     #         repeaters += 1 
#     #     checked.append(char)

#     counts = [string.casefold().count(char) for char in set(string.casefold())]
#     repeaters = sum(1 for count in counts if count > 1)

#     return repeaters

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

1 take a list of ints arg
2 determine the integer value needed to make the sum equal to the next prime
    number greater than the current sum of the list
3 return that number

E

D
List of ints input
Int output
Range to check numbers for primacy

A
- use a helper that determines primacy
    - take an int arg
    - if arg < 2:
        return False
    - for num in range(2:arg**0.5 + 1):
        if arg % num == 0:
            return False
    return True

- list_sum = sum the list
- check_num = list_sum

- find the first prime number higher than the sum of the list
    - while not prime(check_num):
        - check_num += 1
    
- return (check_num - list_sum) # difference of prime and sum

FAILED: ran into problem where while loop never ended
looks like my `prime` function is correct, but somehow wasn't returning 
the correct value - all I changed was doing a print test, and somehow the loop
now ends, but something else seems to be wrong. Found it. I had incorrectly
assigned `check_num = list_sum`, when it must be `check_num = list_sum + 1`.
This is in case the sum of the list is a prime (we want the first prime that
is *greater than* the sum).
"""
# def prime(total):
#     if total < 2:
#         return False
    
#     for num in range(2, total):
#         if (total / num) % 1 == 0:
#             return False
        
#     return True

# def nearest_prime_sum(numbers):
#     list_sum = sum(numbers)
#     check_num = list_sum + 1

#     while not prime(check_num):
#         check_num += 1

#     return (check_num - list_sum)

# print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
# print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
# print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
# print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# # Nearest prime to 163 is 167
# print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

"""
18
P
Create a function that takes a list of integers as an argument. Determine and 
return the index N for which all numbers with an index less than N sum to the 
same value as the numbers with an index greater than N. If there is no index 
that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the 
smallest value.

The sum of the numbers to the left of index 0 is 0. 
Likewise, the sum of the numbers to the right of the last element is 0.

1 take a list of ints arg
2 determine the index at which the sum of elements below that index and the 
    sum of those above that index are equal
3 return that index, or reutrn -1 if no such index
4 if multiple indices satify the requirement, return the smallest one

E
1 the element at the index should not be part of either the left or right 
    (above/below) sums

D
List of int input
Int output
List of lists to store the list slices above and below for comparisson

A
- slices = []

- split the list at the first possible index (1), and save both slices to
    slices list
    - for idx in range(1: len(input) - 1):
        - slices = input[: idx], input[idx + 1:]
        - if sum(slices[0]) == sum(slices[1]):
            return idx

    - return -1

- compare sums of slices for equality

- if equal, return index

- if not, move to next index and repeat
- if none equal, return -1

SOLVED: about 14 minutes, got pretty much right there, 
    could maybe go a little faster, but good
"""

# def equal_sum_index(input):
#     for idx in range(len(input)):
#         slices = [input[: idx], input[idx + 1:]]
#         if sum(slices[0]) == sum(slices[1]):
#             return idx
    
#     return -1

# print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
# print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
# print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
# print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# # The following test case could return 0 or 3. Since we're
# # supposed to return the smallest correct index, the correct
# # return value is 0.
# print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

"""
19
P
Create a function that takes a list of integers as an argument and returns 
the integer that appears an odd number of times. There will always be exactly 
one such integer in the input list.

1 take a list of ints
2 return THE integer that appears an odd number of times
3 there will always be exactly one such int

E

D
List input
Int output

A
- for each element in the list, check if it appears an odd number of times
    use % 2 == 1

- return element

SOLVED: just over 4 mins. Super easy one.
Problem type: Search (sorta)
"""

# def odd_fellow(integers):
#     for element in integers:
#         if integers.count(element) % 2 == 1:
#             return element

# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)

"""
20
P
Create a function that takes a list of numbers, all of which are the 
same except one. Find and return the number in the list that differs 
from all the rest.

The list will always contain at least 3 numbers, and there will always 
be exactly one number that is different.

1 take a list of ints arg
2 find the int that is not identical to the rest
3 return that int
4 list always has 3+ elements, exactly 1 will be different from the rest

E
NOT ALL INTS, can be floats

D
List input
Number output

A
- for each element in the list, count the instances of that value
- if count is == 1, return that value

SOLVED: Under 5 mins, super easy
"""
# def what_is_different(numbers):
#     for num in numbers:
#         if numbers.count(num) == 1:
#             return num

# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)