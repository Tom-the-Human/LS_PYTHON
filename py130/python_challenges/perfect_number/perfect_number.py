"""
The Greek mathematician Nicomachus devised a classification scheme for natural 
numbers (1, 2, 3, ...), identifying each as belonging uniquely to the categories 
of abundant, perfect, or deficient based on a comparison between the number and 
the sum of its positive divisors (the numbers that can be evenly divided into 
the target number with no remainder, excluding the number itself). For instance, 
the positive divisors of 15 are 1, 3, and 5. This sum is known as the Aliquot sum.

Perfect numbers have an Aliquot sum that is equal to the original number.
Abundant numbers have an Aliquot sum that is greater than the original number.
Deficient numbers have an Aliquot sum that is less than the original number.
Examples:

6 is a perfect number since its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.

28 is a perfect number since its divisors are 
1, 2, 4, 7, and 14 and 1 + 2 + 4 + 7 + 14 = 28.

15 is a deficient number since its divisors are 
1, 3, and 5 and 1 + 3 + 5 = 9 which is less than 15.

24 is an abundant number since its divisors are 
1, 2, 3, 4, 6, 8, and 12 and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.

Prime numbers 7, 13, etc. are always deficient since their only divisor is 1.
Write a program that can tell whether a number is perfect, abundant, or deficient.

P
Input: int (PerfectNumber object ?)
Output: string representing "perfect", "deficient", or "abundant"
Explicit:
1 sum all the positive factors of the number
    sum(div for div in range(1, int(num * 0.5 + 1) if num % div == 0)
2 compare the sum to the original number and return a string representing
    their value comparisson (see rules above)
3 primes are always deficient
4 0, negative numbers, and floats are not valid
Implicit:
1 raise exception if number is not valid
    ValueError, "Input must be a positive integer"
2 requires PerfectNumber class, constructor(?), and classify(int) class method
    not sure if constructor actually needed, since it appears that ints
        are passed directly to `classify`

E
rules taken from unit tests
looks pretty straightforward
12 = 6, 4, 3, 2, 1 == 16 == abundant
13 = 1 == deficient
28 = 14, 7, 4, 2, 1 == 28 == perfect

C
check (I think)

H
create PerfectNumber class
    define class method `classify(num)`
    looks like no other methods are required
classify should test whether its argument is perfect, abundant, or deficient
    may be worthwhile to use a helper to get the sum of factors, 
    depending on how concise I can make that code
    classify or a helper will need to handle input validation and return
        the appropriate error if invalid input

D
int input
range, probably
list could be used to collect factors
string output

A
create PerfectNumber class
    define class method `classify(num)`
    looks like no other methods are required

classify should test whether its argument is perfect, abundant, or deficient
    may be worthwhile to use a helper to get the sum of factors, 
    depending on how concise I can make that code
        aliquot = sum(div for div in range(1, int(num * 0.5 + 1) if num % div == 0) ???

    classify or a helper will need to handle input validation and return
        the appropriate error if invalid input
        perhaps `_validate` helper that checks if input is a positive int
            and raises a ValueError with message "Input must be a positive integer"
            or does nothing if input is valid

C
"""
class PerfectNumber:
    @staticmethod
    def _validate(data):
        if isinstance(data, int) and data > 0:
            return

        raise ValueError("Input must be a positive integer")
        
    @staticmethod
    def classify(number):
        PerfectNumber._validate(number)

        aliquot = sum(div for div in range(1, int(number / 2 + 1)) 
                   if number % div == 0)

        if aliquot > number:
            return 'abundant'
        if aliquot < number:
            return 'deficient'
        return 'perfect'