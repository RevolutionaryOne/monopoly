'''This is a text based monopoly game based on the Falmouth version of Monopoly. 
During setup the player can select a range of game options, standard rules, 
standard rules less the auction each turn rule and the final option is to collect fines/taxes into a pot that can be won if 
a player lands on free parking.'''

import random
import board
import player
import ascii_art

# Print the main menu ASCII art
ascii_art.monopoly_ascii()

player_name = input("Please enter your name: ")
print("\n")
print("Welcome to Monopoly, " + player_name + "!")
print("\n")
number_of_players = int(input("Please enter the number of players (2-6): "))
print("\n")
print(f"Great! You have selected {number_of_players} players.")
print("\n")

dice_1 = new.random.randint(1, 6)
dice_2 = new.random.randint(1, 6)

dice_roll = dice_1 + dice_2

print(f"You rolled a {dice_1} and a {dice_2}.")