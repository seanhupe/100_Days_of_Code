import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


## Creating a window and setting the window Size and padding
window = Tk()
window.title("My First GUI Program")
window.minsize(width=700, height=500)
window.config(padx=100, pady=200)

## LABEL
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label.pack()


## BUTTONS
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click Me2", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

## ENTRY component
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
