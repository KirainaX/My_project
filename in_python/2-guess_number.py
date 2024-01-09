# Import the 'random' module to generate random numbers
import random

# Define a function for a number guessing game
def guess_number_game():
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Get the player's initial guess
    player_guess = input("==> Enter a number between 1 and 10: ")

    # Continue the game until the player makes a correct guess or decides to exit
    while player_guess:
        
        # Check if the input is a digit
        if player_guess.isdigit():
            player_guess = int(player_guess)
        else:
            # Prompt the user to enter a valid number if the input is not a digit
            print("")
            player_guess = input("==> You didn't enter a number between 1 and 10: ")

        # Check if the entered number is within the valid range
        if 10 < int(player_guess):
            print("")
            player_guess = input("==> You didn't enter a number between 1 and 10: ")
        elif 1 > int(player_guess):
            print("")
            player_guess = input("==> You didn't enter a number between 1 and 10: ")
        elif player_guess == random_number:
            # If the player guesses the correct number, break out of the loop and print a success message
            print("")
            print("==> Well done, you guessed the correct number :)")
            break
        else:
            # If the guess is incorrect, print a failure message and break out of the loop
            print("")
            print("==> You did not guess the correct number :(")
            print("The random number is {}\nThe number you entered is {}".format(random_number, player_guess))
            break

# Start the game
start = guess_number_game()

# Define a list of valid yes/no responses
listyn = ['y', "yes", 'n', "no"]

# Ask the player if they want to play again
print("")
player_chose = input("==> Do you want to guess again?\n'y' for Yes and 'n' for No: ")
player_chose = player_chose.lower()

# Continue asking the player if they want to play again until a valid response is received
while True:
    print("")
    if player_chose not in listyn:
        # Prompt the user to enter a valid response if it's not in the list
        player_chose = input("==> please enter 'y' for Yes and 'n' for No: ")
    elif player_chose in listyn[0:2]:
        # If the player wants to play again, call the game function and ask again
        guess_number_game()
        print("")
        player_chose = input("==> Do you want to guess again?\n'y' for Yes and 'n' for No: ")
        player_chose = player_chose.lower()
    elif player_chose in listyn[2:]:
        # If the player chooses not to play again, exit the loop
        break
