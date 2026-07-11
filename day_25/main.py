import turtle
import pandas as pd 
screen = turtle.Screen()
screen.title("U>.s states game.")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = list(data["state"])
states_gussed = []
while len(states_gussed) < 50:
    gussed = len(states_gussed)
    user_answer = screen.textinput(title=f"{gussed}/50 ", prompt="The state is:")
    if user_answer == None:
        break
    user_answer = user_answer.title()
    if user_answer == "Exit":
        break
    if user_answer in states_gussed:
        pass
    elif user_answer in states:
        states_gussed.append(user_answer)
        state_data=data.loc[data["state"] == user_answer]
        x_cor = state_data["x"].values[0]
        y_cor = state_data["y"].values[0]
        print(f"{x_cor}  {y_cor}")
        scr=turtle.Turtle()
        scr.hideturtle()
        scr.penup()
        scr.goto(x=x_cor , y= y_cor)
        scr.write(f"{user_answer}",False , align= "center", font=("Courier", 10, "normal"))

screen.exitonclick( )