import re

# def p(regex, text):
#     print(re.findall(regex,
#                      text,
#                      flags=re.IGNORECASE))


# text = ("One fish,\nTwo fish,\nRed fish,\nBlue fish.\n123 456 7890")
# text2 = 'John Silver\nRandy Johnson\nDuke Pettijohn\nJoe_Johnson'

# p(r'\b\w\w\w\b', text) # ['cat']
# p(r'\Bjohn', text2) # ['cht']

# def reg(text, regex):
#     print(re.findall(regex, text, flags=re.MULTILINE))

# strings = [
#     'A grey cat',
#     'A blue caterpillar',
#     'The lazy dog',
#     'The white cat',
#     'A loud dog',
#     '--A loud dog',
#     'Go away dog',
#     'The ugly rat',
#     'The lazy, loud dog'
#     ]

# for s in strings:
#     reg(s, r'l+')

# dates = (
#     '20170111\n' +
#     '2017-01-11\n' +
#     '2017-0111\n' +
#     '201701-11\n' +
#     '2017/01/11'
# )

# reg(dates, r'\b\d\d\d\d-?/?\d\d-?/?\d\d\b')

# text = 'Felix is my firstborn son.'

# vowelless = re.sub(r'[aeiou]', '*', text,)
# print(vowelless)

# def is_url(text):
#     print(bool(re.search(r'^https?://.*\.com$', text)))

# is_url('https://launchschool.com')    # -> true
# is_url('http://example.com')          # -> true
# is_url('https://example.com hello')   # -> false
# is_url('   https://example.com')      # -> false

# def fields(text):
#     print(re.split(r'[ \s,]+', text))

# fields("Pete,201,Student");    # ['Pete', '201', 'Student']
# fields("Pete \t 201   ,  TA"); # ['Pete', '201', 'TA']
# fields("Pete \t 201");         # ['Pete', '201']
# fields("Pete \n 201");         # ['Pete', '\n', '201']

