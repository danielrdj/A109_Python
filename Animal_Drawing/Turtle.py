#########################################
# Daniel Johnson
# Assignment 2.1
# 2/7/19
#
# Description: This program draws a turtle using tkinter.
#
# Inputs: There is no user input.
#
# Outputs: This outputs a picture of a turtle
#########################################
import tkinter
root = tkinter.Tk()

# Size of the window.
wdth = 500
hght = 500

# tkinter setup stuff
root.geometry('%dx%d' % (wdth, hght))  # set window width & height
canvas = tkinter.Canvas(root, width=wdth, height=hght)
canvas.pack()

# Head and drawn below
canvas.create_oval(200, 50, 300, 125, outline="black", fill="light green")

# Eyes drawn below
canvas.create_oval(225, 75, 240, 90, outline="black", fill="black")
canvas.create_oval(260, 75, 275, 90, outline="black", fill="black")

# Smile drawn below
canvas.create_line(225, 65, 275, 65, width=2)


# Legs drawn below
canvas.create_oval(75, 125, 425, 175, outline="black", fill="light green")
canvas.create_oval(75, 325, 425, 375, outline="black", fill="light green")

# Tail drawn below
canvas.create_oval(225, 350, 275, 425, outline="black", fill="light green")



# Body drawn below
canvas.create_oval(100, 100, 400, 400, outline="black", fill="dark green")

# Pattern for turtle's shell
canvas.create_oval(125, 100, 375, 400, outline="black")
canvas.create_oval(150, 100, 350, 400, outline="black")
canvas.create_oval(175, 100, 325, 400, outline="black")
canvas.create_oval(200, 100, 300, 400, outline="black")
canvas.create_oval(225, 100, 275, 400, outline="black")
canvas.create_line(250, 100, 250, 400)

# Pattern for turtle's shell
canvas.create_oval(100, 125, 400, 375, outline="black")
canvas.create_oval(100, 150, 400, 350, outline="black")
canvas.create_oval(100, 175, 400, 325, outline="black")
canvas.create_oval(100, 200, 400, 300, outline="black")
canvas.create_oval(100, 225, 400, 275, outline="black")
canvas.create_line(100, 250, 400, 250)


root.mainloop()

