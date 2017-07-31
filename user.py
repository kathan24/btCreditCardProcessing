__author__ = 'kathan'

from card import Card

class User(object):

    def __init__(self, name, card_number, card_limit):
        self.name = name
        self.card = Card(number=card_number, limit=card_limit)
