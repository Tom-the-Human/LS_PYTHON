"""
Simple loan calculator. Reusing parts of my first calculator program with
significant modification. 
"""

import json
import locale
import os

# Load messages and set locale
with open('mortgage_messages.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LOCALE = locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')     # < Set US or GB here
CURRENCY = locale.localeconv()['currency_symbol']

def messages(message, locale):                  # pylint: disable=w0621
    """
    Accesses and returns output message from OUTPUT dictionary. 
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

# def input_handler(input_str):
#     """
#     Runs all input through cleaning and validation, prompting again
#     if necessary until input is suitable for calculation.
#     """
#     input_str = clean_input(input_str)

#     if input_str is loan_value:
#         while is_valid(loan_value) is False:
#             prompt('invalid_num')
#             loan_value = input(CURRENCY)
#             loan_value = clean_input(loan_value)

#     if input_str is apr:
#         while is_valid(apr) is False:
#             prompt('invalid_num')
#             apr = input()
#             apr = clean_input(apr)

#     if input_str is term_months:
#         while is_valid(term_months) is False:
#             prompt('invalid_term')
#             term_months = input()
#             term_months = clean_input(term_months)
    
    # shell function to contain input cleaning and validation including while loop

def clean_input(input_num):
    """
    Removes common disallowed characters from input string for better UX.
    """
    return input_num.replace(CURRENCY, '').replace(',', '').replace('%', '')

def is_valid(number_str):
    """
    Checks input for validity. Returns True only if number_str will 
    produce useful results.
    """
    if number_str in ('nan', 'inf', 'infinity'):
        return False

    try:
        float(number_str)
    except ValueError:
        return False

    if number_str is apr:
        if float(number_str) < 0:
            return False
    elif float(number_str) <= 0:
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

    loan_value = 0      # pylint: disable=C0103
    apr = 0             # pylint: disable=C0103
    term_months = 0     # pylint: disable=C0103
    # non-constant variables initialized to prevent crash when
    # calling input_handler()

    os.system('clear')

    prompt('welcome')

    prompt('get_loan_amount')
    loan_value = input(CURRENCY)
    # loan_value = input_handler(loan_value)

    loan_value = clean_input(loan_value)

    while is_valid(loan_value) is False:
        prompt('invalid_num')
        loan_value = input(CURRENCY)
        loan_value = clean_input(loan_value)

    loan_value = round(float(loan_value), 2)    # Currency formatting w/ 2 decimal places

    prompt('get_APR')
    apr = input()
    apr = clean_input(apr)

    while is_valid(apr) is False:
        prompt('invalid_num')
        apr = input()
        apr = clean_input(apr)

    apr = float(apr)
    monthly_interest = apr / 100 / 12   # Convert APR percentage to monthly rate

    prompt('get_term')
    term_months = input()
    term_months = clean_input(term_months)

    while is_valid(term_months) is False:
        prompt('invalid_term')
        term_months = input()
        term_months = clean_input(term_months)

    term_months = int(term_months)  # Whole months only

    monthly_payment = round(calc_monthly_payment(loan_value, monthly_interest, term_months), 2)
    m_p = monthly_payment   # To shorten print line
    print_results()

    prompt('again?')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break
