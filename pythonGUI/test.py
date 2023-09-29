from tkinter import *

# define and basic window info
frame = Tk()
frame.title("weird window")
frame.geometry("350x200")

# text boxes
lbl = Label(frame, text="text1")
lbl.grid(row=0, column=0)

lbl2 = Label(frame, text="text2")
lbl2.grid(row=1, column=0)

lbl3 = Label(frame, text="Click ze button")
lbl3.grid(row=3, column=1)

# input
entry1 = Entry(frame)
entry1.grid(row=0, column=1)

entry2 = Entry(frame)
entry2.grid(row=1, column=1)


# function for button
def clicked():
    x = entry1.get()
    y = entry2.get()

    if x == y:
        lbl3.configure(text="True")
    else:
        lbl3.configure(text="Not True")


# buttons
button = Button(frame, text="Validate", command=clicked())
button.grid(row=2, column=1)

# runs program
frame.mainloop()
