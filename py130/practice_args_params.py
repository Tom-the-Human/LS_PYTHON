# 1
def combine(arg1, arg2, arg3):
    return (arg1, arg2, arg3)

print(combine("fart", 5, [1, 2, 3,]))

# 2
def multiply(num1, num2, /,):
    return num1 * num2

print(multiply(14, 123))

# 3
def describe_pet(animal_type, /, name=''):
    print(f'{name} is a {animal_type}.')

describe_pet('cat', 'Honey')

# 4
def calculate_average(*nums):
    if not nums:
        return None
    
    return sum(nums) / len(nums)

print(calculate_average(5, 10, 15))

# 5
def find_person(**kwargs):
    if 'Antonina' in kwargs:
        print(f"Antonina's profession is {kwargs['Antonina']}")
    else:
        print('Antonina not found')

find_person(Tom='AppSec', Amy='housewife', Antonina='Launch School TA')

# 6
def concat_strings(*strings, sep=' '):
    return sep.join(strings)

print(concat_strings('V', 'A', 'P', 'O', 'R', 'W', 'A', 'V', 'E', sep='.'))

# 7
def register(username, /, password, *, age):
    print(f'username: {username}\npassword: {password}\nage: {age}')

register('Tom_the_Human', 123456, age=41)

# 8
def print_message(*, message, level='INFO'):
    print(f'{level}. {message}!')

print_message(level="Do not touch Willie", message="Good advice")


def pack_tools(*tools):
		print(tools)

some_tools = ['saw', 'hammer', 'drill', 'shovel']
a, b, c, d = some_tools # basic unpacking without *
a, b, *c = some_tools # unpacking with *, so that c = ['drill', 'shovel']
# * is used here to pack/collect remaining elements
tools2 = ('shears', 'knife', 'trimmers')

pack_tools(a, b, *c, *tools2) # also unpacking 
# (need * to pass elements individually)
# also shows that multiple starred parameters will work