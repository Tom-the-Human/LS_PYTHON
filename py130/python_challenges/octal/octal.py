"""
Implement octal to decimal conversion. Given an octal input string, your program should produce a decimal output. Treat invalid input as octal 0. Note that the only valid digits in an octal number are 0, 1, 2, 3, 4, 5, 6, and 7.

Note: Implement the conversion yourself. Don't use any built-in or library methods that perform the necessary conversions for you. In this exercise, the code necessary to perform the conversion is what we're looking for.

About Octal (Base-8)

Decimal is a base-10 system. A number 233 in base 10 notation can be understood as a linear combination of powers of 10:

The rightmost digit gets multiplied by 100 = 1
The next digit gets multiplied by 101 = 10
The digit after that gets multiplied by 102 = 100
The digit after that gets multiplied by 103 = 1000
...
The n_th_ digit gets multiplied by 10n-1.
All of these values are then summed.
Thus:

Copy Code
  233 # decimal
= 2*10^2 + 3*10^1 + 3*10^0
= 2*100  + 3*10   + 3*1
Octal numbers are similar, but they use a base-8 system. A number 233 in base 8 can be understood as a linear combination of powers of 8:

The rightmost digit gets multiplied by 80 = 1
The next digit gets multiplied by 81 = 8
The digit after that gets multiplied by 82 = 64
The digit after that gets multiplied by 83 = 512
...
The n_th_ digit gets multiplied by 8n-1.
All of these values are then summed.
Thus:

Copy Code
  233 # octal
= 2*8^2 + 3*8^1 + 3*8^0
= 2*64  + 3*8   + 3*1
= 128   + 24    + 3
= 155

P
Input: Octal object with string representation of octal int
Output: int (decimal value of input)
Explicit:
1 follow all rules above regarding octal numbers and conversion
2 no libraries, must write conversion code yourself
3 if any part input is not a valid octal digit, entire output is 0
Implicit:
1 requires an Octal class with a constructor and a `to_decimal` method
2 Just as with decimal integers, a leading 0 makes no difference and can be ignored

E
Need to confirm my understanding of octal to decimal conversion
OCTAL           |      DECIMAL
10 (8^1 + 0)    ==      8
17 (8^1 + 7*8^0)==      15      Why is 8^0 == 1??? Should've taken more math ...
130 (8^2 + 3*8^1 + 0)== 88 (64 + 24)
Ok, that'll do. I'm getting it. 
How to code this?

C
I get the problem, sure. Little idea how to solve it, but I can get there.

H
create class, constructor and `to_decimal`
constructor stores string as state
`to_decimal` converts string (representing an octal number) to decimal
    outsource input validation
        ensure all chars are valid octal digits, return original input if so
            for loop w/ "01234567"
        return 0 (or "0"?) if not
    reverse the string
    create a total and set to 0
    cycle through each digit and multiply int(digit)*8^index
    add that result to the total

D
string input
int output
maybe a list or dict, but probably not
could use class constant OCTAL_DIGITS = "01234567"

A
create class, constructor and `to_decimal`
constructor stores string as state
`to_decimal` converts string (representing an octal number) to decimal
    outsource input validation
        ensure all chars are valid octal digits, return original input if so
            for loop w/ "01234567"
        return 0 (or "0"?) if not

    reverse the string
        string slicing
    create a total and set to 0
    cycle through each digit and multiply int(digit)*8^index
        enumerated for loop
    add that result to the total
    
C
"""
class Octal:
    def __init__(self, octal_string):
        self.octal_string = octal_string

    def _return_valid_octal_string(self):
        # if not valid, return 0
        # else return original value of self.octal_string
        for digit in self.octal_string:
            if digit not in "01234567":
                return "0"
            
        return self.octal_string


    def to_decimal(self):
        # validate or set to "0" and reverse validated result for math
        octal = self._return_valid_octal_string()[::-1]
        
        decimal = 0
        for idx, digit in enumerate(octal):
            decimal += int(digit) * 8**idx

        return decimal



# oct130 = Octal("130")
# oct4000 = Octal("4000")
# oct999 = Octal("999")

# oct130.to_decimal()
# oct999.to_decimal()