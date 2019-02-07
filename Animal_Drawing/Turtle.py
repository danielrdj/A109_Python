import tkinter
root = tkinter.Tk()
wdth = 500
hght = 500
root.geometry('%dx%d' % (wdth, hght))  # set window width & height
canvas = tkinter.Canvas(root, width=wdth, height=hght)
canvas.pack()

#Head and drawn below
canvas.create_oval(200, 50, 300, 125, outline="black", fill="light green")

#Eyes drawn below
canvas.create_oval(225, 75, 240, 90, outline="black", fill="black")
canvas.create_oval(260, 75, 275, 90, outline="black", fill="black")

#Smile drawn below
canvas.create_line(225, 65, 275, 65, width=2)


#Legs drawn below
canvas.create_oval(75, 125, 425, 175, outline="black", fill="light green")
canvas.create_oval(75, 325, 425, 375, outline="black", fill="light green")

#Tail drawn below
canvas.create_oval(225, 350, 275, 425, outline="black", fill="light green")



#Body drawn below
canvas.create_oval(100, 100, 400, 400, outline="black", fill="dark green")







root.mainloop()

