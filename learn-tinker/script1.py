from curses import window
from tkinter import *

window = Tk()


def km_to_miles():
    t1.delete("1.0", END)
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)


# create button
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

# create input
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# create text field
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()
