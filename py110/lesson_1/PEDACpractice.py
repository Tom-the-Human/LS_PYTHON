'''
Data structures influence your algorithm, and for that reason, these two steps 
are often paired. Deciding what data structure to use is generally easy. A case 
that calls for a list rather than a dictionary, for instance, is generally 
easy to identify. However, designing the right algorithm is far more 
challenging. The biggest problem that students have when writing algorithms 
is providing sufficient detail.

Let's consider another problem. Try to work through the "understand the problem" 
part of this problem on your own, and write the input, output, and rules for it. 
We'll provide a solution below. Later, we'll tackle the data structure and algorithm.
'''

"""
(P)PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.

(D)Data Structure:

input: string
output: list of strings
empty string should output empty list

(A) Algorithm:

take string argument (are inputs ALWAYS strings?)
palindromes = []
check string value against value of reversed(string)
->???how to do same for all possible substrings???<-
    helper function to
    loop through strings getting all substrings
    outer loop from index 0 to 2nd to last index
    inner loop to discover all substrings starting at that index
    possibly while loop (while idx < len(string) ...)*
    append all possible substrings meeting spec to a list
    pass list to function to determine if each is palindrome
    return list of palindromes (new list or mutate argument list?)

so we will have palindrome_substrings(input_string), get_substrings(input_string),
and  find_palindromes(substring_list)
palindrome_substrings() will call get_substrings(), which will return substring_list,
then palindrome_substrings() will pass that list to find_palindromes()
and find_palindromes() will return palindrome_list
return list

"""

def find_palindromes(substring_list):
    palindromes = []
    for substring in substring_list:
        reversed_str = substring[::-1] # slicing, easy way to reverse string in python
        if substring == reversed_str:
            palindromes.append(substring)

    return palindromes 

def get_substrings(string):
    substrings = []
    start_idx = 0

    while start_idx <= (len(string) - 2):
        num_chars = 2
        while num_chars <= (len(string) - start_idx):
            substring = string[start_idx: start_idx + num_chars]
            substrings.append(substring)
            num_chars += 1
        start_idx += 1

    return substrings

        

def palindrome_substrings(input_string):
    substring_list = get_substrings(input_string)

    return find_palindromes(substring_list)


# (E)Test cases:

# Comments show expected return values
print(palindrome_substrings("abcddcbA")) # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]