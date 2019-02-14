#########################################
# Daniel Johnson
# Assignment 2.2
# 2/7/19
#
# Description: This program lets the user play a game of rock paper scissors with the computer.
# It also gives the option for another play once they are finished with their game.
#
# Inputs: The user must input their option to play (rock, paper, or scissors) and then tell the
# computer if they want to play again.
#
# Outputs: This outputs a welcome and instructions to the screen for the user to follow. After
# everything is input, the computer will output the results of the game and ask the user if they
# want to play again
#########################################
import random

# This prompts the user for input
print()
print("It is time to play Rock-Paper-Scissors!")
print()
print("The rules are simple: rock beats scissors, scissors beats paper, paper beats rock")
print("and when both players choose the same option nobody wins.")
print()

# These are some variables that hold the response for the player's option to play in the game
answer = ''
computer_answer = ''
play_again = 'y'
rps_dict = {1: 'r', 2: 'p', 3: 's'}

# This is a loop that keeps the player playing the game unless they choose not to at the end of the loop
while play_again == 'y':

    # This section asks the move that will be played against the computer
    while answer == '':
        answer = ''
        print("What move would you like to play against the computer? Enter \"R\", \"P\", or \"S\"")
        answer = input().lower()
        if answer == "r" or answer == "p" or answer == "s":
            break
        else:
            print("You entered an invalid answer; please enter again.")
            answer = ''
    # This generates the computer's move against the player
    computer_answer = int(random.randint(1, 3))
    computer_answer = rps_dict[computer_answer]

    # Pauses and makes sure the user is ready to see the results
    print("Press enter to see what the computer played.")
    input()

    # This goes through the possible outcomes for the game and displays the proper outcome
    print("The computer entered:", computer_answer, "\n", "\bYou entered:", answer)
    if answer == computer_answer:
        print("It was a tie!")
    elif answer == "r" and computer_answer == "p":
        print("The computer won! :(")
    elif answer == "r" and computer_answer == "s":
        print("You won! :)")
    elif answer == "p" and computer_answer == "r":
        print("You won! :)")
    elif answer == "p" and computer_answer == "s":
        print("The computer won! :(")
    elif answer == "s" and computer_answer == "p":
        print("You won! :)")
    elif answer == "s" and computer_answer == "r":
        print("The computer won! :(")
    else:
        print("Apparently something went wrong :(")

    # This section asks the player if they would like to play again and does not stop until correct input is given.
    print("Would you like to play again? Enter \"Y\" or \"N\"")
    play_again = ''
    while play_again == '':
        print()
        play_again = input().lower()
        if play_again == "y" or play_again == "n":
            answer = ''
            break
        else:
            print("You entered an invalid answer; please enter again.")
            play_again = ''

# Thanks the user for playing since they did not want to play again and the program promptly ends.
print("Thanks for playing!")
