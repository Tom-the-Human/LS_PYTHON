"""
1
Not sure if I should PEDAC these or not since instead of writing code, these
exercises are about fixing code. I'll start without PEDAC and see how it goes.

Our countdown to launch isn't behaving as expected. Why? Change the code so 
that our program successfully counts down from 10 to 1 before launching.

- Variable shadowing problem. `counter` global not accessible inside function.
- Several ways this can be solved. 
    - Easiest but maybe not a good option is to use `global` keyword.
    - Could move everything into the function, but then it's not a "decrease"
        so much as it is just "print_countdown" function.
    - Could eliminate the function and just use `counter -= 1` in the loop.
        I like that best of options so far.
    - 

Oh shit. Wait. There is a problem with the return value. So there are really
two different issues here. `decrease` is just returning the result of
`counter - 1`, not actually decrementing it. 
    - This isn't easily fixed by changing the function, since there is also a
        shadowing issue. 

Yeah, maybe not the expected answer, but this whole mess is easily fixed by
eliminating the function and just decrementing inside the loop. 

Ah, yes of course. The LS solution is to use `counter = decrease(counter)`.
That's quite simple and preserves the function.
"""

# def decrease(counter):
#     return counter - 1

# counter = 10

# for _ in range(10):
#     print(counter)
# #    decrease(counter)
# #    counter -= 1
#     counter = decrease(counter)

# print('LAUNCH!')

"""
2
You have a function that is supposed to reverse a string passed as an 
argument. However, it's not producing the expected output. 
Explain the bug, and provide a solution.

Without any debugging steps, it appears that this code is reassigning `string`
for each character so that on the first iteration "hello" becomes "hhello", on
the second iteration becomes "ehhello", then "lehhello" etc. ending up with 
`string` assigned to "ollehhello".
With a print test, that is proven true.

There are multiple ways to fix this. The simplest may be to initialize a new
string, then assign the characters to it a la `new_string = char + new_string`.
"""

# def reverse_string(string):
#     new_string = ''

#     for char in string:
#         new_string = char + new_string

#     return new_string

# print(reverse_string("hello") == "olleh")

"""
3
You want to multiply all elements of a list by 2. 
However, the function is not returning the expected result. 
Explain the bug, and provide a solution.

It loks like what's happening here is that the list values are not being
updated because ints are immutable. So all we're doing is reassigning the item
variable to a different int, which has no effect on the value stored in the
list. 

One way to fix this is to use `enumerate` and do something like:
`for idx, item in enumerate(lst):
    lst[idx] = item * 2`

This works fine, but LS solution shows how a comprehension is very simple and 
efficient: `return [item * 2 for item in lst]
"""
# def multiply_list(lst):
#     for idx, item in enumerate(lst):
#         lst[idx] = item * 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

"""
4
You have a function that should check whether a key exists in a dictionary 
and returns its value. However, it's raising an error. 
Why is that? How would you fix this code?

At first glace, this seems like it does the same thing as the `get` method.
But it's not working, raising a KeyError instead of returning `None`.

This could be resolved with use of try-except. 

LS solution utilizes the `get` method. I wouldn't have thought of that being
in the spirit of what we're doing here, since it appears to me that this
`get_key_value` is itself a rewrite of `get`. Anyway, it does the same thing,
so why wrap it in another function call?
"""

# def get_key_value(my_dict, key):
#     try:
#         if my_dict[key]:
#             return my_dict[key]
#     except:
#         return None

# print(get_key_value({"a": 1}, "b"))

"""
5
We have a list of events and want to check whether a specific date is
available (i.e., no events planned for that date). 
However, the function always returns the wrong value.

Ok, if I understand right, this is a dict (not a list) of scheduled events.
So if a date is in the dict, it is NOT available for a new event.
If this is the case, the boolean return values just need to be swapped.
The tests seem to bear this out, which is handy since I feel the problem
description is not well written.

Can be easily fixed by using `not in` instead of `in`, or by swapping the
return values. 
"""
events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

# def is_date_available(date):
#     if date not in events:
#         return True

#     return False

# print(is_date_available("2023-08-14"))  # should return False
# print(is_date_available("2023-08-16"))  # should return True

"""
6
We want to create a function that appends a given value to a list. 
However, the function seems to be behaving unexpectedly:

Ok, a simple print(lst) statement shows that the same list is carried over
between function calls. The first call initializes `lst = []` since no list is
passed in. I'm actually a bit unclear why the second call doesn't clear `lst`
since, with no list passed in, it should set `lst` to `[]`. 

Got clarification. `lst` is being created when the function is DEFINED, not
when it is called. So the second call has no effect on `lst` until we update
it within the function body.

LSBot recommends using `None` as the default argument instead of `[]`, then
assigning `lst = None` inside the function if `lst is None`.

Alternatively, we could remove the 2nd arg altogether and just create `lst`
inside the function. That does elminate the option to pass a list in though,
so the other option is probably preferable.
"""

# def append_to_list(value, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(value)
    
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])

"""
7
We defined a function intending to multiply the sum of numbers by a factor. 
However, the function raises an error. Why? How would you fix this code?

Right off the bat, I see that this function name shadows the built-in `sum` 
function, which is probably the issue here. `return factor * sum(numbers)`
becomes a recursive function call, which probably leads to a stack overflow.

Ah, right. so the error we're getting is TypeError because this `sum` function
requires 2 arguments, and we're trying (and failing) to call the built-in 
`sum` that requires only 1 argument.

The simplest fix here is also the best. Rename our function.
"""

# def product(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(product(numbers, 2) == 20)

"""
8
We have a list of lists and want to duplicate it. After making the copy, 
we modify the original list, but the copied list also seems to be affected:

This seems easy. We just need to use `copy.deepcopy` instead of `copy.copy`.
"""
# import copy

# original = [[1], [2], [3]]
# copied = copy.deepcopy(original)

# original[0][0] = 99

# print(copied[0] == [1])

"""
9
We want to remove certain items from a set while iterating over it, but the 
code below throws an error. Why is that and how can we fix it?

Mutating an iterable during iteration seems to be a sure recipe for trouble.
The code below would raise IndexError. NOPE, that's a RuntimeError. Not
familiar with RuntimeError, will need to learn more.

Regardless, it can be avoided by initializing a new set, copying only the
desired elements to the new set, and then either
- use the new set if we don't want to mutate the original, or
- compare sets and remove elements not copied to the new set from the old set,
    which does mutate the original set, so better if that is desired
- OR maybe we can just use copy to avoid this problem

Oh, duh. LS solution is a comprehension, which easily solves it.
`data_set = {item for item in data_set if item % 2 != 0}`
"""
# import copy

# data_set = {1, 2, 3, 4, 5}

# for item in copy.deepcopy(data_set):
#     if item % 2 == 0:
#         data_set.remove(item)

# print(data_set)

"""
10
A developer is trying to remove duplicates from a list. They use a set for 
deduplication, but the order of elements is lost. 
How can we preserve the order?

This might be a good one to PEDAC.

Can't use a comprehension, since that only checks membership once, not at each
element. 

- Could be done with a loop, but that seems verbose.
- I see that `data[2:6]` is an exact list of the unique elements in order, but
    that doesn't work for lists that can't be sliced to get the right result.
- 

LS solution uses a for loop with a set `seen` to contain numbers already in
`unique_data`. Their solution is better, since mine needlessly mutates `data`.
"""
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []

while data:
    if data[0] not in unique_data:
        unique_data.append(data.pop(0))
    else:
        data.pop(0)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed