# GET loan amount, APR, term
# calculate and SET monthly interest rate (APR/12), loan term in months
# monthly_payment = loan_value * (monthly_rate / (1 - (1 + monthly_rate) ** (-term_months)))
# print payment amount as dollars and cents ($xx.xx)
# use Pylint
# consider UX (enter 5% interest as '5' rather than '.05')
# name varaibles carefully, i.e. monthly vs. yearly
# edge cases - no-interest loans, non-integer payment periods, 
# negative numbers, other nonsense inputs

"""
Reusing parts of my calculator program. Should work well here.

"""

import os
import json

with open('mortgage_messages.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

LOCALE = 'en_US.UTF-8'

def messages(message, locale):
    """
    Accesses and returns output message data.
    """
    if message not in OUTPUT[locale]:         # pylint: disable=R1705
        return message      # formatted result must call messages directly
    else:
        return OUTPUT[locale][message]

def prompt(output_key):
    """
    Output formatter.
    """
    message = messages(output_key, LOCALE)
    print(f"=> {message} <=")

def is_valid_amount(number_str):
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

def is_valid_apr(number_str):
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

def is_valid_term(number_str):
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

def calc_monthly_payment(loan_value, monthly_rate, term_months):
    """
    Calculates monthly payment.
    """
    if monthly_rate == 0:
        return loan_value / term_months
    else:
        return loan_value * ((monthly_rate / 100) / (1 - (1 + monthly_rate) ** (-term_months)))

while True:

    os.system('clear')

    prompt('get_loan_amount')
    loan_value = input(messages('currency_symbol', LOCALE))
    loan_value = loan_value.replace('$', '').replace('£', '').replace(',', '')

    while is_valid_amount(loan_value) == False:
        prompt('invalid_num') 
        loan_value = input(messages('currency_symbol', LOCALE))
        loan_value = loan_value.replace('$', '').replace('£', '').replace(',', '')


    loan_value = round(float(loan_value), 2)

    prompt('get_APR')
    apr = input().replace('%', '').replace(',', '')

    while is_valid_apr(apr) == False: 
        prompt('invalid_num')
        apr = input()

    apr = float(apr)
    monthly_rate = apr / 12

    prompt('get_term')
    term_months = input()

    while is_valid_term(term_months) == False:
        prompt('invalid_term')
        term_months = input()

    term_months = int(term_months)

    monthly_payment = round(calc_monthly_payment(loan_value, monthly_rate, term_months), 2)
    prompt(messages('result', LOCALE).format(monthly_payment=monthly_payment))
    # prompt('Monthly payment placeholder.')
    prompt('again?')
    restart = input()
    if restart and restart[0].lower() not in ('y', 's'):
        prompt('goodbye')
        break