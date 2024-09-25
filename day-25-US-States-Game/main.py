import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()   # converts into a list
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Allow user a way to quit game
    if answer_state == "Exit":
        # Create a new list of missing states to by comparing guessed_states and comparing to all_states
        # Using Conditional List Comprehension here to replace the 4 below it
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #print(answer_state)
    # 1. If answer_state is one of the states in the CSV
    if answer_state in all_states:
        # 2. If they get it correct:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]    # pull out the row where state = answer state
        t.goto(state_data.x.item(), state_data.y.item())
        # 3. create a turtle to write the name of the state at the x,y coordinates
        t.write(answer_state)


# # function that takes 2 values, and prints out those values
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # event listener for when the mouse clicks, then it is going to pass over the x & y coordinates
# turtle.onscreenclick(get_mouse_click_coor)
#
# # Alternative way to keep the screen open
# turtle.mainloop()

# screen.exitonclick()
