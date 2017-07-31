__author__ = 'kathan'
import unittest, os
from user import User
from card import Card
from transactions import process_transactions

class TestTransactions(unittest.TestCase):

    def test1(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_file = open(dir_path + '/test_files/test1', 'r')
        transactions = input_file.read()
        input_file.close()

        transactions = transactions.split('\n')

        process_transactions(transactions)