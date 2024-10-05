from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}")



# ---------------------------- UI SETUP ------------------------------- #+
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

## Background tomato image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


## LABEL - Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

## LABEL - Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

## LABEL - Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

## ENTRIES
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "seanhupe@yahoo.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW)

## BUTTONS
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky=EW)
#
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)



window.mainloop()
