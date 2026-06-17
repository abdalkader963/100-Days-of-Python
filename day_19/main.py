from turtle import Turtle , Screen 
#Turtles rase
import random
scr=Screen()
scr.setup(width=500 , height=400)
user=scr.textinput(title="Make you'r bet" , prompt="which turtle is going to win?: ")
colors = ["red" , "blue" , "orange" , "purple" , "green" , "yellow"]
turtls=[]
y= -100

for _ in range(6):
    new_turtle= Turtle(shape= "turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x= -230 , y= y)
    turtls.append(new_turtle)
    y+=50

is_rase_on = True
while is_rase_on:
    for turtle in turtls:
        if turtle.xcor() > 230:
            is_rase_on=False
            winning = turtle.pencolor()
            if winning == user:
                print("You won!")
            else:
                print(f"You lost! {winning} is the winner")   
            break     
        rand = random.randint(0,10)
        turtle.fd(rand)





















scr.exitonclick()