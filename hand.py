'''
Class to define hand object

Comes with the following methods:
add_card - takes card object as a parameter and adds it to the hand
adjust_for_ace - if the value of the hand is over 21 and there is an ace, this method will reduce the ace's value from 11 to 1
'''
from card import * #import card in order to get the card object

class Hand:

    #Initialize chips given to the player. Default amount is 100 but can be added as a parameter
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    #Method to add cards to the hand. Takes a card object as a paramter. Adds the cards value to the hand
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    #Method to adjust the value of an ace in the hand if the hand's value is >21 and there is an ace
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
