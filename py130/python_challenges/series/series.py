"""
Write a program that will take a string of digits and return all the possible 
consecutive number series of a specified length in that string.

For example, the string "01234" has the following 3-digit series:
012
123
234

Likewise, here are the 4-digit series:
0123
1234

Finally, if you ask for a 6-digit series from a 5-digit string, 
you should throw an error.

P
Input: string of digits to constructor, int to `slices`
Output: list of lists of digits
Explicit:
1 take a string of digits, take an int
2 return all possible consecutive digit series' of the length specified by the int
3 if the int is greater than the length of the string, raise a ValueError
Implicit:
1 output must be formatted as nested lists, with each 2nd level list being the length 
    specified by the int and containing a series of individual digits (as ints, 
    not strings) that appear in the same order they appeared in the string.
    There must be a 2nd level list for each possible series of the correct length
2 requires a `Series` class, a constructor that stores a string, 
    and a `slices` instance method

E
This makes sense. Only question really is how to most efficiently solve the problem.
Looks like it can be done a variety of ways.
I don't think I need to work any examples for this.

C
check

H
have the constructor store the string as state
`series` needs to return a nested list with the 
    2nd level lists formatted as described in the rules
to acheive this, we can use a for loop with slicing, 
    along with list coercion and int coercion
    it may be worthwhile to sub list construction to a helper function, 
        but not necessarily

D
string input
int input
nested lists of ints output

A
have the constructor store the string as state

`slices` needs to return a nested list with the 
    2nd level lists formatted as described in the rules

to acheive this, we can use a for loop with slicing, 
    along with list coercion and int coercion
    it may be worthwhile to sub list construction to a helper function, 
        but not necessarily

    something like:
    output = []
    for idx in range(len(string)):
        if (idx + length_input) < len(string):
            output.append(list(int(char) for char in string[idx: idx + length_input]))

C
"""
class Series:
    def __init__(self, digital_string):
        self.digital_string = digital_string

    def slices(self, spec_len):
        length = len(self.digital_string)
        if length < spec_len:
            raise ValueError (
                "The specified length cannot be greater than the string length."
                )

        output = []
        for idx in range(length):
            if idx + spec_len <= length:
                output.append(
                    list(
                        int(char) for char in self.digital_string[idx: idx + spec_len]
                        )
                )
        
        return output
    
# series = Series("01234")
# print(series.slices(9))