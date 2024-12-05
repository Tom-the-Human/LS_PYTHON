"""
1
P
Write a function that rotates a list by moving the first element to the end of
 the list. Do not modify the original list; return a new list instead.
- If the input is an empty list, return an empty list.
- If the input is not a list, return None.
1 Do not mutate the list
2 Return a new list
3 Move only the first element to the end of the list

E
Examples show strings and ints are the list elements in the input.
One is an empty list.
A single element list or empty list should return an identical list.

I previously missed the edge cases showing that non-lists should return `None`

D
List in, list out.

A
- copy the input list with slicing (IF input is of type `list`, else `None`)
- pop element 0 of the copy and
- append it to the copy
"""

# def rotate_list(input):
#     copy_of_input = input[:] if type(input) is list else None

#     if copy_of_input:
#         copy_of_input.append(copy_of_input.pop(0))

#     return copy_of_input

# # All of these examples should print True

# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

"""
2
P
Write a function that rotates the last count digits of a number. To perform 
the rotation, move the first of the digits that you want to rotate to the end 
and shift the remaining digits to the left.

This description is muddy, but the examples are illucidating.

1 take 2 int args
2 Change the first int by moving the digit at the index of the 2nd int
    - ints aren't iterable, so it will be necessary to corce it to an iterable
    - count from the end (right side) of the first int, so `2` becomes `-2`


E
See below and above

D
Very likely will want an intermediate list.

A
- take 2 int args
- coerce the first int to a list with list(str(int))
- pop the element at the index equal to the negative of the 2nd int
- append that element
- coerce back to int with int(join(list))
"""

# def rotate_rightmost_digits(number, idx):
#     number = list(str(number))

#     try:
#         number.append(number.pop(-idx))
#     except IndexError:
#         number.append(number.pop(0))

#     return int(''.join(number))

# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

"""
3
P
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to 
get 329175. Keep the first two digits fixed in place and rotate again to get 
321759. Keep the first three digits fixed in place and rotate again to get 
321597. Finally, keep the first four digits fixed in place and rotate the 
final two digits to get 321579. The resulting number is called the maximum 
rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum 
rotation of that integer. You can (and probably should) use the 
rotate_rightmost_digits function from the previous exercise.

This looks pretty rough at first glance, or at least looks like it'll require
a lot of steps.
Rules
1 First step is to rotate as before.
2 But then, lock the first digit and rotate the second.
3 Lock the 1st and 2nd, and rotate the third, etc.
    - a for loop and negative index should work
    -

E

D
Intermediate list if I'm going to use my previous function.

A
- take a single int arg
- `for idx in len(str(number))`
    - number = rotate_rightmost_digits(number, idx)

    Is that all? Try and find out
"""

# def max_rotation(number):
#     for idx in range(len(str(number))):
#         number = rotate_rightmost_digits(number, -idx)

#     return number


# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

