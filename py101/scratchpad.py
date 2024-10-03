# Write two functions that transform a list of lists containing numbers.
# Both functions should return a list where the nested lists only contain
# even numbers.

# The first function should mutate the list passed as an argument but not the sublists.
# The second function should not mutate the list passed as an argument or the sublists.
import copy

def destructive_even_numbers(num_list):
    for idx, sublist in enumerate(num_list):
        new_sublist = copy.copy(sublist)
        removal = []
        for i, value in enumerate(sublist):
            if value % 2 != 0:
                removal.append(i)
        for i, value in enumerate(reversed(removal)):
            new_sublist.pop(value)
        num_list[idx] = new_sublist


def nondestructive_even_numbers(num_list):
    evens = []
    for sublist in num_list:
        new_sublist = []
        for i, value in enumerate(sublist):
            if value % 2 == 0:
                new_sublist.append(value)
        evens.append(new_sublist)
        
    return evens

numbers1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(id(numbers1))
print(id(numbers1[0]))
destructive_even_numbers(numbers1)
print(numbers1)  # Output: [[2], [4, 6], [8]]
print(id(numbers1))
print(id(numbers1[0]))

numbers2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(id(numbers2))
print(nondestructive_even_numbers(numbers2)) # Output: [[2], [4, 6], [8]]
print(numbers2)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(id(numbers2))

## Bonus Questions ##
# 1. Write some code to prove that your functions have the intended behavior.
#   > I have added print(id()) statements to compare the objects before and after
#   > being passed to the functions. The ids confirm the intended behavior.

# 2. What did you choose as the return value of your mutating function? Why?
#    Can you think of some built-in Python methods that have similar behavior?
#   > I chose to return `None` because the function mutates the list in place. 
#   > Yes, other mutating methods, such as list.append() and list.reverse()
#   > return `None` to conform to the convention that functions should not 
#   > both mutate objects and have a meaningful return value. 

# 3. What are some reasons to choose one function over the other?
#   > All else being equal, it is better to NOT destructively mutate objects.
#   > Since all else is rarely equal, there may be situations in which mutation
#   > is preferable, but generally I'd opt for the non-destructive option. 