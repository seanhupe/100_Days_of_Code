## CHALLENGE
# Modify the add function to take an unlimited number of arguments.
# Use a loop to sum all the arguments inside the function.
# Test it out by calling add() to calculate sum of the arguments.

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 6, 3, 2, 324, 9))

#Key word arguments - kwargs
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.color = kwargs["color"]
        self.seats = kwargs["seats"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
