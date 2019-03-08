# ########################################
# Daniel Johnson
# Assignment 3.1
# 2/21/2019
#
# Description: This code simulates a ball bouncing
#
# Inputs: The user inputs an initial velocity for the ball to be thrown directly up
#
# Outputs: This program outputs the height of the ball depending on the user's input velocity
# and ends one second after the fifth bounce
#
# ########################################
bounced_tf = False #Tells code if ball bounced
bounce_number = 0 #holds bounce number
time = 0 #holds time in seconds
velocity = 0.0 #holds value of velocity
height = 0.0 #holds value of height


#Makes sure that the value entered is not 0 or negative
while velocity <= 0:
    velocity = int(input("Enter the initial velocity of the ball: "))

#loops until 5 bounces are registered
while bounce_number < 5:
    if bounced_tf:
        #applies bounce requirements
        bounce_number += 1
        height *= -0.5
        velocity *= -0.5
        velocity -= 32*1.5
        #prints bounce
        print("Bounce", bounce_number)
        bounced_tf = False

#loops until the height becomes less than or equal to 0
    while height >= 0:
        #prints time and height
        print("Time:", time, "Height:", height)
        height += velocity
        #applies gravity
        velocity -= 32
        time += 1
        if bounce_number == 5:
            SystemExit #exits 1 timestamp after the 5th bounce
    bounced_tf = True
