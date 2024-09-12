import random
from datetime import datetime

def is_odd(int1):
    if int1 % 2:
        return True
    return False
# print(is_odd(-5))

def print_odds_1_to_99():
    for i in range(1, 100, 2):
        print(i, '\n') # newline not needed, each iteration is a new line anyway


def print_evens_1_to_99():
    for i in range(2, 100, 2):
        print(i)
# print_evens_1_to_99()

def find_and_print_room_area():
    length_meters = float(input('Enter room lentgh in meters: '))
    width_meters = float(input('Enter room width in meters: '))

    def get_area(length, width):
        area = length * width
        return area

    print(get_area(length_meters, width_meters))
    print(10.7639 * get_area(length_meters, width_meters)) # in square feet
# find_and_print_room_area()

def tip_calc():
    bill = (float(input('What is the bill amount?: ')))
    percent = (float(input('What percentage would you like to tip?: ')))
    tip = bill * (percent / 100)
    print(f'The tip is ${tip:.2f}')
    print(f'The total is ${tip + bill:.2f}')
# tip_calc()

def sum_or_product():

    def sum(number):
        sum1 = 0
        for i in range(1, number + 1):
            sum1 += i
        print(sum1)
    
    def product(number):
        prod1 = 1
        for i in range(1, number + 1):
            prod1 *= i
        print(prod1)

    num1 = int(input('Please enter an integer greater than 0: '))
    operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

    while operation not in ['s', 'p']:
        operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

    if operation == 's':
        sum(num1)
    elif operation == 'p':
        product(num1)
# sum_or_product()

def short_long_short(str1, str2):
    len_dif = len(str1) - len(str2)
    if len_dif > 0:
        print(str2 + str1 + str2)
    else:
        print(str1 + str2 + str1)
# short_long_short('Ned', 'Homer')

def is_leap_year(year):
    if year > 1751:
        if year % 400 == 0:
            return True
        if year % 4 == 0:
            if year % 100 == 0:
                return False
            return True
    if year < 1752 and year % 4 == 0:
        return True
    return False
# print(is_leap_year(1020))

def multisum(num):
    sum_set = {0,}

    for i in range(0, num + 1, 3):
        sum_set.add(i)
    for i in range(0, num + 1, 5):
        sum_set.add(i)

    return sum(sum_set)

# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)
    
def utf16_value(string_arg):
    value = 0
    for char in (string_arg):
        value += ord(char)

    return value

# print(utf16_value('Four score') == 984)
OMEGA = "\u03A9"
# print(utf16_value(OMEGA) == 937)

def greetings(list_, dict_):
    name = ' '.join(list_)
    title = dict_['title']
    job = dict_['occupation']

    return f'Hello, {name}! Nice to have a {title} {job} around.'

greeting = greetings(
    ["Tom", "W", "Hodges"],
    {"title": "Master", "occupation": "Housekeeper"},
)
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

def who_are_you():
    name = input('What is your name? ')

    if name[-1] == '!':
        return f'HELLO {name.upper()} WHY ARE WE YELLING?'
    
    return f'Hello {name}.'

# print(who_are_you())

def multiply(num1, num2):
    return num1 * num2

def square(num_):
    return multiply(num_, num_)

def float_math():
    num1 = float(input('First float: '))
    num2 = float(input('Second float: '))

    print(f"{num1} + {num2} = "
      f"{num1 + num2}")
    print(f"{num1} - {num2} = "
      f"{num1 - num2}")
    print(f"{num1} * {num2} = "
      f"{num1 * num2}")
    print(f"{num1} / {num2} = "
      f"{num1 / num2}")
    print(f"{num1} // {num2} = "
      f"{num1 // num2}")
    print(f"{num1} % {num2} = "
      f"{num1 % num2}")
    print(f"{num1} ** {num2} = "
      f"{num1 ** num2}")
# float_math()

def penultimate(string_):
    words = string_.split(' ')

    return words[-2]

# print(penultimate('Ultimate pens are best!'))

def xor(val1, val2):
    if (val1 and not val2) or (val2 and not val1):
        return True
    return False

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

def oddities(list_in):
    list_out = []
    for element in range(len(list_in)):
        if element % 2 == 0:
            list_out.append(list_in[element])
    return list_out

def getting_even(list_in):
    return list_in[1::2]
    
# print(getting_even([2, 3, 4, 5, 6]) == [3, 5])     # True
# print(getting_even([1, 2, 3, 4]) == [2, 4])        # True
# print(getting_even(["abc", "def"]) == ['def'])     # True
# print(getting_even([123]) == [])                   # True
# print(getting_even([]) == [])                      # True

#your_name = input("What's your name? ") or "Teddy"
#print(f"{your_name} is {random.randint(20, 100)} years old.")

retirement_calc = {'current age': 0, 
                   'retirement age': 0, 
                   'current year': 0,
                   'retirement year': 0,
                   'work years': 0}

def get_current_age():
    retirement_calc['current age'] = int(input('What is your age? '))

def get_retirement_age():
    retirement_calc['retirement age'] = int(input('What age would you like to retire? '))

def set_current_year():
    retirement_calc['current year'] = datetime.now().year

def calc_retirement_year_and_work_left():
    retirement_calc['work years'] = retirement_calc['retirement age'] - retirement_calc['current age']
    retirement_calc['retirement year'] = retirement_calc['current year'] + retirement_calc['work years']

# get_current_age()
# get_retirement_age()
# set_current_year()
# calc_retirement_year_and_work_left()
# print(f"It's {retirement_calc['current year']}. You will retire in {retirement_calc['retirement year']}.")
# print(f"You have only {retirement_calc['work years']} years of work to go!")

def center_of(string_):
    if len(string_) % 2 == 1:
        mid = string_[len(string_) // 2]
    else:
        mid = string_[len(string_) // 2 - 1: len(string_) // 2 + 1]
    return mid

# -----

def negative(num):
    if num > 0:
        num = -num
    
    return num

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True