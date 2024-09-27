import tkinter

## Creating a window and setting the window Size
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=700, height=500)

## Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
#This packs the label on the screen and has different options
# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(side="top")
# my_label.pack(side="right")
# my_label.pack(expand=True)


window.mainloop()
