"""
Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a 
nucleic acid, in particular DNA. Because nucleic acids are vital to cellular 
functions, mutations tend to cause a ripple effect throughout the cell. 
Although mutations are technically mistakes, a very rare mutation may equip 
the cell with a beneficial attribute. In fact, the macro effects of evolution 
are attributable to the accumulated result of beneficial microscopic mutations 
over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation, 
which replaces one base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken 
from different genomes with a common ancestor, we get a measure of the minimum 
number of point mutations that could have occurred on the evolutionary path 
between the two strands.

This is called the Hamming distance.
```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
```
The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length. 
If you have two sequences of unequal length, you should compute the Hamming 
distance over the shorter length.

P
Input: 2 strings ("strand", "distance")
Output: int representing number of differences between the strings
Explicit:
1 find the number of differences between 2 strings
Implicit:
1 if strings are not equal length only check to the length of the shorter string
    (ignore extra length on either string)
2 preserve all inputs
3 strings may be empty or identical, in either case output is 0
4 requires a `DNA` class and a 
    `hamming_distance()` instance method that takes a single argument

E
implicit rules drawn from examples
visually working through test cases, it all appears clear

C
check

H
write DNA class with a `strand` attribute that takes a string

how to handle distance? for some tests it is hard coded, other times
    a variable is used. either way, doesn't look like a piece of state
        I suppose it could be though. self.distance? doesn't look like 
        that would for the tests, but I may need to experiment

hamming_distnce method compares the 2 strings and returns an int counting the
    differences between the strings up to the length of the shortest string
        probably can do easily with a for loop and counter 
            min(range(len(strand, range(len(distance)))))

what else? looks pretty straightforward now that I get the problem

D
strings
counter should be enough, don't think we need to actually store the differences

A
write DNA class with a `strand` attribute that takes a string

how to handle distance? for some tests it is hard coded, other times
    a variable is used. either way, doesn't look like a piece of state
        I suppose it could be though. self.distance? doesn't look like 
        that would for the tests, but I may need to experiment
        In fact, a DNA object only takes 1 argument to construct, so can't be state


hamming_distnce method compares the 2 strings and returns an int counting the
    differences between the strings up to the length of the shortest string
        find shortest string and use that length to make the loop range
        probably can do easily with a for loop and counter 
            min(range(len(strand, range(len(distance)))))

what else? looks pretty straightforward now that I get the problem

C
"""
class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, distance):
        hamming_distance = 0
        shorter_length = min(len(self.strand), len(distance))

        for idx in range(shorter_length):
            if self.strand[idx] != distance[idx]:
                hamming_distance += 1

        return hamming_distance