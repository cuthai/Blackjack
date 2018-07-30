'''
Class to define deck object

Comes with the following methods:
print - Print count of cards in deck and lists the cards in the deck
shuffle - Shuffles the deck in random orders
deal - Pops out a card from the deck, removing it, and returns it
'''
import random #for shuffle method
from card import * #import card to get the card object

#Standard card suits and ranks
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:

    #Initialize deck class with 2 attributes: suit and rank, based on the given lists above
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    #Method to print out what cards are in the deck. Returns the Deck count and list of cards
    def __str__(self):
        deck_comp = ''
        count = 0
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
            count += 1
        return 'The deck has: ' + str(count) + ' cards' + deck_comp

    #Method to shuffle deck
    def shuffle(self):
        random.shuffle(self.deck)

    #Method to deal a card from the deck. Returns a card object
    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card