# ########################################
# Daniel Johnson
# Assignment 3.2
# 2/21/2019
#
# Description: This program simulates a certain number of dice rolls depending on user input
#
# Inputs: This program takes a number as input to simulate that many dice rolls
#
# Outputs: This outputs a histogram of a number of simulated dice rolls
#
# ########################################
import random
random.seed(109)
#holds amount of dice rolls user wants
dice_rolls = 0

#holds amount of times each amount was rolled
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0]



#takes in user's choice for amount of dice rolls
while dice_rolls <= 0:
    dice_rolls = int(input("How many times do you want to roll the dice? "))



#calculates the random rolls and puts the amounts into their spots in the list
for x in range(dice_rolls):
    dice_roll_1 = random.randint(1,6)
    dice_roll_2 = random.randint(1,6)
    dice_sum = dice_roll_1 + dice_roll_2

    nums[dice_sum] += 1

#this area prints the dice histogram
print("Distribution for", dice_rolls, "simulated dice rolls:")
for x in range(2,13):
    #this accounts for the different spacing when there are 2 digits
    if x >= 10:
        print(x, "s: ", sep='', end='')
    #alternate spacing
    else:
        print(x, "s:  ", sep = '', end = '')
    #part that prints stars
    for y in range(nums[x]):
        print("*", end = '')
    print()