"""
P
https://launchschool.com/exercises/b09d93c8
Description is super long.
1 Init an empty list as a stack (stack = [])
2 init a variable as register assigned `0` (register = 0)
3 Only ints will be used in operations (important for DIV and REMAINDER)
4 Implement the following "commands"
    n: Place an integer value, n, in the register. Do not modify the stack.
    PUSH : Push the current register value onto the stack. Leave the value 
        in the register.
    ADD : Pop a value from the stack and add it to the register value, 
        storing the result in the register.
    SUB : Pop a value from the stack and subtract it from the register value, 
        storing the result in the register.
    MULT : Pop a value from the stack and multiply it by the register value, 
        storing the result in the register.
    DIV : Pop a value from the stack and divide the register value by the 
        popped stack value, storing the integer result back in the register.
    REMAINDER : Pop a value from the stack and divide the register value by 
        the popped stack value, storing the integer remainder of the division 
        back in the register.
    POP : Remove the topmost item from the stack and place it in the register.
    PRINT : Print the register value.

E
Even with examples, this feels a little esoteric at this point, but I will try
my best. Don't want to get stuck here too long though.

D
List as stack, strings as input, maybe a dict of commands?
Made a dict, but what on Earth should the values be?
They should be function calls!!! That's how this can work.

A
Where to even begin? I really have little to no idea how to get these strings
to work as commands. Realizing just now that I have absolutely no idea how 
terminal commands actually work, let alone Python keywords, etc. That is most
probably the point.
- init `stack = []` (do this after function definitions as described below)
- init `register = 0`
To turn the strings into usable information, I think we'll need to use split.
For example, '5 PUSH 3 MULT PRINT' becomes ['5', 'PUSH', '3', 'MULT', 'PRINT']
so then we can do things like `try stack += int(input[0]):` or something.
I think I need at LEAST one helper function because this could get messy.
Probably also a dict of commands. Good use of constants.
- define a function for each command, and build it
    - this may take a couple passes, figuring out for example just what my
        ADD function is doing and acting on. Can args somehow be used in 
        conjunction with these dict values?
    - see the list under "P" for what each function should do
    - I think these should be nested 2nd level functions
        i.e. def minilang():
                def push():
                    code goes here
                def add():
                    etc.
                then, main body of minilang function
    - split input to input list for processing
    - while input:
        COMMANDS.get(word) to call function if in dict, `None` if not
        - if `None`, `try: stack += int(input[idx]),
            except: print("Invalid input")
        - if command requires argument (all of them?)
            - all require `register` so that can be hard coded 
                (NO no args, just `nonlocal`!)
            - all will pop or append to the stack list but don't require an 
                arg for that
            - actually, I think I'll opt for `nonlocal` instead of args since
                these are all very simple nested functions and there's
                no real downside in this particular instance

OK, finally got all the setup coded. Now to figure out how this mess can work.
-
Turns out after defining all the functions, it's just a super simple matter
to alter the register and call the functions from a `for` loop. I DID IT!

"""

# def minilang(string_input):
#     stack = []
#     register = 0
#     code = string_input.split()

#     def n(num):
#         nonlocal register 
#         register = int(num)
    
#     def push():
#         nonlocal register
#         stack.append(register)
    
#     def add():
#         nonlocal register 
#         register += stack.pop()
    
#     def sub():
#         nonlocal register
#         register -= stack.pop()

#     def mult():
#         nonlocal register
#         register *= stack.pop()

#     def div():
#         nonlocal register
#         register //= stack.pop()

#     def remainder():
#         nonlocal register
#         register %= stack.pop()
    
#     def my_pop():
#         nonlocal register
#         register = stack.pop()
    
#     def my_print():
#         nonlocal register
#         print(register)

#     COMMANDS = {'PUSH': push,
#                 'ADD': add,
#                 'SUB': sub,
#                 'MULT': mult,
#                 'DIV': div,
#                 'REMAINDER': remainder,
#                 'POP': my_pop,
#                 'PRINT': my_print}

#     for word in code:
#         try:
#             n(word)
#         except:
#             if word in COMMANDS:
#                 COMMANDS[word]()
#             else:
#                 print("Invalid input")



# minilang('PRINT')
# # 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

# minilang('6 PUSH')
# # (nothing is printed)

"""
5
P
Write a function that takes a string as an argument and returns that string 
with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 
'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its 
corresponding digit character.

You may assume that the string does not contain any punctuation.

1 Return the digit for each english word meaning a digit in a string input.
    - i.e. 'five' = 5

This is shockingly easy compared to the last problem.

Can solve with either a dict or match-case

E
Example shows that all words are separated by spaces, and that is what
is expected in the output, even spaces between the digits

D
Dict would be handy for number conversion. I/O is strings

A
- init a dict of word-digit pairs
- init a word list = split the input by space
- `for word in list:`
    - `if word in dict:`
        - `word = dict[word]`
        - else pass
- `return ' '.join(word_list)
"""

# def word_to_digit(string):
#     digits = {
#         'zero': '0',
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9'
#     }

#     words = string.split()

#     for i, word in enumerate(words):
#         if word in digits:
#             words[i] = digits[word]

#     return ' '.join(words)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

