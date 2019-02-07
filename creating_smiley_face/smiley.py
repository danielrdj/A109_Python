import tkinter
#
#
root = tkinter.Tk()
wdth = 600
hght = 600
root.geometry('%dx%d' % (wdth, hght)) # set window width & height
# https://www.python-course.eu/tkinter_canvas.php
canvas = tkinter.Canvas(root, width=wdth, height=hght)
canvas.pack()
#
#
#
canvas.create_oval(50, 50, 550, 550)
canvas.create_arc(500, 100,)
root.mainloop()