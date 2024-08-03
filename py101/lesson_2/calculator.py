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

with open('calculator.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LANGUAGE = 'es'
#           ^^ change this value to select language

def messages(message, lang):
    """
    Accesses and returns output message data.
    """
    if message not in OUTPUT[lang]:         # pylint: disable=R1705
        return message      # formatted result must call messages directly
    else:
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

prompt('welcome')

while True:

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
            outcome = num1 + num2
        case '-':
            outcome = num1 - num2
        case '*':
            outcome = num1 * num2
        case '/':
            if num2 == 0.0:
                try:
                    outcome = num1 / num2
                except ZeroDivisionError:
                    outcome = None               # pylint: disable=C0103
                    prompt('zero_div')
            else:
                outcome = num1 / num2

    prompt(messages('result', LANGUAGE).format(outcome=outcome))

    prompt('another_calc')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break
