# Question 1
numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop()
print(numbers)
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

# Question 5
def is_color_valid(color):
    return (color == "blue" or color == "green")
print(is_color_valid("blue grey"))
