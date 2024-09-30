import tkinter
from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_results.config(text=f"{km}") 


## Creating a window and setting the window Size
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

## ENTRY components
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

## LABEL - need 4
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_results = Label(text="0")
km_results.grid(column=1, row=1)

## BUTTONS
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=3)




window.mainloop()
