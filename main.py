import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state
states_list = data.state.tolist()
# print(states)
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# screen.bgpic("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)
drawer = turtle.Turtle()
drawer.penup()
drawer.hideturtle()

game_is_on = True
score = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?:").title()
    if answer_state == "Exit":

        states_to_learn = [state for state in states_list if not state in guessed_states]
        pandas.DataFrame(data=states_to_learn).to_csv("states_to_learn.csv")

        # states_to_learn = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        # pandas.DataFrame(data=states_to_learn).to_csv("states_to_learn.csv")

        break
    if states.eq(answer_state).any():
        if not (answer_state in guessed_states):
            guessed_states.append(answer_state)
            score += 1
            state_row = data[data.state == answer_state]
            x_cor = float(state_row.x)
            y_cor = float(state_row.y)
            drawer.goto(x=x_cor, y=y_cor)
            drawer.write(answer_state)


# screen.exitonclick()

# get coor by click on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
