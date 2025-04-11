# # 1
# original = [1, 2, 3, 4, 5]

# def square(num):
#     return num * num

# squares = list(map(square, original))
# print(squares)

# # 2
# nums = [1, 2, 3, 4, 5, 6,]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# # 3
from functools import reduce

# nums = [1, 2, 3, 4, 5, 6, 7,]
# product = reduce(lambda num1, num2: num1 * num2, nums)
# print(product)

# # 4
# strings = ['q', 'we', 'rty', 'uiop', 'asdfg', 'hjkl;']
# lengths = list(map(len, strings))
# print(lengths)

# # 5
# no_nones = list(filter(lambda x: x is not None, [1, 2, None, True, 'Trump is a scammer']))
# print(no_nones)

# # 6
# strings = ['q', 'we', 'rty', 'uiop', 'asdfg', 'hjkl;']
# concat = reduce(lambda x, y: x + y, strings)
# print(concat)

# # 7
# list_of_lists = [
#     [1, 2, 3,],
#     ['aardvark',],
#     [True, False, None,],
#     [.0001, .00001, .000001,],
# ]

# flattened = list(obj for sublist in list_of_lists for obj in sublist)
# print(flattened)

# # 8
# string = "Tom the Human"
# backwards = (char for char in string[::-1])
# for char in backwards:
#     print(char)

# # 9
# def one_to_five():
#     for num in range(1, 6):
#         yield num

# for number in one_to_five():
#     print(number)

# # 10
# def user_str():
#     string = ''
#     while string != 'stop':
#         string = input('Type something: ')
#         yield string

# for user_string in user_str():
#     print(user_string)