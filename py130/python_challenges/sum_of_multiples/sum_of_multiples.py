"""
Write a program that, given a natural number and a set of one or more other 
numbers, can find the sum of all the multiples of the numbers in the set that 
are less than the first number. If the set of numbers is not given, use a 
default set of 3 and 5.

For instance, if we list all the natural numbers up to, but not including, 
20 that are multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18. 
The sum of these multiples is 78.

P
Input: natural number (positive int?) and a set of other numbers
Output: int (sum of all multiples of numbers in set that are less than first number)
Explicit:
1 Follow the rules clearly stated above including
2 use the default set {3, 5} if none is provided
Implicit:
1 creat `SumOfMultiple` class, `sum_up_to` method and `to` method
2 include underscore spacers for output larger than 999
    (or not? seems optional since 1 test shows output without _)
3 Looks like `to` uses the custom input set and `sum_up_to` uses the default set
4 SumOfMultiples requires a constructor that optionally takes an unlimited
    number of int arguments that should be coerced to a set for use
5 count each unique multiple ONCE even if it is a multiple of more than one of 
    the numbers in the input set.

E
Let's work a couple of the smaller test cases to see if I understand:
self.assertEqual(3, SumOfMultiples.sum_up_to(4))
Ok, so `sum_up_to` seems to be using the default set of 3 and 5.
Of course the only multiple of 3 or 5 that is less than 4 is 3 itself.

self.assertEqual(23, SumOfMultiples.sum_up_to(10))
Ok, the number is 10 and the default set is used, so:
mults_of_3 < 10 == 3, 6, 9
mults_of_5 < 10 == 5
3 + 6 + 9 + 5 == 23

self.assertEqual(30, SumOfMultiples(4, 6).to(15))
Ok, now we're using `to` and a custom set:
mults_of_4 < 15 == 4, 8, 12
mults_of_6 < 15 == 6, 12
4 + 8 + 12**2 + 6 == 42
Ah! wrong total, BUT 42 - 30 (expected total) is 12. So I hypothesize that
only UNIQUE multiples should be used. So the multiples should also be in a set.
This tracks, because the problem description shows an example were 15 is a 
multiple of both 3 and 5, and is only counted once.

Ok, I think I've got it.

C
Yep

H
create required class, constructor, and 2 additional methods
    one method can easily just call the other to avoid duplicate code
    since the methods do basically the same thing, only the expected input varies

constructor takes an optional unlimited number of ints and saves them to a set

methods take a "natural number" (math terminology that just means a positive int)
    `sum_up_to` for use without custom set, so doesn't need to be instance method
        can be static or class method
    `to` is called on an instance of the class, which has the custom set as state

when either method is called, it should return the total of the UNIQUE multiples of
    the set it uses which are individually lower than the number given as an argument

D
INPUT
set of ints
positive int
INTERMEDIARY
set of mults
OUTPUT
positive int

A
create required class, constructor, and 2 additional methods
    one method can easily just call the other to avoid duplicate code
    since the methods do basically the same thing, only the expected input varies

constructor takes an optional unlimited number of ints and saves them to a set

methods take a "natural number" (math terminology that just means a positive int)
    `sum_up_to` for use without custom set, so doesn't need to be instance method
        can be static or class method
    `to` is called on an instance of the class, which has the custom set as state

when either method is called, it should return the total of the UNIQUE multiples of
    the set it uses which are individually lower than the number given as an argument
    -   create an empty set
        for loop with nested while < number loop
        for each num in the set
            mult = num
            while mult < natural_num:
                add mult to set
                mult = mult + num

        return sum(set)

C
"""
class SumOfMultiples:
    def __init__(self, *multipliers):
        self.multipliers = set(multipliers) if multipliers else {3, 5}

    @staticmethod
    def sum_up_to(natural_number, multipliers={3, 5}):
        multiples = set()
        for num in multipliers:
            multiple = num
            while multiple < natural_number:
                multiples.add(multiple)
                multiple += num

        return sum(multiples)

    def to(self, natural_number):
        return SumOfMultiples.sum_up_to(natural_number, self.multipliers)
    
# This approach works but isn't very object oriented. LS solution uses a better pattern
"""
LS Solution:
Instance method (to) contains the core algorithm
Class method (sum_up_to) creates an instance with default values 
    and calls the instance method

In your solution, you've implemented:

Static method contains the core algorithm
Instance method calls the static method
"""

