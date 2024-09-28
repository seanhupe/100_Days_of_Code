import tkinter
from tkinter import *
## Import * means to import EVERYthing

# from playground import my_car

## Creating a window and setting the window Size
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=700, height=500)

## LABEL
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
#This packs the label on the screen and has different options
# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(side="top")
# my_label.pack(side="right")
# my_label.pack(expand=True)

## Ways to update the text
#my_label["text"] = "New Text2"
my_label.config(text="New Text3")


## BUTTONS
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(text="Button Got Clicked!")


# button = tkinter.Button()     ## or can use below after using the import * above
button = Button(text="Click Me", command=button_clicked)
button.pack()

## ENTRY component
input = Entry(width=10)
input.pack()
input.get()

# import turtle
# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 80, "bold"))
#


window.mainloop()
