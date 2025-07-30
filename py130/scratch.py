'''
Coding Exercise: Write a function read_and_tally that accepts a file path as 
an argument. The function should read the text from the file, count the 
frequency of each word (case-insensitively), and return a dictionary where 
keys are words and values are their counts. Your function should properly 
handle potential FileNotFoundError.
'''

# def read_and_tally(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#     except FileNotFoundError:
#         print("Please check the file path and try again.")
#         return {}

#     content = content.casefold()
#     word_list = content.split()
#     word_counts = {}

#     for word in word_list:
#         word_counts[word] = word_counts.get(word, 0) + 1

#     return word_counts

'''
Create a PFA with a closure and a PFA using `functools.partial`.
'''

# # with closure
# def multiply(x, y):
#     return x * y

# def mult_maker(factor1):
#     def mult(factor2):
#         return multiply(factor1, factor2)
    
#     return mult

# times10 = mult_maker(10)
# print(times10(5)) # 50


# # with partial
# from functools import partial

# def multiply(x, y):
#     return x * y

# times100 = partial(multiply, 100)
# print(times100(5)) # 500

'''
1. Flexible Data Processing with Lambdas
•   ​Difficulty​: Intermediate
•   ​Topics​: Complex parameter requirements, lambda functions, *args

Write a function process_data that accepts a variable number of positional 
numeric arguments. It must also accept two keyword-only arguments: 
operation and comparator.
•   The operation argument should be a callable (designed to accept a lambda function) 
    that performs a mathematical operation on each number (e.g., squaring it).
•   The comparator argument should also be a callable (designed to accept a lambda 
    function) that takes two arguments and returns a boolean. The function should use 
    this comparator to find the "best" value ​after​ the operation has been applied to 
    all numbers.
•   The function should return the original number (before the operation) that 
    corresponds to the "best" result.
'''
# BAD SOLUTION has bugs, do not reuse, needs a refactor
# def process_data(*args, operation, comparator):
#     nums = [operation(num) for num in args]

#     if len(nums) == 1:
#         return args[0]
    
#     if comparator(nums[0], nums[1]):
#         result = args[0]
#     else:
#         result = args[1]

#     if len(nums) > 2:
#         for i in range(2, len(nums)):
#             if comparator(nums[i], result):
#                 result = args[i]

#     return result


# # Example Usage:
# # Find the original number which is smallest after being squared
# print(process_data(2, 5, -3, 1, operation=lambda x: x**2, comparator=lambda a, b: a < b))
# # Expected output: 1

# # Find the original number which is largest after applying x + 5
# print(process_data(10, 20, 5, 15, operation=lambda x: x + 5, comparator=lambda a, b: a > b))
# # Expected output: 20

'''
2. Decorator for Function Call Auditing
•   ​Difficulty​: Advanced
•   ​Topics​: Complex decorator patterns, closures, file handling, *args, **kwargs

Create a decorator factory audit_log that takes a filename as an argument. 
The decorator it returns should log the details of any calls made to the decorated 
function. Each log entry in the specified file should record the function's name, 
the positional and keyword arguments it was called with, and its return value.
'''
# def audit_log(filename):
#     def wrapper_factory(og_func):
#         def wrapper(*args, **kwargs):
#             result = og_func(*args, **kwargs)
#             with open(filename, 'a') as file:
#                  file.write(f"Called {og_func.__name__} with args={args}, kwargs={kwargs} and returned {result}")
#             return result
#         return wrapper
#     return wrapper_factory

# @audit_log("audit.txt")
# def add(x, y):
#     return x + y

# @audit_log("audit.txt")
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# add(5, 3)
# greet("Alice")
# greet("Bob", greeting="Hi")

# # After running, the file "audit.txt" should contain something like:
# # Called `add` with args=(5, 3), kwargs={} and returned 8
# # Called `greet` with args=('Alice',), kwargs={} and returned 'Hello, Alice!'
# # Called `greet` with args=('Bob',), kwargs={'greeting': 'Hi'} and returned 'Hi, Bob!'

'''
3. Python Package Structure and Best Practices
•   ​Difficulty​: Intermediate
•   ​Topics​: Packaging concepts, module best practices (Conceptual)
You are tasked with creating a new Python package called textools. 
This package will contain two main functionalities: 
string manipulation and text analysis.

1.  Describe the complete directory structure for this package.
Include the project root, the package directory, a tests directory, 
and any essential files like __init__.py, setup.py (or pyproject.toml), 
and README.md.
2.  Where would you place modules for string manipulation (e.g., reversing.py) 
and text analysis (e.g., frequency.py)?
3.  Explain the role of the __init__.py file within the textools package directory. 
How can you use it to make functions from your modules directly accessible 
from the package level (e.g., import textools; textools.reverse_string(...))?

Directory Structure
textools_package/
    src/
        textools_Tom-the-Human/
            __init__.py
            textools.py
            reversing.py
            frequency.py
            (other modules here, if any)
    tests/
    LICENSE
    pyproject.toml
    README.md

This example package structure follows what is outlined in the lesson about
creating a package for PyPI. The __init__.py file is used to tell Python that
this directory contains a package. I understand that normally this file is empty,
so, I don't really know how to use it to make functions from modules directly
accessible. 

'''
#

