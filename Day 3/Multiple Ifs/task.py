print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Ticket is $7.")
    else:
        bill = 12
        print("Ticket is $12.")

    photo = (input("Do you want a photo taken? Type Y or N: ")).upper()
    if photo == "Y":
        bill += 3
    print(f"You owe ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