"""
6
P
A prime number is a positive number that is evenly divisible only by itself 
and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is 
not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. 
Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns 
true if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem. 
Your task is to programmatically determine whether a number is prime without 
relying on functions that already do that for you.

1 Return true if the integer input is prime
2 Return false if it is non-prime
3 No add-on packages
4 1 is not prime

E
No news here

D
Maybe a list to hold divisors?

A
I have a feeling there is a very easy answer to this that I'm not seeing.
Maybe it'll be clearer as I work through, like with problem 4.
I read that to check for primeness I can try dividing it by every number 
from 2 up to the square root of the number. Sounds like a plan.

- create a list of the numbers from 2 to the square root of the number (incl)
    - can be done with range and using `math.sqrt` though I'm unsure if that
        is considered using an add-on package, which is prohibited.
- if the result of dividing the number by any number in the list results
    in an int, return False
- if the number is 1 or less, return False
- else True?

Maybe that's all there is to it?

"""
# import math

# def is_prime(num):
#     if num <= 1:
#         return False
    
#     divisors = [integer for integer in range(2, int(math.sqrt(num)) + 1)]

#     for d in divisors:
#         if (num / d) % 1 == 0:
#             return False
    
#     return True

# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

"""
7
P
The Fibonacci series is a sequence of numbers in which each number is the sum 
of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The 
third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be 
represented as:
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number, 
where nth is an argument passed to the function:
1 Take an int argument and
2 Return the number that occupies that position in the Fibonacci sequence

E
We are starting with index 1, but other than that, nothing really noteworthy

D
I'll need something to hold Fibonacci numbers, such as a list ...
but I can't actually just list all Fibonacci numbers as that list would be
infinite! Can a range or other generator work? 

Actually maybe I won't do that at all, maybe I can just write a function
that calculates the number using a loop.

Oh! We don't need ALL the F numbers, we only need a list of 2.
We'll init the list to [1, 1]

A
I think a loop can do this. It's something like:

- init `f_nums = [1, 1]`
- init `counter = 2` (because the list already contains the first 2 numbers)
- `while num < counter:`
    - `f_nums = [f_nums[1], (f_nums[0] + f_nums[1])]`
    - counter += 1

- if num in [1, 2] return 1

- return f_nums[1]

I think this should work well, though not the most readable. I could do better
naming and assign a varaible or 2. Might just.
"""
# def fibonacci(num):
#     if num in [1, 2]:
#         return 1
    
#     f_nums = [1, 1]
#     counter = 2

#     while counter < num:
#         f_nums = [f_nums[1], f_nums[0] + f_nums[1]]
#         counter += 1

#     answer = f_nums[1]
    
#     return answer

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True

