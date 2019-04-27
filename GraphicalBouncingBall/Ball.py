#########################################
# Daniel Johnson
# Assignment 6.2
# 4/26/19
#
# Description: This program simulates a bouncing ball
#
# Inputs: There is no user input
#
# Outputs: This outputs a graphical ball bouncing
#
# Resources used:
# https://stackoverflow.com/questions/2679418/how-to-get-the-coordinates-of-an-object-in-a-tkinter-canvas
# Frank Witmer's example code
#########################################



import random
import tkinter
class Ball:
    def __init__(self, canvas, color, size):
        self.color = color
        self.velocity = random.randint(5, 10)
        self.size = size

        canvas.update()
        #print(canvas.winfo_width())
        self.location_x = random.randint(40, canvas.winfo_width() - 40)
        self.location_y = random.randint(40, canvas.winfo_height() - 40)

        #self.location_x = 100
        #self.location_y = 20

        self.canvasID = canvas.create_oval(self.location_x, self.location_y, self.location_x + size, self.location_y - size, fill=color, width=1)

    def update_location(self, canvas):
        #Adjusts height of the ball according to gravity
        self.location_y += self.velocity
        self.velocity += 32

        #Checks to see if the ball has bounced
        if self.location_y > canvas.winfo_height():
            self.location_y = (canvas.winfo_height()) - ((self.location_y - (canvas.winfo_height())) * 0.5)
            self.velocity = -0.5 * self.velocity
            self.velocity += 32*1.5

            #Stops ball at the bottom after it loses enough velocity and height
            if 32 > self.velocity > 0 and self.location_y > canvas.winfo_height():
                self.location_y = 500
                self.velocity = 0

        #print("previous height:", 500-self.location_y_previous)


    def get_delta_y(self,canvas):
        return self.location_y - canvas.coords(self.canvasID)[3]

    def get_canvasID(self):
        return self.canvasID
