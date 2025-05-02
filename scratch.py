# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out. It's a dark night and no
# one can see each other. But you were flying nearby and you can see in the
# dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children,
# i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.


# jeffs answer

# def find_children(string):
#     sorted_alpha_list = sorted(string, key=str.upper) # organize into noncased alphabet

#     print(sorted_alpha_list)

#     final_list = []
#     for char in sorted_alpha_list:
#         if final_list == [] or char.casefold() != final_list[-1].casefold(): # if first char or new char make upper
#             final_list.append(char.upper())
#         else:
#             final_list.append(char.lower())

#     return ''.join(final_list)

def find_children(string):

    list_3 = sorted(string, key=lambda letter: (letter.lower(), letter.isupper()))

    one_word = "".join(list_3)

    return one_word


print(find_children("abBA")  == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")
