#  In this example, we want to select the key-value pairs where the value is 'Fruit'.
# P - given a dictionary, "select" the items with the value 'Fruit'. 
# E - only 1 test given, expected output a dictionary of apple and pear. 
#       Could come up with more, but doesn't seem necessary for the exercise.
# D - dictionaries in and out are required. Don't think any others are applicable.
# A - Initialize an empty dictionary. 
#       Use a for loop to check the input dictionary for matching values. 
#       Add items with matching values to the new dictionary.
#       Return the new dictionary.
# C

def select_fruit(input_dict):
    fruits = {}
    for key, value in input_dict.items():
        if value == 'Fruit':
            fruits[key] = value

    return fruits


produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }touch