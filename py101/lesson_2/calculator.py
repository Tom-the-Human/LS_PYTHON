"""
calculator.py

I followed the directions mostly, but took opportunities 
to experiment and try variations on the suggested code. 
In the end, much of code is what is suggested, but there 
are differences. Most notably I decided to use floats rather 
than ints because I think a calculator that can only handle 
whole numbers lacks utility. 

Function docstrings only added to satisfy Pylint.
Why does Pylint think the variable 'result' is meant to be a constant?
"""

def prompt(message):
    """
    Output formatter.
    """
    print(f"=> {message} <=")

def invalid_number(number_str):
    """
    Checks if number is valid.
    """
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')
prompt("What's the first number?")
num1 = input()

while invalid_number(num1):
    prompt("Hmm ... that doesn't look right. Please enter a valid number.")
    num1 = input()

num1 = float(num1)

prompt("What's the second number?")
num2 = input()

while invalid_number(num2):
    prompt("Hmm ... that doesn't look right. Please enter a valid number.")
    num2 = input()

num2 = float(num2)

prompt("Enter '+' to add, '-' to subtract, '*' to multiply, or '/' to divide.")
operator = input()

while operator not in ['+', '-', '*', '/']:
    prompt('Please choose a valid operator: +, -, *, or /!')
    operator = input()

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0.0:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                result = None
                prompt("Cannot divide by zero!")
        else:
            result = num1 / num2

prompt(f'Result: {result}')
