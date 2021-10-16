import turtle
import pandas
screen = turtle.Screen()
screen.setup(width=700, height=500)
tim = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinate)
# Clicking on any of the states gives you the x and y co-ordinates of the state
# print(answer_state)

#  Convert te guess to Title Case ✔️
#  Check if the guess is among the 50 states ✔️
screen.tracer(0)
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
states_list = []
score = 0
while len(states_list) < 50:
    answer_state = screen.textinput(title=f"Score: {score}/50 ", prompt="Guess a states name?").title()
    if answer_state == "Exit":
        learn_states = [state for state in all_states if state not in states_list]
        new_data = pandas.DataFrame(learn_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for each_state in states.state:
        if each_state == answer_state:
            states_list.append(answer_state)
            data = states[states.state == each_state]
            pos_x = data.iloc[0]['x']
            pos_y = data.iloc[0]['y']
            tim.penup()
            tim.hideturtle()
            tim.setpos(x=pos_x, y=pos_y)
            tim.write(answer_state, align="center", font=("courier", 10, "normal"))
            screen.update()
            score += 1
#  Write correct guesses on to the map ✔️
#  Use a loop to allow the user to keep guessing ✔️
#  record the correct guesses in a list ✔️
#  Keep track of the score ✔️
# states_to_learn.csv ✔️


# Alternative way of keeping our screen open even though our code has finished running
# Screen doesn't exit on click
turtle.mainloop()
