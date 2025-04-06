# file = open('example.txt', 'r') # read mode, default
# file = open('example.txt', 'w') # write mode, create new or truncate existing file
# file = open('example.txt', 'a') # append mode
# there are more modes, but these will be most used


# print(file) # semi-useless object description
# print(file.read()) # file text (probably what we usually want to see)

# better way to handle is to use file.read() in an assignment,
# then close the file ... currently the file remains open, using resources

# content = file.read()
# file.close()
# print(content)
# print(repr(content)) # pythonic view of text
# including exposed newlines, could be copy/pasted to recreate object


# content = file.readlines() # list of lines as strings, newlines includes
# file.close()

# print(content)
# print(repr(content)) # same as above in this case


# first = file.readline() # gets a single line from the file
# second = file.readline() # same method gets successive lines
# file.close()
# print(first, second) # lines as shown in file
# print(repr(first), repr(second)) # lines as would be used to reproduce them
# Note that file.readline returns an empty string
# once it detects the end of file.


# for line in file:
#     print(repr(line)) # or print(line) alternatively
# prints each line
# file.close()

# ------------
# file = open('output.txt', 'w') # open in write mode (creates new file if doesn't exist)
# file.write("It's planting season.\n") # add a single line

# lines = ['I need to finish moving soil\n', 'and get some plants in the ground.']
# file.writelines(lines) # adds multiple lines from list (or other collection?)
# file.close()


# file = open('output.txt', 'a') # open in append mode
# file.write("I hope this summer isn't too hot.\n")
# lines = ['The work is hard,\n', 'but I do enjoy it.\n']
# file.writelines(lines)
# file.close()

# -----------
# use `with` to automatically close files after use and free up resources
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line)

# `with` is a context manager, which is a kind of construct commonly used
# with files, network connections, and database connections

# -----------
# it's best practice to include error handling when working with files
# try:
#     with open('wrong_path.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print('The file does not exist')

