__author__ = 'kathan'
import unittest, os
from transactions import process_transactions, get_user_balance


class TestTransactions(unittest.TestCase):

    def test_print_summary(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test1.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        summary = process_transactions(transactions)

        expected = [
            'Lisa: $-100',
            'Tom: $600'
        ]

        self.assertEquals(summary, expected)

    def test_user_account(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test1.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)

        self.assertEquals(get_user_balance('Lisa'), -100)
        self.assertEquals(get_user_balance('toM'), 600)

    def test_ignore_charge(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test2.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)

        self.assertEquals(get_user_balance('Lisa'), -100)
        self.assertEquals(get_user_balance('toM'), 501)

    def test_charging_and_crediting_before_adding_card(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test3.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)

        self.assertEquals(get_user_balance('Lisa'), -100)
        self.assertEquals(get_user_balance('toM'), 600)

    def test_duplicate_user(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test4.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)

        self.assertEquals(get_user_balance('Lisa'), -300)
        self.assertEquals(get_user_balance('toM'), 800)

    def test_invalid_card_charge(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test5.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)

        self.assertEquals(get_user_balance('Lisa'), -100)
        self.assertEquals(get_user_balance('quincy'), None)
        self.assertEquals(get_user_balance('toM'), 501)

    def test_invalid_card_summary(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test5.txt', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        summary = process_transactions(transactions)

        expected = [
            'Lisa: $-100',
            'Quincy: error',
            'Tom: $501'
        ]

        self.assertEquals(summary, expected)
