"""
Write a program to determine whether a triangle is 
equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has exactly two sides of the same length.

A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0, 
and the sum of the lengths of any two sides must be greater than the length 
of the third side.

P
Input: 3 integers, each representing a side length
Output: string representing type of triangle OR 
    raise ValueError if not a valid triangle
Explicit:
1 rules for triangles outlined clearly in problem statement
Implicit:
1 test cases provide a variety of example of invalid triangles 
    that should raise ValueError
2 these include, negative input, illegal size inequality (i.e. 1, 1, 3)
    and 0 length sides
3 worth noting, floats are acceptable lengths (i.e. 0.4, 0.6, 0.3)

E
tests show that we must use a Triangle class and the lengths will be used to
    instantiate a triangle object
the class includes a `kind` method that returns the string representing
    the kind of triangle
it appears that the ValueError should be thrown during Triangle instantiation
    so maybe the __init__ method needs to contain the error handling

C
so far so good

H
create a Triangle class
the __init__ method must include input validation
    if input is invalid, raise ValueError
include kind instance method
    return kind of triangle depending on relative lengths

is that it?

D
Triangle class
tuple of side lengths
string output

A
create a Triangle class
the __init__ method must include input validation
    if input is invalid, raise ValueError
        if (sum(a, b, c) - max(a, b, c)) <= max(a, b, c) == ValueError
        if any(a, b, c) <= 0 == ValueError

include kind instance method
    will be a valid triangle if ValueError not thrown, so assume validity
    return kind of triangle depending on relative lengths
        if all equal, return equilateral
        if 2 sides equal, return isosceles
        else return scalene

I think that's it. Let's code.
C
"""
class Triangle():
    def __init__(self, side1, side2, side3):
        self.side_tup = (side1, side2, side3)
        self.longest = max(self.side_tup)
        self.total = sum(self.side_tup)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if any(side <= 0 for side in self.side_tup) or \
        (self.total - self.longest) <= self.longest:
            raise ValueError
        

    @property
    def kind(self):
        if self.side1 == self.side2 and self.side1 == self.side3:
            return "equilateral"
        
        if self.side1 in (self.side2, self.side3) or \
        self.side2 in (self.side1, self.side3):
            return "isosceles"
        
        return "scalene"
        




# good_tri = Triangle(1, 2, 3)
# bad_tri = Triangle(-1, 2, 4)
# worse_tri = Triangle(1, 2, 1)
