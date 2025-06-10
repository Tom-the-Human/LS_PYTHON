"""
Create a clock that is independent of date.

You should be able to add minutes to and subtract minutes from the time 
represented by a given Clock object. Note that you should not mutate Clock 
objects when adding and subtracting minutes -- create a new Clock object.

Two clock objects that represent the same time should be equal to each other.

You may not use any built-in date or time functionality; 
just use arithmetic operations.

P
Input: 1 or 2 ints, also arithmetic
Output: Clock object
Explicit:
1 Clock objects should not be mutated (mutable?), when using a Clock instance
    with arithmetic, result should be new Clock
2 if 2 Clocks have same time, they should be equal
Implicit:
1 When arithemetic, ints represent minutes added or subtracted
2 first int passed to Clock.at() is hours (24 hour cycle), 
    2nd int is minutes (60 minute cycle)
3 string representation of a Clock should be 'HH:MM'
4 greatest possible output '23:59' (1 minute to midnight), 
    least possible '00:00' (midnight)
5 Clocks are exclusively constructed using the `Clock.at()` method (??)
    not 100% sure how to acheive this - 
        is `at` the constructor? (maybe `at` calls `__init__`)
6 will require methods such as str, eq, gt, lt, and others needed for +/-

E
unittests show basic construction is via the `at` method i.e.
str(Clock.at(11, 9)) == '11:09'
also
str(Clock.at(10)) + 61 == '11:01'
*note that the "+ 61" is not part of the argument to `at` ...
this is a little mysterious as to how the math gets done when it's not passed
What I think is happening here is
#1 Clock.at(10) is evaluated first, so a Clock object '10:00'
#2 Then Clock + 61 is evaluated, which results NEW Clock representing '11:01'

C
I think I understand. Still a little foggy on construction via `at()`

H
Clock class:
- constants HRS_A_DAY, MINS_AN_HR
- at method
    - constructor, or just calls constructor?
    - if calls, how to deny direct access to constructor (i.e. Clock(1, 2))?
        - can __init__ be nested? is that necessary?
    - takes up to 3 args (cls, hours, minutes) (if only cls, '00:00')
    - creates instance, assigns hours & minutes as state
    - hours must be in range(0, 25), minutes in range(0, 61)
        - if arg is > range, wrap calc
- instances must allow addition & subtraction with ints
- str method
    - return 'HR:MN'
- eq
    - if both clocks have same hours, mins, they are equal
- other arithmetic and comparrison methods as needed
    - may need to look some of these up

D
ints
strings
Clock instances
?

A
Clock class:
- constants HRS_A_DAY, MINS_AN_HR
- at method
    - constructor, or just calls constructor?
    - if calls, how to deny direct access to constructor (i.e. Clock(1, 2))?
        - can __init__ be nested? is that necessary?
        - just having a standard __init__ method will pass the tests,
            - we just won't access it directly
            - if was building a real program, probably would want access control
    - takes up to 3 args (cls, hours, minutes) (if only cls, '00:00')
    - creates instance, assigns hours & minutes as state
    - hours must be in range(0, 25), minutes in range(0, 61)
        - if arg is > range, wrap calc
- instances must allow addition & subtraction with ints
- __str__ method
    - return 'HR:MN'
- __eq__
    - if both clocks have same hours, mins, they are equal
    - may also need __gt__ or __lt__
- other arithmetic and comparrison methods as needed
    - may need to look some of these up
    - __add__
    - __sub__

C
"""
class Clock:
    HRS_IN_DAY = 24
    MINS_IN_HR = 60
    MINS_IN_DAY = HRS_IN_DAY * MINS_IN_HR

    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    @classmethod
    def at(cls, hours, mins=0):
        hours, mins = cls.fix_time(hours, mins)
        return cls(hours, mins)
    
    @classmethod
    def fix_time(cls, hours, mins):
        while mins >= cls.MINS_IN_HR:
            mins -= cls.MINS_IN_HR
            hours += 1

        while hours >= cls.HRS_IN_DAY:
            hours -= cls.HRS_IN_DAY

        return hours, mins

    def __str__(self):
        str_hrs = str(self.hours) if len(str(self.hours)) == 2 \
                    else f'0{self.hours}'
        str_mins = str(self.mins) if len(str(self.mins)) == 2 \
                    else f'0{self.mins}'
        return f'{str_hrs}:{str_mins}'
    
    def __eq__(self, other):
        if isinstance(other, Clock):
            if self.hours == other.hours and self.mins == other.mins:
                return True
            
        return False
    
    def __add__(self, mins):
        # Create new instance with new time, also handle calculating new time
        # Could probably call fix_time instead
        new_mins = self.mins + mins
        return Clock.at(self.hours, new_mins)

    def __sub__(self, mins):
        # Create new instance with new time, also handle calculating new time
        # Could probably call fix_time instead
        new_mins = self.mins - mins
        new_hours = self.hours

        while new_mins < 0:
            new_mins = Clock.MINS_IN_HR - abs(new_mins)
            new_hours = new_hours - 1

        while new_hours < 0:
            new_hours = Clock.HRS_IN_DAY - abs(new_hours)

        return Clock.at(new_hours, new_mins)
    
# test_clock = Clock.at(10, 5)
# print(test_clock)
# test_hrs = Clock.at(100, 5)
# print(test_hrs)
# test_mins = Clock.at(10, 500)
# print(test_mins)

# test_eq = Clock.at(10, 5)
# print(test_eq == test_mins)
# print(test_eq == test_clock)

# test_add = test_clock + 10
# test_sub = test_clock - 10
# print(test_add, test_sub)
# print(test_add is test_clock)
# print(test_sub is test_clock)