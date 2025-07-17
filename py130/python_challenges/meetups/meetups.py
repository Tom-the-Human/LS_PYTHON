"""
Meetups are a great way to meet people who share a common interest. 
Typically, meetups happen monthly on the same day of the week. For example, 
a meetup's meeting may be set as:

The first Monday of January 2021
The third Tuesday of December 2020
The teenth Wednesday of December 2020
The last Thursday of January 2021

In this program, we'll construct objects that represent a meetup date. 
Each object takes a month number (1-12) and a year (e.g., 2021). 
Your object should be able to determine the exact date of the meeting in the 
specified month and year. For instance, if you ask for the 2nd Wednesday of 
May 2021, the object should be able to determine that the meetup for that 
month will occur on the 12th of May, 2021.

The descriptors that may be given are strings: 'first', 'second', 'third', 
'fourth', 'fifth', 'last', and 'teenth'. The case of the strings is not 
important; that is, 'first' and 'fIrSt' are equivalent. Note that "teenth" 
is a made up word. There was a meetup whose members realized that there are 
exactly 7 days that end in '-teenth'. Therefore, it's guaranteed that each 
day of the week (Monday, Tuesday, ...) will have exactly one date that is the 
"teenth" of that day in every month. That is, every month has exactly one 
"teenth" Monday, one "teenth" Tuesday, etc. The fifth day of the month may 
not happen every month, but some meetup groups like that irregularity.

The days of the week are given by the strings 'Monday', 'Tuesday', 
'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'. 
Again, the case of the strings is not important.

P
Input: Meetup object with int args (year, month number)
Output: Exact date of meeting
Explicit:
1 program must be able to create Meetup objects with 2 int args
2 objects must have a `day` method that accepts 2 string args (day, count) 
    (case-insensitive) (i.e. 
                        (Wednesday, second), 
                        (Monday, Fifth), 
                        (TUESDAY, teenth), 
                        (saturday, last),
                        etc)
3 when that method is called, the date should be returned as a `date` obj
Implicit:
1 will require datetime module ... only `datetime.date`?
2 return None if no such date found (i.e. fifth day doesn't occur)

E
The test cases are all of the same format:

    def test_third_sunday_of_december_2014(self):
        meetup = Meetup(2014, 12)
        self.assertEqual(date(2014, 12, 21), meetup.day('Sunday', 'third'))

This alone is enough to help me design the class. 
I think the sticky part of this problem may be in using `datetime` appropriately.
Also determining which is the third Sunday (in this case).
Can I collect all the Sundays to list? All days in the month to a dict?
If a list, could index to find third element. But what if it's the "teenth" Sunday?
Then indexing wouldn't work, but I could check the dates against a range(13-20).
For fifth Sunday, I'd have to first check against the length of the list.

H
define class Meetup
constructor takes 2 int args
define Meetup.day, which takes 2 string args
looks like no validation or error handling is required for these tests
Meetup.day must return the expected date object

D
date object
possibly a list or dict
ranges almost certainly

A
define class Meetup
constructor takes 2 int args (year, month_number)
- would normally want to validate args, but tests don't require it

define Meetup.day, which takes 2 string args
- would normally want to validate args, but tests don't require it

looks like no validation or error handling is required for these tests

Meetup.day must return the expected date object
- how to use date objects? will need to figure out

day(self, weekday, qualifier):
 - for self, retrieve all the dates in that month that are on the right weekday
    - need to find syntax for retreiving these via datetime
    - save date objects to a list
    - if qualifier is "teenth"
        - return the object whose date is in range(13, 20)
    - elif qualifier is "last"
        - return the last date in the list
    - elif qualifier is "fifth"
        - check that the length of the list is > 4
            - if so, return the date at index 4
    - else
        - return the date corresponding to the list index - 1
            - "first" = days[0]
            - "third" == days[2]
C
"""

import calendar
from datetime import date

class Meetup:
    WEEKDAYS = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    ORDS = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4,
        'last': -1
    }

    def __init__(self, year, month_num):
        self.year = year
        self.month_num = month_num


    def day(self, wkday, ordinal):
        last_day = calendar.monthrange(self.year, self.month_num)[1]

        days = [
            date(self.year, self.month_num, i) 
            for i in range(1, last_day + 1) 
            if date(self.year, self.month_num, i).weekday() 
            == Meetup.WEEKDAYS[wkday.casefold()]
            ] 

        match ordinal.casefold():
            case 'teenth':
                teenth = [d for d in days if d.day in range(13, 20)]
                return teenth[0]
            case 'fifth':
                if len(days) >= 5:
                    return days[Meetup.ORDS[ordinal.casefold()]]
                else:
                    return None
            case _:
                return days[Meetup.ORDS[ordinal.casefold()]]
