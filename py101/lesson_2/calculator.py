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

import os
import json


with open('calculator.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LANGUAGE = 'en'
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
    if number_str in ('nan', 'infinity'):
        return True
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def run_calculation(num1, num2, operator):
    match operator:
        case '+':
            outcome = num1 + num2
        case '-':
            outcome = num1 - num2
        case '*':
            outcome = num1 * num2
        case '/':
            if num2 == False:
                try:
                    outcome = num1 / num2
                except ZeroDivisionError:
                    outcome = 'nan (some say ∞)'               # pylint: disable=C0103
                    prompt('zero_div')
            else:
                outcome = num1 / num2
    return outcome

prompt('welcome')

while True:

    os.system('clear')

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

    outcome = run_calculation(num1, num2, operator)

    prompt(messages('result', LANGUAGE).format(outcome=outcome))

    prompt('another_calc')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break
