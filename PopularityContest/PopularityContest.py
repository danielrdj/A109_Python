#########################################
# Daniel Johnson
# Assignment 6.2
# 4/26/19
#
# Description: This program lets the user play a game that lets them guess which name was more popular in 2015
#
# Inputs: The user inputs their response to the given questions as "1" or "2" and "y" and "n" to take a guess and tell the
# program if they want to play again
#
# Outputs: This outputs a question to the use asking which name was more popular in 2015. They respond and then the
# program outputs whether or not they are correct and then displays the percentage they got correct at the end.
#########################################

import random
import BabyNames


boy_file = open("boynames2015.txt","r")
girl_file = open("girlnames2015.txt","r")
girl_list = []
boy_list = []

#############
# This method
# takes a file
# object and list
# object to add
# babyname objects
# to the list
#############
def make_name_list(file,name_list):
    first_line = True
    for line in file:
        if first_line:
            first_line = False
            continue

        temp = line.split("\n")
        temp = temp[0].split(" ")
        name_list.append(BabyNames.BabyName(temp[0], temp[1], temp[2]))


make_name_list(boy_file,boy_list)
make_name_list(girl_file,girl_list)


#loop for the names
correct = 0
count = 0
play_again = True
while play_again:
    count += 1
    rand_num_1 = random.randint(0,999)
    rand_num_2 = random.randint(0,999)

    girl = girl_list[rand_num_1]
    boy = boy_list[rand_num_2]

    girl_name = girl.name
    boy_name = boy.name

    girl_rank = girl.rank
    boy_rank = boy.rank

    girl_birth = girl.num_birth
    boy_birth = boy.num_birth

    answer = " There were " + girl_birth + " girls named " + girl_name + " and " + boy_birth + " boys named " + boy_name + " in 2015."
    response = input("In 2015, was the name " + girl_name + " (1) or " + boy_name + " (2) more popular (enter 1 or 2)? ")

    if girl > boy and response == "1":
        print("Correct!" + answer)
        correct += 1
    elif (not(girl > boy)) and response == "2":
        print("Correct!" + answer)
        correct += 1
    else:
        print("Incorrect!" + answer)

    response = input("Would you like to play again (y/n)?")
    if response.lower() == "y" or response.lower() == "yes":
        play_again = True
        print("\n")
    else:
        play_again = False
        print("You either entered No or something invalid")
        print("The percentage you guessed correctly was:", str(int(correct/count * 100)) + "%")





