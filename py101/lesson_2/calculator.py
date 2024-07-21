# get first and second numbers
# ask user for operation to perform
# perform operation on the numbers
# print the result to the terminal

print('Welcome to Calculator!')

num1 = int(input("What's the first number?\n"))
num2 = int(input("What's the second number?\n"))

print("Enter '+' to add, '-' to subtract, '*' to multiply, or '/' to divide.")
operator = input()

result = 0

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
    case _:
        print('Invalid input. Please start over.')

print(f'Result: {result}')