"""
Write a program that manages robot factory settings.

When robots come off the factory floor, they have no name. 
The first time you boot them up, a random name is generated, 
such as RX837 or BC811.

Every once in a while, we need to reset a robot to its factory settings, 
which means that their name gets wiped. The next time you ask, 
it will respond with a new random name.

The names must be random; they should not follow a predictable sequence. 
Random names means there is a risk of collisions. 
Your solution should not allow using the same name twice.

P
Input: Robot object (takes no args)
Output: unique robot name (unittest shows name seeds ...)
Explicit:
1 when a Robot is created, it should be assigned a random, unique name
2 ensure that no names are repeated, perhaps w/ check against a class variable
3 allow for wiping/reseting a name, assigning a new random name
Implicit:
?

E
The tests show a regex that will be used to determine whether a name is valid.
They also show a couple of ints labeled as name seeds - it looks like these
will be used to force trying to create a new robot with an already-used name.

From what I can see, it doesn't look like any specific method names are needed
although I'll want to use a `name` property to handle logic regarding naming.
Specifically, if a chosen name is taken, another should be generated at random
until the name isn't already taken.

C
I think so - check!

H
create a Robot class with
- a `taken_names` list
- a constructor
- a name property that
    - generates a name
    - checks to see if the name is in the `taken_names` list
    - if not, applies it to the robot object
    - if so, generates a new name and checks that one against the list
- while tests don't seem to specifically check for this, problem indicates need
    to be able to reset/rename, so perhaps a separate method for this
    - this method could be used by the name property if the given name is taken

D
Robot class, instances
list of taken names

A
create a Robot class with
- a `taken_names` list
- a constructor

- a name property that
    - generates a name
    - checks to see if the name is in the `taken_names` list
    - if not, applies it to the robot object
    - if so, generates a new name and checks that one against the list

- tests require a reset method
    - this method could be used by the name property if the given name is taken

C
"""
from random import choice

class Robot:
    taken_names = set()

    def __init__(self):
        self._name = None
        self.name

    @property
    def name(self):
        if self._name == None:
            name = Robot._generate_name()
            
            while name in Robot.taken_names:
                name = Robot._generate_name()

            Robot.taken_names.add(name)
            self._name = name


        return self._name
    
    @staticmethod
    def _generate_name():
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '1234567890'
        return choice(letters) + choice(letters) \
            + choice(digits) + choice(digits) + choice(digits)
    
    def reset(self):
        Robot.taken_names.discard(self._name)
        self._name = None

# bot1 = Robot()
# bot2 = Robot()
# print(bot1._name, bot1.name)
# print(bot2._name)
# print(Robot.taken_names)