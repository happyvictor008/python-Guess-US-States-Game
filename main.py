import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. STATE GAME")
img_name = "blank_states_img.gif"

screen.addshape(img_name)
turtle.shape(img_name)

# # Find X,Y ON SCREEN
#
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

correct_guess = 0
guessed_states = []

game_data = pd.read_csv("50_states.csv")
all_states = len(game_data["state"])

while correct_guess < all_states:
    answer_data = screen.textinput(title = f"{correct_guess}/{all_states} States Correct", prompt = "What's another state's name?").title()
    if answer_data is not None:
        hit_data = game_data[game_data["state"].str.lower() == answer_data.lower()]
        print(hit_data)
        if not hit_data.empty:
            correct_guess += 1
            guessed_states.append(answer_data)
            text_t = turtle.Turtle()
            text_t.penup()
            text_t.hideturtle()
            xcor = hit_data.x.item()
            ycor = hit_data.y.item()
            print(xcor,ycor)
            text_t.goto(xcor,ycor)
            text_t.write(hit_data.state.item())

    if answer_data.lower() == "exit":
        states_to_learn = [s for s in game_data["state"].to_list() if s not in guessed_states]
        file = pd.DataFrame(states_to_learn)
        file.to_csv("states_to_learn.csv")
        break


# States for not being guessed by user:

screen.exitonclick()