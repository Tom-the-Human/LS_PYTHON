"""
Write some code that converts modern decimal numbers into their Roman number 
equivalents.

The Romans were a clever bunch. They conquered most of Europe and ruled it 
for hundreds of years. They invented concrete and straight roads and even 
bikinis. One thing they never discovered though was the number zero. This 
made writing and dating extensive histories of their exploits slightly more 
challenging, but the system of numbers they came up with is still in use 
today. For example the BBC uses Roman numerals to date their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. 
Notice that these letters have lots of straight lines and are hence easy to 
hack into stone tablets.

```
 1  => I
10  => X
 7  => VII
 
```
There is no need to be able to convert numbers larger than about 3000. 
(The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each 
digit separately starting with the left most digit and skipping any digit 
with a value of zero.

To see this in practice, consider the example of 1990. 
In Roman numerals, 1990 is MCMXC:
```
1000=M
900=CM
90=XC
```
2008 is written as MMVIII:
```
2000=MM
8=VIII
```

P
Input: integer (num to be converted)
Output: string (Romanized number)
Explicit:
1 handle the digits individually and then combine for the output (concatenation)
2 ?
Implicit:
1 requires a RomanNumeral class
2 requires a `to_roman()` method

E
This looks pretty strightforward. from the examples, I see we'll need conversions
for the base digits, as well as the powers of 10 (X, C, M)
Can easily designate a dict for conversion table

2035 == MMXXXV
length == 4
idx 0 == idx -4 == thousands
so:
2 == 2000
0 == pass/ignore
3 == 30
5 == 5
we can look up f"{digit}{'0'*(length - 1)} to get MM
    how can this be further generalized?
    roman_num = ''
        mult = len(self.num) - 1
        idx = 0
        while mult >= 0:
            if num[idx] != '0':
                roman_num += CONVERSION_TABLE[f"{num[idx]}{'0'*mult}]
            mult -= 1
            idx += 1
        # looks good, let's try it

            mult = 3, idx = 0
        1 roman_num += '2000' == 'MM'
            mult = 2, idx = 1
        2 # num[idx] == '0', so no change at this iteration
            mult = 1, idx = 2
        3 roman_num += '30' == 'XXX' => 'MMXXX'
            mult = 0, idx = 3
        4 roman_num += '5' == 'V' => 'MMXXXV'


721 == DCCXXI

C
check

H
create RomanNumeral class
class constant CONVERSION_TABLE dict
constructor takes an int, saved as self.num

to_roman() method takes only self
    coerces self.num to string
    set empty string `roman_num`
    create `roman_num` from conversions concatenated together

    return `roman_num`

D
int input
dictionary for string conversion
string output

A
create RomanNumeral class
class constant CONVERSION_TABLE dict
    stringified digits as keys, roman equivalents as values
constructor takes an int, saved as self.num

to_roman() method takes only self
    coerces self.num to string
    set empty string `roman_num`
    create `roman_num` from conversions concatenated together
        for digit in str(num)
            roman_num += CONVERSION_TABLE[digit]
    OOOH! This WON'T work!

taking another run at to_roman()
    coerce to string
    get length
    place = 

        
    return `roman_num`

C
"""
class RomanNumeral:
    CONVERSION_TABLE = {
        # ones
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX',
        # tens
        '10': 'X',
        '20': 'XX',
        '30': 'XXX',
        '40': 'XL',
        '50': 'L',
        '60': 'LX',
        '70': 'LXX',
        '80': 'LXXX',
        '90': 'XC',
        # hundreds
        '100': 'C',
        '200': 'CC',
        '300': 'CCC',
        '400': 'CD',
        '500': 'D',
        '600': 'DC',
        '700': 'DCC',
        '800': 'DCCC',
        '900': 'CM',
        # thousands
        '1000': 'M',
        '2000': 'MM',
        '3000': 'MMM'
    }

    def __init__(self, number):
        self.num = str(number)

    def to_roman(self):
        roman_num = ''
        mult = len(self.num)
        idx = 0

        while mult > 0:
            if self.num[idx] != '0':
                roman_num += self.CONVERSION_TABLE[
                    f"{self.num[idx]}{'0' * (mult - 1)}"
                    ]
            mult -= 1
            idx += 1

        return roman_num
