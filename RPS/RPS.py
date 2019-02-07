import random


print()
print("It is time to play rock paper scissors!")
print()
print("The rules are simple: rock beats scissors, scissors beats paper, paper beats rock")
print("and when both players choose the same option nobody wins.")
print()

answer = ''
computer_answer = ''
play_again = 'y'
while play_again == 'y':
    while answer == '':
        answer = ''
        print("What move would you like to play against the computer? Enter \"R\", \"P\", or \"S\"")
        answer = input().lower()
        if answer == "r" or answer == "p" or answer == "s":
            break
        else:
            print("You entered an invalid answer; please enter again.")
            answer = ''
    computer_answer = int(random.randint(1, 3))
    if computer_answer == 1:
        computer_answer = 'r'
    elif computer_answer == 2:
        computer_answer = 'p'
    elif computer_answer == 3:
        computer_answer = 's'

    print("Press enter to see what the computer played.")
    input()
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
print("Thanks for playing!")
