import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

new_turtle = Turtle()
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win?   Enter a color:  ")
colors = ["red", "orange", "SlateGray4", "green", "RoyalBlue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(all_turtles)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
