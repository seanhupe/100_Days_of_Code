from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win?   Enter a color:  ")
colors = ["red", "orange", "SlateGray4", "green", "RoyalBlue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])



#
# tim2 = Turtle(shape="turtle")
# tim2.penup()
# tim2.goto(x=-230, y=100)
#
# tim3 = Turtle(shape="turtle")
# tim3.penup()
# tim3.goto(x=-230, y=-50)
#
# tim4 = Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(x=-230, y=50)
#
# tim5 = Turtle(shape="turtle")
# tim5.penup()
# tim5.goto(x=-230, y=-12)
#
# tim6 = Turtle(shape="turtle")
# tim6.penup()
# tim6.goto(x=-230, y=12)

screen.exitonclick()
