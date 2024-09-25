import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

# function that takes 2 values, and prints out those values
def get_mouse_click_coor(x, y):
    print(x, y)


# event listener for when the mouse clicks, then it is going to pass over the x & y coordinates
turtle.onscreenclick(get_mouse_click_coor)

# Alternative way to keep the screen open
turtle.mainloop()

# screen.exitonclick()
