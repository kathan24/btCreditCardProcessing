__author__ = 'kathan'
import os, sys
from user import User
import fileinput


def process_transactions(transactions):
    user_accounts = {}

    for transaction in transactions:
        user_account = transaction.split(' ')

        # check for the valid command
        if user_account[0].lower() == 'add':
            card_limit = int(user_account[3].replace("$", ""))
            user_accounts[user_account[1].lower()] = User(name=user_account[1], card_number=user_account[2], card_limit=card_limit)
        elif user_account[0].lower() == 'charge':
            user = user_accounts[user_account[1].lower()]
            charge = int(user_account[2].replace("$", ""))
            if charge + user.card.balance <= user.card.limit and user.card.is_valid:
                user.card.balance += charge
        elif user_account[0].lower() == 'credit':
            user = user_accounts[user_account[1].lower()]
            credit = int(user_account[2].replace("$", ""))

            if user.card.is_valid:
                user.card.balance -= credit

    for key in sorted(user_accounts):
        if user_accounts[key].card.is_valid:
            print "{0}: ${1}".format(user_accounts[key].name, user_accounts[key].card.balance)
        else:
            print "{0}: error".format(user_accounts[key].name)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    argument = sys.argv
    transactions = []

    if len(argument) > 1:
        file_path = sys.argv

        input_file = open(dir_path + '/' + file_path[1], 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')
    else:
        for line in fileinput.input():
            transactions.append(line)

    if transactions:
        process_transactions(transactions)


""" questions
1. can one user have multiple cards ?
2. what if the total charge is less than limit but increasing the charge it increases the total charge more than limit. is it valid ?
like
Add Tom 4111111111111111 $1000
Charge Tom $500
Charge Tom $400
Charge Tom $300    // is this valid as charge will be 1200 which is more than limit
3. will file name have the path mentioned or should i assume that the file is in the project directory?
4. what if user has one card. another card is added by the same user. should i overwrite?
"""