'''
Script to run the Card Game: Blackjack
'''
#Import Class objects and methods
from card import *
from deck import *
from hand import *
from chips import *
from actions import *
from conditions import *

#Initial message
player_chips = Chips()
print('Welcome to Blackjack! The goal is to get the value of your cards closer to 21 than the dealer without going over. Face cards = 10, Ace = 11 or 1')

while True:
    #Initialize variables.
    playing = True
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    bet = take_bet(player_chips.total)

    #Deal cards to each hand
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Actual game loop
    while playing:
        show_some(player_hand,dealer_hand)
        playing = hit_or_stand(deck,player_hand)

    #Dealer game loop
    show_all(player_hand,dealer_hand)
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips,bet)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_chips,bet)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_chips,bet)
        else:
            push()
    else:
        player_busts(player_chips,bet)

    #Inform Player of their chips total 
    print("Player's winnings stand at: ",player_chips.total)
        
    # Ask to play again
    if player_chips.total == 0:
        print('No more chips left! You Lose!')
        break
    else:
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' | ")
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break