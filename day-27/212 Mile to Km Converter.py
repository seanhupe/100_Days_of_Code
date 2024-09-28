import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


## Creating a window and setting the window Size
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=250)
window.config(padx=100, pady=0)

## LABEL - need 4
my_label1 = Label(font=("Arial", 12))
my_label1.config(text="Miles")
my_label1.grid(column=3, row=0)
# my_label.config(padx=50, pady=50)
# my_label.pack()

my_label2 = Label(font=("Arial", 12))
my_label2.config(text="Km")
my_label2.grid(column=3, row=2)

my_label3 = Label(font=("Arial", 12))
my_label3.config(text="is equal to")
my_label3.grid(column=1, row=2)

my_label3 = Label(font=("Arial", 12))
my_label3.config(text="0")
my_label3.grid(column=2, row=2)

## BUTTONS
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


## ENTRY component
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=2, row=0)

window.mainloop()
