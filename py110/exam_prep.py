"""
1. Explain the output of the following code:
"""
# python

# def multiply_by(factor):
#     return lambda x: x * factor

# double = multiply_by(2)
# triple = multiply_by(3)

# numbers = [1, 2, 3, 4, 5]
# print(list(map(double, numbers)))
# print(list(map(triple, numbers)))

"""
This likely is more complex than what I'd actually encounter on the exam,
but I will do my best with it.

The `multiply_by` function takes an int argument ... not important here,
  I've only been asked to explain output. Since I don't know what the `map`
  function does, this would be pretty hard to predict. Taking a guess,
  printing a list of a map of `double` and `numbers` is going to print a list
  of twice the values of the elements in `number`, so `[2, 4, 6, 8, 10], and
  with `triple` and `numbers`, an output of thrice the value, 
  i.e. `[3, 6, 9, 12, 15]`

  This is correct.

Now to explain this output, given that I don't know the `map` function, I
will still try. Line 13 calls `map` with the arguments `double` (which in turn 
calls `multiply_by`, which countains a lambda that multiplies variable `x`
by the `factor` parameter (2 in this case)) and `numbers`. Not understanding 
how `map` works, I can only surmise that the elements of numbers are being
"mapped" to `x` in `multiply_by`, resulting in a list of the elements in
`numbers` multiplied by 2, the argument used by `double`. Similarly on line
14, `triple` is used with `map` and `numbers` to perform the same action, only
multiplying by 3, since that is the argument passed by `triple`.  
"""

"""
2. What will be the result of the following list comprehension? Explain why.

['BANANA', 'CHERRY']

This comprehension creates a new list with all uppercase copies of only the
words from the list `words` than have a length of greater than 5. Since 
'apple' and 'date' do not have greater than 5 characters, they are not
included in the new list.
"""
# python

# words = ['apple', 'banana', 'cherry', 'date']
# result = [word.upper() for word in words if len(word) > 5]
# print(result)

"""
3. Describe the difference between sorted() and list.sort(). 
When would you use one over the other?

`sorted` is non-mutating and returns a sorted copy of the list argument.
Shallow or deep, I don't know ... shallow. So be wary that nested structures 
will be shared between the original and sorted copy.

`list.sort` is mutating and returns `None`. It sorts the list that it is
called on. 

Choosing one or the other will depend on a) whether mutation is desired or not
and b) the desired return value/ how it's being used in the code. For example,
sorted must be used if a sorted copy is desired, and list.sort must be used
if mutating the original list is necessary. 
"""

"""
4. Given the following dictionary, write a single line of code that creates 
a new dictionary with the same keys, but where each value is the length of 
the original value:
"""
# python

# fruit_colors = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'date': 'brown'}

# fruit_length = {key: len(value) for key, value in fruit_colors.items()}

# print(fruit_length)

"""
5. Explain what the following code does and what its output will be:

The first line initializes the `numbers` variable, which is assigned a list
of ints, 1 through 5 inclusive.
The next line initializes `squared`, which is assigned a function call to 
`map` utilizing a lambda squaring each element from the `numbers` list.
Again, I am unfamiliar with `map` but I belive that this will result in a 
list of the squared numbers, so [1, 4, 9, 16, 25]. (Actually, it results in
a map object, which doesn't seem to be directly printable without coercion).
The next line initializes `evens`, which is assigned a function call to
`filter` (which I am also not very familiar with - results in filter view 
object that is not directly printable without coercion), 
using a lambda to check for even-ness (divisibility by 2 with no remainder), 
and the `squared` variable. This should result in filtering out 
all the odd numbers from the collection.
Finally, the last line prints a list of `evens`, which is `[4, 16]`.

"""
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# evens = filter(lambda x: x % 2 == 0, squared)
# print(list(evens))
"""
6. What will be the output of the following code? Explain why.

The first and second lines initilize `tuple1` and `tuple2`, which are assigned
`(1, 2, 3)` and `(4, 5, 6)` respectively.
The third line initilizes `combined` which assigned `[*tuple1, *tuple2]`,
where the `*` operator performs tuple unpacking, resulting in the list:
`[1, 2, 3, 4, 5, 6]`
This list is printed on the final line.
"""
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined = [*tuple1, *tuple2]
# print(combined)


"""
USE LAMBDAS TO SOLVE THE FOLLOWING 5 PROBLEMS
1. Given a list of integers, create a new list containing the squares of
 even numbers only.
"""
num_list = [1, 2, 3, 4, 5, 6, 7]

print([(lambda num: num**2)(num) for num in num_list if num % 2 == 0])


"""
2. From a list of strings, create a new list containing only the strings that
 start with a vowel, converted to uppercase.
"""
str_list = ['a', 'boot', 'can', 'destroy', 'even', 'fifty', 'guys']

print([string.capitalize() for string in str_list 
       if string[0].lower() in 'aeiou'])

"""
3. Given two lists of equal length, create a list of tuples where each tuple
 contains the product of the corresponding elements from both lists.
"""
list1 = [0, 9, 8, 7, 6]
list2 = [1, 2, 3, 4, 5]

"""
4. From a list of dictionaries containing 'name' and 'age' keys, create a new
 list of names for people who are older than 18.
"""
family = [
    {"name": "Tom", "age": 41},
    {"name": "Amy", "age": 36},
    {"name": "Margot", "age": 12},
    {"name": "Teet", "age": 9},
    {"name": "Felix", "age": 0}
]

"""
5. Given a list of words, create a new list containing the length of each
 word, but only if the word has an odd number of characters.
"""
words = [
    'mana', 'health', 'strength', 
    'armor', 'dexterity', 'willpower', 
    'gold', 'level', 'inventory'
]