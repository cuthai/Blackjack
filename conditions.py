'''
Functions for win conditions.

Comes with the following methods: All return player_chips based on the outcome of the game
player_busts - Player's cards go over 21
player_wins - Player's card's value is greater than the dealer's
dealer_busts - Dealer's cards go over 21
dealer_wins - Dealer's card's value is greater than the player's
push - the two sides tie
'''
from chips import *

#
def player_busts(player_chips,bet):
    print("Player busts!")
    player_chips.lose_bet(bet)
    return player_chips

#
def player_wins(player_chips,bet):
    print("Player wins!")
    player_chips.win_bet(bet)
    return player_chips

#
def dealer_busts(player_chips,bet):
    print("Dealer busts!")
    player_chips.win_bet(bet)
    return player_chips

#
def dealer_wins(player_chips,bet):
    print("Dealer wins!")
    player_chips.lose_bet(bet)
    return player_chips

#
def push():
    print("Dealer and Player tie! It's a push.")
