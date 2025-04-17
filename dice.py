import random
import player
import board

def dice_roll(player):
    dice_1 = random.randint(1, 2)
    dice_2 = random.randint(1, 2)
    total = dice_1 + dice_2

    if dice_1 == dice_2:
        player.double_counter += 1
        print(f"You rolled a double {dice_1}!")
        # Move the player the number of spaces rolled
        # Carry out game logic for that space
        # Return for next role
        # Check if the player has rolled 3 doubles in a row - if so, go to jail
        if player.double_counter == 3:
            print("You rolled 3 doubles in a row! Go to jail.")
            player.double_counter = 0 # Reset the double counter
            board.go_to_jail() # Move player to jail
        else:
            print("Move", total, "spaces.") 
            dice_roll(player) # Call the function again to roll again
            
    else:
        player.double_counter = 0 # Reset the double counter if previous roll increased it
        print(f"You rolled {dice_1} and {dice_2}")
        print(f"Move {total} spaces.") 
        # Move the player the number of spaces rolled


    
