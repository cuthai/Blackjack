'''
Functions for player actions

Comes with the following methods:
take_bet - asks the player for a bet and returns it
hit - adds card from deck to player's hand
hit_or_stand - asks the player if they want to continue to hit or to stop
show_some - shows the player's hand and some of the dealer's hand
show_all - shows the player's hand and the dealer's hand
'''
from hand import *

#Method to ask for the player's bet. Takes the player's balance as a paramter. Returns the player's bet
def take_bet(balance):
    bet = 0
    while True:
        try:
            bet = int(input(f'How many chips would you like to bet? Balance: {balance} |'))
        except ValueError:
            print('Please enter a number.')
        else:
            if bet > balance:
                print('Bet is higher than balance. Please enter another number.')
            else:
                break
    return bet

#Method if the player wants to hit to add the card to the hand. Takes in the current deck and player's hand as parameters. add_card comes from the hand class
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#Method to ask the player if they wants to hit or stay. Takes in the current deck and player's hand as parameters.
#If the player hits, this will call the hit method. Returns true if player continues to hit, and false if the player stops.
def hit_or_stand(deck,hand):
    action = input("Would you like to hit? Enter 'y' or 'n' | ")
    if action == 'yes' or action == 'y':
        hit(deck,hand)
        if hand.value > 21:
            return False
        else:
            return True
    else:
        return False

#Method to show the player and some of dealer's hands. Only shows one card from the dealer's hand. Takes the player hand and the dealer hand as parameters
def show_some(player,dealer):
    print("Player's hand. Value: ",player.value)
    for card in player.cards:
        print(card)
    print("Dealer's hand. Value: ",dealer.cards[1].value)
    print('<card hidden>')
    print(dealer.cards[1])

#Method to show the player and all of the dealer's hands. Takes the player hand and the dealer hand as parameters
def show_all(player,dealer):
    print('Printing all Cards')
    print("Player's hand. Value: ",player.value)
    for card in player.cards:
        print(card)
    print("Dealer's hand. Value: ",dealer.value)
    for card in dealer.cards:
        print(card)