"""
8
P
In the previous exercise, we developed a procedural solution for computing 
the nth Fibonacci number.

This sequence can also be computed using a recursive function. A recursive 
function is one in which the function calls itself. For example, 
the following function is a recursive function that computes the sum of all 
integers between 1 and n:
`def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n - 1)`

Recursive functions are a bit difficult to understand for novice programmers, 
but it's worth putting in a little time early on to see what recursion looks 
like. Recursion can, in some situations, greatly simplify some algorithms.

A recursive function has three primary qualities:

It must have a base case. This is a condition that tells the function to stop 
recursing and begin the process of returning to the first call to the 
function. This is often the simplest case - the condition for which you 
already know the answer. In sum_recursive, the base case occurs when n == 1. 
At this point, we know the answer: sum_recursive(1) == 1. 
Thus, we can return the value 1.
The function must call itself except when handling the base case.
Each recursive call must be "closer" to the base case than the current call. 
For instance, in sum_recursive(3), we call sum_recursive(2), which is closer 
to the base case. Likewise, sum_recursive(2) subsequently calls 
sum_recursive(1), which is the base case.
You may recall from the previous exercise that the Fibonacci sequence follows 
a simple set of rules:
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

If you study this set of rules, you can see that the algorithm is 
defined recursively:
1 - The base case occurs when the argument is 1 or 2; both of these 
arguments result in a value of 1.
2 - The Fibonacci function calls itself. In fact, it calls itself twice.
3 - Except when dealing with the base case, each call to the Fibonacci 
function comes closer to the base case. In this case, both F(n - 1) and 
F(n - 2) are closer to the base case than F(n).

Given this recursive algorithm, try to write a recursive function that 
computes the nth Fibonacci number, where nth is an argument passed to the 
function.

1 Same rules as before except
2 must use recursion

E
Same examples as before

D
Same as before, I imagine

A
Hmm ... feels like it should be natural to include recursion here but I'm
having a bit of trouble wrapping my head around it, even though I've used it
a couple of times before. 
Actually, I think I got it. Instead of the loop, or maybe as part of the loop,
I could call the function again. Or perhaps, there is a recursive helper?

It starts the same, for sure.
- init two `1`s to a list or individual vars, probably doesn't matter which
- probably also init the counter?

I don't know. My brain won't work. This is later than I usually study.
I could maybe get there in the morning, but now is when I have time, so I'm
reading the discussion and answer.

It appears a counter isn't needed here, nor the initialization of `1`s.

My ACTUAL first step last time was to return 1 `if num in [1, 2]`.
That is the same here, though LS uses the condition `if num <= 2` which means
the same thing if no negative numbers are ever passed as the arg. Their
version is perhaps more robust if negatives are used.

Then all that happens is returning `fibonacci(num -1) + fibonacci(num - 2)`,
but I don't yet understand why this actually works. I'll play with a bit to
gain understanding. I do see that it is basically a direct copy of the actual
Fibonacci formula.

I still cannot understand how the correct result is being achieved. This is
highly opaque to me, even after playing, printing, and rereading.

I am slightly heartened to see that no other students have submitted their
alternate solutions, which means that few, if any, have been found.
And possibly, most have had as much difficulty as I have with this.
"""
# def fibonacci(num):
#     if num <= 2:
#         return 1
#     #print(num)
#     return fibonacci(num - 1) + fibonacci(num - 2)

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True
# print(fibonacci(7))

# Having failed to understand this, I feel reluctant to move on,
# since the next exercise is refactoring this one.
# But I will do so in the morning. And perhaps revisit this as well.

"""
9
P
Our recursive fibonacci function from the previous exercise isn't very 
efficient. It starts slowing down with an nth argument value somewhere around 
35-60, depending on your system. One way to improve the performance of our 
recursive fibonacci function (and other recursive functions) is to use 
memoization.

Memoization is an approach that involves saving a computed answer for future 
reuse, instead of computing it from scratch every time it is needed. In the 
case of our recursive fibonacci function, using memoization saves calls to 
fibonacci(nth - 2) because the necessary values have already been computed by 
the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci 
function to use memoization.

An image representing the computation of the 7th Fibonacci number is shown 
below. It is the same image that was shown in the previous exercise, except 
this one highlights the values that have previously been computed.
    [image showing each number calculated once, which isn't helping me since
        I still don't understand how this mess returns the right value]

Hint: One approach to memoization is to use a lookup table, such as an object,
for storing and accessing previously computed values.

1 return the nth fibonacci value as before but
2 use memoization to avoid calls to fibonacci(nth - 2)

*Maybe I'm too focused on the need to understand how this works. I just don't
how the right value is being reached. I thought what was happening was that
when each recursive function reaches 2 or 1, - wait, I finally got it. And I
was on the right track but just missing a detail. The recursive function works
by more or less "branching" itself as many times as needed for `n` to be
1 or 2, and each instance of the function receiving `n` of 1 or 2 returns `1`.
At each recursive call, `n` is reduced by either 1 or 2, and there are 2 calls 
per recursion until an instance receives 1 or 2, which causes it to return `1`
to the previous call.
So for `n = 7`, there are eventually 13 instances of `fibonacci` each returning
`1` back up the chain and adding together until ultimately 13 is returned by
the first instance.

So in this memoization, it seems we're supposed to reach the same end without
calculating the `(n - 2)`s? This is also difficult for me to understand,
having only just figured out what (I think) was happening last exercise.*

E
No new examples. Just the image and the previous examples.

D
A list to store calculated values, I guess?

A
I honestly feel a bit lost still. Memoization sounds like some hybrid of the
last 2 solutions. And I've been here for over 30 minutes just looking at this 
problem and writing about it. Not making progress.

- init a global list `calced_vals` to store values?
- how does that help prevent repeated calculations?

Ok, I looked at LS's solution. My understanding is still a little shaky, but
getting there. They used a dict instead of a list. But basically its just an
introduction of an `elif` clause checking to see if the result of an instance
of `fibonacci(num - 1) + fibonacci(num - 2)` is already in the dict, adding
that value to the dict if it is not present. 

To test my understanding (what little of it there is), I'm going to try a
variation with a set. So when the result is returned, I'll check to see if -
scratch that. I just reasoned why it must be a dict. The dict looks something
like `{3:2, 4:3, 5:5, 6:8, 7:13, ...}`, as it gets populated by 
key=n, value=result, we can just check to see if `n` is already in it and get
the result without all the recursion. With a set or list, we can append the
result, but don't have a way to recognise it as the result of a given `n`.

"""
# def fibonacci(num):
#     if num <= 2:
#         return 1
    
