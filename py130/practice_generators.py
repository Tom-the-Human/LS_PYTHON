# 1
# numbers = (1/num for num in range(1, 11))
# for number in numbers:
#     print(number)

# 2
# def recip(n):
#     num = 1
#     while num <= n:
#         yield 1 / num
#         num += 1

# for val in recip(7):
#     print(val)

# 3
# strings = ['a', 'cloud', 'never', 'dies']
# capitalized = (string.capitalize() for string in strings)
# print(tuple(capitalized))

# 4
# def caps(strings_list):
#     for string in strings_list:
#         yield string.capitalize()

# print(tuple(caps(['a',
#              'beep',
#                'clothing',
#                  'dog-eared',
#                    'Each one teach one.',
#                      'FOR THE BENEFIT OF ALL BEINGS'])))

# 5
# words = ["it's", 
#          'not', 
#          'clear', 
#          'from', 
#          'this problem', 
#          'description',
#          'if the list or the string',
#          'must have a length of at least 5',]
# capit = (word.capitalize() for word in words if len(word) >= 5)
# print(set(capit))

# 6
def cap_if_less_than_5(list_of_strings):
    for string in list_of_strings:
        if len(string) < 5:
            yield string.capitalize()

items = ['this', 'is', 'a list of', 'strings',]

print(set(cap_if_less_than_5(items)))