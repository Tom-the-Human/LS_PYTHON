"""
The diamond exercise takes as its input a letter, and outputs it in a diamond shape. 
Given a letter, it prints a diamond starting with 'A', 
with the supplied letter at the widest point.

The first row contains one 'A'.
The last row contains one 'A'.
All rows, except the first and last, have exactly two identical letters.
The diamond is horizontally symmetric.
The diamond is vertically symmetric.
The diamond has a square shape (width equals height).
The letters form a diamond shape.
The top half has the letters in ascending order.
The bottom half has the letters in descending order.
The four corners (containing the spaces) are triangles.
Examples

Diamond for letter 'A':
A

Diamond for letter 'C':
  A
 B B
C   C
 B B
  A

Diamond for letter 'E':
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A

P
Input: a single-char string (all examples are UPPERCASE)
Output: a multiline string in a specific configuration
Explicit:
1 Diamond always starts with 'A' 
    and adds a row for each letter between 'A' and the input letter
2 once the row for the input letter is reached, the diamond begins to close,
    so all previous rows are printed again in reverse order
    until the final line which is also always 'A'
3 each row separates it's 2 printed letters by a number of SPACES that increases
    by 1 for the second row and 2 for each subsequent row
4 that covers most rules above, but refer above for disambiguation
Implicit:
1 examples show that each row needs to CENTER it's output with SPACES to acheive
    the diamond effect
2 requires `Diamond` class and `make_diamond` class method
3 each row ends with a "\n" newline char

E
Let's look at some custom examples:
Input: B
" A "
"B B"   # all rows len 3, which happens to be 1 more than 'B's place in
" A "   # the alphabet, also row 'B' has 1 space, equal to its index in alphabet

Input: H
       A       \n# 7 spaces either side of A + \n
      B B      # 6 spaces either side of B, 1 space between
     C   C     # 5 spaces sides, 3 between 
    D     D    # 4 spaces sides, 5 between
   E       E   
  F         F  
 G           G 
H             H # 15 chars (H + ' '*13 + H) H is 8th char of alphabet (idx 7)
 G           G 
  F         F  
   E       E   
    D     D    
     C   C     
      B B      
       A       

There is a mathematical relationship here
The number of spaces between the 2 letters on a given row is:
    (2 * alphabet(idx)) - 1 for every character after A
    Each row must be padded with enough spaces to be the same length as the
        longest line in the diamond (target char), with the additional spaces
        evenly split among the leading and trailing sides of the line
        ie. 'C' is at index 2
            2 * 2 - 1 = 3 spaces between the 'C's
            'H' is at index 7
            2 * 7 - 1 = 13 spaces between the 'H's
            therefor 10 spaces need to be padded to the C line, 5 on each side

C
I understand the problem

H
create `Diamond` class, `make_diamond` class method
init class constant ALPHABET
method returns the whole multiline diamond
    calculates each string as a function of the index of the target letter
        and the current letter
    I note that the tests are expecting a single long string of output
        so an appropriate strategy might be to use a helper to formulate each line
        and have `make_diamond` simply be responsible for joining all the output

D
string input
string output
may use a list to collect lines or parts of lines

A
create `Diamond` class, `make_diamond` class method
init class constant ALPHABET

method returns the whole multiline diamond
    calculates each string as a function of the index of the target letter
        and the current letter

    
    l_pad, r_pad = (interstice(target) - interstice(char)) // 2



    I note that the tests are expecting a single long string of output
        so an appropriate strategy might be to use helper(s) to formulate each line
        and have `make_diamond` simply be responsible for joining all the output
    
    interstice(char) = (' ' * 2 * ALPHABET.index(char)) - 1

    append a \n to each line before collection

C
"""
class Diamond:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def interstice(cls, char):
        return ' ' * ((2 * cls.ALPHABET.index(char)) - 1)
    
    @classmethod
    def pad(cls, curr_char, target):
        return ' ' * ((len(cls.interstice(target)) - len(cls.interstice(curr_char))) // 2)
    
    @classmethod
    def make_row(cls, curr_char, target):
        return (
            f"{cls.pad(curr_char, target)}{curr_char}"
            f"{cls.interstice(curr_char)}{curr_char}"
            f"{cls.pad(curr_char, target)}\n"
        )
    
    @classmethod
    def make_diamond(cls, target):
        index = cls.ALPHABET.index
        if target == 'A':
            return 'A\n'

        curr_char = 'B'
        row_a = f'{cls.pad(curr_char, target)} A {cls.pad(curr_char, target)}\n'
        diamond = row_a
        # top half
        while index(curr_char) < index(target):
            diamond += cls.make_row(curr_char, target)
            curr_char = cls.ALPHABET[index(curr_char) + 1]

        diamond += f'{target}{cls.interstice(target)}{target}\n'

        # # bottom half
        while index(curr_char) > 1:
            curr_char = cls.ALPHABET[index(curr_char) - 1]
            diamond += cls.make_row(curr_char, target)

        diamond += row_a


        return diamond

print(Diamond.make_diamond('Z'))

