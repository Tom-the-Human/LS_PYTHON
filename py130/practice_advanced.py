"""
Write a program that prints the longest sentence in a string based on 
the number of words. You should also print the 
number of words in the longest sentence.

Sentences may end with periods (.), exclamation points (!), or question 
marks (?). You should treat any sequence of characters that are not 
spaces or sentence-ending characters as a word. Thus, -- should count 
as a word. Log the longest sentence and its word count. Pay attention to 
the expected output, and be sure you preserve the punctuation from the end 
of the sentence.

Note that this problem is about manipulating and processing strings. 
As such, every detail about the string matters 
(e.g., case, punctuation, tabs, spaces, etc.).

P
Input: string (possibly multiline as in first couple tests)
Output: string (longest sentence + word count)
Explicit:
1 find the longest sentence based on number of words
2 typical punctuation rules ([., !, ?,] can end a sentence)
3 any sequence of chars except space or sentence-ending punctuation is a word
4 preserve the punctuation and other details such as case, spaces, etc

Implicit:
1 what to do if multiple sentences are same length???

E
"-- should count as a word" from the problem setup, so that's important
for word count

some_text = (
    "I'm making up some text for an example. I need to understand "
    "how to solve this problem. Perhaps this is enough text."
    )

longest sentence == I need to understand how to solve this problem.
The longest sentence has 9 words.

1 divide string into sentences, while retaining all data as is
2 count individual words in each sentence to determine length
3 compare sentence lengths
4 return longest sentence along with word count 

C
check

H
Just using split won't work, too many possible chars to split on, AND we want
to keep the punctuation intact.
Code my own modified split function? Seems like maybe a good one for a closure.
Maybe can pass whole input to modified splitter or standard split and
    - use '.' for first run, result should be list
    - if using standard split, concat each item in list with '.' to replace it
    - could see something like `def splitter(string, punct):` which
        does both bits automatically and returns the list of strings
    - could use a partial function and rerun with each required punctuation ie
        for string in sentences: if '?' in string: splitter(string, '?') --
        but that would need to be assigned to something and this could possibly
        get pretty messy and cause a 3 layer nested list with sentences at
        each layer of nesting. Could flatten via nested generator expression

Once sentences are separated and listed, how to count words and compare?
Words are any sequence not including a space or sentence-ending punctuation
I think splitting on space and counting the length of the newly generated list
    would work. Would certainly work for all given examples, but not for
    nonsense like "The quick ! brown . . . fox" ie rogue spaces & punctuation
    If going this route, save unsplit sentence and word count to a dict.
    We'll need the dict to find longest length and return associated string

D
String input
List of strings to store captured sentences?
Maybe a dict with sentences and word count
String output

A
define a splitter helper function that calls split with sentence-ending punctuation
    if that punctuator is present in the string
        if the final char in the string matches the punctuator, append
            the punctuator to all new substrings created by split
        else append to all but the final one
    do the same for each of the other sentence-enders
    flatten and return resulting list of strings
    closure or partial function might make this more efficient, i.e.
        get_sentences = splitter(string)
        for punctuator in ".!?"
        list_of_sentences += get_sentences(punctuator)

once all sentences are in the list, intact
sentence_word_count = dict()
each sentence will be a dict key with its word count for the value

find the highest value and format a string as shown in examples, using that pair

no instructions given for what to do if multiple sentences are equal length,
    so I'll let Python decide what to do there and observe result
"""
# # from functools import partial

# # def splitter(string, punct):
# #     # return list of sentences with punctuation intact
# #     # not a good solution because it also returns multisentence strings
# #     #   that don't happen to contain `punct`
# #     final_char = string[-1]

# #     if punct in string:
# #         sentences = string.split(punct)
# #         blanks = sentences.count('')
# #         while blanks:
# #             sentences.remove('')
# #             blanks -= 1

# #         # clean list of strings that contain other punctuators!
# #         def clean(sentence):
# #             for ender in ['.', '?', '!']:
# #                 if ender in sentence:
# #                     return False
                
# #                 return True
            
# #         cleaned_list = []
# #         for idx in range(len(sentences)):
# #             if clean(sentences[idx]):
# #                 cleaned_list.append(sentences[idx])

# #         # add `punct` back in
# #         if final_char == punct:
# #             for idx in range(len(cleaned_list)):
# #                 cleaned_list[idx] += punct
# #         else:
# #             for idx in range(len(cleaned_list[:-1])):
# #                 cleaned_list[idx] += punct

# #         return sentences

# #     return []

# # def longest_sentence(string):
# #     sentence_list = []
# #     get_sentences = partial(splitter, string)
# #     for punctuation in '.?!':
# #         sentence_list += get_sentences(punctuation)

# #     word_counts = dict()
# #     for sentence in sentence_list:
# #         word_counts[sentence] = len(sentence.split(' ')) # should get number of words

# #     longest, count = max(word_counts.items())

# #     return f"{longest}\n\nThe longest sentence has {count} words."

# #     # find the maximum value in the dict pairs
# #     # format the output with the pair
# #     # return the output

# def split_into_sentences(text):
#     """
#     Manually splits the text into sentences using '.', '!', or '?' as terminators.
#     Each sentence includes its ending punctuation.
#     """
#     sentences = []
#     current_sentence = ""
    
#     for char in text:
#         current_sentence += char
#         if char in ".!?":
#             # We found the end of a sentence; strip and add if non-empty.
#             stripped = current_sentence.strip()
#             if stripped:
#                 sentences.append(stripped)
#             current_sentence = ""
    
#     # If text doesn't end with a sentence terminator, you may want to include the leftover.
#     if current_sentence.strip():
#         sentences.append(current_sentence.strip())
        
#     return sentences

# def longest_sentence(text):
#     sentences = split_into_sentences(text)
    
#     if not sentences:
#         return ""
    
#     # Build a dictionary mapping each sentence to its word count.
#     # Splitting on whitespace works because any sequence of non-space characters is a word.
#     sentence_word_counts = {sentence: len(sentence.split()) for sentence in sentences}
    
#     # Get the sentence having maximum word count. (In case of a tie, Python's max returns one arbitrarily.)
#     longest = max(sentence_word_counts, key=sentence_word_counts.get)
#     count = sentence_word_counts[longest]
    
#     return f"{longest}\n\nThe longest sentence has {count} words."


import re

def longest_sentence(text):
    sentences = re.findall(r'[A-Z]+[^.!?]*[.!?]', text)

    longest = [
        max(sentence.split(), key=len) for sentence in sentences
        ]
    
    print(longest)

    return f"{longest[0]}\nThe longest sentence has {len(longest[0].split())} words."


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

print(longest_sentence(long_text))
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

print(longest_sentence(longer_text))
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

print(longest_sentence("Where do you think you're going? What's up, Doc?"))
# Where do you think you're going?
#
# The longest sentence has 6 words.

print(longest_sentence("To be or not to be! Is that the question?"))
# To be or not to be!
#
# The longest sentence has 6 words.

# r'[A-Z]+[^.?!]*[.?!]'