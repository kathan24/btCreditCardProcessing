__author__ = 'kathan'
from luhn import *

class Card(object):
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit
        self.balance = 0
        self.is_valid = verify(number)

