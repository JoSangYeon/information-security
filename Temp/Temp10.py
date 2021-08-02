from tkinter import *

window = Tk()


def clear():
    mylist = window.grid_slaves()
    for i in mylist:
        i.destroy()


def clearBot():
    mylist = bottomWindow.grid_slaves()
    for i in mylist:
        i.destroy()


Label(window, text='Hello World!').grid(row=0)
Button(window, text='Clear', command=clear).grid(row=1)

bottomWindow = Frame(window)
bottomWindow.grid(row=2)

Label(bottomWindow, text='bottom Label').grid(row=5)
Button(bottomWindow, text='bottom Button', command=clearBot).grid(row=6)

window.mainloop()