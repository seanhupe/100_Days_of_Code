from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win?   Enter a color:  ")


tim = Turtle()
tim.penup()
tim.goto(x=-230, y=-100)

screen.exitonclick()
