'''
Class to define chips

Comes with the following methods:
win_bet - adds the bet to the total chip count
lost_bet - removes the bet from the total chip count
'''
class Chips:

    #Initialize chips given to the player. Default amount is 100 but can be added as a parameter
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    #Method to add the bet if the player won
    def win_bet(self,bet):
        self.total += bet

    #Method to remove the bet if the player lost
    def lose_bet(self,bet):
        self.total -= bet