#     if num in calced_vals:
#         return calced_vals[num]
#     #print(num)
#     calced_vals[num] = fibonacci(num - 1) + fibonacci(num - 2)
#     return calced_vals[num]

# calced_vals = {}

# print(fibonacci(1) == 1)         # True
# print(fibonacci(2) == 1)         # True
# print(fibonacci(3) == 2)         # True
# print(fibonacci(4) == 3)         # True
# print(fibonacci(5) == 5)         # True
# print(fibonacci(6) == 8)         # True
# print(fibonacci(12) == 144)      # True
# print(fibonacci(20) == 6765)     # True
# print(fibonacci(7))

"""
10
P
As we've seen in the last few exercises, the Fibonacci series is a 
computationally simple series, However, the results grow at an incredibly 
rapid rate. For example, the 100th Fibonacci number is 
354,224,848,179,261,915,075 -- that's enormous, especially considering that 
it takes six iterations just to find the first 2-digit Fibonacci number.

Write a function that calculates and returns the index of the first Fibonacci 
number that has the number of digits specified by the argument. The first 
Fibonacci number has an index of 1. You may assume that the argument is 
always an integer greater than or equal to 2.

So if I understand right, what is wanted here is that we return the POSITION
in the F sequence of the first F number with `num` number of digits.
I.e. the firs F number with 2 digits is 13, the 7th number in the series.
Hence `find_fibonacci_index_by_length(2) == 7`. Ok. Good. New problem that I
can understand more easily.
1 find and return the position/index of the first F number with the number of 
    digits specified

Well, I still don't know how to get the answer, but carrying on.

E
No news, except that some very big numbers will need to be calculated!

D
I think the solution involves calling the previous function (or can, and 
probably should). So I'll use a dict again.

A
I'm actually not sure the last function is helpful here, now that I've copied
it below and am looking at it. Well, I do see a way for it to work.
- take a length argument (length being number of digits)
- while no number in the dict has a length equal to `length`
    - find this with `len(str(fibonacci(num)))` (starting w/ `length`, because
        `length` is less than the result we want and greater than 1)
        - actually don't bother checking the dict, just check the return value
            of `fibonacci(number)`
    - if return value is less than `length` increment the `number`
    - hmm ... this is causing a RecursionError with the last example, but
        works otherwise - I think `length` is too low a starting value.
        Maybe `2 * length`?
            Oh! that acutally made it worse somehow. Now the 2nd to last one
            is causing the error, with only 1/10th the length!
            Same with `2 / length`, though I would expect that.
            Why this would happen with `2 * length` is a mystery to me, though

Ok, LS solution is similar but just using a straight/procedural function like
the first Fibonacci function in this series. My solution works, but we would 
have to also use `sys` to set the recursion depth at a greater limit, so
it's safe to say my solution is not as good as LS's.
"""
import sys

sys.set_int_max_str_digits(50_000)

def fibonacci(num):
    if num <= 2:
        return 1
    
    if num in calced_vals:
        return calced_vals[num]
    #print(num)
    calced_vals[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return calced_vals[num]

def find_fibonacci_index_by_length(length):
    number = length

    while len(str(fibonacci(number))) < length:
        number += 1
    print(number)
    return number


calced_vals = {}

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)