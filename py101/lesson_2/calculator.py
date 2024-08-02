"""
calculator.py

I followed the directions mostly, but took opportunities 
to experiment and try variations on the suggested code. 
In the end, much of code is what is suggested, but there 
are differences. 

Function docstrings added to satisfy Pylint.
Why does Pylint think the variable 'result' is meant to be a constant? 
Found a code to disable the invalid-name flag.
"""

import json

with open('calculator.json', 'r') as file:
    OUTPUT = json.load(file)

def messages(message, lang='es'):
    """
    Accesses and returns output message data.
    """
    return OUTPUT[lang][message]

def prompt(output_key):
    """
    Output formatter.
    """
    message = messages(output_key, LANGUAGE)
    print(f"=> {message} <=")

def invalid_num(number_str):
    """
    Checks if number is valid.
    """
    try:
        float(number_str)
    except ValueError:
        return True

    return False

LANGUAGE = 'es'

while True:
    prompt('welcome')
    prompt('get_first_num')
    num1 = input()

    while invalid_num(num1):
        prompt('invalid_num')
        num1 = input()

    num1 = float(num1)

    prompt('get_second_num')
    num2 = input()

    while invalid_num(num2):
        prompt('invalid_num')
        num2 = input()

    num2 = float(num2)

    prompt('get_operator')
    operator = input()

    while operator not in ['+', '-', '*', '/']:
        prompt('invalid_operator')
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
                    result = None #pylint: disable=C0103
                    prompt('zero_div')
            else:
                result = num1 / num2

#can't get fstring to work without assigning at runtime FIX THIS
    OUTPUT['en']['result'] = f'Result: {result}' 
    OUTPUT['es']['result'] = f'El resultado: {result}'
    prompt('result') 

    prompt('another_calc')
    restart = input()
    if restart and restart[0].lower() != 'y':
        prompt('goodbye')
        break
