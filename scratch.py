"""
Create a function that converts an integer (0-999999) 
into its English word representation.

P
Input: int
Output: string
Explicit:
1 return a string representation of the integer passed in
2 cover ints 0 through 999,999
Implicit:
1 follow the formatting displayed in the test cases
    (that "fifty thousand" might be a monky-wrench)

E
From examples, I see the following:
No "ands" or other fluff, just digits and "place" (I guess?) words 
    i.e. 'thousand', 'hundred'
I think any solution will need to use multiple dictionaries and conditionals
ones dict - standard digit names i.e. 'one', 'two', etc
tens dict - alternate digits names if occupying tens place i.e 'twenty', 'thirty'
what about teens???
    maybe a whole dict just for 'ten' through 'nineteen'
    however, no test cases include numbers in this range!
    logically they are needed, but could skip if just writing to the tests
    are needed by problem description

Words are space separated

From last test, looks like I need to evaluate not just if digit is in the
next-to-last place, but if it occupies ANY tens position, for example:
    (My own test case)
    print(number_to_words(223060) == "two hundred twenty three thousand sixty")
    SO:                    ^  ^ both of these carots point to tens positions
                            tens dict is accessed to get 'twenty', 'sixty'
    since numbers >= 1000000 not allowed, only have 2 positions to cover
    and that's only in the event that there are enough digits in the input

C
check

H
corece to string and reverse
    - string to handle digits separately for dict matching
    - reverse to make it easier to determine which dict to use for each digit
    - if using teens dict, will need to also pop previous number from output
for each digit in the string, append appropriate word to output list
    - some words will be appended based on place only, i.e. 'hundred', 'thousand'
        - these need to be placed in the list BEFORE the number word
            - i.e. 246 > '642' > ['six', 'forty', 'hundred', 'two'] >
                ['two', 'hundred', 'forty', 'six'] > 'two hundred forty six'

D
int input
string of int
dicts of number word permutations
list of words (strings)
string output

A
'zero' should only be output if the input is 0, so handle this case up front
- 'zero' is not a part of any other output, so 0 can typically be ignored
    (except in the case of '10': 'ten')

3 constants
    - ones dict
    - tens dict
    - teens dict

coerce to string and reverse
    - string to handle digits separately for dict matching
    - reverse to make it easier to determine which dict to use for each digit
    - if using teens dict, will need to also pop previous number from output

init word_list = []
for each digit in the string, append appropriate word to output list
    - some words will be appended based on place only, i.e. 'hundred', 'thousand'
        - these need to be placed in the list BEFORE the number word
            - i.e. 246 > '642' > ['six', 'forty', 'hundred', 'two'] >
                ['two', 'hundred', 'forty', 'six'] > 'two hundred forty six'

    enumerated for loop to iterate through digits and look up word based on index
        - if idx == 2 or 5, append 'hundred'
        - elif idx == 3, append 'thousand'
        - if idx == 1 or 4 AND digit IS 1, use TEENS dict
            - discard previous word from list before adding new one
            - lookup will have to include previous number, i.e. if previous number
                was 5, lookup should be '15', which has the value 'fifteen'
                - slice of digits[idx:idx-1:- 1]?????
                    - couldn't get slice to work, so used concatenation
        - if idx == 1 or 4 AND digit is NOT 1, use TENS dict
        - else use ONES dict


C
"""
ONES = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

TENS = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety',
}

TEENS = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

def number_to_words(num):
    """
    Convert a number to its English word representation.
    Args:
        num (int): An integer between 0 and 999999
    Returns:
        str: The English word representation of the number
    """
    if num == 0:
        return 'zero'
    
    digits = str(num)[::-1] # reverse order string
    # reverse makes indexing easier during translation
    num_words = []

    for idx, digit in enumerate(digits):
        # insert word based on index before word based on char
        # (it will appear in correct order after we reverse the list)
        if digit != '0' and (idx == 2 or idx == 5):
            # only append 'hundred' if a non-zero value in this position
            num_words.append('hundred')
        elif idx == 3:
            # always append 'thousand' if this index exists
            num_words.append('thousand')

        # 0 needs no representation in output
        if digit == '0':
            continue

        # lookup translation in correct dict based on index and digit
        if digit == '1' and (idx == 1 or idx == 4):
            # TEENS
            # if adding word from TEENS dict, first remove last word in list
            # since teens represent current AND previous digit
            num_words.pop()
            num_words.append(TEENS[digits[idx] + digits[idx - 1]])
        elif idx == 1 or idx == 4:
            # TENS
            num_words.append(TENS[digit])
        else:
            # ONES
            num_words.append(ONES[digit])

    return ' '.join(num_words[::-1]) # reverse list and join for final output

# Test cases
print(number_to_words(0) == "zero")
print(number_to_words(23) == "twenty three")
print(number_to_words(105) == "one hundred five")
print(number_to_words(1234) == "one thousand two hundred thirty four")
print(number_to_words(50000) == "fifty thousand")
# My tests
print(number_to_words(16) == 'sixteen')
print(number_to_words(161616) == 'one hundred sixty one thousand six hundred sixteen')
print(number_to_words(999999) == 'nine hundred ninety nine thousand nine hundred ninety nine')
print(number_to_words(1812))