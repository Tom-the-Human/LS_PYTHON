"""
Simple loan calculator. Reusing parts of my calculator program. Should work well here.
"""

import json
import locale
import os

with open('mortgage_messages.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LOCALE = locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')     # < Set US or GB here
CURRENCY = locale.localeconv()['currency_symbol']

def messages(message, locale):                  # pylint: disable=w0621
    """
    Accesses and returns output message data.
    """
    if message not in OUTPUT[locale]:           # pylint: disable=R1705
        return message      # formatted result must call messages directly

    return OUTPUT[locale][message]

def prompt(output_key):
    """
    Output formatter.
    """
    message = messages(output_key, LOCALE)
    print(f"=> {message} <=")

def is_amount_valid(number_str):
    """
    Checks if amount is valid.
    """
    if number_str in ('nan', 'inf', 'infinity'):
        return False

    try:
        float(number_str)
    except ValueError:
        return False

    if float(number_str) <= 0:
        return False

    return True

def is_apr_valid(number_str):
    """
    Checks if APR is valid.
    """
    if number_str in ('nan', 'inf', 'infinity'):
        return False

    try:
        float(number_str)
    except ValueError:
        return False

    if float(number_str) < 0:
        return False

    return True

def is_term_valid(number_str):
    """
    Checks if term length is valid.
    """
    if number_str in ('nan', 'inf', 'infinity'):
        return False

    try:
        int(number_str)
    except ValueError:
        return False

    if int(number_str) <= 0:
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

while True:

    os.system('clear')

    prompt('welcome')
    prompt('get_loan_amount')
    loan_value = input(CURRENCY)
    loan_value = loan_value.replace('$', '').replace('£', '').replace(',', '')

    while is_amount_valid(loan_value) is False:
        prompt('invalid_num')
        loan_value = input(CURRENCY)
        loan_value = loan_value.replace('$', '').replace('£', '').replace(',', '')


    loan_value = round(float(loan_value), 2)

    prompt('get_APR')
    apr = input().replace('%', '').replace(',', '')

    while is_apr_valid(apr) is False:
        prompt('invalid_num')
        apr = input()

    apr = float(apr)
    monthly_interest = apr / 100 / 12

    prompt('get_term')
    term_months = input()

    while is_term_valid(term_months) is False:
        prompt('invalid_term')
        term_months = input()

    term_months = int(term_months)

    monthly_payment = round(calc_monthly_payment(loan_value, monthly_interest, term_months), 2)
    m_p = monthly_payment   # to shorten print line
    print_results()

    prompt('again?')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break
