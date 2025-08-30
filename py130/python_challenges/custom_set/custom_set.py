'''
Create a custom set type.

Sometimes it is necessary to define a custom data structure of some type. 
In some languages, including Python, there is a built-in Set or set type. 
For this problem, you're expected to implement your own custom set type: you 
may not use the built-in set type.

How this type works internally doesn't matter, as long as it behaves like a 
set of unique elements that can be manipulated in several well defined ways. 
Once you've reached a solution, feel free to play around with using the 
built-in implementation of set.

For simplicity, you may assume that all elements of a set must be numbers.

P
Input: custom set type
Output: implementation not important, but behave just as built-in set
Explicit:
1 just assume only numbers will be used as elements
2 internals don't matter as long as it acts like a set of unique elements
3 no use of built-in set
Implicit:
1 constructor accepts an optional iterable argument
2 a number of set methods are expected to be available, including
    intersection, difference, union, add, is_same, is_disjoint,
    is_subset, is_empty, contains
3 t??? 

E
The tests involve testing behavior mainly via a number of methods.
These methods cover most of the built-in set methods, though it looks like
    not `clear`, `issuperset`, `update`, or `remove` - may implement some
    or all of these anyway if they look to prove helpful.

One thing I don't see is any method to determine that data is unique before
adding it to the set. This should likely be handled in the add method itself.

Also left wondering if, as in the linked list problem, I'm doing something
other than using a built-in collection to collect elements. I'm not really
sure how to do that here. I can apparently use a list behind the scenes,
or at least I need to accept lists as arguments anyway. 

The bit about all elements being numbers might be a clue. Does numbers mean
ints, or are floats also allowed? All the tests show only small ints, the
types of values that Python caches - is this helpful?

H

D

A

C
'''
class CustomSet:
    def __init__(self, seed=tuple()):
        # call add for each element in the seed list
        self.data = []
        for num in seed:
            self.add(num)

    def add(self, number):
        # takes a single int or float
        # will be called a lot internally, but also available externally
        if number not in self.data:
            self.data.append(number)

    def contains(self, number):
        # number is in set
        return number in self.data

    def difference(self, other):
        # return elements in self not in other
        return CustomSet([n for n in self.data if n not in other.data])

    def intersection(self, other):
        # return set of common elements
        return CustomSet([n for n in self.data if n in other.data])

    def is_disjoint(self, other):
        # sets have no common elements
        return not any(n in other.data for n in self.data)

    def is_empty(self):
        # set contains no objects
        return not self.data

    def is_same(self, other):
        # both sets contain same objects
        return self.is_subset(other) and other.is_subset(self)

    def is_subset(self, other):
        # all elements in self are in other
        return all(n in other.data for n in self.data)

    def union(self, other):
        # return set of all elements from both sets
        return CustomSet(self.data + other.data)
    
    def __eq__(self, other):
        return self.is_same(other)