# 1
# P
# For each object shown below, demonstrate how you would access the letter g.
# Explicitly
# Access the value 'g' in each collection
# Implicitly
# I'll print it to be sure
# Use of indices and keys will be necessary

# E
# Only the collection inputs are provided, output should be the letter 'g'.
# I'll use print statements to ensure success.

# D
# Lists and dicts, lists of dicts, dicts of lists, lists of lists of lists ...

# A
# For each item, locate the necessary key or index needed at each level
#   of each nested collection. Use these in sequence to print the
#   element at the correct location.
# Number of steps is determined by level of nesting.

# C
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print(list(dict2['3rd'].keys())[0])


# 2
# P
# For each of these collection objects, demonstrate
#  how you would change the value 3 to 4.
# Explicitly
# Reassign each targeted value `3` in each collection to `4`.
# Implicitly
# Use a print statement to confirm correct reassignment.

# E
# As before, none given, only inputs provided. 
# Outputs will be correctly altered collections.

# D
# Same as before, combos of dicts and lists

# A
# 1 Use a reassignment statement with the correct indices and/or keys
#   to reassign the target.
# 2 Print the updated collection.
# 3 Repeat for each collection.

# C
lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2)

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2)


# 3
# Does not require coding.
# I mistakenly thought that `a` would be changed by changing lst[0],
#   but of course that's not the case. All changing lst[0] does is
#   reassign that index to a new value. However, reassigning `a`
#   would also change lst[0]. 


# 4
# P
# Given the object shown below, print the name, age, and gender of each family member:
# Explicitly
# 1 output should follow this pattern:
#   "{name} is a {age}-year-old {male or female}."
# 2 Print this output for each family member.
# Implicitly
# 1 ?

# E
# Expected output is as "Herman is a 32-year-old male." for each family member

# D
# Dicts, formatted strings to retrieve info from dicts

# A
# 1 create a for loop to iterate though the dict
# 2 for each person, print the f-string using nested dict keys where necessary

# C
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for person in munsters:
    print(f"{person} is a {munsters[person]['age']}-year-old {munsters[person]['gender']}.")
