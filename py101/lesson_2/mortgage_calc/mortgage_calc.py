"""
Simple loan calculator. Reusing parts of my first calculator program with
significant modification. Uses locale codes to automatically support
different currency symbols as well as languages whose translations are added
to the json OUTPUT dictionary.
"""

import json
import locale
import os

# Load messages and set locale
with open('mortgage_messages.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LOCALE = locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')     # < Set en_US, en_GB, or es_ES
CURRENCY = locale.localeconv()['currency_symbol']

def messages(message, locale):                  # pylint: disable=w0621
    """
    Accesses and returns message from OUTPUT dictionary. 
    Alternatively returns input strings if message is not found 
    to be a dictionary key.
    """
    if message not in OUTPUT[locale]:           # pylint: disable=R1705
        return message      # formatted result must call messages directly

    return OUTPUT[locale][message]

def prompt(output_key):
    """
    Format prompts output to user.
    """
    message = messages(output_key, LOCALE)
    print(f"=> {message} <=")

def input_handler(input_str, input_type):
    """
    Runs all input through cleaning and validation, prompting again
    if necessary until input is suitable for calculation. Using 3 different
    loops to support 3 custom prompts. Explored collapsing them to single
    while loop with embedded if statements, but that was hard to read
    and not much shorter.
    """
    input_str = clean_input(input_str)

    if input_type == 'loan_value':
        while is_valid(input_str, 'loan_value') is False:
            prompt('invalid_num')
            input_str = clean_input(input(CURRENCY))

        input_str = round(float(input_str), 2)  # Currency formatting w/ 2 decimal places

    elif input_type == 'apr':
        while is_valid(input_str, 'apr') is False:
            prompt('invalid_num')
            input_str = clean_input(input())

        input_str = float(input_str)

    elif input_type == 'term_months':
        while is_valid(input_str, 'term_months') is False:
            prompt('invalid_term')
            input_str = clean_input(input())

        input_str = int(input_str)  # Whole months only

    return input_str

def clean_input(input_num):
    """
    Removes common disallowed characters from input string for better UX.
    """
    return input_num.replace(CURRENCY, '').replace(',', '').replace('%', '')

def is_valid(number_str, input_type):
    """
    Checks input for validity. Returns True only if number_str will 
    produce useful calculation results.
    """
    if number_str in ('nan', 'inf', 'infinity'):
        return False

    if input_type == 'term_months':
        try:
            int(number_str)
        except ValueError:
            return False
    else:
        try:
            float(number_str)
        except ValueError:
            return False

    if input_type != 'apr' and float(number_str) <= 0:
        return False

    if input_type == 'apr' and float(number_str) < 0:
        return False

    return True

def calc_monthly_payment(loan_amount, monthly_rate, months):
    """
    Calculates monthly payment.
    """
    if monthly_rate == 0:
        return loan_amount / months

    return loan_amount * ((monthly_rate) / (1 - (1 + monthly_rate) ** (-months)))

def print_results():
    """
    Prints results to terminal.
    """
    prompt(messages('print_amount', LOCALE).format(CURRENCY=CURRENCY, loan_value=loan_value))
    prompt(messages('print_apr', LOCALE).format(apr=apr))
    prompt(messages('print_term', LOCALE).format(term_months=term_months))
    prompt(messages('print_result', LOCALE).format(CURRENCY=CURRENCY, monthly_pay=m_p))

# Main loop
while True:

    os.system('clear')

    prompt('welcome')

    prompt('get_loan_amount')
    loan_value = input_handler(input(CURRENCY), 'loan_value')

    prompt('get_APR')
    apr = input_handler(input(), 'apr')

    monthly_interest = apr / 100 / 12   # Convert APR to monthly rate

    prompt('get_term')
    term_months = input_handler(input(), 'term_months')

    monthly_payment = round(calc_monthly_payment(loan_value, monthly_interest, term_months), 2)
    m_p = monthly_payment   # To shorten print line
    print_results()

    prompt('again?')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break
