import board
import player
import ascii_art
import dice
'''This is a text based monopoly game based on the Falmouth version of Monopoly. 
During setup the player can select a range of game options, standard rules, 
standard rules less the auction each turn rule and the final option is to collect fines/taxes into a pot that can be won if 
a player lands on free parking.'''

# Print the main menu ASCII art
ascii_art.monopoly_ascii()

# Test player
p1 = player.Player("Lee", "Car")

# Test dice roll function
dice.dice_roll(p1)