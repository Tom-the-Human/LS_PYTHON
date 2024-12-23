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
"""

def to_weird_case(string):
    words = string.split()

    for i in range(2, len(words), 3):
        chars = list(words[i])
        for j in range(1, len(chars), 2):
            chars[j] = chars[j].upper()
        words[i] = ''.join(chars)
        
    print(words)
    return ' '.join(words)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)