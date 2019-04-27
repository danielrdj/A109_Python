import tkinter
import random
import Ball

#creates window
window = tkinter.Tk()
window.geometry('+%d+%d' % (25,25)) # set location of window
#height and width
wdth = 500
hght = 500
window.geometry('%dx%d' % (wdth, hght)) # set window width & height
window.title("Bouncing Balls")
canvas = tkinter.Canvas(window, width=wdth, height=hght, bg="white")
canvas.pack()





#moves the balls by calling a method within their class
def move_ball(b):
    b.update_location(canvas)
    canvas.move(b.get_canvasID(), 0, b.get_delta_y(canvas))
    window.after(300, move_ball, b)






#Creates balls
ball1 = Ball.Ball(canvas, "blue", random.randint(10, 60))
ball2 = Ball.Ball(canvas, "red", random.randint(10,60))
#Moves balls
window.after(300, move_ball, ball1)
window.after(300, move_ball, ball2)




window.mainloop()