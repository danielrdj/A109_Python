import tkinter
root = tkinter.Tk()

# Size of the window.
wdth = 200
hght = 200

# tkinter setup stuff
root.geometry('%dx%d' % (wdth, hght))  # set window width & height
canvas = tkinter.Canvas(root, width=wdth, height=hght)
canvas.pack()


canvas.create_oval(50, 50, 125, 150, outline="black", fill="light green") #x0, y0, x1, y1

canvas.create_line(150, 175, 175, 125, width=2) #x0, y0, x1, y1

canvas.create_line(150, 180, 175, 180, width=2) #x0, y0, x1, y1





root.mainloop()