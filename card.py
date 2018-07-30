'''
Class to define card object

Come with the following methods:
print - Prints card object with Suit and Rank
'''
#Value of cards, assigned to the card itself
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    #Initialize card class with 2 attributes: suit and rank. Value is based on rank and the values dictionary
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    #Method to print out what the card is. Returns the ranks and suit of the card
    def __str__(self):
        return self.rank + ' of ' + self.suit