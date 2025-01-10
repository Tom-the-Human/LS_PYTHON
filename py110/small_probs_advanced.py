"""
1
P
A 3x3 matrix can be represented by a list of nested lists: an outer list that
contains three sub-lists that each contain three elements. 
For example, the 3x3 matrix shown below:
1  5  8
4  7  2
3  9  6
is represented by the following list of lists:
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
The transpose of a 3x3 matrix is the matrix that results from exchanging the 
rows and columns of the original matrix. For example, the transposition of the 
matrix shown above is:
1  4  3
5  7  9
8  2  6
Write a function that takes a list of lists that represents a 3x3 matrix and 
returns the transpose of the matrix. You should implement the function on your 
own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a 
new matrix and leave the input matrix list unchanged.

1 take a list of lists
2 return a NEW list of lists with the rows and columns transposed as in the 
    example
3 do not modify the input list

E
I can see that all of the elements at a given nested index i.e. list[x][0]
end up in the same sublist, i.e. list[0], so that may be a way to get some
spaghetti off the plate.

D
2D list input
2d list output
might implement some additional lists, or maybe a dict?
something like
for sub in list:
    for idx in range(len(sub)):
        dict[sub[idx]] = idx

would populate a dictionary so that the list elements are keys and the values are
the index of the sublist they should end up in. That's good! But maybe it's
better if instead, the dict is set up like idx: [num at idx for sub in list]

A
- get a dict of num: idx in sublist
    for sub in list:
    for idx in range(len(sub)):
        dict[sub[idx]] = idx

- make new list with values determining which sublist the num should be in
    new list = 

- return new list

Didn't do it in 20 mins, and had help from ChatGPT, but got there without too
much heartache. I see many of the other LS students' solutions use only list
comprehensions. Their list comprehenshions look a lot like the one I imbedded in
my dict comprehension. The dict works, but is perhaps not the most 
strightforward approach.
"""
# def transpose(matrix):
#     trans = {idx: [sub[idx] for sub in matrix] for idx in range(len(matrix))}

#     return list(trans.values())

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# new_matrix = transpose(matrix)

# print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
# print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True


"""
2
P
In the previous exercise, you wrote a function that transposed a 3x3 matrix 
represented by a list of lists.

Matrix transposes are not limited to 3x3 matrices, or even square matrices. 
Any matrix can be transposed simply by switching columns with rows.

Modify your transpose function from the previous exercise so that it works 
with any MxN matrix with at least one row and one column.

1 take a list of lists
2 return a NEW list of lists with the rows and columns transposed as in the 
    example
3 do not modify the input list
4 make it work regardless of list length or nested list length

E
Examples show single row matrices, single column matrixes, 
single element matrices, as well as longer, non-square matrices. 

D
List in
List out
Can be done other ways, but I'll stick with the dict approach that worked before

A
modify previous function to be "squareness-agnostic"

s
might help to break out to for loops and then refactor to comprehension

for idx in range(len(matrix)):      # for index of each row
    [row[idx] for row in matrix]    # get at item at same index IN each row
    if idx < len(row)               # should help if columns longer than rows

Wow, I don't think I learned anything from this since I mostly copied from
ChatGPT. My attempt to reason through took almost the whole time and then I 
ended up trying an approach that GPT gave in response to a prompt I worded badly.
Only to think a bit more and realize that the previous response Chat GPT gave 
(but I modified) would solve this problem. I think the other solution I was given
MIGHT work for a matrix where the rows have different lengths, but am not sure.
"""
# def transpose(matrix):
#     # trans = {
#     #         idx: [row[idx] for row in matrix if idx < len(row)] 
#     #         for idx in range(max(len(row)
#     #         for row in matrix))
#     #         }

#     trans = {idx: [sub[idx] for sub in matrix] for idx in range(len(matrix[0]))}

#     return list(trans.values())


# # All of these examples should print True
# print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
# print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
# print(transpose([[1]]) == [[1]])

# matrix_3_by_5 = [
#     [1, 2, 3, 4, 5],
#     [4, 3, 2, 1, 0],
#     [3, 7, 8, 6, 2],
# ]
# expected_result = [
#     [1, 4, 3],
#     [2, 3, 7],
#     [3, 2, 8],
#     [4, 1, 6],
#     [5, 0, 2],
# ]

# print(transpose(matrix_3_by_5) == expected_result)

"""
3
P
90 degree rotation. Similar to above problems, but 
1  5  8
4  7  2
3  9  6
should instead become
3  4  1
9  7  5
6  2  8
So, we're rotating clockwise, i.e. row 0 becomes column 2, 
column 2 becomes row 2, row 2 becomes column 0, column 0 become row 0. 
The center element of a square with an odd number of rows and columns 
would not move, whereas there is no specific center of any other type of matrix. 

E
Confirms my understanding as stated above, but I am still not sure how to
effectively code this. Something like `row_len, col_len = col_len, row_len`
may be helpful. Maybe not. What is true about this for sure? The above is true
for the result, but is it actually helpful to code it that way? Maybe.
One thing I see is that elements in row[0] will become the elements in the last
column, so it's like `
for row in matrix:
    for num in row:
        new_mtrx.append([num])
        That's not right. I need a break and some food.

"""
def rotate90(matrix):

    pass


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)