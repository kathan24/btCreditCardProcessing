__author__ = 'kathan'
import os, sys
from user import User
import fileinput

USER_ACCOUNTS = {}

def process_transactions(transactions):
    """
    :param transactions: list of transaction from
    :return: summary of users
    """
    """
    :param transactions:
    :return:
    """
    USER_ACCOUNTS.clear()

    summary = []

    for transaction in transactions:
        user_account = transaction.split(' ')

        if user_account[0].lower() == 'add':
            card_limit = int(user_account[3].replace("$", ""))

            if not USER_ACCOUNTS.get(user_account[1].lower()):
                USER_ACCOUNTS[user_account[1].lower()] = User(name=user_account[1], card_number=user_account[2], card_limit=card_limit)

        elif user_account[0].lower() == 'charge' and USER_ACCOUNTS.get(user_account[1].lower()):
            user = USER_ACCOUNTS[user_account[1].lower()]
            charge = int(user_account[2].replace("$", ""))

            if charge + user.card.balance <= user.card.limit and user.card.is_valid:
                user.card.balance += charge

        elif user_account[0].lower() == 'credit' and USER_ACCOUNTS.get(user_account[1].lower()):
            user = USER_ACCOUNTS[user_account[1].lower()]
            credit = int(user_account[2].replace("$", ""))

            if user.card.is_valid:
                user.card.balance -= credit

    for key in sorted(USER_ACCOUNTS):
        if USER_ACCOUNTS[key].card.is_valid:
            summary.append("{0}: ${1}".format(USER_ACCOUNTS[key].name, USER_ACCOUNTS[key].card.balance))
        else:
            summary.append("{0}: error".format(USER_ACCOUNTS[key].name))

    return summary


def get_user_balance(user):
    """
    :param user: User name to get the balance
    :return: Balance if user is present and card is valid
    """
    if not user or not USER_ACCOUNTS.get(user.lower()):
        return
    else:
        user = USER_ACCOUNTS.get(user.lower())

        if user.card.is_valid:
            return user.card.balance
        else:
            return


if __name__ == "__main__":
    argument = sys.argv
    transactions = []

    if len(argument) > 1:
        file_path = sys.argv

        input_file = open(file_path[1], 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')
    else:
        for transaction in fileinput.input():
            transactions.append(transaction)

    if transactions:
        summary = process_transactions(transactions)
        for user_summary in summary:
            print user_summary
