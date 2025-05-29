"""
Write a program that can generate the lyrics of the 99 Bottles of Beer song. 
See the test suite for the entire song.

P
Input:  `verse` method takes an int
        `lyrics` method takes no arg
Output: string of appropriate verse or whole song respectively
Explicit:
1 generate the appropriate lyric given the method and input
Implicit:
1 a verse begins with a number of "bottles of beer" consonsant with the int given,
    takes "one down" and has (int - 1) remaining
2 when 0 bottles are reached output should say "no more" instead of 0
3 "verse 0" includes the line: 
    "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

E
The examples are quite clear
We have a `verse` method that takes an int and returns the appropriate 2 lines
We also have a `lyrics` method that take no argument and returns the whole song

C
check

H
More than one way to do this, but one looks like a clear winner.
-   A) create a dict of each verse with the int as the key, and simply return the
        value associated with the input, or all the values for `lyrics`
        or similarly, a tuple or list with each verse at the appropriate index
    B) `verse` simply returns an f-string dependant on the input, and
        `lyrics` uses a loop to call it for all numbers from 99-0 inclusive
        only trick for this is getting "no more" where "0" would be output, but
        that's no big deal.

    (B) is the way.

D
int put
string output

A
`verse` simply returns an f-string dependant on the input, and

`lyrics` uses a loop to call it for all numbers from 99-0 inclusive
    for num in range(99, -1, -1)

only trick for this is getting "no more" where "0" would be output, but
that's no big deal.
    string replace would work, or even just an "else" clause in a variable assignment
    this is actually turning out to be trickier than expected due to some things I
    didn't notice earlier:
    in the case of 1 bottle, that line needs to say "bottle" instead of "bottles"
    this can occur on either line of a verse, but not both in the same verse

DAMN, I totally missed the need for a `verses` method than takes multiple ints.
Easy enough to add and have it just call `verse` for each int

C
"""
class BeerSong:
    @staticmethod
    def verse(num):
        beer_bottles = f'{num} bottles'
        bottle = 'one'

        if num - 1 > 1:
            remaining_bottles = f'{num - 1} bottles'
        elif num - 1 == 1:
            remaining_bottles = '1 bottle'
        elif num - 1 == 0:
            beer_bottles = '1 bottle'
            remaining_bottles = 'no more bottles'
            bottle = 'it'
            

        if num:
            return (
            f"{beer_bottles} of beer on the wall, {beer_bottles} of beer.\n"
            f"Take {bottle} down and pass it around, {remaining_bottles} of beer on the wall.\n"
            )
        
        return (
        f"No more bottles of beer on the wall, no more bottles of beer.\n"
        f"Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        )
    
    @classmethod
    def verses(cls, start, end):
        output = ''
        for num in range(start, end, -1):
            output += cls.verse(num) + '\n'
        output += cls.verse(end)

        return output

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)
    
# print(BeerSong.verse(1))
# print(BeerSong.verse(0))
# print(BeerSong.lyrics())
# print(BeerSong.verses(99, 96))